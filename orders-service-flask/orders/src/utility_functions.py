from jwt import decode
from jwt.exceptions import InvalidSignatureError, DecodeError
import os
from src.schemas import OrderStatusSchema, OrderItemsSchema, OrdersSchema
from src.config import PUBLIC_KEY, TOKEN_ENCODING_ALGORITHM, DATABASE_DIR_PATH
from src.models import *

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)

def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	db.create_all()
	db.session.add(OrderStatus(0, "Pending"))
	db.session.add(OrderStatus(1, "Completed"))
	db.session.add(OrderStatus(2, "Cancelled"))
	db.session.commit()

def haveCustomerAccessToOrder(order_id, customer_id):
	order = Orders.query.get(order_id)
	if order is None:
		return True
	else:
		return customer_id == order.customer_id

def isOrderInPendingStatus(order):
	return order.order_status_code == 0

def makeOrderDict(order):
	orderDict = {}
	
	orderDict['order_id'] = order.id
	orderDict['customer_id'] = order.customer_id
	
	order_status = OrderStatus.query.get(order.order_status_code)
	statusSchema = OrderStatusSchema(strict=True)
	orderDict['order_status'] = statusSchema.dump(order_status).data
	
	order_items = OrderItems.query.filter_by(order_id=order.id).all()
	itemsSchema = OrderItemsSchema(strict=True, many=True, exclude = ('id', 'order_id'))
	orderDict['order_items'] = itemsSchema.dump(order_items).data
	
	return orderDict

def createErrorResult(message, code):
	errorResult = [None, None, None]
	errorResult[1] = {'status' : 'fail', 'message' : message}
	errorResult[2] = code
	return errorResult

def decodeToken(token, public_key, encodingAlgorithm):
	try:
		decodedToken = decode(token, public_key, algorithms=[encodingAlgorithm])
		return decodedToken
	except (DecodeError, InvalidSignatureError):
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
