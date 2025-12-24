from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.role import UserRole
from werkzeug.security import generate_password_hash

app = create_app()

USERS = [
    {
        "name": "Surveyor Test",
        "email": "surv@local.test",
        "password": "password",
        "role": "SURV",
    },
]

with app.app_context():
    surveyor_role = UserRole.query.filter_by(code="SURV").first()

    surveyor = User(
        name="Surveyor Test",
        email="surv@local.test",
        password_hash=generate_password_hash("password"),
        role_id=surveyor_role.id
    )

    db.session.add(surveyor)
    db.session.commit()

    print("Surveyor user created.")
