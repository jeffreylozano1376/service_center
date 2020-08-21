import os

class Config(object):
    # cryptographic key: generates signatures or tokens for protection against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'