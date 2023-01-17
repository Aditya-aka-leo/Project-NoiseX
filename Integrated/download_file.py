import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
#sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request
#from genre_classf_CNN import * 
from JsonExtractor import *
from os import path
from pydub import AudioSegment

def download_from_s3(url):
    import wget
    output_directory="/home/ubuntu/Project-NoiseX/songs"
    url=url
    filename = wget.download(url,out=output_directory)
    print(filename)
    #s_genre=genre(filename)
    s_finger_print=audio_finger_print(filename)
    #print(s_genre)
    print(s_finger_print)    
    return "none"
download_from_s3("https://noisex.s3.ap-south-1.amazonaws.com/songs/1673933965681.mp3")    










