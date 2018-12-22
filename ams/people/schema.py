from ams.config import ma, db
from ams.models import Person


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
