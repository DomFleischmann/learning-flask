import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wil-never-guess'
    # ... add more variables here as needed