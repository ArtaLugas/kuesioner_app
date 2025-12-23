from app import create_app
from app.extensions import db
from app.models.role import UserRole

app = create_app()

with app.app_context():
    roles = [
        {"code": "SURV", "label": "Surveyor"},
        {"code": "KOOR", "label": "Koordinator Surveyor"},
        {"code": "ADM", "label": "Admin"},
    ]

    for r in roles:
        exists = UserRole.query.filter_by(code=r["code"]).first()
        if not exists:
            db.session.add(UserRole(**r))

    db.session.commit()
    print("User roles seeded.")