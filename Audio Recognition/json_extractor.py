
import base64
import hashlib
import hmac
import os
import sys
import time
import json
import requests
from subprocess import Popen
json_path = "audio_details.json"
import PlatForm_Segregation as pt

'''
Replace "###...###" below with your project's host, access_key and access_secret.
'''
access_key = "2f5437bd7d3a1681d15d7e12ab614421"
access_secret = "6mrJrUFc03yizpUeq3MSTC63bWMcPCkjwl9mKDJl"
requrl = "http://identify-eu-west-1.acrcloud.com/v1/identify"

http_method = "POST"
http_uri = "/v1/identify"
# default is "fingerprint", it's for recognizing fingerprint, 
# if you want to identify audio, please change data_type="audio"
data_type = "audio"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
    timestamp)  

sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                 digestmod=hashlib.sha1).digest()).decode('ascii')


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
# File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better

# Audio trimming
from email.mime import base   
import pydub    # pydub is a python library for manipulating audio
from pydub import AudioSegment  # AudioSegment is a class for representing an audio file and a way to slice and manipulate it
import os 

base_dir = r"D:\NoiseX temp\Audio_recognition"   # change this to your own directory
# export_dir = r"E:\Project\audio_clustering\songs\export"    # if you want to export audio file to some other directory, uncomment this and in line 57 change base_dir to export_dir

sound = AudioSegment.from_mp3(os.path.join(base_dir, "Night.mp3"))

first_cut_point = (1*60 + 18) * 1000   # 1 minute 18 seconds   
last_cut_point = (1*60 + 33) * 1000    # 1 minute 33 seconds

sound_clip = sound[first_cut_point:last_cut_point]  # create a sound clip from the first_cut_point to the last_cut_point

sound_clip.export(os.path.join(base_dir, "trimmed.mp3"), format="mp3")  # export the sound clip as an mp3 file

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# open the file and read the content
f = open("./trimmed.mp3", "rb")
sample_bytes = os.path.getsize("./trimmed.mp3")   # get the size of the file

files = [
    ('sample', ('trimmed.mp3', open('trimmed.mp3', 'rb'), 'audio/mpeg'))   # create a tuple of the file name, file content and file type
]
data = {'access_key': access_key,
        'sample_bytes': sample_bytes,
        'timestamp': str(timestamp),
        'signature': sign,
        'data_type': data_type,
        "signature_version": signature_version}   # create a dictionary of the data to be sent

r = requests.post(requrl, files=files, data=data)    # send the request to the server
r.encoding = "utf-8"    # set the encoding of the response to utf-8
jsonString=(r.text)     # get the response as a string
content = json.loads(jsonString)    # convert the string to a dictionary


with open('audio_details.json', 'w') as outfile:     
    outfile.write(jsonString)

pt.plat()

