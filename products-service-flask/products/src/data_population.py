from src.models import *

def populate_database():
	# Categories
	db.session.add(Categories('Shoes'))
	db.session.add(Categories('T-Shirts'))
	db.session.add(Categories('Jackets'))
	db.session.add(Categories('Trousers'))
	db.session.add(Categories('Shirts'))
	
	# Products (TODO)
	
	# Product resources (TODO)
