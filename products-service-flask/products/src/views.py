from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from src.schemas import CategoriesSchema
from src.models import db, Categories

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

@views_blueprint.route('/products/categories/<category_id>', methods=['PUT'])
def change_category_name(category_id):
	if not category_id.isdigit():
		return jsonify({'status' : 'fail', 'message' : "'category_id' must be int!"})
	
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
