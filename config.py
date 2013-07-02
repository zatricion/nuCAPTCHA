import os

class Configuration(object):  
    
    if 'RDS_HOSTNAME' in os.environ:
        engine = 'peewee.MySQLDatabase'
        name = os.environ['RDS_DB_NAME']
        user = os.environ['RDS_USERNAME']
        passwd = os.environ['RDS_PASSWORD']
        host = os.environ['RDS_HOSTNAME']
    else:
      DATABASE = {
        'name': 'nucaptcha',
        'engine': 'peewee.MySQLDatabase',
        'user': 'root',
        'host': 'localhost'
      }
    DEBUG = True
    SECRET_KEY = 'ae09rjyh5ijjogej-tw4jtogidfjoigj'
