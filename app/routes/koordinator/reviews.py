from . import bp
from app.policy.interview_policy import enforce_interview_policy
from app.audit.logger import log_action


@bp.route("/interviews/<int:id>", methods=["GET"])
def view_interview(id):
    enforce_interview_policy("view", id)
    return {"id": id}


@bp.route("/interviews/<int:id>/verify", methods=["POST"])
def verify_interview(id):
    enforce_interview_policy("verify", id)

    # bussines logic (update status -> verified)

    log_action("verify_interview", id)
    return {"status": "verified"}


@bp.route("/interviews/<int:id>/return", methods=["POST"])
def return_interview(id):
    enforce_interview_policy("return", id)
    return {"status": "returned"}
