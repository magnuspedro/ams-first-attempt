from marshmallow import Schema, fields


class CompetitionSchema(Schema):
    id = fields.Number()
    event_id = fields.Number()
    modality_id = fields.Number()
