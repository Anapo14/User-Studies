import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'microsoft'
    sqlalch_database_uri = os.environ.get('database_url') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')