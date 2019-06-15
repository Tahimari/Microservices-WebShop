import os

PROJECT_ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
DATABASE_DIR_PATH = os.path.join(PROJECT_ROOT_PATH, 'db')
DATABASE_FILE_NAME = 'db.sqlite'
DATABASE_FILE_PATH = os.path.join(DATABASE_DIR_PATH, DATABASE_FILE_NAME)
PUBLIC_KEY = "secret"
TOKEN_ENCODING_ALGORITHM = 'HS256'

APP_RUNNING_PORT = 80
APP_HOST_ADDRESS = '0.0.0.0'
APP_DEBUG_MODE = True

