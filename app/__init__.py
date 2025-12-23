from dotenv import load_dotenv
import os

# 🔑 LOAD ENV PERTAMA
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

from flask import Flask, request
from .config import Config
from .extensions import db, migrate

# import models untuk migration
from app import models

# middleware
from app.middleware.auth_session import auth_session
from app.middleware.session_guard import session_guard


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    from .routes.health import bp as health_bp
    from .routes.auth import bp as auth_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)

    # ============================
    # GLOBAL REQUEST GUARD (LOCKED)
    # ============================
    @app.before_request
    def global_guard():
        # whitelist routes
        if request.endpoint in (
            "auth.login",
            "health.health",
        ):
            return

        # 1. AUTH boundary
        auth_session()

        # 2. SESSION guard
        session_guard()

        # role_check & policy
        # → akan ditambahkan di level blueprint / route

    return app