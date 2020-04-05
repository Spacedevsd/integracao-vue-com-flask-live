from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_vuejs import Vue

db = SQLAlchemy()
ma = Marshmallow()
vue = Vue()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)
    vue.init_app(app)

    from . import views
    app.register_blueprint(views.contact)

    return app
