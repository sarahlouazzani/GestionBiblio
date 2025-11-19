from flask import Blueprint, request, jsonify, render_template
from .. import db
from ..models.reservations import Reservation

reservations_bp = Blueprint("reservations", __name__, url_prefix="/reservations")

@reservations_bp.route("/page", methods=["GET"])
def reservations_page():
    return render_template("reservations.html")

@reservations_bp.route("/", methods=["GET"])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{
        "id": r.id,
        "book_id": r.book_id,
        "user_id": r.user_id,
        "date_reserved": r.date_reserved,
        "status": r.status
    } for r in reservations])

@reservations_bp.route("/", methods=["POST"])
def add_reservation():
    data = request.json
    try:
        with db.session.begin():
            new_reservation = Reservation(
                book_id=data["book_id"],
                user_id=data["user_id"]
            )
            db.session.add(new_reservation)
        return jsonify({"message": "Réservation enregistrée", "reservation_id": new_reservation.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@reservations_bp.route("/<int:reservation_id>", methods=["PUT"])
def update_reservation(reservation_id):
    data = request.json
    try:
        with db.session.begin():
            reservation = Reservation.query.get_or_404(reservation_id)
            reservation.status = data.get("status", reservation.status)
        return jsonify({"message": "Réservation mise à jour"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@reservations_bp.route("/<int:reservation_id>", methods=["DELETE"])
def delete_reservation(reservation_id):
    try:
        with db.session.begin():
            reservation = Reservation.query.get_or_404(reservation_id)
            db.session.delete(reservation)
        return jsonify({"message": "Réservation supprimée"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
