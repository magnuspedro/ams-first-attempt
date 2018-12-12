from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    description = fields.Str()
    size = fields.Str()
    price = fields.Float()
    amount = fields.Number()
    color = fields.Str()
    event_id = fields.Number()
