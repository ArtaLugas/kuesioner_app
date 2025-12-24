from flask import Blueprint
from app.middleware.role_check import require_role

bp = Blueprint("koordinator", __name__, url_prefix="/koordinator")


@bp.before_request
def enforce_koordinator_role():
    require_role("KOOR")


from . import reviews  # noqa: F401, E402
