from app.extensions import db


class Interview(db.Model):
    __tablename__ = "interviews"

    id = db.Column(db.Integer, primary_key=True)

    status_id = db.Column(
        db.Integer,
        db.ForeignKey("interview_statuses.id"),
        nullable=False
    )

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime)
