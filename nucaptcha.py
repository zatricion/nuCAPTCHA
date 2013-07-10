"""
this is the "secret sauce" -- a single entry-point that resolves the
import dependencies.  If you're using blueprints, you can import your
blueprints here too.

then when you want to run your app, you point to main.py or `main.app`
"""
from app import db
from app import app as application

from auth import *
from admin import admin
# from api import api
from models import *
from views import *
from scripts import setup

admin.setup()
# api.setup()

IM_DIR = 'images/'
SEC_DIR = 'secondary/'

setup.initialize(IM_DIR, SEC_DIR)

if __name__ == '__main__':
    app.run(port=8080)
