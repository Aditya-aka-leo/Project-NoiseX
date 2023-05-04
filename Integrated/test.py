import sys
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting')
sys.path.append(r'/home/ubuntu/Project-NoiseX/Integrated/Genre Classification')
sys.path.append(r'/home/ubuntu/Project-NoiseX/songs')
from flask import Flask, request
from genre_classf_CNN import *
from JsonExtractor import *

print(audio_finger_print('Billie Eilish - Bellyache.mp3'))
