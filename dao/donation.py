import datetime

from config import db


class Donation(db.Model):
    did = db.Column(db.Integer, primary_key=True)
    supplyName = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    unit = db.Column(db.String(30), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
