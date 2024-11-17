from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ufuehfhixhdbfieiehcock'   #key picked by rayan saeed
    app.config['SQLALCHEMY_DATABASE_URI']= f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists(f"Website/{DB_NAME}"):
        db.create_all(app=any)
        print(f'Created Database!')
    else:
        print('Database Exists!')
