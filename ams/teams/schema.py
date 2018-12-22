from ams.config import ma
from ams.models import Team


class TeamsSchema(ma.ModelSchema):
    class Meta:
        model = Team
