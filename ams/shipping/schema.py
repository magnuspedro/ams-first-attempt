from marshmallow import Schema, fields


class ShippingSchema(Schema):
    id = fields.Number()
    amount = fields.Number()
    ticket_id = fields.Number()
    sales_id = fields.Number()
    distributions = fields.Number()
