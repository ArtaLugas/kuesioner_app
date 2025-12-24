from app import create_app
from app.extensions import db
from app.models.interview import Interview
from app.models.interview_status import InterviewStatus
from app.models.user import User

app = create_app()

with app.app_context():
    surv = User.query.filter_by(email="surv@local.test").first()
    if not surv:
        raise Exception("Surveyor user not found")

    draft = InterviewStatus.query.filter_by(code="draft").first()
    if not draft:
        raise Exception("Draft status not found")

    interview = Interview(
        status_id=draft.id,
        created_by=surv.id,
    )

    db.session.add(interview)
    db.session.commit()

    print(f"Interview created with ID: {interview.id}")
