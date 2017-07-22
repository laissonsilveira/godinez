# Import log
import logging
from logging import StreamHandler

# Import flask and template operators
from flask import Flask

# Import MongoKit
from flask_mongoalchemy import MongoAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Define log
file_handler = StreamHandler()
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# connect to the database
db = MongoAlchemy(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.views import main

# Register blueprint(s)
app.register_blueprint(main)
