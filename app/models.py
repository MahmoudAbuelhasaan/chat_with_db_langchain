from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from datetime import datetime

from app import db

class User(db.model):
    id = db.Columne(db.Integer, primary_key=True)

