"""
models imports app, but app does not import models so we haven't created
any loops.
"""
import datetime
from peewee import *
from flask_peewee.auth import BaseUser # provides password helpers..

from app import db
import functools

def unique_save(cls = None, column = 'filename'):
    """ A class decorator to make classes only save filenames if unique. """
    if cls is None:
        return functools.partial(unique_save, column = column)
    
    def new_save(self, *args, **kwargs):
        cls_col = getattr(cls, column)
        self_col = getattr(self, column)
        x = cls.select().where(cls_col == self_col)
        present = list(x)
        if not present:
            return super(cls, self).save(*args, **kwargs) 
            
    setattr(cls, 'save', new_save)
    return cls


class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username

@unique_save
class Image(db.Model):
    filename = CharField()
    answer   = CharField()

@unique_save
class Secondary(db.Model):
    filename = CharField()  
    pos_count  = IntegerField(default=0)
    neg_count  = IntegerField(default=0)
    neut_count = IntegerField(default=0)
    known      = BooleanField(index=True, default=False)
