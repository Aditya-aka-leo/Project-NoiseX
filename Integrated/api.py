import sys
sys.path.append(r'D:\Project-NoiseX\Integrated\Audio FingerPrinting')
sys.path.append(r'D:\Project-NoiseX\Integrated\Genre Classification')
from flask import Flask, request
from genre_classf_CNN import * 
from JsonExtractor import *



app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    return genre(url)

@app.route('/af')
def af():
    url = request.args.get('url')
    return audio_finger_print(url)

app.run(host='0.0.0.0',port=5000, debug=True)



