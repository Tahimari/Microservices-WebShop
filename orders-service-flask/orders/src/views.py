from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from src.schemas import OrderStatusSchema, OrderItemsSchema, OrdersSchema
from src.models import *
from src.utility_functions import *

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/orders/<order_id>', methods=['POST'])
def add_order_item(order_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
	
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customer_id = decodedToken['customer_id']
		
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
	
	order = Orders.query.get(order_id)
	if order is None:
		new_order = Orders(order_id, customer_id)
		db.session.add(new_order)
		order = new_order
	
	if not isOrderInPendingStatus(order):
		return jsonify({'status' : 'fail', 'message' : 'Cannot add new items - order is not in Pending status!'}), 403
	
	product_id = int(request.json['product_id'])
	quantity = int(request.json['quantity'])
	new_order_item = OrderItems(order_id, product_id, quantity)
	
	try:
		db.session.add(new_order_item)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'New item added'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
	
@views_blueprint.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
		
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customer_id = decodedToken['customer_id']
	
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
		
	searched_order = Orders.query.get(order_id)
	if searched_order is None:
		return jsonify({'status' : 'fail', 'message' : 'Order not found!'}), 404
	
	if searched_order.order_items is None:
		return jsonify({'status' : 'fail', 'message' : 'searched_order.order_items is None'}), 404
	
	orderDict = makeOrderDict(searched_order)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = orderDict
	return jsonify(responseData), 200

@views_blueprint.route('/orders', methods=['GET'])
def get_customer_orders():
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customerID = decodedToken['customer_id']
	
	customerOrders = Orders.query.filter_by(customer_id=customerID).all()
	customerOrdersList = []
	
	for order in customerOrders:
		tempDict = makeOrderDict(order)
		customerOrdersList.append(tempDict)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = customerOrdersList
	return jsonify(responseData), 200

@views_blueprint.route('/orders/<order_id>', methods=['DELETE'])
def remove_order(order_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
	
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customer_id = decodedToken['customer_id']
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
		
	order = Orders.query.get(order_id)
	if order is None:
		return jsonify({'status' : 'fail', 'message' : "Order doesn't exist!"}), 404
	if not isOrderInPendingStatus(order):
		return jsonify({'status' : 'fail', 'message' : 'Cannot delete order - order is not in Pending status!'}), 403
	try:
		for item in order.order_items:
			db.session.delete(item)
			
		db.session.delete(order)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Order deleted!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/orders/<order_id>/<product_id>', methods=['DELETE'])
def remove_order_item(order_id, product_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
	if not product_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'product_id must be int!'}), 400
	
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customer_id = decodedToken['customer_id']
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
	
	order = Orders.query.get(order_id)
	if order is None:
		return jsonify({'status' : 'fail', 'message' : 'Order not found!'}), 404
	if not isOrderInPendingStatus(order):
		return jsonify({'status' : 'fail', 'message' : 'Cannot delete item - order is not in Pending status!'}), 403
	
	order_item = OrderItems.query.filter_by(order_id=order_id, product_id=product_id).first()
	if order_item is None:
		return jsonify({'status' : 'fail', 'message' : "Order item doesn't exist!"}), 404	
	try:
		db.session.delete(order_item)
		order_item = OrderItems.query.filter_by(order_id=order_id).first()
		if order_item is None:
			db.session.delete(order)
		
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Order item deleted!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409


@views_blueprint.route('/orders/<order_id>/<product_id>', methods=['PUT'])
def change_product_quantity(order_id, product_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
	if not product_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'product_id must be int!'}), 400
		
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	customer_id = decodedToken['customer_id']
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
	
	order_item = OrderItems.query.filter_by(order_id=order_id, product_id=product_id).first()
	if order_item is None:
		return jsonify({'status' : 'fail', 'message' : "Order item doesn't exist!"}), 404
		
	if 'new_quantity' not in request.json.keys():
		return jsonify({'status' : 'fail', 'message' : 'Invalid JSON request! Cannot find new_quantity!'}), 400
	
	new_quantity = request.json['new_quantity']
	if not isinstance(new_quantity, int) or new_quantity <= 0:
		return jsonify({'status' : 'fail', 'message' : 'new_quantity must be positive integer!'}), 400
		
	try:
		order_item.quantity = request.json['new_quantity']
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Changed product quantity!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/orders/status_codes', methods=['GET'])
def get_all_possible_status_codes():
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
	
	statusCodes = OrderStatus.query.all()
	statusCodesSchema = OrderStatusSchema(many=True, strict=True)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = statusCodesSchema.dump(statusCodes).data
	
	return jsonify(responseData), 200
	
@views_blueprint.route('/orders/<order_id>', methods=['PUT'])
def change_order_status(order_id):
	if not order_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : 'Order ID must be integer!'}), 400
	
	tokenValidationResult = decodeAndValidateToken(request.json)
	decodedToken = tokenValidationResult[0]
	if decodedToken is None:
		responseDict = tokenValidationResult[1]
		responseCode = tokenValidationResult[2]
		return jsonify(responseDict), responseCode
		
	customer_id = decodedToken['customer_id']
	if not haveCustomerAccessToOrder(order_id, customer_id):
		return jsonify({'status' : 'fail', 'message' : 'Access denied'}), 403
		
	if 'new_status_code' not in request.json.keys():
		return jsonify({'status' : 'fail', 'message' : 'Cannot find new_status!'}), 400
		
	new_status_code = request.json['new_status_code']
	if not isinstance(new_status_code, int) or new_status_code < 0:
		return jsonify({'status' : 'fail', 'message' : 'new_status_code must be non-negative integer!'}), 400
	
	new_status = OrderStatus.query.get(new_status_code)
	if new_status is None:
		return jsonify({'status' : 'fail', 'message' : 'No such order status!'}), 400
	
	order = Orders.query.get(order_id)
	if order is None:
		return jsonify({'status' : 'fail', 'message' : 'Order not found!'}), 404
		
	try:
		order.order_status_code = new_status_code
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Changed order status!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
