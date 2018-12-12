from marshmallow import Schema, fields


class DistributionSchema(Schema):
    id = fields.Number()
    amount_given = fields.Number()
    amount_sold = fields.Number()
    ticket_id = fields.Number()
    salesperson_id = fields.Number()
