from flask import Flask, request
from genre_classf_CNN import* 

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if url == "lol":
        return genre()

    elif url == "xd":
        return "xd"

@app.route('/af')
def af():
    url = request.args.get('url')
    if url == "lol":
        return genre()

    elif url == "xd":
        return "xd"

app.run(host='0.0.0.0',port=5000, debug=True)