from ams.models import Sales
from ams.config import ma


class SalesSchema(ma.ModelSchema):
    class Meta:
        model = Sales
        # Make FK work in the JSON
        include_fk = True
