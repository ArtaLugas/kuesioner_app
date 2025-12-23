from flask import Blueprint, request, session, abort
from werkzeug.security import check_password_hash
from app.models.user import User
from app.models.role import UserRole
from app.extensions import db

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        abort(403)

    user = User.query.filter_by(email=email, deleted_at=None).first()
    if not user:
        abort(403)

    if not check_password_hash(user.password_hash, password):
        abort(403)

    role = UserRole.query.get(user.role_id)
    if not role:
        abort(403)

    session.clear()
    session["user_id"] = user.id
    session["role"] = role.code
    session.permanent = True

    return {"status": "ok"}, 200


@bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return {"status": "ok"}, 200