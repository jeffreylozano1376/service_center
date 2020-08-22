from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    service_items = db.relationship('Service_Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'
    # create password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # verify password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

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