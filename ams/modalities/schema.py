from marshmallow import Schema, fields


class ModalitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    fee = fields.Float()
    sex = fields.Str()
