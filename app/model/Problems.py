from app import db
from mongoalchemy import fields


class Problems(db.Document):
    config_collection_name = 'problems'

    title = fields.StringField()
    description = fields.StringField()
