from marshmallow import Schema, fields


class TaxesSchema(Schema):
    id = fields.Number()
    percentage = fields.Float()
    sales_id = fields.Number()
