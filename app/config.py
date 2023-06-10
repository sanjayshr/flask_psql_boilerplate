import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@my-postgres:5432/myflaskdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False