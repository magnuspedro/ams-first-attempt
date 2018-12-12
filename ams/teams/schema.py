from marshmallow import Schema, fields


class TeamsSchema(Schema):
    id = fields.Number()
    student_id = fields.Number()
    modality_id = fields.Number()
