from flask import session, abort

def require_role(expected_role):
    if session.get("role") != expected_role:
        abort(403)
