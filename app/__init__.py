from dotenv import load_dotenv
import os

# 🔑 LOAD ENV PALING PERTAMA (WAJIB)
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

from flask import Flask, request  # noqa: E402
from .config import Config        # noqa: E402
from .extensions import db, migrate  # noqa: E402

from app import models  # noqa: F401, E402

from app.middleware.auth_session import auth_session  # noqa: E402
from app.middleware.session_guard import session_guard  # noqa: E402
from app.middleware.block_if_locked import block_if_locked  # noqa: E402

from .routes.health import bp as health_bp  # noqa: E402
from .routes.auth import bp as auth_bp  # noqa: E402
from app.routes.surveyor import bp as surveyor_bp  # noqa: E402
from app.routes.koordinator import bp as koordinator_bp  # noqa: E402
from app.routes.admin import bp as admin_bp  # noqa: E402


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(surveyor_bp)
    app.register_blueprint(koordinator_bp)
    app.register_blueprint(admin_bp)

    # ============================
    # GLOBAL REQUEST GUARD
    # ============================
    @app.before_request
    def global_guard():
        if request.endpoint in (
            "auth.login",
            "health.health",
        ):
            return

        auth_session()
        session_guard()
        block_if_locked()

    return app
