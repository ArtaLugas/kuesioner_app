from app import create_app
from app.extensions import db
from app.models.interview import Interview
from app.models.interview_status import InterviewStatus
from app.models.user import User

app = create_app()

with app.app_context():
    # ambil user surveyor (owner interview)
    surv = User.query.filter_by(email="surv@local.test").first()
    if not surv:
        raise Exception("Surveyor user not found")

    # ambil status SUBMITTED (WAJIB)
    submitted = InterviewStatus.query.filter_by(code="submitted").first()
    if not submitted:
        raise Exception("Submitted status not found")

    # buat interview langsung dalam kondisi SUBMITTED
    interview = Interview(
        status_id=submitted.id,
        created_by=surv.id,
    )

    db.session.add(interview)
    db.session.commit()

    print("Interview READY FOR KOORDINATOR VERIFY")
    print(f"Interview ID: {interview.id}")
