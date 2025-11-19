from flask import Blueprint, request, jsonify, render_template
from .. import db
from ..models.books import Book

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("/page", methods=["GET"])
def books_page():
    return render_template("books.html")

@books_bp.route("/", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "isbn": b.isbn,
        "stock": b.stock,
        "available": b.available
    } for b in books])

@books_bp.route("/", methods=["POST"])
def add_book():
    data = request.json
    try:
        with db.session.begin():
            new_book = Book(
                title=data["title"],
                author=data["author"],
                isbn=data.get("isbn"),
                stock=data.get("stock", 1),
                available=data.get("available", True)
            )
            db.session.add(new_book)
        return jsonify({"message": "Livre ajouté avec succès", "book_id": new_book.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    try:
        with db.session.begin():
            book = Book.query.get_or_404(book_id)
            book.title = data.get("title", book.title)
            book.author = data.get("author", book.author)
            book.isbn = data.get("isbn", book.isbn)
            book.stock = data.get("stock", book.stock)
            book.available = data.get("available", book.available)
        return jsonify({"message": "Livre mis à jour"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        with db.session.begin():
            book = Book.query.get_or_404(book_id)
            db.session.delete(book)
        return jsonify({"message": "Livre supprimé"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
