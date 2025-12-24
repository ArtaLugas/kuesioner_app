from flask import session, abort
from app.models.interview import Interview
from app.models.interview_status import InterviewStatus


def enforce_interview_policy(action: str, interview_id: int):
    interview = Interview.query.get(interview_id)
    if not interview:
        abort(404)

    role = session.get("role")
    user_id = session.get("user_id")

    status = InterviewStatus.query.get(interview.status_id)
    status_code = status.code

    # -------- SURVEYOR --------
    if role == "SURV":
        if interview.created_by != user_id:
            abort(403)

        if action == "view":
            return

        if action == "edit":
            if status_code == "DRAFT" and interview.review_started_at is None:
                return

        if action == "submit":
            if status_code == "DRAFT":
                return

        abort(403)

    # -------- KOORDINATOR --------
    if role == "KOOR":
        if action == "view":
            return

        if action == "verify" and status_code == "SUBMITTED":
            return

        if action == "return" and status_code == "VERIFIED":
            return

        abort(403)

    # -------- ADMIN --------
    if role == "ADM":
        if action == "view":
            return

        if action == "verify" and status_code == "SUBMITTED":
            return

        if action == "return" and status_code == "VERIFIED":
            return

        if action == "lock" and status_code == "VERIFIED":
            return

        abort(403)

    abort(403)
