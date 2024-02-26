from flask import Flask
from flask_migrate import Migrate
from app.routes.user import user as user_blueprint
from app.routes.hello import hello as hello_blueprint
from .database import db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError
from time import sleep


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        while True:
            try:
                if not database_exists(db.engine.url):
                    create_database(db.engine.url)
                db.create_all()
                break
            except OperationalError:
                print("Database not ready yet...")
                sleep(5)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(hello_blueprint)

    return app