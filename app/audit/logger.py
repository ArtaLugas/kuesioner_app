from flask import session
from app.extensions import db
from app.models.audit_log import AuditLog


def log_action(action: str, interview_id: int):
    user_id = session.get("user_id")
    if not user_id:
        return  # tidak ada session → tidak log

    log = AuditLog(
        user_id=user_id,
        interview_id=interview_id,
        action=action
    )
    db.session.add(log)
    db.session.commit()
