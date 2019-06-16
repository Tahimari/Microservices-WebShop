from flask import Flask
from flask_cors import CORS

# Init app
app = Flask(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
	app.run(debug=True, port=80)
