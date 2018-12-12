from marshmallow import Schema, fields


class TicketSchema(Schema):
    id = fields.Number()
    code = fields.String()
    price = fields.Float()
    status = fields.Integer()
    amount = fields.Integer()
    lot = fields.String()
    event_id = fields.Number()
