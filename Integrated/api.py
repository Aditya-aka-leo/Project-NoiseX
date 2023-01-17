import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request , jsonify
from genre_classf_CNN import * 
from JsonExtractor import *
from download_file import *
app = Flask(__name__)

@app.route('/')
def index():
    url="https://noisex.s3.ap-south-1.amazonaws.com/songs/"+request.args.get('url')
    audio_data=download_from_s3(url)
    return jsonify(audio_data)

app.run(host='0.0.0.0',port=5000)



