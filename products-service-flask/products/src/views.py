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
