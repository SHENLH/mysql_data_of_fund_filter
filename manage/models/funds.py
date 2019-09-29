import sqlalchemy as db

from manage.models.model import Model, BASE


class Funds(BASE, Model):
    __tablename__ = "t_ff_funds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    windcode = db.Column(db.String(10), nullable=False, primary_key=True)

    def __repr__(self):
        return f"<Funds {self.windcode}>"
