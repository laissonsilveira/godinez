# coding=utf-8
import json
import os

from bson.objectid import ObjectId
from flask import Blueprint, Response, render_template, request
from app import mongo


def mount_web_path(folder):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))), folder)


main = Blueprint(
    'godinez',
    __name__,
    template_folder=mount_web_path(folder='web'),
    static_folder=mount_web_path(folder='web/dist')
)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/issues', methods=['GET', 'POST', 'PUT'])
def crud_issues():
    status = 200
    issues = mongo.db.issues
    data = {}

    try:
        if request.method == 'GET':
            result = []
            for s in issues.find():
                result.append({'title': s['title'], 'description': s['description']})
            data = json.dumps({'data': result})

        elif request.method == 'POST':
            title = request.json['title']
            description = request.json['description']

            if title and description:
                issue_id = issues.insert({'title': title, 'description': description})
                new_issue = issues.find_one({'_id': issue_id})
                result = {'title': new_issue['title'], 'description': new_issue['description']}
                data = json.dumps({'data': result})
            else:
                data = json.dumps({
                    'code': 500,
                    'message': 'Dados da issues não informados corretamente'
                })
                status = 500

        elif request.method == 'PUT':
            issue = json.loads(request.data)

            if '_id' not in issue:
                data = json.dumps({
                    'code': 500,
                    'message': 'ID da Issue não informado'
                })
                status = 500
            else:
                issues.update_one({'_id': ObjectId(issue['_id'])},
                                       {'$set': {'title': issue['title'], 'description': issue['description']}})
                data = json.dumps({'message': 'Issue atualizada com sucesso'})

    except Exception as e:
        data = json.dumps({
            'code': 500,
            'message': str(e.args)
        })
        status = 500

    return Response(data, status=status, mimetype='application/json')


@main.route('/issues/<id>', methods=['DELETE', 'PUT', 'GET'])
def delete_issue(id):
    status = 200
    issues = mongo.db.issues
    data = {}

    try:
        if request.method == 'DELETE':
            result = issues.delete_one({'_id': ObjectId(id)})
            if result.deleted_count == 1:
                data = json.dumps({'message': 'Issue delatada com sucesso'})
            else:
                data = json.dumps({
                    'code': 500,
                    'message': 'Error ao deletar Issue'
                })
                status = 500



    except Exception as e:
        data = json.dumps({
            'code': 500,
            'message': str(e.args)
        })
        status = 500

    return Response(data, status=status, mimetype='application/json')
