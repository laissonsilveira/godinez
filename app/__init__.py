# Import log
import logging
from logging import StreamHandler

# Import flask and template operators
from flask import Flask

# Import MongoKit
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Define log
file_handler = StreamHandler()
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# connect to the database
mongo = PyMongo(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.views import main

# Register blueprint(s)
app.register_blueprint(main)
