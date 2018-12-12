from marshmallow_sqlalchemy import ModelSchema
from ams.models import Student


class StudentSchema(ModelSchema):
    class Meta:
        model = Student
