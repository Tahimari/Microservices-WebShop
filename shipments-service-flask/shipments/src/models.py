from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ShipmentStates(db.Model):
	__tablename__ = 'shipment_states'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False, unique=True)
	description = db.Column(db.Text, nullable=True)
	
	def __init__(self, id, name, description=None):
		self.id = id
		self.name = name
		self.description = description


class ShipmentTypes(db.Model):
	__tablename__ = 'shipment_types'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128), nullable=False, unique=True)
	price = db.Column(db.Float, nullable=False)
	shipping_time = db.Column(db.Integer, nullable=False)
	description = db.Column(db.Text, nullable=True)
	
	def __init__(self, name, price, shipping_time, description=None):
		self.name = name
		self.price = price
		self.shipping_time = shipping_time
		self.description = description

class PersonalData(db.Model):
	__tablename__ = 'personal_data'
	__table_args__ = (
        db.UniqueConstraint('first_name', 'last_name', 'phone_number', \
			name = 'unique_personal_data'),
	)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(128), nullable=False)
	last_name = db.Column(db.String(128), nullable=False)
	phone_number = db.Column(db.String(9), nullable=False)
	
	def __init__(self, first_name, last_name, phone_number):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number

class AddressData(db.Model):
	__tablename__ = 'address_data'
	__table_args__ = (
        db.UniqueConstraint('address_line', 'postal_code', 'city', 'country', \
			name = 'unique_address_data'),
	)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	address_line = db.Column(db.String(512), nullable=False)
	postal_code = db.Column(db.String(128), nullable=False)
	city = db.Column(db.String(128), nullable=False)
	country = db.Column(db.String(128), nullable=False)
	
	def __init__(self, address_line, postal_code, city, country):
		self.address_line = address_line
		self.postal_code = postal_code
		self.city = city
		self.country = country

class MailingData(db.Model):
	__tablename__ = 'mailing_data'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	personal_data_id = db.Column(db.Integer, db.ForeignKey('personal_data.id'), nullable=False)
	address_data_id = db.Column(db.Integer, db.ForeignKey('address_data.id'), nullable=False)
	
	personal_data = db.relationship('PersonalData', backref='mailing_data', lazy='joined')
	address_data = db.relationship('AddressData', backref='mailind_data', lazy='joined')
	
	def __init__(self, personal_data_id, address_data_id):
		self.personal_data_id = personal_data_id
		self.address_data_id = address_data_id

class Shipments(db.Model):
	__tablename__ = 'shipments'
	__table_args__ = (
        db.UniqueConstraint('customer_id', 'order_id', name = 'unique_shipment'),
	)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	customer_id = db.Column(db.Integer, nullable=False)
	order_id = db.Column(db.Integer, nullable=False)
	shipment_type_id = db.Column(db.Integer, db.ForeignKey('shipment_types.id'), nullable=False)
	shipment_state_id = db.Column(db.Integer, db.ForeignKey('shipment_states.id'), nullable=False)
	mailing_data_id = db.Column(db.Integer, db.ForeignKey('mailing_data.id'), nullable=True)
	
	shipment_type = db.relationship('ShipmentTypes', backref='shipments', lazy='joined')
	shipment_state = db.relationship('ShipmentStates', backref='shipments', lazy='joined')
	mailing_data = db.relationship('MailingData', backref='shipments', lazy='joined')
	
	def __init__(self, customer_id, order_id, shipment_type_id, mailing_data_id=None):
		self.customer_id = customer_id
		self.order_id = order_id
		self.shipment_type_id = shipment_type_id
		self.shipment_state_id = 0
		self.mailing_data_id = mailing_data_id
