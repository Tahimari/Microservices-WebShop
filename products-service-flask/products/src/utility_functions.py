import os
from src.models import *
from src.schemas import *
from src.config import DATABASE_DIR_PATH
from src.seed import seed_db

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)

def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	# Create schema
	db.create_all()
	
	# Fill database with data
	seed_db()

	# Commit changes
	db.session.commit()

def makeProductDict(product):
	productDict = {}
	
	productDict['id'] = product.id
	productDict['name'] = product.name
	productDict['price'] = product.price
	
	category = Categories.query.get(product.category_id)
	categorySchema = CategoriesSchema(strict=True)
	productDict['category'] = categorySchema.dump(category).data
	
	productResources = ProductResources.query.filter_by(product_id=product.id).first()
	resourcesSchema = ProductResourcesSchema(strict=True)
	productDict['resources'] = resourcesSchema.dump(productResources).data
	
	return productDict
