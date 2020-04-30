import bcrypt as bcrypt

from config import db
from dao.request import Request
from dao.donation import Donation

class User(db.Model):

    uid = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    dateOfBirth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    zipCode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    requests = db.relationship('Request', backref='user', lazy=True)
    donations = db.relationship('Donation', backref='user', lazy=True)
    username = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # user = id, firstname, lastname, email, phone, date_birth, address, city, zipcode, country

    def getAllUsers(self):
        return self.query.all()
    
    def getUserById(self, user_id):
        return self.query.filter_by(uid=user_id)

    def create(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry):
        return uid

    def delete(self, uid):
        return uid