from flask import session, abort, request

def role_required(expected_role):
    def wrapper():
        if session.get("role") != expected_role:
            abort(403)
    return wrapper
