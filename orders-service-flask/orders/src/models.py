from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OrderStatus(db.Model):
	__tablename__ = 'order_status_codes'
	
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(128), nullable=False, unique=True)
	order = db.relationship('Orders', backref='order_status', lazy=True)
	
	def __init__(self, id, description):
		self.id = id
		self.description = description

class Orders(db.Model):
	__tablename__ = 'orders'
	
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, nullable=False)
	order_status_code = db.Column(db.Integer, db.ForeignKey('order_status_codes.id'), nullable=False)
	order_items = db.relationship('OrderItems', backref='order', lazy='joined')
	
	def __init__(self, id, customer_id):
		self.id = id
		self.customer_id = customer_id
		self.order_status_code = 0

class OrderItems(db.Model):
	__tablename__ = 'order_items'
	__table_args__ = (
        db.UniqueConstraint('order_id', 'product_id', name='unique_order_product'),
	)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
	product_id = db.Column(db.Integer, nullable=False)
	quantity = db.Column(db.Integer, nullable=False)
	
	def __init__(self, order_id, product_id, quantity):
		self.order_id = order_id
		self.product_id = product_id
		self.quantity = quantity
