from app import create_app
from app.extensions import db
from app.models.interview_status import InterviewStatus

app = create_app()

with app.app_context():
    statuses = [
        {"code": "DRAFT", "sequence": 1, "is_final": False},
        {"code": "SUBMITTED", "sequence": 2, "is_final": False},
        {"code": "VERIFIED", "sequence": 3, "is_final": False},
        {"code": "LOCKED", "sequence": 4, "is_final": True},
    ]

    for s in statuses:
        exists = InterviewStatus.query.filter_by(code=s["code"]).first()
        if not exists:
            db.session.add(InterviewStatus(**s))

    db.session.commit()
    print("Interview statuses seeded.")
