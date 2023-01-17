import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request
from genre_classf_CNN import * 
from JsonExtractor import *

app = Flask(__name__)

@app.route('/')
def index():
    return xd

@app.route('/gc')
def gc():
    url = request.args.get('url')
    return genre(url)

@app.route('/af')
def af():
    url = request.args.get('url')
    x = audio_finger_print(url)
    return x

app.run(host='0.0.0.0',port=5000)



