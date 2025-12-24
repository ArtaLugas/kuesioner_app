from . import bp
from app.policy.interview_policy import enforce_interview_policy
from app.audit.logger import log_action


@bp.route("/interviews/<int:id>", methods=["GET"])
def view_interview(id):
    enforce_interview_policy("view", id)
    return {"id": id}


@bp.route("/interviews/<int:id>/lock", methods=["POST"])
def lock_interview(id):
    enforce_interview_policy("lock", id)

    # bussines logic (update status -> locked)

    log_action("lock_interview", id)
    return {"status": "locked"}
