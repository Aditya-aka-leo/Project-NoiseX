import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request
from genre_classf_CNN import * 
from JsonExtractor import *
def download_from_s3(url):
    import wget
    output_directory=""
    url=""
    filename = wget.download(url)
    print(filename)
    s_genre=genre(filename)
    s_finger_print=audio_finger_print(filename)
    print(s_genre)
    print(s_finger_print)    
    return "none"
    










