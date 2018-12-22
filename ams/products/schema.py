from ams.models import Product
from ams.config import ma


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        # Make FK work in the JSON
        include_fk = True
