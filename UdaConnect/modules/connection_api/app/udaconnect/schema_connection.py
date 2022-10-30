from app.udaconnect.model_connection import Connection

from marshmallow import Schema, fields
from marshmallow_sqlalchemy.convert import ModelConverter as BaseModelConverter

from app.udaconnect.schema_person import PersonSchema
from app.udaconnect.schema_location import LocationSchema


class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
