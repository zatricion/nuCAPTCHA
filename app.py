from nucaptcha import application

# flask-peewee database, but could be SQLAlchemy instead.
from flask_peewee.db import Database

application.config.from_object('config.Configuration')

# instantiate the db wrapper
db = Database(application)

# Here I would set up the cache, a task queue, etc.