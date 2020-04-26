import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p_scrt_key-YOU-w1ll-never-guess34y32irbkjb!'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'