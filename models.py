"""
@package models
module that sets up all of the MySQL tables used
"""
from peewee import *
import nucaptcha

class Image(nucaptcha.db.Model):
    filename = CharField()
    answer   = CharField()
    
class Secondary(nucaptcha.db.Model):
    filename   = CharField()

class SecCounts(nucaptcha.db.Model):
    sec = ForeignKeyField(Secondary, related_name = 'counts')
    pos_count  = IntegerField()
    neg_count  = IntegerField()
    neut_count = IntegerField()
    

class KnownSecondaries(nucaptcha.db.Model):
    pass