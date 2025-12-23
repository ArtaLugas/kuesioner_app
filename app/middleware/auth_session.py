from flask import session, abort

def auth_session():
    if "user_id" not in session:
        abort(403)