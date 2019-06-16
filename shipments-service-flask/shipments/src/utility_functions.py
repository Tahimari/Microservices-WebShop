import os
from src.models import *
from src.config import DATABASE_DIR_PATH

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)

def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	# Create database schema
	db.create_all()
	
	# Add shipment states
	db.session.add(ShipmentStates(0, "Pending"))
	db.session.add(ShipmentStates(1, "Completed"))
	db.session.add(ShipmentStates(2, "Cancelled"))
	
	# Add shipment types
	db.session.add(ShipmentTypes("Paczkomat 24/7", 12.99, 3, \
	"Paczkomaty to system skrytek pocztowych, ustawionych w różnych miejscach " \
	"na terenie całego kraju, podobnych w obsłudze do bankomatów, w których " \
	"możliwy jest odbiór przesyłki o dowolnej, dogodnej dla adresata porze, " \
	"24 godziny na dobę przez 7 dni w tygodniu."))
	db.session.add(ShipmentTypes("Przysyłka kurierska", 18.99, 2))
	db.session.add(ShipmentTypes("Odbiór osobisty", 0, 0, "Odbiór w siedzibie sklepu"))
	db.session.add(ShipmentTypes("Paczka za pobraniem", 29.99, 5, "Płatność przy odbiorze"))
	
	# Commit transaction
	db.session.commit()
