from manage.connection import make_default_session
from manage.models import Funds


def funds_list():
    session = make_default_session()()
    ret = session.query(Funds).filter().all()
    ret = [x.windcode for x in ret]
    return ret


if __name__ == '__main__':
    data = funds_list()
    print(len(data))
    print(len(set(data)))
