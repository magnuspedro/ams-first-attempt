from marshmallow import Schema, fields


class BoughtSchema(Schema):
    id = fields.Number()
    price = fields.Float()
    product_id = fields.Number()
