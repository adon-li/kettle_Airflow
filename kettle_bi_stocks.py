#!/usr/bin/env python
# -*- coding:utf-8 -*-

import getpass
import os

import paramiko

from contextlib import contextmanager
from airflow.exceptions import AirflowException
from airflow.hooks.base_hook import BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow import DAG
from airflow.contrib.operators.vertica_operator import VerticaOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.models import Variable
from airflow.contrib.hooks import SSHHook
from base64 import b64encode
from select import select
from airflow import configuration
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from bi_stock.bi_goods_stock_sub_new import stock_distribute, remaining
from bi_stock.bi_product_season_plan_category import init


class SSHOperator(BaseOperator):
    """
    SSHOperator to execute commands on given remote host using the ssh_hook.

    :param ssh_hook: predefined ssh_hook to use for remote execution
    :type ssh_hook: :class:`SSHHook`
    :param ssh_conn_id: connection id from airflow Connections
    :type ssh_conn_id: str
    :param remote_host: remote host to connect
    :type remote_host: str
    :param command: command to execute on remote host
    :type command: str
    :param timeout: timeout for executing the command.
    :type timeout: int
    :param do_xcom_push: return the stdout which also get set in xcom by airflow platform
    :type do_xcom_push: bool
    """

    template_fields = ('command',)

    @apply_defaults
    def __init__(self,
                 ssh_hook=None,
                 ssh_conn_id=None,
                 remote_host=None,
                 command=None,
                 timeout=10,
                 do_xcom_push=False,
                 *args,
                 **kwargs):
        super(SSHOperator, self).__init__(*args, **kwargs)
        self.ssh_hook = ssh_hook
        self.ssh_conn_id = ssh_conn_id
        self.remote_host = remote_host
        self.command = command
        self.timeout = timeout
        self.do_xcom_push = do_xcom_push

    def execute(self, context):
        try:
            if self.ssh_conn_id and not self.ssh_hook:
                self.ssh_hook = SSHHook(ssh_conn_id=self.ssh_conn_id)

            if not self.ssh_hook:
                raise AirflowException("can not operate without ssh_hook or ssh_conn_id")

            if self.remote_host is not None:
                self.ssh_hook.remote_host = self.remote_host

            ssh_client = self.ssh_hook.get_conn()

            if not self.command:
                raise AirflowException("no command specified so nothing to execute here.")

            # Auto apply tty when its required in case of sudo
            get_pty = False
            if self.command.startswith('sudo'):
                get_pty = True

            # set timeout taken as params
            stdin, stdout, stderr = ssh_client.exec_command(command=self.command,
                                                            get_pty=get_pty,
                                                            timeout=self.timeout
                                                            )
            # get channels
            channel = stdout.channel

            # closing stdin
            stdin.close()
            channel.shutdown_write()

            agg_stdout = b''
            agg_stderr = b''

            # capture any initial output in case channel is closed already
            stdout_buffer_length = len(stdout.channel.in_buffer)

            if stdout_buffer_length > 0:
                agg_stdout += stdout.channel.recv(stdout_buffer_length)

            # read from both stdout and stderr
            while not channel.closed or channel.recv_ready() or channel.recv_stderr_ready():
                readq, _, _ = select([channel], [], [], self.timeout)
                for c in readq:
                    if c.recv_ready():
                        line = stdout.channel.recv(len(c.in_buffer))
                        line = line
                        agg_stdout += line
                        self.log.info(line)
                    if c.recv_stderr_ready():
                        line = stderr.channel.recv_stderr(len(c.in_stderr_buffer))
                        line = line
                        agg_stderr += line
                        self.log.warning(line)
                if stdout.channel.exit_status_ready() \
                        and not stderr.channel.recv_stderr_ready() \
                        and not stdout.channel.recv_ready():
                    stdout.channel.shutdown_read()
                    stdout.channel.close()
                    break

            stdout.close()
            stderr.close()

            exit_status = stdout.channel.recv_exit_status()
            if exit_status is 0:
                # returning output if do_xcom_push is set
                if self.do_xcom_push:
                    enable_pickling = configuration.getboolean('core',
                                                               'enable_xcom_pickling')
                    if enable_pickling:
                        return agg_stdout
                    else:
                        return b64encode(agg_stdout)

            else:
                error_msg = agg_stderr
                raise AirflowException("error running cmd: {0}, error: {1}"
                                       .format(self.command, error_msg))

        except Exception as e:
            raise AirflowException("SSH operator error: {0}".format(str(e)))

        return True

    def tunnel(self):
        ssh_client = self.ssh_hook.get_conn()
        ssh_client.get_transport()


