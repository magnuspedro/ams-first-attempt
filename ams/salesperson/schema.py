from marshmallow import Schema, fields


class SalespersonSchema(Schema):
    id = fields.Number()
    person_id = fields.Number()
