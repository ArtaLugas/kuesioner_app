from flask import request, abort
from app.models.interview import Interview
from app.models.interview_status import InterviewStatus

WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}


def block_if_locked():
    # READ selalu boleh
    if request.method not in WRITE_METHODS:
        return

    # Ambil interview_id dari URL
    interview_id = None
    if request.view_args:
        interview_id = request.view_args.get("id")

    # Fallback: ambil dari body JSON
    if not interview_id:
        data = request.get_json(silent=True) or {}
        interview_id = data.get("interview_id")

    # Tidak terkait interview → lewati
    if not interview_id:
        return

    interview = Interview.query.get(interview_id)
    if not interview:
        abort(404)

    status = InterviewStatus.query.get(interview.status_id)
    if status and status.is_final:
        abort(403)
