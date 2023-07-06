from ..extensions import db


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    tickets = db.relationship("Ticket", back_populates='customer')


class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='open')
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship("Customer", back_populates='tickets')