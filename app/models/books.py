from .. import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(20), unique=True)
    stock = db.Column(db.Integer, default=1)
    available = db.Column(db.Boolean, default=True)

    loans = db.relationship("Loan", backref="book", lazy=True)
    reservations = db.relationship("Reservation", backref="book", lazy=True)
