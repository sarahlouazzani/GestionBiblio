from .. import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date_loaned = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    returned = db.Column(db.Boolean, default=False)