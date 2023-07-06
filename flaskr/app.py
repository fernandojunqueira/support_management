from flask import Flask

from .extensions import db, migrate
from .routes.customer import bp as customer_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(customer_bp)

    return app