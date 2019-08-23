import os
from flask import Blueprint, request, jsonify
import time, random, requests, json
from src.config import S3_BUCKET, S3_SECRET, S3_KEY
from sqlalchemy.exc import IntegrityError
from src.schemas import *
from src.models import *
from src.utility_functions import makeProductDict
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)

views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/products/categories', methods=['GET'])
def get_all_categories():
    categories = Categories.query.all()
    categoriesSchema = CategoriesSchema(many=True, strict=True)

    responseData = {}
    responseData['status'] = 'success'
    responseData['data'] = categoriesSchema.dump(categories).data

    return jsonify(responseData), 200


# @views_blueprint.route('/admin/products/categories', methods=['POST'])
# def add_product_category():
#     if postData is None:
#         errorMessage = 'Cannot find JSON object in request body!'
#         return jsonify({'status': 'fail', 'message': errorMessage}), 400
#
#     if 'category_name' not in postData.keys():
#         errorMessage = "Cannot find 'category_name' in request body!"
#         return jsonify({'status': 'fail', 'message': errorMessage}), 400
#
#     category_name = postData['category_name']
#     newCategory = Categories(category_name)
#
#     try:
#         db.session.add(newCategory)
#         db.session.commit()
#         return jsonify({'status': 'success', 'message': 'New category added!'}), 200
#     except IntegrityError as e:
#         errorInfo = e.orig.args
#         return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
#
#
# @views_blueprint.route('/admin/products/categories/<int:category_id>', methods=['PUT'])
# def change_category_name(category_id):
#     requestJSON = request.json
#
#     if requestJSON is None:
#         errorMessage = 'Cannot find JSON object in request body!'
#         return jsonify({'status': 'fail', 'message': errorMessage}), 400
#
#     categoryToChange = Categories.query.get(category_id)
#     if categoryToChange is None:
#         return jsonify({'status': 'fail', 'message': "Category doesn't exist!"}), 404
#
#     if 'category_name' not in requestJSON.keys():
#         errorMessage = "Cannot find 'category_name' in request body!"
#         return jsonify({'status': 'fail', 'message': errorMessage}), 400
#
#     try:
#         categoryToChange.name = requestJSON['category_name']
#         db.session.commit()
#         return jsonify({'status': 'success', 'message': 'Changed category name!'}), 200
#     except IntegrityError as e:
#         errorInfo = e.orig.args
#         return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
#
#
# @views_blueprint.route('/admin/products/categories/<int:category_id>', methods=['DELETE'])
# def remove_category(category_id):
#     categoryToDelete = Categories.query.get(category_id)
#     if categoryToDelete is None:
#         return jsonify({'status': 'fail', 'message': "Category doesn't exist!"}), 404
#
#     try:
#         db.session.delete(categoryToDelete)
#         db.session.commit()
#         return jsonify({'status': 'success', 'message': 'Category deleted!'}), 200
#     except IntegrityError as e:
#         errorInfo = e.orig.args
#         return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409


@views_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Products.query.get(product_id)
    if product is None:
        return jsonify({'status': 'fail', 'message': "Product doesn't exist!"}), 404

    productDict = makeProductDict(product)

    responseData = {'status': 'success', 'data': productDict}
    return jsonify(responseData), 200


@views_blueprint.route('/products', methods=['GET'])
def get_all_products():
    query = request.args.get('query');
    if query:
        products = Products.query.filter(Products.name.contains(query)).all()
    else:
        page = request.args.get('page', 1, type=int)
        products = Products.query.paginate(page=page, per_page=9)
    productList = []

    for product in products.items:
        tempDict = makeProductDict(product)
        productList.append(tempDict)

    responseData = {}
    responseData['status'] = 'success'
    responseData['data'] = productList

    return jsonify(responseData), 200


@views_blueprint.route('/products/<string:category_name>', methods=['GET'])
def get_all_products_in_category(category_name):
    category = Categories.query.filter_by(name=category_name).first()

    if category is None:
        return jsonify({'status': 'fail', 'message': "Category doesn't exist!"}), 404

    page = request.args.get('page', 1, type=int)
    products = Products.query.filter_by(category_id=category.id).paginate(page=page, per_page=9)
    productList = []

    for product in products.items:
        tempDict = makeProductDict(product)
        productList.append(tempDict)

    responseData = {}
    responseData['status'] = 'success'
    responseData['data'] = productList

    return jsonify(responseData), 200

