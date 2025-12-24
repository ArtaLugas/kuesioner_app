from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.role import UserRole
from werkzeug.security import generate_password_hash

app = create_app()

USERS = [
    {
        "name": "Koordinator Test",
        "email": "koor@local.test",
        "password": "password",
        "role": "KOOR",
    },
]

with app.app_context():
    koordinator_role = UserRole.query.filter_by(code="KOOR").first()

    koordinator = User(
        name="Koordinator Test",
        email="koor@local.test",
        password_hash=generate_password_hash("password"),
        role_id=koordinator_role.id
    )

    db.session.add(koordinator)
    db.session.commit()

    print("Koordinator user created.")
