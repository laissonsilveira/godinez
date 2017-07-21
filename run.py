#!/usr/bin/python
from flask import Flask
from flask import send_file

import logging
from logging import StreamHandler

app = Flask(__name__,static_folder='webapp')

@app.route('/')
def hello_world():
    return send_file('webapp/index.html')

@app.route('/emerson')
def emerson():
    return 'Bixona!'


@app.route('/laisson/<id>')
def laisson(id):
    return 'Param -> ' + id
    
file_handler = StreamHandler()
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

if __name__ == '__main__':
    app.run(debug=True)
