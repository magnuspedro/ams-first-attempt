from marshmallow import Schema, fields


class TransactionSchema(Schema):
    id = fields.Number()
    amount = fields.Float()
    sold_id = fields.Number()
    sales_id = fields.Number()
