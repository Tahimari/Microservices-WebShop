from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from src.models import *
from src.schemas import *

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/shipments/types', methods=['GET'])
def get_shipment_types():
	shipmentTypes = ShipmentTypes.query.all()
	typesSchema = ShipmentTypesSchema(many=True, strict=True)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = typesSchema.dump(shipmentTypes).data
	
	return jsonify(responseData), 200

@views_blueprint.route('/shipments/states', methods=['GET'])
def get_shipment_states():
	shipmentStates = ShipmentStates.query.all()
	statesSchema = ShipmentStatesSchema(many=True, strict=True)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = statesSchema.dump(shipmentStates).data
	
	return jsonify(responseData), 200
