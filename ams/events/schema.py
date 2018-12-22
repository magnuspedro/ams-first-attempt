from ams.config import ma
from ams.models import Event


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event
