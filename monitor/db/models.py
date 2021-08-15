from sqlalchemy import Column, Integer, String, Date, DECIMAL, Sequence, DateTime
from db.database import Base


class TbSycmUvSrcEffectsDetail(Base):
    __tablename__ = 'tb_sycm_uv_src_effects_detail'
    __table_args__ = {'schema': 'hmcdata'}
    st_date = Column(String(10), primary_key=True)
    statDate = Column(Integer)
    uv = Column(Integer)
    uv_ratio = Column(Integer)
    item_id = Column(String(141))
    item_pict_url = Column(String(768))
    item_detail_url = Column(String(586))
    item_title = Column(String(768))
    cltItmPayByrCnt = Column(Integer)
    payByrCnt = Column(Integer)
    cartByrCnt = Column(Integer)
    pv = Column(Integer)
    payRate = Column(DECIMAL)
    jpSelfUv = Column(Integer)
    cltCnt = Column(Integer)
    directPayByrCnt = Column(Integer)
    payItmCnt = Column(Integer)
    jpUv = Column(Integer)
    expUv = Column(Integer)
    fansPayByrCnt = Column(Integer)
    ordItmPayByrCnt = Column(Integer)
    crtByrCnt = Column(Integer)
    crtRate = Column(DECIMAL)
    shop_name = Column(String(141))
    shop_id = Column(Integer)
    uni_key = Column(String)

    def __init__(self, st_date=None, statDate=None, uv=None, uv_ratio=None, item_id=None, item_pict_url=None,
                 item_detail_url=None, item_title=None, cltItmPayByrCnt=None, payByrCnt=None, cartByrCnt=None, pv=None,
                 payRate=None, jpSelfUv=None, cltCnt=None, directPayByrCnt=None, payItmCnt=None, jpUv=None, expUv=None,
                 fansPayByrCnt=None, ordItmPayByrCnt=None, crtByrCnt=None, crtRate=None, shop_name=None,
                 shop_id=None, uni_key=None):
        self.st_date = st_date
        self.statDate = statDate
        self.uv = uv
        self.uv_ratio = uv_ratio
        self.item_id = item_id
        self.item_pict_url = item_pict_url
        self.item_detail_url = item_detail_url
        self.item_title = item_title
        self.cltItmPayByrCnt = cltItmPayByrCnt
        self.payByrCnt = payByrCnt
        self.cartByrCnt = cartByrCnt
        self.pv = pv
        self.payRate = payRate
        self.jpSelfUv = jpSelfUv
        self.cltCnt = cltCnt
        self.directPayByrCnt = directPayByrCnt
        self.payItmCnt = payItmCnt
        self.jpUv = jpUv
        self.expUv = expUv
        self.fansPayByrCnt = fansPayByrCnt
        self.ordItmPayByrCnt = ordItmPayByrCnt
        self.crtByrCnt = crtByrCnt
        self.crtRate = crtRate
        self.shop_name = shop_name
        self.shop_id = shop_id
        self.uni_key = uni_key


class StOpShopOnlineEveryMin(Base):
    __tablename__ = 'st_op_shop_online_everymin'
    st_date = Column(String(10), primary_key=True)
    uv_visitors_cnt = Column(Integer)
    pay_trade_amt = Column(DECIMAL)
    platform = Column(String)
    shop_name = Column(String)
    data_src_ = Column(String)
    gmt_modified=Column(String)

    def __init__(self, st_date=None, uv_visitors_cnt=None, pay_trade_amt=None, platform=None, shop_name=None,
                 data_src_=None,gmt_modified=None):
        self.st_date=st_date
        self.uv_visitors_cnt=uv_visitors_cnt
        self.pay_trade_amt=pay_trade_amt
        self.platform=platform
        self.shop_name=shop_name
        self.data_src_=data_src_
        self.gmt_modified=gmt_modified
