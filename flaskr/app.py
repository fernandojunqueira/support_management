from flask import Flask

from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)
    migrate.init_app(app, db)

    return app