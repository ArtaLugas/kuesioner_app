from . import bp
from app.policy.interview_policy import enforce_interview_policy
from app.audit.logger import log_action


@bp.route("/interviews", methods=["GET"])
def list_interviews():
    return {"data": []}


@bp.route("/interviews/<int:id>", methods=["GET"])
def view_interview(id):
    enforce_interview_policy("view", id)
    return {"id": id}


@bp.route("/interviews/<int:id>", methods=["PUT"])
def edit_interview(id):
    enforce_interview_policy("edit", id)
    return {"status": "edited"}


@bp.route("/interviews/<int:id>/submit", methods=["POST"])
def submit_interview(id):
    enforce_interview_policy("submit", id)

    # bussines logic (update status -> submitted)

    log_action("submit_interview", id)
    return {"status": "submitted"}
