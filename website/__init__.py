import os
import secrets

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def _database_uri() -> str:
    """Use DATABASE_URL (e.g. a hosted Postgres) when set, otherwise a local SQLite file."""
    url = os.environ.get("DATABASE_URL")
    if url:
        # Some providers still hand out the legacy "postgres://" scheme.
        return url.replace("postgres://", "postgresql://", 1)
    return "sqlite:///database.db"  # stored in Flask's instance/ folder


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
    app.config["SQLALCHEMY_DATABASE_URI"] = _database_uri()
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

    db.init_app(app)

    from .auth import auth
    from .models import User
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    return app
