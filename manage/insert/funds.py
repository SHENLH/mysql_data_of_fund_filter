from manage.connection import make_default_session
from manage.models import Funds
from manage.wind import funds
from manage.config import UPDATE_DATE


def insert(date=UPDATE_DATE):
    data = funds.csi_open_funds(date)
    data = set(data)
    data = [Funds(windcode=x) for x in data]
    session = make_default_session()()
    session.add_all(data)
    session.commit()
    session.close()


if __name__ == '__main__':
    insert()
