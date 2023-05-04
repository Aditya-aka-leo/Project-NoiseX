import sys
import os
sys.path.append(r'/home/leo/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/leo/Integrated/Genre Classification')
sys.path.append(r'/home/leo/Integrated/songs')
from flask import Flask, request , jsonify
from genre_classf_CNN import * 
# from JsonExtractor import *
from download_file import *
app = Flask(__name__)

@app.route('/')
def index():
    url=os.path.join("https://noisex-songs.s3.ap-south-1.amazonaws.com",request.args.get('url'))
    audio_data=download_from_s3(url)
    return jsonify(audio_data)

app.run(host='0.0.0.0',port=5000)
