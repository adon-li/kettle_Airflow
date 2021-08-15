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
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '//'.join([LOG_DIR, 'monitor_default.log']),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
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
    "茵曼":{"address":"13栋1楼前台","name":"行政部曼倩"},
    "初语":{"address":"12栋南梯7楼","name":"供应链管理办公室艾莉"}
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
SHOP_ID = {'茵曼童装旗舰店': {'shop_id': 142198236, 'seller_id': 2719809625},
           '生活在左旗舰店': {'shop_id': 108231462, 'seller_id': 1947403838},
           '达丽坊服饰旗舰店': {'shop_id': 66984172, 'seller_id': 710608278},
           'pass旗舰店': {'shop_id': 112736202, 'seller_id': 2182013355},
           'samyama旗舰店': {'shop_id': 115394119, 'seller_id': 2249377411},
           '水生之城': {'shop_id': 60553320, 'seller_id': 375594758},
           '初语旗舰店': {'shop_id': 68905897, 'seller_id': 761679524},
           '秋壳旗舰店': {'shop_id': 62560090, 'seller_id': 488320269},
           '初语童装旗舰店': {'shop_id': 126813856, 'seller_id': 2579790840},
           '茵曼家具旗舰店': {'shop_id': 136852150, 'seller_id': 2587984881},
           '茵曼旗舰店': {'shop_id': 57301243, 'seller_id': 130974249},
           '茵曼箱包旗舰店': {'shop_id': 108443046, 'seller_id': 1965714898},
           "茵曼服饰配件旗舰店":{'shop_id':108357058,'seller_id':1957567118},
           "iumi旗舰店": {
               "shopUrl": "//iumi.tmall.com",
               "shop_id": "73151152",
               "seller_id": "1019292692"
           },
           "zk旗舰店": {
               "shopUrl": "//zknz.tmall.com",
               "shop_id": "100163346",
               "seller_id": "1044264726"
           },
           "太平鸟官方旗舰店": {
               "shopUrl": "//pb89.tmall.com",
               "shop_id": "57300711",
               "seller_id": "112394247"
           },
           "maxmartin玛玛绨旗舰店": {
               "shopUrl": "//maxmartin.tmall.com",
               "shop_id": "103047260",
               "seller_id": "1644880265"
           },
           "戚米旗舰店": {
               "shopUrl": "//qimi.tmall.com",
               "shop_id": "105779984",
               "seller_id": "1766047907"
           },
           "ELAND官方旗舰店": {
               "shopUrl": "//eland.tmall.com",
               "shop_id": "105788454",
               "seller_id": "1770528988"
           },
           "对白旗舰店": {
               "shopUrl": "//duibai.tmall.com",
               "shop_id": "107329277",
               "seller_id": "1870451655"
           },
           "优衣库官方旗舰店": {
               "shopUrl": "//uniqlo.tmall.com",
               "shop_id": "57303596",
               "seller_id": "196993935"
           },
           "拉夏贝尔官方旗舰": {
               "shopUrl": "//lachapelle.tmall.com",
               "shop_id": "111717832",
               "seller_id": "2146742267"
           },
           "ZARA官方旗舰店": {
               "shopUrl": "//zara.tmall.com",
               "shop_id": "113462750",
               "seller_id": "2228361831"
           },
           "裂帛服饰旗舰店": {
               "shopUrl": "//ripfs.tmall.com",
               "shop_id": "58014452",
               "seller_id": "228784630"
           },
           "韩都衣舍旗舰店": {
               "shopUrl": "//handuyishe.tmall.com",
               "shop_id": "58501945",
               "seller_id": "263817957"
           },
           "ochirly官方旗舰店": {
               "shopUrl": "//ochirly.tmall.com",
               "shop_id": "58674200",
               "seller_id": "272205633"
           },
           "ONLY官方旗舰店": {
               "shopUrl": "//only.tmall.com",
               "shop_id": "60129786",
               "seller_id": "356060330"
           },
           "妖精的口袋旗舰店": {
               "shopUrl": "//yaojingdekoudai.tmall.com",
               "shop_id": "60300724",
               "seller_id": "362409818"
           },
           "七格格旗舰店": {
               "shopUrl": "//othermix.tmall.com",
               "shop_id": "61054779",
               "seller_id": "394695430"
           },
           "森马官方旗舰店": {
               "shopUrl": "//semir.tmall.com",
               "shop_id": "61127277",
               "seller_id": "397341302"
           },
           "逸阳旗舰店": {
               "shopUrl": "//esey.tmall.com",
               "shop_id": "61412736",
               "seller_id": "408107205"
           },
           "veromoda官方旗舰店": {
               "shopUrl": "//veromoda.tmall.com",
               "shop_id": "61773004",
               "seller_id": "420567757"
           },
           "artka官方旗舰店": {
               "shopUrl": "//artka.tmall.com",
               "shop_id": "62112343",
               "seller_id": "444076877"
           },
           "amii旗舰店": {
               "shopUrl": "//amii.tmall.com",
               "shop_id": "62195084",
               "seller_id": "451135386"
           },
           "乐町官方旗舰店": {
               "shopUrl": "//leting.tmall.com",
               "shop_id": "62767848",
               "seller_id": "513051429"
           },
           "moco官方旗舰店": {
               "shopUrl": "//moco.tmall.com",
               "shop_id": "63240547",
               "seller_id": "581746910"
           },
           "伊芙丽官方旗舰": {
               "shopUrl": "//eifini.tmall.com",
               "shop_id": "63721895",
               "seller_id": "641725918"
           },
           "fiveplus官方旗舰店": {
               "shopUrl": "//fiveplus.tmall.com",
               "shop_id": "65707026",
               "seller_id": "685140573"
           },
           "艾格官方旗舰店": {
               "shopUrl": "//etam.tmall.com",
               "shop_id": "66961931",
               "seller_id": "710962071"
           },
           "哥弟官方旗舰店": {
               "shopUrl": "//girdear.tmall.com",
               "shop_id": "67694825",
               "seller_id": "728443962"
           },
           "初语旗舰店": {
               "shopUrl": "//chuyu.tmall.com",
               "shop_id": "68905897",
               "seller_id": "761679524"
           },
           "衣品天成女装旗舰店": {
               "shopUrl": "//eptisonfs.tmall.com",
               "shop_id": "69906704",
               "seller_id": "803368268"
           },
           "初棉旗舰店": {
               "shopUrl": "//chumian.tmall.com",
               "shop_id": "72455858",
               "seller_id": "912835464"
           },
           "lrud旗舰店": {
               "shopUrl": "//lrud.tmall.com",
               "shop_id": "114461749",
               "seller_id": "2264201946"
           },
           "治木工坊旗舰店": {
               "shopUrl": "//zhimugongfang.tmall.com",
               "shop_id": "73402183",
               "seller_id": "1030778510"
           },
           "家逸旗舰店": {
               "shopUrl": "//jiayijjyp.tmall.com",
               "shop_id": "100668426",
               "seller_id": "1066329044"
           },
           "源氏木语家居旗舰店": {
               "shopUrl": "//yuanshimuyu.tmall.com",
               "shop_id": "101529349",
               "seller_id": "1105025069"
           },
           "林氏木业家具旗舰店": {
               "shopUrl": "//lshmy.tmall.com",
               "shop_id": "57301625",
               "seller_id": "143584903"
           },
           "哥帕菲家居旗舰店": {
               "shopUrl": "//gepafei.tmall.com",
               "shop_id": "103704802",
               "seller_id": "1642946911"
           },
           "美克美家官方旗舰店": {
               "shopUrl": "//meikemeijia.tmall.com",
               "shop_id": "103404629",
               "seller_id": "1660593285"
           },
           "麦田家居旗舰店": {
               "shopUrl": "//maitian.tmall.com",
               "shop_id": "105735987",
               "seller_id": "1772995108"
           },
           "华谊家具旗舰店": {
               "shopUrl": "//huayijiaju.tmall.com",
               "shop_id": "106444345",
               "seller_id": "1819934535"
           },
           "茵曼女鞋旗舰店": {
               "shopUrl": "//inmannx.tmall.com",
               "shop_id": "107160445",
               "seller_id": "1835235939"
           },
           "家居源家具旗舰店": {
               "shopUrl": "//customizedfurniture.tmall.com",
               "shop_id": "108143912",
               "seller_id": "1911411704"
           },
           "二黑木作": {
               "shopUrl": "//tooblack.taobao.com",
               "shop_id": "113767108",
               "seller_id": "2228290021"
           },
           "luckysac旗舰店": {
               "shopUrl": "//luckysac.tmall.com",
               "shop_id": "114446876",
               "seller_id": "2289469223"
           },
           "MUMO木墨": {
               "shopUrl": "//mumolife.taobao.com",
               "shop_id": "34059034",
               "seller_id": "23739472"
           },
           "茵曼内衣旗舰店": {
               "shopUrl": "//inmanny.tmall.com",
               "shop_id": "177176098",
               "seller_id": "2996366394"
           },
           "ZAOZUO旗舰店": {
               "shopUrl": "//zaozuo.tmall.com",
               "shop_id": "266324282",
               "seller_id": "3017251987"
           },
           "名门匠橡旗舰店": {
               "shopUrl": "//mingmenjiangxiang.tmall.com",
               "shop_id": "404070660",
               "seller_id": "3051910325"
           },
           "青岛一木旗舰店": {
               "shopUrl": "//qingdaoyimu.tmall.com",
               "shop_id": "189769877",
               "seller_id": "3191764880"
           },
           "摩登主妇生活馆": {
               "shopUrl": "//mdzf.taobao.com",
               "shop_id": "61739784",
               "seller_id": "413996455"
           },
           "永益饰佳旗舰店": {
               "shopUrl": "//yysj.tmall.com",
               "shop_id": "62269246",
               "seller_id": "459805913"
           },
           "维莎旗舰店": {
               "shopUrl": "//weisha.tmall.com",
               "shop_id": "62377351",
               "seller_id": "470164086"
           },
           "北欧表情家居NORHOR": {
               "shopUrl": "//norho.taobao.com",
               "shop_id": "50035",
               "seller_id": "50035"
           },
           "胖橙子布艺": {
               "shopUrl": "//ofat.taobao.com",
               "shop_id": "69071116",
               "seller_id": "689730212"
           },
           "原始原素家居旗舰店": {
               "shopUrl": "//yuanshiyuansu.tmall.com",
               "shop_id": "68814207",
               "seller_id": "758744253"
           },
           "光明家具旗舰店": {
               "shopUrl": "//guangming.tmall.com",
               "shop_id": "70293189",
               "seller_id": "822939859"
           },
           "优梵艺术旗舰店": {
               "shopUrl": "//uvanart.tmall.com",
               "shop_id": "71539955",
               "seller_id": "872353151"
           },
           "唯妮美旗舰店": {
               "shopUrl": "//weinimei.tmall.com",
               "shop_id": "71830600",
               "seller_id": "885152160"
           },
           "HarborHouse家居旗舰店": {
               "shopUrl": "//harborhouse.tmall.com",
               "shop_id": "57299751",
               "seller_id": "92668878"
           },
           "三彩官方旗舰店": {
               "shopUrl": "//threecolour.tmall.com",
               "shop_id": "68368000",
               "seller_id": "745475881"
           },
           "金狐狸旗舰店": {
               "shopUrl": "//jinhuli.tmall.com",
               "shop_id": "73308575",
               "seller_id": "1026415371"
           },
           "莱夫箱包旗舰店": {
               "shopUrl": "//laifu.tmall.com",
               "shop_id": "100179231",
               "seller_id": "1044713328"
           },
           "米熙箱包旗舰店": {
               "shopUrl": "//mixixb.tmall.com",
               "shop_id": "101283724",
               "seller_id": "1094577300"
           },
           "欧时纳箱包旗舰店": {
               "shopUrl": "//juststar.tmall.com",
               "shop_id": "101691052",
               "seller_id": "1113077706"
           },
           "山水集旗舰店": {
               "shopUrl": "//shanshuiji.tmall.com",
               "shop_id": "101720656",
               "seller_id": "1114645587"
           },
           "伊米妮旗舰店": {
               "shopUrl": "//emini.tmall.com",
               "shop_id": "57301011",
               "seller_id": "122343103"
           },
           "aza旗舰店": {
               "shopUrl": "//azams.tmall.com",
               "shop_id": "57301524",
               "seller_id": "138468814"
           },
           "蓝舞旗舰店": {
               "shopUrl": "//lanwu.tmall.com",
               "shop_id": "105956654",
               "seller_id": "1685377206"
           },
           "万达名品箱包": {
               "shopUrl": "//shop129660120.taobao.com",
               "shop_id": "129660120",
               "seller_id": "1796102966"
           },
           "菲妮诗旗舰店": {
               "shopUrl": "//fanice.tmall.com",
               "shop_id": "107692780",
               "seller_id": "1894907077"
           },
           "wolfhorse箱包旗舰店": {
               "shopUrl": "//wolfhorse.tmall.com",
               "shop_id": "110455091",
               "seller_id": "2076567689"
           },
           "千姿百袋旗舰店": {
               "shopUrl": "//qianzibaidai.tmall.com",
               "shop_id": "60237200",
               "seller_id": "359484699"
           },
           "Hello 宅小姐": {
               "shopUrl": "//shop127404863.taobao.com",
               "shop_id": "127404863",
               "seller_id": "60817262"
           },
           "mracehomme旗舰店": {
               "shopUrl": "//mracehomme.tmall.com",
               "shop_id": "63538579",
               "seller_id": "617642921"
           },
           "拉菲斯汀旗舰店": {
               "shopUrl": "//lafestin.tmall.com",
               "shop_id": "67173900",
               "seller_id": "714688689"
           },
           "朱尔旗舰店": {
               "shopUrl": "//zooler.tmall.com",
               "shop_id": "67464350",
               "seller_id": "722491027"
           },
           "pmsix旗舰店": {
               "shopUrl": "//pmsix.tmall.com",
               "shop_id": "67484711",
               "seller_id": "723038269"
           },
           "木村耀司旗舰店": {
               "shopUrl": "//mcysjpn.tmall.com",
               "shop_id": "68472907",
               "seller_id": "748793950"
           },
           "aspensport旗舰店": {
               "shopUrl": "//aspensport.tmall.com",
               "shop_id": "68521767",
               "seller_id": "749711636"
           },
           "jansport旗舰店": {
               "shopUrl": "//jansport.tmall.com",
               "shop_id": "70002657",
               "seller_id": "807956257"
           },
           "小象包袋箱包旗舰店": {
               "shopUrl": "//xiaoxiangbaodai.tmall.com",
               "shop_id": "70276118",
               "seller_id": "822457842"
           },
           "artmi旗舰店": {
               "shopUrl": "//artmi.tmall.com",
               "shop_id": "70294401",
               "seller_id": "823258756"
           },
           "简佰格旗舰店": {
               "shopUrl": "//jonbag.tmall.com",
               "shop_id": "70428876",
               "seller_id": "829250210"
           },
           "铭佳童话旗舰店": {
               "shopUrl": "//mingjiatonghua.tmall.com",
               "shop_id": "73519871",
               "seller_id": "1036144608"
           },
           "米奇丁当旗舰店": {
               "shopUrl": "//miqidida.tmall.com",
               "shop_id": "73523732",
               "seller_id": "1036640987"
           },
           "米妮哈鲁童装旗舰店": {
               "shopUrl": "//minizaru.tmall.com",
               "shop_id": "100705598",
               "seller_id": "1067628403"
           },
           "棉叔叔旗舰店": {
               "shopUrl": "//mianshushu.tmall.com",
               "shop_id": "103963858",
               "seller_id": "1655415934"
           },
           "minipeace旗舰店": {
               "shopUrl": "//minipeace.tmall.com",
               "shop_id": "103871164",
               "seller_id": "1683598224"
           },
           "jnbybyjnby旗舰店": {
               "shopUrl": "//jnbybyjnby.tmall.com",
               "shop_id": "103891671",
               "seller_id": "1684548055"
           },
           "铅笔俱乐部童装旗舰店": {
               "shopUrl": "//pencilclub.tmall.com",
               "shop_id": "104447871",
               "seller_id": "1690429904"
           },
           "千趣会官方旗舰店": {
               "shopUrl": "//senshukaimy.tmall.com",
               "shop_id": "105947989",
               "seller_id": "1743112933"
           },
           "船鼠旗舰店": {
               "shopUrl": "//chuanshu.tmall.com",
               "shop_id": "105507988",
               "seller_id": "1744940626"
           },
           "honeypig旗舰店": {
               "shopUrl": "//honeypig.tmall.com",
               "shop_id": "114635358",
               "seller_id": "1920070699"
           },
           "裂帛童装旗舰店": {
               "shopUrl": "//liebo.tmall.com",
               "shop_id": "110917163",
               "seller_id": "2098876698"
           },
           "lavi旗舰店": {
               "shopUrl": "//lavimy.tmall.com",
               "shop_id": "111875620",
               "seller_id": "2108082193"
           },
           "骆驼童装旗舰店": {
               "shopUrl": "//luotuotz.tmall.com",
               "shop_id": "111963326",
               "seller_id": "2122324108"
           },
           "osa童装旗舰店": {
               "shopUrl": "//osatz.tmall.com",
               "shop_id": "112659507",
               "seller_id": "2165643600"
           },
           "安奈儿旗舰店": {
               "shopUrl": "//annil.tmall.com",
               "shop_id": "58105291",
               "seller_id": "240252102"
           },
           "初语童装旗舰店": {
               "shopUrl": "//chuyutz.tmall.com",
               "shop_id": "126813856",
               "seller_id": "2579790840"
           },
           "amii童装旗舰店": {
               "shopUrl": "//amiitz.tmall.com",
               "shop_id": "154916672",
               "seller_id": "2863720993"
           },
           "蒙蒙摩米旗舰店": {
               "shopUrl": "//mesamis.tmall.com",
               "shop_id": "156093513",
               "seller_id": "2878663563"
           },
           "韩都衣舍童装旗舰店": {
               "shopUrl": "//handuyishetz.tmall.com",
               "shop_id": "165619466",
               "seller_id": "2934594227"
           },
           "玛玛绨童装旗舰店": {
               "shopUrl": "//mamati.tmall.com",
               "shop_id": "294441628",
               "seller_id": "3395424870"
           },
           "英氏官方旗舰店": {
               "shopUrl": "//yeehooformybaby.tmall.com",
               "shop_id": "60371054",
               "seller_id": "366168649"
           },
           "小猪班纳旗舰店": {
               "shopUrl": "//pepco.tmall.com",
               "shop_id": "60648292",
               "seller_id": "379773991"
           },
           "马拉丁官方旗舰店": {
               "shopUrl": "//mlatin.tmall.com",
               "shop_id": "62379610",
               "seller_id": "470348031"
           },
           "五粒豆旗舰店": {
               "shopUrl": "//fivepeas.tmall.com",
               "shop_id": "62541496",
               "seller_id": "485619069"
           },
           "巴拉巴拉官方旗舰": {
               "shopUrl": "//balabala.tmall.com",
               "shop_id": "63734363",
               "seller_id": "642320867"
           },
           "pptown旗舰店": {
               "shopUrl": "//pptown.tmall.com",
               "shop_id": "66840726",
               "seller_id": "708193560"
           },
           "davebella旗舰店": {
               "shopUrl": "//davebella.tmall.com",
               "shop_id": "70263793",
               "seller_id": "821690375"
           },
           "布布发现童装旗舰店": {
               "shopUrl": "//bubufaxian.tmall.com",
               "shop_id": "72780288",
               "seller_id": "925721517"
           },
           "笛莎旗舰店": {
               "shopUrl": "//deesha.tmall.com",
               "shop_id": "57300079",
               "seller_id": "94395476"
           },
           "颜域旗舰店": {
               "shopUrl": "//yanyu.tmall.com",
               "shop_id": "73152092",
               "seller_id": "1020209367"
           },
           "茵曼旗舰店": {
               "shopUrl": "//inman.tmall.com",
               "shop_id": "57301243",
               "seller_id": "130974249"
           },
           "罗衣旗舰店": {
               "shopUrl": "//roeyshouse.tmall.com",
               "shop_id": "57301382",
               "seller_id": "133708381"
           },
           "彩黛妃旗舰店": {
               "shopUrl": "//caidaifei.tmall.com",
               "shop_id": "109701531",
               "seller_id": "2037787891"
           },
           "UR官方旗舰店": {
               "shopUrl": "//urfs.tmall.com",
               "shop_id": "111020545",
               "seller_id": "2104668892"
           },
           "Massimo Dutti官方旗舰店": {
               "shopUrl": "//massimodutti.tmall.com",
               "shop_id": "113272316",
               "seller_id": "2183380830"
           },
           "rumere旗舰店": {
               "shopUrl": "//rumere.tmall.com",
               "shop_id": "113074026",
               "seller_id": "2210369896"
           },
           "dfvc旗舰店": {
               "shopUrl": "//dfvc.tmall.com",
               "shop_id": "114747456",
               "seller_id": "2273197995"
           },
           "范思蓝恩旗舰店": {
               "shopUrl": "//fashionline.tmall.com",
               "shop_id": "58501607",
               "seller_id": "263805063"
           },
           "UR DADA搭配师品牌": {
               "shopUrl": "//urdada.taobao.com",
               "shop_id": "136554844",
               "seller_id": "2672952762"
           },
           "mecity女装旗舰店": {
               "shopUrl": "//mecity.tmall.com",
               "shop_id": "566813579",
               "seller_id": "3175325124"
           },
           "HM官方旗舰店": {
               "shopUrl": "//hm.tmall.com",
               "shop_id": "548921262",
               "seller_id": "3676232520"
           },
           "ein旗舰店": {
               "shopUrl": "//ein.tmall.com",
               "shop_id": "62100927",
               "seller_id": "443465738"
           },
           "yiner官方旗舰店": {
               "shopUrl": "//yiner.tmall.com",
               "shop_id": "62688323",
               "seller_id": "504729396"
           },
           "艾尚臣旗舰店": {
               "shopUrl": "//aishangchen.tmall.com",
               "shop_id": "65119722",
               "seller_id": "675269713"
           },
           "橡莎旗舰店": {
               "shopUrl": "//xsa.tmall.com",
               "shop_id": "67834222",
               "seller_id": "732288809"
           },
           "魅斑服饰旗舰店": {
               "shopUrl": "//meibanfushi.tmall.com",
               "shop_id": "68046668",
               "seller_id": "737576795"
           },
           "弗洛拉旗舰店": {
               "shopUrl": "//fuluola.tmall.com",
               "shop_id": "70101700",
               "seller_id": "812148330"
           },
           "kuose阔色旗舰店": {
               "shopUrl": "//kuose.tmall.com",
               "shop_id": "73232281",
               "seller_id": "1023197390"
           },
           "cachecache旗舰店": {
               "shopUrl": "//cachecachebmnw.tmall.com",
               "shop_id": "100106353",
               "seller_id": "1041248422"
           },
           "库恩玛维旗舰店": {
               "shopUrl": "//kuhnmarvin.tmall.com",
               "shop_id": "104124499",
               "seller_id": "1658594886"
           },
           "pullandbear官方旗舰店": {
               "shopUrl": "//pullandbear.tmall.com",
               "shop_id": "106020408",
               "seller_id": "1787625780"
           },
           "盛放旗舰店": {
               "shopUrl": "//seenfaan.tmall.com",
               "shop_id": "107444223",
               "seller_id": "1870127567"
           },
           "猫酱紫CATFACE": {
               "shopUrl": "//maojiangzi.taobao.com",
               "shop_id": "108934575",
               "seller_id": "1994593259"
           },
           "materialgirl官方旗舰店": {
               "shopUrl": "//materialgirl.tmall.com",
               "shop_id": "109004689",
               "seller_id": "2002445600"
           },
           "crz旗舰店": {
               "shopUrl": "//crz.tmall.com",
               "shop_id": "57675838",
               "seller_id": "203872810"
           },
           "omont服饰旗舰店": {
               "shopUrl": "//omont.tmall.com",
               "shop_id": "110441637",
               "seller_id": "2075892917"
           },
           "吾欢喜的衣橱": {
               "shopUrl": "//bigeve8.taobao.com",
               "shop_id": "111126855",
               "seller_id": "2103587316"
           },
           "两三事旗舰店": {
               "shopUrl": "//liangsanshi.tmall.com",
               "shop_id": "60261884",
               "seller_id": "360512874"
           },
           "小谷粒女装 YESIAMXIAOG": {
               "shopUrl": "//xiaoguli.taobao.com",
               "shop_id": "65626181",
               "seller_id": "380101244"
           },
           "逆光女装": {
               "shopUrl": "//neato.taobao.com",
               "shop_id": "61383051",
               "seller_id": "388826934"
           },
           "ONE MORE": {
               "shopUrl": "//shop71858911.taobao.com",
               "shop_id": "71858911",
               "seller_id": "417132578"
           },
           "MG小象欧美街拍时尚女装": {
               "shopUrl": "//mgxxjia.taobao.com",
               "shop_id": "64185146",
               "seller_id": "479184430"
           },
           "秋壳旗舰店": {
               "shopUrl": "//qiumai.tmall.com",
               "shop_id": "62560090",
               "seller_id": "488320269"
           },
           "梅子熟了 文艺复古清新女装": {
               "shopUrl": "//suisui215.taobao.com",
               "shop_id": "63256853",
               "seller_id": "50454948"
           },
           "范洛FanoStudios": {
               "shopUrl": "//4--u.taobao.com",
               "shop_id": "73355081",
               "seller_id": "581894172"
           },
           "大喜自制独立复古女装": {
               "shopUrl": "//zhaoyandaxi.taobao.com",
               "shop_id": "73319344",
               "seller_id": "704298669"
           },
           "a02官方旗舰店": {
               "shopUrl": "//a02.tmall.com",
               "shop_id": "70524593",
               "seller_id": "832551907"
           },
           "TeenieWeenie官方旗舰店": {
               "shopUrl": "//teenieweenie.tmall.com",
               "shop_id": "105774025",
               "seller_id": "1771485843"
           },
           "puella官方旗舰店": {
               "shopUrl": "//puella.tmall.com",
               "shop_id": "145901297",
               "seller_id": "2785769724"
           },
           "donoratico达衣岩旗舰店": {
               "shopUrl": "//donoratico.tmall.com",
               "shop_id": "388223705",
               "seller_id": "2945543028"
           },
           "诗篇官方旗舰店": {
               "shopUrl": "//psalter.tmall.com",
               "shop_id": "64121476",
               "seller_id": "651856143"
           },
           "梵希蔓旗舰店": {
               "shopUrl": "//vimlylg.tmall.com",
               "shop_id": "65219342",
               "seller_id": "676649324"
           },
           "森宿旗舰店": {
               "shopUrl": "//samstree.tmall.com",
               "shop_id": "70592301",
               "seller_id": "835044995"
           },
           "osa品牌服饰旗舰店": {
               "shopUrl": "//osa.tmall.com",
               "shop_id": "57299937",
               "seller_id": "94153930"
           },
           "尼班诗官方旗舰店": {
               "shopUrl": "//nibbuns.tmall.com",
               "shop_id": "103226456",
               "seller_id": "1652742042"
           },
           "bershka官方旗舰店": {
               "shopUrl": "//bershka.tmall.com",
               "shop_id": "106020458",
               "seller_id": "1787605898"
           },
           "娜娜日记官方旗舰店": {
               "shopUrl": "//nanariji.tmall.com",
               "shop_id": "111554761",
               "seller_id": "2073641741"
           },
           "pass旗舰店": {
               "shopUrl": "//passfs.tmall.com",
               "shop_id": "112736202",
               "seller_id": "2182013355"
           },
           "jcoolstory旗舰店": {
               "shopUrl": "//jcoolstory.tmall.com",
               "shop_id": "63090785",
               "seller_id": "556579141"
           },
           "honeys官方旗舰店": {
               "shopUrl": "//honeys.tmall.com",
               "shop_id": "66128301",
               "seller_id": "692726067"
           },
           "cicishop旗舰店": {
               "shopUrl": "//cicishop.tmall.com",
               "shop_id": "67132586",
               "seller_id": "714256382"
           },
           "forever21官方旗舰店": {
               "shopUrl": "//forever21.tmall.com",
               "shop_id": "69644818",
               "seller_id": "791583018"
           },
           "tyakasha官方旗舰店": {
               "shopUrl": "//tyakasha.tmall.com",
               "shop_id": "70359330",
               "seller_id": "826997706"
           },
           "伊顿珍妮旗舰店": {
               "shopUrl": "//etongenius.tmall.com",
               "shop_id": "70488925",
               "seller_id": "831501409"
           }
           }
logging.config.dictConfig(LOGGING)
