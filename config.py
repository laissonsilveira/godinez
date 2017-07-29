# Define the application directory
import os

# Statement for enabling the development environment
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Mongo configuration - DEV
# MONGOALCHEMY_SERVER = 'localhost'
# MONGOALCHEMY_DATABASE = 'godinez_db'
# MONGOALCHEMY_PORT = '27017'
MONGO_DBNAME = 'godinez_db'

# Mongo configuration - PROD (Heroku)
# MONGOALCHEMY_SERVER = 'ds025469.mlab.com'
# MONGOALCHEMY_DATABASE = 'heroku_xnk208n3'
# MONGOALCHEMY_PORT = '25469'
# MONGOALCHEMY_USER = 'chaves'
# MONGOALCHEMY_PASSWORD = 'kikohahaha'

# Secret key for signing cookies
SECRET_KEY = "gogodizez"
