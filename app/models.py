from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    service_items = db.relationship('Service_Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Service_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(64), index=True)
    item_brand = db.Column(db.String(64), index=True)
    item_model = db.Column(db.String(64), index=True)
    serial_num = db.Column(db.Integer, index=True)
    req_serv = db.Column(db.String(64), index=True)
    date_recvd = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Service_Item {self.customer} {self.item_brand} {self.item_model}>'