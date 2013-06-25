from flask import Flask

# flask-peewee database, but could be SQLAlchemy instead.
from flask_peewee.db import Database

application = Flask(__name__) # had to call it application for elastic beanstalk
app = application 
#app.config.from_object('config.Configuration')

# instantiate the db wrapper
db = Database(app)

# Here I would set up the cache, a task queue, etc.


@app.route('/')
def hello_world():
    return "Hello world! %s"
    
#execfile("nucaptcha.py")
