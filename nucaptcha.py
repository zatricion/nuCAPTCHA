"""
this is the "secret sauce" -- a single entry-point that resolves the
import dependencies.  If you're using blueprints, you can import your
blueprints here too.

then when you want to run your app, you point to main.py or `main.app`
"""
from app import app, db

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
###
if __name__ == '__main__':
    setup.initialize(IM_DIR, SEC_DIR)
    app.run(host='0.0.0.0')
