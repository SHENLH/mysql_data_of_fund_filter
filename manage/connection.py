from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from manage.config import DATABASE


def driver(user, passwd, host, port, database):
    engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}?charset=utf8mb4")
    return engine


def default_driver():
    engine = driver(**DATABASE)
    return engine


def make_session(_driver):
    session = sessionmaker(bind=_driver)
    return session


def make_default_session():
    _driver = default_driver()
    session = make_session(_driver)
    return session


