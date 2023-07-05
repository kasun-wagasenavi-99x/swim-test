from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return 'Python - Flask app - 2 running!'