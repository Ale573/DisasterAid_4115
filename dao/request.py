import datetime

from config import db


class Request(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    supplyName = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    status = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(100))
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)

    def getAllRequests(self):
        return self.query.all()

    @staticmethod
    def getRequestById(request_id):
        return Request.query.filter_by(rid=request_id)

    def create(self, user):
        user.requests.append(self)
        db.session.commit()
