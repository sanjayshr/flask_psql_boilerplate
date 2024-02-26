from app.models.user import User
from app.database import db

def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]


def create_new_user(data):
    user = User()
    user.username = data.get('username')
    user.email = data.get('email')
    user.set_password(data.get('password'))
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

