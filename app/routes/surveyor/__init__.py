from flask import Blueprint
from app.middleware.role_check import require_role

bp = Blueprint("surveyor", __name__, url_prefix="/surveyor")

@bp.before_request
def enforce_surveyor_role():
    require_role("SURV")

# 🔑 WAJIB: import route files
from . import interviews