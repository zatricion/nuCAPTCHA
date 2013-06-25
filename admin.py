"""
admin imports app, auth and models, but none of these import admin
so we're OK
"""
from flask_peewee.admin import Admin, ModelAdmin

from app import application, db
from auth import auth
from models import User

admin = Admin(application, auth)
auth.register_admin(admin)
# or you could admin.register(User, ModelAdmin) -- you would also register
# any other models here.