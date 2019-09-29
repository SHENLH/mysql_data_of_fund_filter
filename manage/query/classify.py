from manage.connection import make_default_session
from manage.models import Funds

session = make_default_session()()

ret = session.query(Funds).filter(Funds.windcode == "000009.OF").all()[0]
print(ret)
print(ret.classify[0].classify)
print(ret.basic_info[0].benchmark)
