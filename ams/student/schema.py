from ams.config import ma
from ams.models import Student


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
