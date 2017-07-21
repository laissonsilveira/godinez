#!/usr/bin/python
from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return send_file('app/templates/index.html')


@app.route('/emerson')
def emerson():
    return 'Bixona!'


@app.route('/laisson/<id>')
def laisson(id):
    return 'Param -> ' + id


if __name__ == '__main__':
    app.run(debug=True)
