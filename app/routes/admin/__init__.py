
from flask import Blueprint
from app.middleware.role_check import require_role

bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.before_request
def enforce_admin_role():
    require_role("ADM")


from . import interviews  # noqa: F401, E402
