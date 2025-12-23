from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.role import UserRole
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin_role = UserRole.query.filter_by(code="ADM").first()

    admin = User(
        name="System Admin",
        email="admin@local.test",
        password_hash=generate_password_hash("admin123"),
        role_id=admin_role.id
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin user created.")