import os

class Configuration(object):  
    
    if 'RDS_HOSTNAME' in os.environ:
        DATABASE = {
            'default': {
                'ENGINE': 'peewee.MySQLDatabase',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }
    else:
      DATABASE = {
        'name': 'nucaptcha',
        'engine': 'peewee.MySQLDatabase',
        'user': 'root',
        'host': 'localhost'
      }
    DEBUG = True
