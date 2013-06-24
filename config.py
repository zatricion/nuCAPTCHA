import os

class Configuration(object):  
    
    if 'RDS_HOSTNAME' in os.environ:
        DATABASE = {
          'engine': 'peewee.MySQLDatabase',
          'name': os.environ['RDS_DB_NAME'],
          'user': os.environ['RDS_USERNAME'],
          'password': os.environ['RDS_PASSWORD'],
          'host': os.environ['RDS_HOSTNAME'],
          'port': os.environ['RDS_PORT'],
        }
    else:
      DATABASE = {
        'name': 'nucaptcha',
        'engine': 'peewee.MySQLDatabase',
        'user': 'root',
        'host': 'localhost'
      }
    DEBUG = False