class SSHMHook(SSHHook):
    def __init__(self,
                 ssh_conn_id=None,
                 remote_host=None,
                 remote_port=None,
                 username=None,
                 password=None,
                 key_file=None,
                 timeout=10,
                 keepalive_interval=30):
        self.remote_port = remote_port
        self.ssh_conn_id = ssh_conn_id
        self.remote_host = remote_host
        self.username = username
        self.password = password
        self.key_file = key_file
        self.timeout = timeout
        self.keepalive_interval = keepalive_interval
        # Default values, overridable from Connection
        self.compress = True
        self.no_host_key_check = True
        self.client = None
        super(SSHHook, self).__init__(ssh_conn_id)

    def get_conn(self):
        if not self.client:
            self.log.debug('Creating SSH client for conn_id: %s', self.ssh_conn_id)
            if self.ssh_conn_id is not None:
                conn = self.get_connection(self.ssh_conn_id)
                if self.username is None:
                    self.username = conn.login
                if self.password is None:
                    self.password = conn.password
                if self.remote_host is None:
                    self.remote_host = conn.host
                if self.remote_port is None:
                    self.remote_port = conn.port
                if conn.extra is not None:
                    extra_options = conn.extra_dejson
                    self.key_file = extra_options.get("key_file")

                    if "timeout" in extra_options:
                        self.timeout = int(extra_options["timeout"], 10)

                    if "compress" in extra_options \
                            and extra_options["compress"].lower() == 'false':
                        self.compress = False
                    if "no_host_key_check" in extra_options \
                            and extra_options["no_host_key_check"].lower() == 'false':
                        self.no_host_key_check = False

            if not self.remote_host:
                raise AirflowException("Missing required param: remote_host")

            # Auto detecting username values from system
            if not self.username:
                self.log.debug(
                    "username to ssh to host: %s is not specified for connection id"
                    " %s. Using system's default provided by getpass.getuser()",
                    self.remote_host, self.ssh_conn_id
                )
                self.username = getpass.getuser()

            host_proxy = None
            user_ssh_config_filename = os.path.expanduser('~/.ssh/config')
            if os.path.isfile(user_ssh_config_filename):
                ssh_conf = paramiko.SSHConfig()
                ssh_conf.parse(open(user_ssh_config_filename))
                host_info = ssh_conf.lookup(self.remote_host)
                if host_info and host_info.get('proxycommand'):
                    host_proxy = paramiko.ProxyCommand(host_info.get('proxycommand'))

                if not (self.password or self.key_file):
                    if host_info and host_info.get('identityfile'):
                        self.key_file = host_info.get('identityfile')[0]

            try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                if self.no_host_key_check:
                    # Default is RejectPolicy
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                if self.password and self.password.strip():
                    client.connect(hostname=self.remote_host,
                                   port=self.remote_port,
                                   username=self.username,
                                   password=self.password,
                                   timeout=self.timeout,
                                   compress=self.compress,
                                   sock=host_proxy)
                else:
                    client.connect(hostname=self.remote_host,
                                   port=self.remote_port,
                                   username=self.username,
                                   key_filename=self.key_file,
                                   timeout=self.timeout,
                                   compress=self.compress,
                                   sock=host_proxy)

                if self.keepalive_interval:
                    client.get_transport().set_keepalive(self.keepalive_interval)

                self.client = client
            except paramiko.AuthenticationException as auth_error:
                self.log.error(
                    "Auth failed while connecting to host: %s, error: %s",
                    self.remote_host, auth_error
                )
            except paramiko.SSHException as ssh_error:
                self.log.error(
                    "Failed connecting to host: %s, error: %s",
                    self.remote_host, ssh_error
                )
            except Exception as error:
                self.log.error(
                    "Error connecting to host: %s, error: %s",
                    self.remote_host, error
                )
        return self.client


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 7, 30),
    'email': ['dingwendong@inman.cc'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),

}

dag = DAG('kettle_bi_stocks_dag', schedule_interval='03 0/2 * * *', default_args=default_args, catchup=False)

sshHookhmc = SSHMHook(ssh_conn_id='hmc_kettle')

iom_produce_init = SSHOperator(task_id='iom_produce_init', ssh_hook=sshHookhmc,
                               command='source /etc/profile;/home/kettle/data-integration/kitchen.sh -file=/home/kettle/bi_goods_stock_sub_new/iom_produce_init.kjb -log=/home/kettle/log/iom_produce_init.log -level=Basic',
                               dag=dag)

bi_goods_stocks_sub_new_init = SSHOperator(task_id='bi_goods_stocks_sub_new_init', ssh_hook=sshHookhmc,
                                           command='source /etc/profile;/home/kettle/data-integration/pan.sh -file=/home/kettle/bi_goods_stock_sub_new/bi_goods_stocks_sub_new_init.ktr -log=/home/kettle/log/bi_goods_stocks_sub_new_init.log -level=Basic',
                                           dag=dag)

