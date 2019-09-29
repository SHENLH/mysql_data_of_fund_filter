"""
basic
~~~~~
对应数据库fund_filter_production.t_ff_basic_info，包含基金的基础数据
"""
from manage.query.funds import funds_list
from manage.util import funds_split
from manage.wind.basic import wss
from manage.connection import make_default_session


def funds():
    _funds = funds_list()
    _funds = funds_split(_funds)
    return _funds


def prepare(fund_separated, date):
    data = []
    for separate in fund_separated:
        info = wss(separate, date)
        data.extend(info)
    return data


def insert(date):
    funds_separated = funds()
    data = prepare(funds_separated, date)
    session = make_default_session()()
    session.add_all(data)
    session.commit()
    session.close()


if __name__ == '__main__':
    insert("2019-09-30")
