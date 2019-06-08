import os
from src.models import *
from src.schemas import *
from src.config import DATABASE_DIR_PATH

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)

def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	db.create_all()
	db.session.add(Categories('Shoes'))
	db.session.add(Categories('T-Shirts'))
	db.session.add(Categories('Jackets'))
	db.session.add(Categories('Trousers'))
	db.session.add(Categories('Shirts'))
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
