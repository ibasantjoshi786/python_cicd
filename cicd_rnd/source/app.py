from flask import Flask, request
from cicd_rnd.source.calculator import *

# Create a Flask web application
app = Flask(__name__)


# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/calculate')
def calculate_add():
    data = request.get_json()
    no_1 = data["no_1"]
    no_2 = data["no_2"]
    operation = data["operation"]
    result = "Operation not supported"
    if operation == 'sum':
        result = "The addition of the 2 no is : " + str(addition(no_1, no_2))
    elif operation == 'subtraction':
        result = "The subtraction of the 2 no is : " + str(subtraction(no_1, no_2))

    return {"result": result}


if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run(host="0.0.0.0")

