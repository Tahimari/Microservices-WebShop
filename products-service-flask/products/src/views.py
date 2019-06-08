from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from src.schemas import *
from src.models import *
from src.utility_functions import makeProductDict

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/products/categories', methods=['POST'])
def add_product_category():
	postData = request.json
	
	if postData is None:
		errorMessage = 'Cannot find JSON object in request body!'
		return jsonify({'status' : 'fail', 'message' : errorMessage}), 400
	
	if 'category_name' not in postData.keys():
		errorMessage = "Cannot find 'category_name' in request body!"
		return jsonify({'status' : 'fail', 'message' : errorMessage}), 400
	
	category_name = postData['category_name']
	newCategory = Categories(category_name)
	
	try:
		db.session.add(newCategory)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'New category added!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/products/categories', methods=['GET'])
def get_all_categories():
	categories = Categories.query.all()
	categoriesSchema = CategoriesSchema(many=True, strict=True)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = categoriesSchema.dump(categories).data
	
	return jsonify(responseData), 200

@views_blueprint.route('/products/categories/<int:category_id>', methods=['PUT'])
def change_category_name(category_id):
	requestJSON = request.json
	
	if requestJSON is None:
		errorMessage = 'Cannot find JSON object in request body!'
		return jsonify({'status' : 'fail', 'message' : errorMessage}), 400
	
	categoryToChange = Categories.query.get(category_id)
	if categoryToChange is None:
		return jsonify({'status' : 'fail', 'message' : "Category doesn't exist!"}), 404
	
	if 'category_name' not in requestJSON.keys():
		errorMessage = "Cannot find 'category_name' in request body!"
		return jsonify({'status' : 'fail', 'message' : errorMessage}), 400	
	
	try:
		categoryToChange.name = requestJSON['category_name']
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Changed category name!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/products/categories/<int:category_id>', methods=['DELETE'])
def remove_category(category_id):
	categoryToDelete = Categories.query.get(category_id)
	if categoryToDelete is None:
		return jsonify({'status' : 'fail', 'message' : "Category doesn't exist!"}), 404
	
	try:
		db.session.delete(categoryToDelete)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Category deleted!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/products/<int:category_id>', methods=['POST'])
def add_new_product(category_id):
	category = Categories.query.get(category_id)
	if category is None:
		return jsonify({'status' : 'fail', 'message' : "Category doesn't exist!"}), 400
	
	requestJSON = request.json
	
	if requestJSON is None:
		errorMessage = 'Cannot find JSON object in request body!'
		return jsonify({'status' : 'fail', 'message' : errorMessage}), 400
	
	jsonKeys = ['name', 'price', 'picture_file_url', 'product_description']
	
	for key in jsonKeys:
		if key not in requestJSON.keys():
			errorMessage = 'Invalid JSON object in request body!'
			return jsonify({'status' : 'fail', 'message' : errorMessage}), 400
	
	name = requestJSON['name']
	price = requestJSON['price']
	picture_file_url = requestJSON['picture_file_url']
	product_description = requestJSON['product_description']
	
	try:
		newProduct = Products(category_id, name, price)
		db.session.add(newProduct)
		db.session.flush()
		newProductResources = ProductResources(\
				newProduct.id, \
				picture_file_url, \
				product_description)
		db.session.add(newProductResources)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'New product added!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409

@views_blueprint.route('/products/<int:category_id>/<int:product_id>', methods=['GET'])
def get_product(category_id, product_id):
	product = Products.query.get(product_id)
	if product is None:
		return jsonify({'status' : 'fail', 'message' : "Product doesn't exist!"}), 404
	
	if category_id != product.category_id:
		return jsonify({'status' : 'fail', 'message' : "Product doesn't belong to category with id: %s" % category_id}), 400
	
	productDict = makeProductDict(product)
	
	responseData = { 'status' : 'success', 'data' : productDict }
	return jsonify(responseData), 200

@views_blueprint.route('/products/<int:category_id>', methods=['GET'])
def get_all_products_in_category(category_id):
	category = Categories.query.get(category_id)
	
	if category is None:
		return jsonify({'status' : 'fail', 'message' : "Category doesn't exist!"}), 404
	
	products = Products.query.filter_by(category_id=category.id).all()
	productList = []
	
	for product in products:
		tempDict = makeProductDict(product)
		productList.append(tempDict)
	
	responseData = {}
	responseData['status'] = 'success'
	responseData['data'] = productList
	
	return jsonify(responseData), 200

@views_blueprint.route('/products/<int:category_id>/<int:product_id>', methods=['DELETE'])
def delete_product(category_id, product_id):
	product = Products.query.get(product_id)
	if product is None:
		return jsonify({'status' : 'fail', 'message' : "Product doesn't exist!"}), 404
		
	if category_id != product.category_id:
		return jsonify({'status' : 'fail', 'message' : "Product doesn't belong to category with id: %s" % category_id}), 400

	try:
		db.session.delete(product)
		db.session.commit()
		return jsonify({'status' : 'success', 'message' : 'Product deleted!'}), 200
	except IntegrityError as e:
		errorInfo = e.orig.args
		return jsonify({'status' : 'fail', 'message' : errorInfo[0]}), 409
