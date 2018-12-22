from ams.conf import ma
from ams.models import Salesperson


class SalespersonSchema(ma.ModelSchema):
    class Meta:
        model = Salesperson
