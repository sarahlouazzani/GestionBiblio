from .. import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date_reserved = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="active")

