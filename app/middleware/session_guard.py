from flask import session, abort
from app.models.user import User


def session_guard():
    user = User.query.get(session.get("user_id"))
    if not user or user.deleted_at is not None:
        session.clear()
        abort(403)
