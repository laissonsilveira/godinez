import json
from flask import Blueprint, Response
from flask import send_file
from app.model import Problems
from app import db
from bson import ObjectId
from mongoalchemy.document import Document

main = Blueprint('blueprint_%s' % __name__, __name__)


def encode_model(obj, recursive=False):
    if obj is None:
        return obj
    if isinstance(obj, Document):
        out = obj.wrap()
        for k, v in out.items():
            if isinstance(v, ObjectId):
                if k is None:
                    out['_id'] = str(v)
                    del (out[k])
                else:
                    # Unlikely that we'll hit this since ObjectId is always NULL key
                    out[k] = str(v)
            else:
                out[k] = encode_model(v)
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, unicode):
        return obj
    else:
        raise TypeError("Could not JSON-encode type '%s': %s" % (type(obj), str(obj)))
    return out


@main.route('/')
def index_view():
    return send_file('static/templates/index.html')


@main.route('/find', methods=['GET'])
def find_problems():
    status = 200
    try:
        query = db.session.query(Problems)
        problems = query.all()
        data = json.dumps(problems, default=encode_model)

    except Exception as e:
        data = json.dumps({
            'code': 500,
            'message': str(e.args)
        })
        status = 500

    return Response(data, status=status, mimetype='application/json')
