import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request
from genre_classf_CNN import * 
from JsonExtractor import *
from os import path
from pydub import AudioSegment
import os
def del_files():
    path = r"/home/ubuntu/Project-NoiseX/songs/"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)

def call_models(filename):
    mp3_name=filename
    wav_name=filename[:-3]+"wav"
    print(wav_name)
    s_finger_print=audio_finger_print(filename)
    s_genre_print=genre(wav_name)
    #print(s_finger_print)
    #print(s_genre_print)
    s_data=s_finger_print
    s_data["Genre"]=s_genre_print
    return s_data
   # audio_finger_print(
    


def mp3_to_wav(src,des):
    des=src[:-3]
    des=des+"wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(des, format="wav")

def download_from_s3(url):
    del_files()
    import wget
    output_directory="/home/ubuntu/Project-NoiseX/songs"
    url=url
    filename = wget.download(url,out=output_directory)
    src=os.path.join(output_directory,filename)
    mp3_to_wav(src,output_directory)
    final_data=call_models(filename)
    return final_data
#download_from_s3("https://noisex.s3.ap-south-1.amazonaws.com/songs/1673933965681.mp3")    









