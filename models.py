"""
models imports app, but app does not import models so we haven't created
any loops.
"""
import datetime
from peewee import *
from flask_peewee.auth import BaseUser # provides password helpers..

from app import db

class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username

class Image(db.Model):
    filename = CharField(unique=True)
    answer   = CharField()
    
class Secondary(db.Model):
    filename = CharField(unique=True)

class SecCounts(db.Model):
    sec = ForeignKeyField(Secondary, related_name = 'counts')
    pos_count  = IntegerField()
    neg_count  = IntegerField()
    neut_count = IntegerField()
    known      = BooleanField(index=True, default=False)
    
