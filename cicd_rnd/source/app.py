from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!. I am a flask web server. v1'

if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run()
