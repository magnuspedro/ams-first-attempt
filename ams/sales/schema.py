from marshmallow import Schema, fields


class SalesSchema(Schema):
    id = fields.Number()
    value = fields.Float()
    discount = fields.Float()
    taxes_id = fields.Float()
    student_id = fields.Number()
    salesperson_id = fields.Number()
    ticket_id = fields.Number()
