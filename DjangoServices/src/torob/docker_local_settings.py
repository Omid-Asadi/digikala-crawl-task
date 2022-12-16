""" General settings """
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

""" Database login info """
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')

REST_DEFAULT_PAGINATION_SIE = os.environ.get('REST_DEFAULT_PAGINATION_SIE')
