from ams.models import Modality
from ams.config import ma


class ModalitySchema(ma.ModelSchema):
    class Meta:
        model = Modality
