import sqlalchemy as db
from sqlalchemy.orm import relationship
from manage.models.model import BASE, Model


class Classify(BASE, Model):
    __tablename__ = "t_ff_classify"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    windcode = db.Column(db.String(10), db.ForeignKey('t_ff_funds.windcode'), nullable=False)
    branch = db.Column(db.String(10), nullable=False)
    classify = db.Column(db.String(20), nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)

    funds = relationship("Funds", backref="classify")

    def __repr__(self):
        return f"<Classify {self.windcode}>"
