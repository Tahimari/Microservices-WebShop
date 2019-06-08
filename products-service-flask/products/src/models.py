from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categories(db.Model):
	__tablename__ = 'categories'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128), nullable=False, unique=True)
	
	products = db.relationship('Products', backref='category', lazy='joined')
	
	def __init__(self, name):
		self.name = name

class Products(db.Model):
	__tablename__ = 'products'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
	name = db.Column(db.String(128), nullable=False)
	price = db.Column(db.Float, nullable=False)
	
	resources = db.relationship('ProductResources', backref='product', lazy='joined')
	
	def __init__(self, category_id, name, price):
		self.category_id = category_id
		self.name = name
		self.price = price

class ProductResources(db.Model):
	__tablename__ = 'product_resources'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
	pictureFileUrl = db.Column(db.String(2048), nullable=False),
	productDescription = db.Column(db.Text, nullable=True)
	
	def __init__(self, product_id, pictureFileUrl, productDescription):
		self.product_id = product_id
		self.pictureFileUrl = pictureFileUrl
		self.productDescription = productDescription
