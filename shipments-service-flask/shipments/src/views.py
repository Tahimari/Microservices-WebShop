from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from src.models import *
from src.schemas import *
from src.utility_functions import decodeAndValidateToken

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

@views_blueprint.route('/shipments', methods=['POST'])
def add_new_shipment():
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	requestJSON = request.json
	customerID = decodedToken["customer_id"]
	orderID = requestJSON["order_id"]
	shipmentTypeID = requestJSON["shipment_type_id"]
	
	shipmentType = ShipmentTypes.query.get(shipmentTypeID)
	
	if shipmentType is None:
		return jsonify({'status' : 'fail', 'message' : "Invalid 'shipment_type_id' value: no such shipment type!"}), 400
	
	personalDataInJson = requestJSON["mailing_data"]["personal_data"]
	firstName = personalDataInJson["first_name"]
	lastName = personalDataInJson["last_name"]
	phoneNumber = personalDataInJson["phone_number"]
	
	personalData = PersonalData.query.filter_by(\
			first_name = firstName, \
			last_name = lastName, \
			phone_number = phoneNumber).first()
	
	if personalData is None:
		personalData = PersonalData(firstName, lastName, phoneNumber)
		try:
			db.session.add(personalData)
			db.session.flush()
		except IntegrityError as e:
			errorInfo = e.orig.args
			return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
	
	addressDataInJson = requestJSON["mailing_data"]["address_data"]
	addressLine = addressDataInJson["address_line"]
	postalCode = addressDataInJson["postal_code"]
	city = addressDataInJson["city"]
	country = addressDataInJson["country"]
	
	addressData = AddressData.query.filter_by(\
			address_line = addressLine, \
			postal_code = postalCode, \
			city = city, \
			country = country).first()
	
	if addressData is None:
		addressData = AddressData(addressLine, postalCode, city, country)
		try:
			db.session.add(addressData)
			db.session.flush()
		except IntegrityError as e:
			errorInfo = e.orig.args
			return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
	
	try:
		personalDataID = personalData.id
		addressDataID = addressData.id
		
		mailingData = MailingData(personalDataID, addressDataID)
		db.session.add(mailingData)
		db.session.flush()
		
		mailingDataID = mailingData.id
		newShipment = Shipments(customerID, orderID, shipmentTypeID, mailingDataID)
		db.session.add(newShipment)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'New shipment added!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
