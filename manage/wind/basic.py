"""
basic
~~~~~
对应数据库fund_filter_production.t_ff_basic_info，包含基金的基础数据，从Wind提取
"""
from manage.wind import w
from manage.models import BasicInfo


def wss(fund_codes, date):
    data = w.wss(fund_codes,
                 "sec_name,fund_fullname,fund_setupdate,fund_benchmark,fund_corp_fundmanagementcompany,"
                 "fund_investscope,fund_structuredfundornot,fund_firstinvesttype,fund_investtype")
    codes = data.Codes
    data = data.Data
    ret = []
    for i in range(len(codes)):
        bi = BasicInfo(
            windcode=codes[i],
            sec_name=data[0][i],
            fullname=data[1][i],
            setup_date=data[2][i],
            benchmark=data[3][i],
            company=data[4][i],
            invest_scope=data[5][i],
            structured=data[6][i],
            first_invest_type=data[7][i],
            invest_type=data[8][i],
            update_date=date
        )
        ret.append(bi)
    return ret
