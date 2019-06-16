from flask import Flask
from flask_cors import CORS
from src.models import *
from src.config import *
from src.utility_functions import doesDatabaseExist, prepare_database

# Init app
app = Flask(__name__)

# Config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_FILE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init database
db.init_app(app)
app.app_context().push()

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def run_app(debug_mode):
	if not doesDatabaseExist(DATABASE_FILE_PATH):
		prepare_database()

	app.run(debug=debug_mode, host=APP_HOST_ADDRESS, port=APP_RUNNING_PORT)

if __name__ == '__main__':
	run_app(debug_mode=APP_DEBUG_MODE)
