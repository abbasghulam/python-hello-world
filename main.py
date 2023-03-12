from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World!'

app.run(debug=True, host='0.0.0.0', port='5000')
