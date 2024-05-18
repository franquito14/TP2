
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/goodbye')
def goodbye():
    return 'Goodbye, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')