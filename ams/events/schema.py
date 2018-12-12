from marshmallow import Schema, fields


class EventSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    starting_date = fields.Date()
    ending_date = fields.Date()
    price = fields.Float()
