from flask import Flask, jsonify
from src.config import APP_DEBUG_MODE, APP_HOST_ADDRESS, APP_RUNNING_PORT

# Init app
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def hello():
	return jsonify({"response" : "ping ping pong!"})

if __name__ == '__main__':
	app.run(debug=APP_DEBUG_MODE, host=APP_HOST_ADDRESS, port=APP_RUNNING_PORT)
