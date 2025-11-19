from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from .. import db
from ..models.users import User

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/page", methods=["GET"])
def users_page():
    return render_template("users.html")

@users_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get("email")).first()
    
    if user and user.check_password(data.get("password")):
        session["user_id"] = user.id
        session["user_name"] = user.name
        session["user_role"] = user.role
        return jsonify({"message": "Connexion réussie", "user": {"name": user.name, "role": user.role}}), 200
    
    return jsonify({"error": "Email ou mot de passe incorrect"}), 401

@users_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Déconnexion réussie"}), 200

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    
    if User.query.filter_by(email=data.get("email")).first():
        return jsonify({"error": "Cet email est déjà utilisé"}), 400
    
    try:
        with db.session.begin():
            new_user = User(
                name=data["name"],
                email=data["email"],
                role=data.get("role", "member")
            )
            new_user.set_password(data["password"])
            db.session.add(new_user)
        return jsonify({"message": "Inscription réussie", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email, "role": u.role} for u in users])

@users_bp.route("/", methods=["POST"])
def add_user():
    data = request.json
    try:
        with db.session.begin():
            new_user = User(
                name=data["name"],
                email=data["email"],
                role=data.get("role","member")
            )
            db.session.add(new_user)
        return jsonify({"message": "Utilisateur ajouté", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    try:
        with db.session.begin():
            user = User.query.get_or_404(user_id)
            user.name = data.get("name", user.name)
            user.email = data.get("email", user.email)
            user.role = data.get("role", user.role)
        return jsonify({"message": "Utilisateur mis à jour"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        with db.session.begin():
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
        return jsonify({"message": "Utilisateur supprimé"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
