from app.extensions import db


class UserRole(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    label = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<UserRole {self.code}>"
