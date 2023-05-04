import sys
sys.path.append(r'/home/leo/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/leo/Integrated/Genre Classification')
sys.path.append(r'/home/leo/Integrated/songs')
from flask import Flask, request
from genre_classf_CNN import * 
from JsonExtractor import *
from os import path
from pydub import AudioSegment
import os
def del_files():
    path = r"/home/leo/Integrated/songs"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)

def call_models(filename):
   # s_finger_print=audio_finger_print(filename)
    s_genre_print=genre(filename)
    #print(s_finger_print)
    #print(s_genre_print)
    #s_data=s_finger_print
    #s_data["Genre"]=s_genre_print
    return s_genre_print
   # audio_finger_print(
    

def download_from_s3(url):
    del_files()
    import wget
    output_directory="/home/leo/Integrated/songs"
    url=url
    filename = wget.download(url,out=output_directory)
    src=os.path.join(output_directory,filename)
    final_data=call_models(filename)
    return final_data
    


#print(download_from_s3("https://noisex-songs.s3.ap-south-1.amazonaws.com/1683164001788.wav"))



