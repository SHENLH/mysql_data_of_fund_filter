
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Model(object):
    def to_dict(self):
        items = self.__dict__
        attrs = {}
        for k, v in items.items():
            if k != "_sa_instance_state":
                attrs[k] = v
        return attrs
