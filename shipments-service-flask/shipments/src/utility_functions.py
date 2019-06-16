from jwt import decode
from jwt.exceptions import InvalidSignatureError, DecodeError, ExpiredSignatureError
import os
from src.models import *
from src.config import PUBLIC_KEY, TOKEN_ENCODING_ALGORITHM, DATABASE_DIR_PATH
from src.schemas import *

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)

def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	# Create database schema
	db.create_all()
	
	# Add shipment states
	db.session.add(ShipmentStates(0, "Pending"))
	db.session.add(ShipmentStates(1, "Completed"))
	db.session.add(ShipmentStates(2, "Cancelled"))
	
	# Add shipment types
	db.session.add(ShipmentTypes("Paczkomat 24/7", 12.99, 3, \
	"Paczkomaty to system skrytek pocztowych, ustawionych w różnych miejscach " \
	"na terenie całego kraju, podobnych w obsłudze do bankomatów, w których " \
	"możliwy jest odbiór przesyłki o dowolnej, dogodnej dla adresata porze, " \
	"24 godziny na dobę przez 7 dni w tygodniu."))
	db.session.add(ShipmentTypes("Przysyłka kurierska", 18.99, 2))
	db.session.add(ShipmentTypes("Odbiór osobisty", 0, 0, "Odbiór w siedzibie sklepu"))
	db.session.add(ShipmentTypes("Paczka za pobraniem", 29.99, 5, "Płatność przy odbiorze"))
	
	# Commit transaction
	db.session.commit()

def decodeToken(token, public_key, encodingAlgorithm):
	try:
		decodedToken = decode(token, public_key, algorithms=[encodingAlgorithm])
		return decodedToken
	except (DecodeError, InvalidSignatureError, ExpiredSignatureError):
		return None

def validateTokenData(decodedToken):
	validationResult = [False, None]
	
	if 'customer_id' not in decodedToken.keys():
		validationResult[1] = "There is no customer_id in token!"
		return validationResult
		
	customer_id = decodedToken['customer_id']
	if customer_id is None or not isinstance(customer_id, int):
		validationResult[1] = 'Invalid value type: customer_id must be int!'
		return validationResult
	
	validationResult[0] = True
	return validationResult

def createErrorResult(message, code):
	errorResult = [None, None, None]
	errorResult[1] = {'status' : 'fail', 'message' : message}
	errorResult[2] = code
	return errorResult

def decodeAndValidateToken(requestJson):
	if requestJson is None:
		resultValues = createErrorResult('Cannot find JSON object in request body!', 400)
		return resultValues
	
	if 'token' not in requestJson.keys():
		resultValues = createErrorResult('Authorization token not found!', 403)
		return resultValues
	
	token = requestJson['token']
	decodedToken = decodeToken(token, PUBLIC_KEY, TOKEN_ENCODING_ALGORITHM)
	if decodedToken is None:
		resultValues = createErrorResult('Cannot decode token!', 400)
		return resultValues

	tokenValidation = validateTokenData(decodedToken)
	if not tokenValidation[0]:
		resultValues = createErrorResult(tokenValidation[1], 400)
		return resultValues

	return [decodedToken, None, None]

def makeShipmentDict(shipment):
	shipmentDict = {}
	
	shipmentDict['customer_id'] = shipment.customer_id
	shipmentDict['order_id'] = shipment.order_id
	
	shipmentState = ShipmentStates.query.get(shipment.shipment_state_id)
	shipmentStateSchema = ShipmentStatesSchema(strict=True)
	shipmentDict['shipment_state'] = shipmentStateSchema.dump(shipmentState).data
	
	shipmentType = ShipmentTypes.query.get(shipment.shipment_type_id)
	shipmentTypeSchema = ShipmentTypesSchema(strict=True)
	shipmentDict['shipment_type'] = shipmentTypeSchema.dump(shipmentType).data
	
	mailingDataDict = {}
	mailingData = MailingData.query.get(shipment.mailing_data_id)
	
	personalData = PersonalData.query.get(mailingData.personal_data_id)
	personalDataSchema = PersonalDataSchema(strict=True)
	mailingDataDict['personal_data'] = personalDataSchema.dump(personalData).data
	
	addressData = AddressData.query.get(mailingData.address_data_id)
	addressDataSchema = AddressDataSchema(strict=True)
	mailingDataDict['address_data'] = addressDataSchema.dump(addressData).data
	
	shipmentDict['mailing_data'] = mailingDataDict
	return shipmentDict


