from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_graphql import GraphQLView
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    migrate = Migrate(app, db)

    from .models.users import User
    from .models.books import Book
    from .models.loans import Loan
    from .models.reservations import Reservation

    from .routes.books_routes import books_bp
    from .routes.users_routes import users_bp
    from .routes.loans_routes import loans_bp
    from .routes.reservations_routes import reservations_bp

    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(loans_bp)
    app.register_blueprint(reservations_bp)

    from .graphql.schema import schema

    app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    @app.route("/test")
    def test():
        return "Le backend fonctionne !"

    @app.route("/")
    def index():
        from flask import render_template
        return render_template("home.html")

    return app
