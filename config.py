import os

class Configuration(object):  
    
    if 'RDS_HOSTNAME' in os.environ:
        DATABASE = {
                'engine': 'peewee.MySQLDatabase',
                'name': os.environ['RDS_DB_NAME'],
                'user': os.environ['RDS_USERNAME'],
                'passwd': os.environ['RDS_PASSWORD'],
                'host': os.environ['RDS_HOSTNAME']
        }
    else:
      DATABASE = {
        'name': '/home/ubuntu/test.db',
        'engine': 'peewee.SqliteDatabase',
      }
    DEBUG = True
    SECRET_KEY = 'ae09rjyh5ijjogej-tw4jtogidfjoigj'
