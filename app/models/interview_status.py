from app.extensions import db


class InterviewStatus(db.Model):
    __tablename__ = "interview_statuses"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    is_final = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<InterviewStatus {self.code}>"
