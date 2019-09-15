import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this'

    # Enable Flask's debugging features. Should be False in production
    DEBUG = True