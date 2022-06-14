'''
app initialization
'''
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri   # heroku postgresql db


db = SQLAlchemy(app)
mongo = PyMongo(app)

# routes rely on app and db variables therefore must be imported after these
from food_fiesta import routes # noqa
