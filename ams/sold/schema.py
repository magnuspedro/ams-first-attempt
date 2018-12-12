from marshmallow import Schema, fields


class SoldSchema(Schema):
    id = fields.Number()
    price = fields.Float()
    product_id = fields.Number()
