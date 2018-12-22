from flask import Blueprint, jsonify, request
from ams.models import Modality
from ams.modalities import schema
from ams.config import db
modalities = Blueprint('modalities', __name__)


@modalities.route("/modality")
def get_modality():

    obj_modality = db.session.query(Modality).all()

    schema = schema.ModalitySchema(many=True)
    modalities = schema.dump(obj_modality)

    return jsonify(modalities.data)


@modalities.route("/modality", methods=['POST'])
def register_modality():
    posted_modality = schema.ModalitySchema().load(request.get_json(), session=db.session)

    modality = posted_modality.data

    db.session.add(modality)
    db.session.commit()

    new_modality = schema.ModalitySchema().dump(modality).data

    return jsonify(new_modality), 201