stock_distribute = PythonOperator(
    task_id='stock_distribute',
    python_callable=stock_distribute,
    dag=dag)

remaining = PythonOperator(
    task_id='remaining',
    python_callable=remaining,
    dag=dag)

bi_goods_stocks_sub_new = SSHOperator(task_id='bi_goods_stocks_sub_new', ssh_hook=sshHookhmc,
                                      command='source /etc/profile;/home/kettle/data-integration/pan.sh -file=/home/kettle/bi_goods_stock_sub_new/bi_goods_stocks_sub_new.ktr -log=/home/kettle/log/bi_goods_stocks_sub_new.log -level=Basic',
                                      dag=dag)

continue_product_update = SSHOperator(task_id='continue_product_update', ssh_hook=sshHookhmc,
                                      command='source /etc/profile;/home/kettle/data-integration/pan.sh -file=/home/kettle/bi_goods_stock_sub_new/continue_product.ktr -log=/home/kettle/log/continue_product.log -level=Basic',
                                      dag=dag)

product_season_new = SSHOperator(task_id='product_season_new', ssh_hook=sshHookhmc,
                                 command='source /etc/profile;/home/kettle/data-integration/kitchen.sh -file=/home/kettle/bi_goods_stock_sub_new/product_season_new.kjb -log=/home/kettle/log/product_season_new.log -level=Basic',
                                 dag=dag)

bi_product_season_plan_init = SSHOperator(task_id='bi_product_season_plan_init', ssh_hook=sshHookhmc,
                                          command='source /etc/profile;/home/kettle/data-integration/pan.sh -file=/home/kettle/bi_product_season_plan/bi_product_season_plan_init.ktr -log=/home/kettle/log/bi_product_season_plan_init.log -level=Basic',
                                          dag=dag)

update_bi_product_season_plan = PythonOperator(
    task_id='update_bi_product_season_plan',
    python_callable=init,
    dag=dag)

bi_product_season_plan_category = SSHOperator(task_id='bi_product_season_plan_category', ssh_hook=sshHookhmc,
                                              command='source /etc/profile;/home/kettle/data-integration/kitchen.sh -file=/home/kettle/bi_product_season_plan/bi_product_season_plan.kjb -log=/home/kettle/log/bi_product_season_plan.log -level=Basic',
                                              dag=dag)

bi_product_category_class_target = SSHOperator(task_id='bi_product_category_class_target', ssh_hook=sshHookhmc,
                                               command='source /etc/profile;/home/kettle/data-integration/kitchen.sh -file=/home/kettle/bi_product_category_class_target/bi_product_category_class_target.kjb -log=/home/kettle/log/bi_product_category_class_target.log -level=Basic',
                                               dag=dag)

bi_stock_now = MySqlOperator(task_id='bi_stock_now',
                             mysql_conn_id='mysql_hmc',
                             sql='''TRUNCATE TABLE bi_stock_now;

                                    INSERT INTO bi_stock_now(product_sn,onway_nums,stock)
                                    select product_sn,sum(production_onway_nums) as production_onway_nums,sum(total_in_stock) as total_in_stock
                                    FROM hmcdata.bi_goods_stock_sub_new bgssn 
                                    group by product_sn
                                    having sum(production_onway_nums)>0 or sum(total_in_stock)>0;'''
                             , dag=dag)

bi_shop_saleinfo_return_goods = SSHOperator(task_id='bi_shop_saleinfo_return_goods', ssh_hook=sshHookhmc,
                                            command='source /etc/profile;/home/kettle/data-integration/kitchen.sh -file=/home/kettle/bi_shop_saleinfo_return_goods/bi_shop_saleinfo_return_goods.kjb -log=/home/kettle/log/bi_shop_saleinfo_return_goods.log -level=Basic',
                                            dag=dag)

init_product_info_new = SSHOperator(task_id='init_product_info_new', ssh_hook=sshHookhmc,
                                            command='source /etc/profile;/home/kettle/data-integration/pan.sh -file=/home/kettle/bi_goods_stock_sub_new/init_product_info_new.ktr -log=/home/kettle/log/init_product_info_new.log -level=Basic',
                                            dag=dag)

iom_produce_init >> bi_goods_stocks_sub_new_init >> stock_distribute >> remaining >> continue_product_update \
>> bi_goods_stocks_sub_new >> product_season_new >> bi_product_season_plan_init >> update_bi_product_season_plan >> bi_product_season_plan_category \
>> bi_product_category_class_target >> bi_stock_now >> bi_shop_saleinfo_return_goods >> init_product_info_new
