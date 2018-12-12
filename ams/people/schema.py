from marshmallow_sqlalchemy import ModelSchema
from ams.config import ma
from ams.models import Person
from ams.student.schema import StudentSchema


class PersonSchema(ModelSchema):
    class Meta:
        model = Person
