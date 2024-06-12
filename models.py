from datetime import datetime

#from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

#bcrypt = Bcrypt()
db = SQLAlchemy()

class Patient(db.Model):
    """Model for patients"""

    __tablename__ = "patients"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.Text, 
        nullable=False,
    )
    address = db.Column(
        db.Text,
        nullable=False
    )
    city = db.Column(
        db.Text,
        nullable=False
    )
    frequency = db.Column(
        db.Integer,
        nullable=False
    )
    timeframe_start = db.Column(
        db.Text,
        nullable=False
    )
    timeframe_end = db.Column(
        db.Text, 
        nullable=False
    )
    preferred_days = db.Column(
        db.Text,
    )
    preferred_times = db.Column(
        db.Text,
    )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    

def connect_db(app):
    """Connect this database to Flask app.
    """

    db.app = app
    db.init_app(app)

