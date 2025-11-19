from flask import Blueprint, request, jsonify, render_template
from .. import db
from ..models.loans import Loan
from ..models.books import Book

loans_bp = Blueprint("loans", __name__, url_prefix="/loans")

@loans_bp.route("/page", methods=["GET"])
def loans_page():
    return render_template("loans.html")

@loans_bp.route("/", methods=["GET"])
def get_loans():
    loans = Loan.query.all()
    return jsonify([{
        "id": l.id,
        "book_id": l.book_id,
        "user_id": l.user_id,
        "date_loaned": l.date_loaned,
        "due_date": l.due_date,
        "returned": l.returned
    } for l in loans])

@loans_bp.route("/", methods=["POST"])
def add_loan():
    data = request.json
    try:
        with db.session.begin():
            book = Book.query.get_or_404(data["book_id"])
            if book.stock <= 0:
                return jsonify({"error": "Stock insuffisant"}), 400
            book.stock -= 1
            new_loan = Loan(
                book_id=book.id,
                user_id=data["user_id"],
                due_date=data.get("due_date")
            )
            db.session.add(new_loan)
        return jsonify({"message": "Prêt enregistré", "loan_id": new_loan.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@loans_bp.route("/<int:loan_id>", methods=["PUT"])
def update_loan(loan_id):
    data = request.json
    try:
        with db.session.begin():
            loan = Loan.query.get_or_404(loan_id)
            loan.returned = data.get("returned", loan.returned)
            loan.due_date = data.get("due_date", loan.due_date)
        return jsonify({"message": "Prêt mis à jour"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@loans_bp.route("/<int:loan_id>", methods=["DELETE"])
def delete_loan(loan_id):
    try:
        with db.session.begin():
            loan = Loan.query.get_or_404(loan_id)
            book = Book.query.get(loan.book_id)
            if book:
                book.stock += 1
            db.session.delete(loan)
        return jsonify({"message": "Prêt supprimé"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
