# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
 settings for ETL project.

"""
import os
import platform
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPIDER = '/home/bi/spider'
DATA_SOURCE = {
    'vertica_70': {
        'engine': 'vertica',
        'host': '120.55.188.105',
        'port': ####,
        'user': '####',
        'passwd': '####',
        'db': 'huimei'
    },
    'vertica_90': {
        'engine': 'vertica',
        'host': '106.15.24.126',
        'port': ####,
        'user': 'hmc',
        'passwd': '####',
        'db': 'hmcdata'
    },
    'mysql_1': {
        'engine': 'mysql',
        'host': 'rdso1122t7mw6xnbh93j.mysql.rds.aliyuncs.com',
        'port': ####,
        'user': 'inman',
        'passwd': '####',
        'db': 'bi_elephant',
    },
    'mysql_hmc': {
        'engine': 'mysql',
        'host': 'rm-uf6xd393y559jo5sh774.mysql.rds.aliyuncs.com',
        'port': ####,
        'user': '####',
        'passwd': '####',
        'db': 'hmcdata',
    },
    'o2o': {
        'engine': 'mysql',
        'host': '192.168.10.149',
        'port': ####,
        'user': 'sync_bi',
        'passwd': '####',
        'db': '####',
    },
    'o2o_local': {
        'engine': 'mysql',
        'host': '192.168.7.36',
        'port': ####,
        'user': 'sync_bi',
        'passwd': '####',
        'db': '####',
    },
    'o2o_test': {
        'engine': 'mysql',
        'host': 'rds46108z23hh61v28f4j.mysql.rds.aliyuncs.com',
        'port': ####,
        'user': '####',
        'passwd': '####',
        'db': '####',
    },
    'hmc_upms': {
        'engine': 'mysql',
        'host': 'rm-uf675a36o6ks070yg.mysql.rds.aliyuncs.com',
        'port': ####,
        'user': '####',
        'passwd': '####',
        'db': '####',
    },
    'hmc_scm_product': {
        'engine': 'mysql',
        'host': 'prod-hmcloud-app-ro.rwlb.rds.aliyuncs.com',
        'port': ####,
        'user': '',
        'passwd': '',
        'db': '',
        'ssh': '',
    },
    'hmc_product_center': {
        'engine': 'mysql',
        'host': 'drds6bw1kxvd2jr6.drds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '', },
    'hmc_trade_center': {
        'engine': 'mysql',
        'host': 'prod-hmcloud-center-ro.rwlb.rds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': ,
        'db': '',
    },
    'hmc_member_center': {
        'engine': 'mysql',
        'host': 'prod-hmcloud-center-ro.rwlb.rds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '',
    },
    'hmc_pay_gateway': {
        'engine': 'mysql',
        'host': 'drds6bw1kxvd2jr6.drds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '',
    },
    'hmc_oms_business': {
        'engine': 'mysql',
        'host': 'prod-hmcloud-app-ro.rwlb.rds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '',
    },
    'hmc_trade_center_read': {
        'engine': 'mysql',
        'host': 'drdsfacb76n6r7as.drds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '',
    },
    'polardb': {
        'engine': 'mysql',
        'host': 'pc-uf66dc9644we4n0wb.rwlb.rds.aliyuncs.com',
        'port': ,
        'user': '',
        'passwd': '',
        'db': '',
    },
}
SSH_SOURCE = {
    'hmc': {
        'ssh_host': "101.132.157.108",
        'ssh_port': ,
        'ssh_user': "",
        'ssh_password': ""
    },
    'o2o': {
        'ssh_host': "121.40.54.213",
        'ssh_port': ,
        'ssh_user': "",
        'ssh_password': ""
    }
}

if platform.system() == 'Windows':
    LOG_DIR = '/'.join([BASE_DIR, '/log'])
elif platform.system() == 'Linux':
    LOG_DIR = '/'.join([SPIDER, '/log'])
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
        # ????????????
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'monitor_default.log']),  # ??????????????????
            'maxBytes': 1024 * 1024 * 5,  # ????????????
            'backupCount': 5,  # ????????????
            'formatter': 'standard',  # ????????????formatters????????????
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'monitor_error.log']),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'monitor_info.log']),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'request.log']),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'script.log']),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'sourceDns.webdns.views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        'sourceDns.webdns.util': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True
        },
        'ETL': {
            'handlers': ['console', 'error', 'info'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
WARNING_ORDER_NUM=10
EMAIL={
    "username":"alarm@inman.cc",
    "password":"Hkjni#9u8"
}
NEIGOU_ADDRESS={
    "??????":{"address":"13???1?????????","name":"???????????????"},
    "??????":{"address":"12?????????7???","name":"??????????????????????????????"}
}
CHUNKSIZE = 5000
SSH_SOURCE = {
    'hmc': {
        'ssh_host': "101.132.157.108",
        'ssh_port': ,
        'ssh_user': "",
        'ssh_password': ""
    }
}
REDIS_SOURCE = {
    'local_redis': {
        'host': '192.168.7.112',
        'port': ,
        'password': '',
        'db':
    },
    'bi_redis': {
        'host': '127.0.0.1',
        'port': ,
        'password': '',
        'db':
    }
}
SHOP_ID = {'?????????????????????': {'shop_id': 142198236, 'seller_id': 2719809625},
           '?????????????????????': {'shop_id': 108231462, 'seller_id': 1947403838},
           '????????????????????????': {'shop_id': 66984172, 'seller_id': 710608278},
           'pass?????????': {'shop_id': 112736202, 'seller_id': 2182013355},
           'samyama?????????': {'shop_id': 115394119, 'seller_id': 2249377411},
           '????????????': {'shop_id': 60553320, 'seller_id': 375594758},
           '???????????????': {'shop_id': 68905897, 'seller_id': 761679524},
           '???????????????': {'shop_id': 62560090, 'seller_id': 488320269},
           '?????????????????????': {'shop_id': 126813856, 'seller_id': 2579790840},
           '?????????????????????': {'shop_id': 136852150, 'seller_id': 2587984881},
           '???????????????': {'shop_id': 57301243, 'seller_id': 130974249},
           '?????????????????????': {'shop_id': 108443046, 'seller_id': 1965714898},
           "???????????????????????????":{'shop_id':108357058,'seller_id':1957567118},
           "iumi?????????": {
               "shopUrl": "//iumi.tmall.com",
               "shop_id": "73151152",
               "seller_id": "1019292692"
           },
           "zk?????????": {
               "shopUrl": "//zknz.tmall.com",
               "shop_id": "100163346",
               "seller_id": "1044264726"
           },
           "????????????????????????": {
               "shopUrl": "//pb89.tmall.com",
               "shop_id": "57300711",
               "seller_id": "112394247"
           },
           "maxmartin??????????????????": {
               "shopUrl": "//maxmartin.tmall.com",
               "shop_id": "103047260",
               "seller_id": "1644880265"
           },
           "???????????????": {
               "shopUrl": "//qimi.tmall.com",
               "shop_id": "105779984",
               "seller_id": "1766047907"
           },
           "ELAND???????????????": {
               "shopUrl": "//eland.tmall.com",
               "shop_id": "105788454",
               "seller_id": "1770528988"
           },
           "???????????????": {
               "shopUrl": "//duibai.tmall.com",
               "shop_id": "107329277",
               "seller_id": "1870451655"
           },
           "????????????????????????": {
               "shopUrl": "//uniqlo.tmall.com",
               "shop_id": "57303596",
               "seller_id": "196993935"
           },
           "????????????????????????": {
               "shopUrl": "//lachapelle.tmall.com",
               "shop_id": "111717832",
               "seller_id": "2146742267"
           },
           "ZARA???????????????": {
               "shopUrl": "//zara.tmall.com",
               "shop_id": "113462750",
               "seller_id": "2228361831"
           },
           "?????????????????????": {
               "shopUrl": "//ripfs.tmall.com",
               "shop_id": "58014452",
               "seller_id": "228784630"
           },
           "?????????????????????": {
               "shopUrl": "//handuyishe.tmall.com",
               "shop_id": "58501945",
               "seller_id": "263817957"
           },
           "ochirly???????????????": {
               "shopUrl": "//ochirly.tmall.com",
               "shop_id": "58674200",
               "seller_id": "272205633"
           },
           "ONLY???????????????": {
               "shopUrl": "//only.tmall.com",
               "shop_id": "60129786",
               "seller_id": "356060330"
           },
           "????????????????????????": {
               "shopUrl": "//yaojingdekoudai.tmall.com",
               "shop_id": "60300724",
               "seller_id": "362409818"
           },
           "??????????????????": {
               "shopUrl": "//othermix.tmall.com",
               "shop_id": "61054779",
               "seller_id": "394695430"
           },
           "?????????????????????": {
               "shopUrl": "//semir.tmall.com",
               "shop_id": "61127277",
               "seller_id": "397341302"
           },
           "???????????????": {
               "shopUrl": "//esey.tmall.com",
               "shop_id": "61412736",
               "seller_id": "408107205"
           },
           "veromoda???????????????": {
               "shopUrl": "//veromoda.tmall.com",
               "shop_id": "61773004",
               "seller_id": "420567757"
           },
           "artka???????????????": {
               "shopUrl": "//artka.tmall.com",
               "shop_id": "62112343",
               "seller_id": "444076877"
           },
           "amii?????????": {
               "shopUrl": "//amii.tmall.com",
               "shop_id": "62195084",
               "seller_id": "451135386"
           },
           "?????????????????????": {
               "shopUrl": "//leting.tmall.com",
               "shop_id": "62767848",
               "seller_id": "513051429"
           },
           "moco???????????????": {
               "shopUrl": "//moco.tmall.com",
               "shop_id": "63240547",
               "seller_id": "581746910"
           },
           "?????????????????????": {
               "shopUrl": "//eifini.tmall.com",
               "shop_id": "63721895",
               "seller_id": "641725918"
           },
           "fiveplus???????????????": {
               "shopUrl": "//fiveplus.tmall.com",
               "shop_id": "65707026",
               "seller_id": "685140573"
           },
           "?????????????????????": {
               "shopUrl": "//etam.tmall.com",
               "shop_id": "66961931",
               "seller_id": "710962071"
           },
           "?????????????????????": {
               "shopUrl": "//girdear.tmall.com",
               "shop_id": "67694825",
               "seller_id": "728443962"
           },
           "???????????????": {
               "shopUrl": "//chuyu.tmall.com",
               "shop_id": "68905897",
               "seller_id": "761679524"
           },
           "???????????????????????????": {
               "shopUrl": "//eptisonfs.tmall.com",
               "shop_id": "69906704",
               "seller_id": "803368268"
           },
           "???????????????": {
               "shopUrl": "//chumian.tmall.com",
               "shop_id": "72455858",
               "seller_id": "912835464"
           },
           "lrud?????????": {
               "shopUrl": "//lrud.tmall.com",
               "shop_id": "114461749",
               "seller_id": "2264201946"
           },
           "?????????????????????": {
               "shopUrl": "//zhimugongfang.tmall.com",
               "shop_id": "73402183",
               "seller_id": "1030778510"
           },
           "???????????????": {
               "shopUrl": "//jiayijjyp.tmall.com",
               "shop_id": "100668426",
               "seller_id": "1066329044"
           },
           "???????????????????????????": {
               "shopUrl": "//yuanshimuyu.tmall.com",
               "shop_id": "101529349",
               "seller_id": "1105025069"
           },
           "???????????????????????????": {
               "shopUrl": "//lshmy.tmall.com",
               "shop_id": "57301625",
               "seller_id": "143584903"
           },
           "????????????????????????": {
               "shopUrl": "//gepafei.tmall.com",
               "shop_id": "103704802",
               "seller_id": "1642946911"
           },
           "???????????????????????????": {
               "shopUrl": "//meikemeijia.tmall.com",
               "shop_id": "103404629",
               "seller_id": "1660593285"
           },
           "?????????????????????": {
               "shopUrl": "//maitian.tmall.com",
               "shop_id": "105735987",
               "seller_id": "1772995108"
           },
           "?????????????????????": {
               "shopUrl": "//huayijiaju.tmall.com",
               "shop_id": "106444345",
               "seller_id": "1819934535"
           },
           "?????????????????????": {
               "shopUrl": "//inmannx.tmall.com",
               "shop_id": "107160445",
               "seller_id": "1835235939"
           },
           "????????????????????????": {
               "shopUrl": "//customizedfurniture.tmall.com",
               "shop_id": "108143912",
               "seller_id": "1911411704"
           },
           "????????????": {
               "shopUrl": "//tooblack.taobao.com",
               "shop_id": "113767108",
               "seller_id": "2228290021"
           },
           "luckysac?????????": {
               "shopUrl": "//luckysac.tmall.com",
               "shop_id": "114446876",
               "seller_id": "2289469223"
           },
           "MUMO??????": {
               "shopUrl": "//mumolife.taobao.com",
               "shop_id": "34059034",
               "seller_id": "23739472"
           },
           "?????????????????????": {
               "shopUrl": "//inmanny.tmall.com",
               "shop_id": "177176098",
               "seller_id": "2996366394"
           },
           "ZAOZUO?????????": {
               "shopUrl": "//zaozuo.tmall.com",
               "shop_id": "266324282",
               "seller_id": "3017251987"
           },
           "?????????????????????": {
               "shopUrl": "//mingmenjiangxiang.tmall.com",
               "shop_id": "404070660",
               "seller_id": "3051910325"
           },
           "?????????????????????": {
               "shopUrl": "//qingdaoyimu.tmall.com",
               "shop_id": "189769877",
               "seller_id": "3191764880"
           },
           "?????????????????????": {
               "shopUrl": "//mdzf.taobao.com",
               "shop_id": "61739784",
               "seller_id": "413996455"
           },
           "?????????????????????": {
               "shopUrl": "//yysj.tmall.com",
               "shop_id": "62269246",
               "seller_id": "459805913"
           },
           "???????????????": {
               "shopUrl": "//weisha.tmall.com",
               "shop_id": "62377351",
               "seller_id": "470164086"
           },
           "??????????????????NORHOR": {
               "shopUrl": "//norho.taobao.com",
               "shop_id": "50035",
               "seller_id": "50035"
           },
           "???????????????": {
               "shopUrl": "//ofat.taobao.com",
               "shop_id": "69071116",
               "seller_id": "689730212"
           },
           "???????????????????????????": {
               "shopUrl": "//yuanshiyuansu.tmall.com",
               "shop_id": "68814207",
               "seller_id": "758744253"
           },
           "?????????????????????": {
               "shopUrl": "//guangming.tmall.com",
               "shop_id": "70293189",
               "seller_id": "822939859"
           },
           "?????????????????????": {
               "shopUrl": "//uvanart.tmall.com",
               "shop_id": "71539955",
               "seller_id": "872353151"
           },
           "??????????????????": {
               "shopUrl": "//weinimei.tmall.com",
               "shop_id": "71830600",
               "seller_id": "885152160"
           },
           "HarborHouse???????????????": {
               "shopUrl": "//harborhouse.tmall.com",
               "shop_id": "57299751",
               "seller_id": "92668878"
           },
           "?????????????????????": {
               "shopUrl": "//threecolour.tmall.com",
               "shop_id": "68368000",
               "seller_id": "745475881"
           },
           "??????????????????": {
               "shopUrl": "//jinhuli.tmall.com",
               "shop_id": "73308575",
               "seller_id": "1026415371"
           },
           "?????????????????????": {
               "shopUrl": "//laifu.tmall.com",
               "shop_id": "100179231",
               "seller_id": "1044713328"
           },
           "?????????????????????": {
               "shopUrl": "//mixixb.tmall.com",
               "shop_id": "101283724",
               "seller_id": "1094577300"
           },
           "????????????????????????": {
               "shopUrl": "//juststar.tmall.com",
               "shop_id": "101691052",
               "seller_id": "1113077706"
           },
           "??????????????????": {
               "shopUrl": "//shanshuiji.tmall.com",
               "shop_id": "101720656",
               "seller_id": "1114645587"
           },
           "??????????????????": {
               "shopUrl": "//emini.tmall.com",
               "shop_id": "57301011",
               "seller_id": "122343103"
           },
           "aza?????????": {
               "shopUrl": "//azams.tmall.com",
               "shop_id": "57301524",
               "seller_id": "138468814"
           },
           "???????????????": {
               "shopUrl": "//lanwu.tmall.com",
               "shop_id": "105956654",
               "seller_id": "1685377206"
           },
           "??????????????????": {
               "shopUrl": "//shop129660120.taobao.com",
               "shop_id": "129660120",
               "seller_id": "1796102966"
           },
           "??????????????????": {
               "shopUrl": "//fanice.tmall.com",
               "shop_id": "107692780",
               "seller_id": "1894907077"
           },
           "wolfhorse???????????????": {
               "shopUrl": "//wolfhorse.tmall.com",
               "shop_id": "110455091",
               "seller_id": "2076567689"
           },
           "?????????????????????": {
               "shopUrl": "//qianzibaidai.tmall.com",
               "shop_id": "60237200",
               "seller_id": "359484699"
           },
           "Hello ?????????": {
               "shopUrl": "//shop127404863.taobao.com",
               "shop_id": "127404863",
               "seller_id": "60817262"
           },
           "mracehomme?????????": {
               "shopUrl": "//mracehomme.tmall.com",
               "shop_id": "63538579",
               "seller_id": "617642921"
           },
           "?????????????????????": {
               "shopUrl": "//lafestin.tmall.com",
               "shop_id": "67173900",
               "seller_id": "714688689"
           },
           "???????????????": {
               "shopUrl": "//zooler.tmall.com",
               "shop_id": "67464350",
               "seller_id": "722491027"
           },
           "pmsix?????????": {
               "shopUrl": "//pmsix.tmall.com",
               "shop_id": "67484711",
               "seller_id": "723038269"
           },
           "?????????????????????": {
               "shopUrl": "//mcysjpn.tmall.com",
               "shop_id": "68472907",
               "seller_id": "748793950"
           },
           "aspensport?????????": {
               "shopUrl": "//aspensport.tmall.com",
               "shop_id": "68521767",
               "seller_id": "749711636"
           },
           "jansport?????????": {
               "shopUrl": "//jansport.tmall.com",
               "shop_id": "70002657",
               "seller_id": "807956257"
           },
           "???????????????????????????": {
               "shopUrl": "//xiaoxiangbaodai.tmall.com",
               "shop_id": "70276118",
               "seller_id": "822457842"
           },
           "artmi?????????": {
               "shopUrl": "//artmi.tmall.com",
               "shop_id": "70294401",
               "seller_id": "823258756"
           },
           "??????????????????": {
               "shopUrl": "//jonbag.tmall.com",
               "shop_id": "70428876",
               "seller_id": "829250210"
           },
           "?????????????????????": {
               "shopUrl": "//mingjiatonghua.tmall.com",
               "shop_id": "73519871",
               "seller_id": "1036144608"
           },
           "?????????????????????": {
               "shopUrl": "//miqidida.tmall.com",
               "shop_id": "73523732",
               "seller_id": "1036640987"
           },
           "???????????????????????????": {
               "shopUrl": "//minizaru.tmall.com",
               "shop_id": "100705598",
               "seller_id": "1067628403"
           },
           "??????????????????": {
               "shopUrl": "//mianshushu.tmall.com",
               "shop_id": "103963858",
               "seller_id": "1655415934"
           },
           "minipeace?????????": {
               "shopUrl": "//minipeace.tmall.com",
               "shop_id": "103871164",
               "seller_id": "1683598224"
           },
           "jnbybyjnby?????????": {
               "shopUrl": "//jnbybyjnby.tmall.com",
               "shop_id": "103891671",
               "seller_id": "1684548055"
           },
           "??????????????????????????????": {
               "shopUrl": "//pencilclub.tmall.com",
               "shop_id": "104447871",
               "seller_id": "1690429904"
           },
           "????????????????????????": {
               "shopUrl": "//senshukaimy.tmall.com",
               "shop_id": "105947989",
               "seller_id": "1743112933"
           },
           "???????????????": {
               "shopUrl": "//chuanshu.tmall.com",
               "shop_id": "105507988",
               "seller_id": "1744940626"
           },
           "honeypig?????????": {
               "shopUrl": "//honeypig.tmall.com",
               "shop_id": "114635358",
               "seller_id": "1920070699"
           },
           "?????????????????????": {
               "shopUrl": "//liebo.tmall.com",
               "shop_id": "110917163",
               "seller_id": "2098876698"
           },
           "lavi?????????": {
               "shopUrl": "//lavimy.tmall.com",
               "shop_id": "111875620",
               "seller_id": "2108082193"
           },
           "?????????????????????": {
               "shopUrl": "//luotuotz.tmall.com",
               "shop_id": "111963326",
               "seller_id": "2122324108"
           },
           "osa???????????????": {
               "shopUrl": "//osatz.tmall.com",
               "shop_id": "112659507",
               "seller_id": "2165643600"
           },
           "??????????????????": {
               "shopUrl": "//annil.tmall.com",
               "shop_id": "58105291",
               "seller_id": "240252102"
           },
           "?????????????????????": {
               "shopUrl": "//chuyutz.tmall.com",
               "shop_id": "126813856",
               "seller_id": "2579790840"
           },
           "amii???????????????": {
               "shopUrl": "//amiitz.tmall.com",
               "shop_id": "154916672",
               "seller_id": "2863720993"
           },
           "?????????????????????": {
               "shopUrl": "//mesamis.tmall.com",
               "shop_id": "156093513",
               "seller_id": "2878663563"
           },
           "???????????????????????????": {
               "shopUrl": "//handuyishetz.tmall.com",
               "shop_id": "165619466",
               "seller_id": "2934594227"
           },
           "????????????????????????": {
               "shopUrl": "//mamati.tmall.com",
               "shop_id": "294441628",
               "seller_id": "3395424870"
           },
           "?????????????????????": {
               "shopUrl": "//yeehooformybaby.tmall.com",
               "shop_id": "60371054",
               "seller_id": "366168649"
           },
           "?????????????????????": {
               "shopUrl": "//pepco.tmall.com",
               "shop_id": "60648292",
               "seller_id": "379773991"
           },
           "????????????????????????": {
               "shopUrl": "//mlatin.tmall.com",
               "shop_id": "62379610",
               "seller_id": "470348031"
           },
           "??????????????????": {
               "shopUrl": "//fivepeas.tmall.com",
               "shop_id": "62541496",
               "seller_id": "485619069"
           },
           "????????????????????????": {
               "shopUrl": "//balabala.tmall.com",
               "shop_id": "63734363",
               "seller_id": "642320867"
           },
           "pptown?????????": {
               "shopUrl": "//pptown.tmall.com",
               "shop_id": "66840726",
               "seller_id": "708193560"
           },
           "davebella?????????": {
               "shopUrl": "//davebella.tmall.com",
               "shop_id": "70263793",
               "seller_id": "821690375"
           },
           "???????????????????????????": {
               "shopUrl": "//bubufaxian.tmall.com",
               "shop_id": "72780288",
               "seller_id": "925721517"
           },
           "???????????????": {
               "shopUrl": "//deesha.tmall.com",
               "shop_id": "57300079",
               "seller_id": "94395476"
           },
           "???????????????": {
               "shopUrl": "//yanyu.tmall.com",
               "shop_id": "73152092",
               "seller_id": "1020209367"
           },
           "???????????????": {
               "shopUrl": "//inman.tmall.com",
               "shop_id": "57301243",
               "seller_id": "130974249"
           },
           "???????????????": {
               "shopUrl": "//roeyshouse.tmall.com",
               "shop_id": "57301382",
               "seller_id": "133708381"
           },
           "??????????????????": {
               "shopUrl": "//caidaifei.tmall.com",
               "shop_id": "109701531",
               "seller_id": "2037787891"
           },
           "UR???????????????": {
               "shopUrl": "//urfs.tmall.com",
               "shop_id": "111020545",
               "seller_id": "2104668892"
           },
           "Massimo Dutti???????????????": {
               "shopUrl": "//massimodutti.tmall.com",
               "shop_id": "113272316",
               "seller_id": "2183380830"
           },
           "rumere?????????": {
               "shopUrl": "//rumere.tmall.com",
               "shop_id": "113074026",
               "seller_id": "2210369896"
           },
           "dfvc?????????": {
               "shopUrl": "//dfvc.tmall.com",
               "shop_id": "114747456",
               "seller_id": "2273197995"
           },
           "?????????????????????": {
               "shopUrl": "//fashionline.tmall.com",
               "shop_id": "58501607",
               "seller_id": "263805063"
           },
           "UR DADA???????????????": {
               "shopUrl": "//urdada.taobao.com",
               "shop_id": "136554844",
               "seller_id": "2672952762"
           },
           "mecity???????????????": {
               "shopUrl": "//mecity.tmall.com",
               "shop_id": "566813579",
               "seller_id": "3175325124"
           },
           "HM???????????????": {
               "shopUrl": "//hm.tmall.com",
               "shop_id": "548921262",
               "seller_id": "3676232520"
           },
           "ein?????????": {
               "shopUrl": "//ein.tmall.com",
               "shop_id": "62100927",
               "seller_id": "443465738"
           },
           "yiner???????????????": {
               "shopUrl": "//yiner.tmall.com",
               "shop_id": "62688323",
               "seller_id": "504729396"
           },
           "??????????????????": {
               "shopUrl": "//aishangchen.tmall.com",
               "shop_id": "65119722",
               "seller_id": "675269713"
           },
           "???????????????": {
               "shopUrl": "//xsa.tmall.com",
               "shop_id": "67834222",
               "seller_id": "732288809"
           },
           "?????????????????????": {
               "shopUrl": "//meibanfushi.tmall.com",
               "shop_id": "68046668",
               "seller_id": "737576795"
           },
           "??????????????????": {
               "shopUrl": "//fuluola.tmall.com",
               "shop_id": "70101700",
               "seller_id": "812148330"
           },
           "kuose???????????????": {
               "shopUrl": "//kuose.tmall.com",
               "shop_id": "73232281",
               "seller_id": "1023197390"
           },
           "cachecache?????????": {
               "shopUrl": "//cachecachebmnw.tmall.com",
               "shop_id": "100106353",
               "seller_id": "1041248422"
           },
           "?????????????????????": {
               "shopUrl": "//kuhnmarvin.tmall.com",
               "shop_id": "104124499",
               "seller_id": "1658594886"
           },
           "pullandbear???????????????": {
               "shopUrl": "//pullandbear.tmall.com",
               "shop_id": "106020408",
               "seller_id": "1787625780"
           },
           "???????????????": {
               "shopUrl": "//seenfaan.tmall.com",
               "shop_id": "107444223",
               "seller_id": "1870127567"
           },
           "?????????CATFACE": {
               "shopUrl": "//maojiangzi.taobao.com",
               "shop_id": "108934575",
               "seller_id": "1994593259"
           },
           "materialgirl???????????????": {
               "shopUrl": "//materialgirl.tmall.com",
               "shop_id": "109004689",
               "seller_id": "2002445600"
           },
           "crz?????????": {
               "shopUrl": "//crz.tmall.com",
               "shop_id": "57675838",
               "seller_id": "203872810"
           },
           "omont???????????????": {
               "shopUrl": "//omont.tmall.com",
               "shop_id": "110441637",
               "seller_id": "2075892917"
           },
           "??????????????????": {
               "shopUrl": "//bigeve8.taobao.com",
               "shop_id": "111126855",
               "seller_id": "2103587316"
           },
           "??????????????????": {
               "shopUrl": "//liangsanshi.tmall.com",
               "shop_id": "60261884",
               "seller_id": "360512874"
           },
           "??????????????? YESIAMXIAOG": {
               "shopUrl": "//xiaoguli.taobao.com",
               "shop_id": "65626181",
               "seller_id": "380101244"
           },
           "????????????": {
               "shopUrl": "//neato.taobao.com",
               "shop_id": "61383051",
               "seller_id": "388826934"
           },
           "ONE MORE": {
               "shopUrl": "//shop71858911.taobao.com",
               "shop_id": "71858911",
               "seller_id": "417132578"
           },
           "MG??????????????????????????????": {
               "shopUrl": "//mgxxjia.taobao.com",
               "shop_id": "64185146",
               "seller_id": "479184430"
           },
           "???????????????": {
               "shopUrl": "//qiumai.tmall.com",
               "shop_id": "62560090",
               "seller_id": "488320269"
           },
           "???????????? ????????????????????????": {
               "shopUrl": "//suisui215.taobao.com",
               "shop_id": "63256853",
               "seller_id": "50454948"
           },
           "??????FanoStudios": {
               "shopUrl": "//4--u.taobao.com",
               "shop_id": "73355081",
               "seller_id": "581894172"
           },
           "??????????????????????????????": {
               "shopUrl": "//zhaoyandaxi.taobao.com",
               "shop_id": "73319344",
               "seller_id": "704298669"
           },
           "a02???????????????": {
               "shopUrl": "//a02.tmall.com",
               "shop_id": "70524593",
               "seller_id": "832551907"
           },
           "TeenieWeenie???????????????": {
               "shopUrl": "//teenieweenie.tmall.com",
               "shop_id": "105774025",
               "seller_id": "1771485843"
           },
           "puella???????????????": {
               "shopUrl": "//puella.tmall.com",
               "shop_id": "145901297",
               "seller_id": "2785769724"
           },
           "donoratico??????????????????": {
               "shopUrl": "//donoratico.tmall.com",
               "shop_id": "388223705",
               "seller_id": "2945543028"
           },
           "?????????????????????": {
               "shopUrl": "//psalter.tmall.com",
               "shop_id": "64121476",
               "seller_id": "651856143"
           },
           "??????????????????": {
               "shopUrl": "//vimlylg.tmall.com",
               "shop_id": "65219342",
               "seller_id": "676649324"
           },
           "???????????????": {
               "shopUrl": "//samstree.tmall.com",
               "shop_id": "70592301",
               "seller_id": "835044995"
           },
           "osa?????????????????????": {
               "shopUrl": "//osa.tmall.com",
               "shop_id": "57299937",
               "seller_id": "94153930"
           },
           "????????????????????????": {
               "shopUrl": "//nibbuns.tmall.com",
               "shop_id": "103226456",
               "seller_id": "1652742042"
           },
           "bershka???????????????": {
               "shopUrl": "//bershka.tmall.com",
               "shop_id": "106020458",
               "seller_id": "1787605898"
           },
           "???????????????????????????": {
               "shopUrl": "//nanariji.tmall.com",
               "shop_id": "111554761",
               "seller_id": "2073641741"
           },
           "pass?????????": {
               "shopUrl": "//passfs.tmall.com",
               "shop_id": "112736202",
               "seller_id": "2182013355"
           },
           "jcoolstory?????????": {
               "shopUrl": "//jcoolstory.tmall.com",
               "shop_id": "63090785",
               "seller_id": "556579141"
           },
           "honeys???????????????": {
               "shopUrl": "//honeys.tmall.com",
               "shop_id": "66128301",
               "seller_id": "692726067"
           },
           "cicishop?????????": {
               "shopUrl": "//cicishop.tmall.com",
               "shop_id": "67132586",
               "seller_id": "714256382"
           },
           "forever21???????????????": {
               "shopUrl": "//forever21.tmall.com",
               "shop_id": "69644818",
               "seller_id": "791583018"
           },
           "tyakasha???????????????": {
               "shopUrl": "//tyakasha.tmall.com",
               "shop_id": "70359330",
               "seller_id": "826997706"
           },
           "?????????????????????": {
               "shopUrl": "//etongenius.tmall.com",
               "shop_id": "70488925",
               "seller_id": "831501409"
           }
           }
logging.config.dictConfig(LOGGING)
