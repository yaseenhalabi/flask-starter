from flask import Flask, jsonify

app = Flask(__name__)

# Route to display a welcome message
@app.route('/')
def hello():
    return "Welcome to the Flask API!"

# Route to return a JSON response
@app.route('/data')
def get_data():
    data = {'name': 'John Doe', 'age': 30}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
