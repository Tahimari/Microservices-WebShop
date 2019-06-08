import os
from src.models import *
from src.config import DATABASE_DIR_PATH

def doesDatabaseExist(pathToDatabase):
	return os.path.isfile(pathToDatabase)
	
def prepare_database():
	if not os.path.exists(DATABASE_DIR_PATH):
		os.mkdir(DATABASE_DIR_PATH)
	
	db.create_all()
	db.session.commit()
