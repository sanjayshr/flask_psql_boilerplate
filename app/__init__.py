from flask import Flask
from flask_migrate import Migrate
from app.routes.user import user as user_blueprint
from .database import db
from sqlalchemy_utils import database_exists, create_database


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        db.create_all()

    app.register_blueprint(user_blueprint)

    return app