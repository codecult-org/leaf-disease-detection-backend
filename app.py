from flask import Flask
import function

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/checking')
def sup():
    return function.evaluate()
