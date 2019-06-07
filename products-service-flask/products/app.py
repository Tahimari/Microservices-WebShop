from flask import Flask, jsonify

# Init app
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def hello():
	return jsonify({"response" : "ping ping pong!"})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)