@views_blueprint.route('/admin/products/<int:category_id>', methods=['POST'])
def add_new_product(category_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        url = os.environ.get('USERS_URL') + "/users/token"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth_token
        }

        response = requests.request('GET', url, headers=headers)
        json_response = response.json()
        if json_response['data']['admin']:
            category = Categories.query.get(category_id)
            if category is None:
                return jsonify({'status': 'fail', 'message': "Category doesn't exist!"}), 400

            requestForm = request.form

            if requestForm is None:
                errorMessage = 'Cannot find JSON object in request body!'
                return jsonify({'status': 'fail', 'message': errorMessage}), 400

            name = requestForm.get('name')
            price = requestForm.get('price')
            product_description = requestForm.get('product_description')
            picture_file = request.files['file']

            try:
                picture_key = str(random.randint(1000, 9999)) + str(time.time()) + picture_file.filename
                my_bucket = s3.Bucket(S3_BUCKET)
                my_bucket.Object(picture_key).put(Body=picture_file)
                object_acl = s3.ObjectAcl(S3_BUCKET, picture_key)
                object_acl.put(ACL='public-read')
                picture_url = 'https://s3.eu-central-1.amazonaws.com/' + S3_BUCKET + '/' + picture_key;

                newProduct = Products(category_id, name, price)
                db.session.add(newProduct)
                db.session.flush()
                newProductResources = ProductResources( \
                    newProduct.id, \
                    picture_url, \
                    product_description)
                db.session.add(newProductResources)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'New product added!'}), 200
            except IntegrityError as e:
                errorInfo = e.orig.args
                return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
        else:
            errorMessage = 'You must be admin to add new entry!'
            return jsonify({'status': 'fail', 'message': errorMessage}), 400
    else:
        errorMessage = 'Cannot find token!'
        return jsonify({'status': 'fail', 'message': errorMessage}), 400

@views_blueprint.route('/admin/products/edit/<int:product_id>', methods=['POST'])
def change_product_data(product_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        url = os.environ.get('USERS_URL') + "/users/token"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth_token
        }

        response = requests.request('GET', url, headers=headers)
        json_response = response.json()
        if json_response['data']['admin']:
            product = Products.query.get(product_id)
            if product is None:
                return jsonify({'status': 'fail', 'message': "Product doesn't exist!"}), 404

            requestForm = request.form

            if requestForm is None:
                errorMessage = 'Cannot find JSON object in request body!'
                return jsonify({'status': 'fail', 'message': errorMessage}), 400


            try:
                product.name = requestForm.get('name')
                product.price = requestForm.get('price')
                productResources = ProductResources.query.filter_by(product_id=product.id).first()

                try:
                    file = request.files['file']
                except:
                    file = None

                if file:
                    picture_file = request.files['file']
                    picture_key = str(random.randint(1000, 9999)) + str(time.time()) + picture_file.filename
                    my_bucket = s3.Bucket(S3_BUCKET)
                    my_bucket.Object(picture_key).put(Body=picture_file)
                    object_acl = s3.ObjectAcl(S3_BUCKET, picture_key)
                    object_acl.put(ACL='public-read')
                    productResources.picture_file_url = 'https://s3.eu-central-1.amazonaws.com/' + S3_BUCKET + '/' + picture_key;

                productResources.product_description = requestForm.get('product_description')
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Product data changed!'}), 200
            except IntegrityError as e:
                errorInfo = e.orig.args
                return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
        else:
            errorMessage = 'You must be admin to add new entry!'
            return jsonify({'status': 'fail', 'message': errorMessage}), 400
    else:
        errorMessage = 'Cannot find token!'
        return jsonify({'status': 'fail', 'message': errorMessage}), 400


@views_blueprint.route('/admin/products/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        url = os.environ.get('USERS_URL') + "/users/token"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth_token
        }

        response = requests.request('GET', url, headers=headers)
        json_response = response.json()
        if json_response['data']['admin']:
            product = Products.query.get(product_id)
            if product is None:
                return jsonify({'status': 'fail', 'message': "Product doesn't exist!"}), 404

            try:
                db.session.delete(product)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Product deleted!'}), 200
            except IntegrityError as e:
                errorInfo = e.orig.args
                return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
        else:
            errorMessage = 'You must be admin to add new entry!'
            return jsonify({'status': 'fail', 'message': errorMessage}), 400
    else:
        errorMessage = 'Cannot find token!'
        return jsonify({'status': 'fail', 'message': errorMessage}), 400


@views_blueprint.route('/admin/products/<int:category_id>', methods=['DELETE'])
def remove_all_products_from_category(category_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        url = os.environ.get('USERS_URL') + "/users/token"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth_token
        }

        response = requests.request('GET', url, headers=headers)
        json_response = response.json()
        if json_response['data']['admin']:
            category = Categories.query.get(category_id)

            if category is None:
                return jsonify({'status': 'fail', 'message': "Category doesn't exist!"}), 404

            products = Products.query.filter_by(category_id=category.id).all()

            if products is None:
                message = 'Nothing to do, no product to delete in that category!'
                return jsonify({'status': 'success', 'message': message}), 200

            try:
                for product in products:
                    db.session.delete(product)

                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Products deleted!'}), 200
            except IntegrityError as e:
                errorInfo = e.orig.args
                return jsonify({'status': 'fail', 'message': errorInfo[0]}), 409
        else:
            errorMessage = 'You must be admin to add new entry!'
            return jsonify({'status': 'fail', 'message': errorMessage}), 400
    else:
        errorMessage = 'Cannot find token!'
        return jsonify({'status': 'fail', 'message': errorMessage}), 400