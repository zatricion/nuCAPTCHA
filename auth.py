"""
auth imports app and models, but none of those import auth
so we're OK
"""
from flask_peewee.auth import Auth  # Login/logout views, etc.

from app import application, db
from models import User

auth = Auth(application, db, user_model=User)