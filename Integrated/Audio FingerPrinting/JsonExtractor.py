def audio_finger_print(song_name):
    import base64
    import hashlib
    import hmac
    import os
    import sys
    import time
    import json
    import requests
    from subprocess import Popen
    json_path = r"/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting/audio_details.json"
    import PlatForm_Segregation as pt
    import ffprobe
    '''
    Replace "###...###" below with your project's host, access_key and access_secret.
    '''
    access_key = "e29847bce69fd11d8a6bc7284f537647"
    access_secret = "uCz61R0cOVh4EFqSjTeHQrxS8fmBSjm2lZFhUuar"
    requrl = "http://identify-ap-southeast-1.acrcloud.com/v1/identify"

    http_method = "POST"
    http_uri = "/v1/identify"

    data_type = "audio"
    signature_version = "1"
    timestamp = time.time()

    string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
        timestamp)  

    sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                    digestmod=hashlib.sha1).digest()).decode('ascii')
    from email.mime import base   
    from pydub import AudioSegment  
    import os 

    base_dir = r"/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting/" 
    song_dir=r"/home/ubuntu/Project-NoiseX/songs/"
    song_dir=os.path.join(song_dir,song_name)
   # song_dir=song_dir+"./"+song_name

    sound = AudioSegment.from_file(song_dir, "mp3")

    first_cut_point = (1*60 + 18) * 1000      
    last_cut_point = (1*60 + 33) * 1000    

    sound_clip = sound[first_cut_point:last_cut_point]  

    sound_clip.export(os.path.join(base_dir, "trimmed.mp3"), format="mp3")  
    trimmed_path=base_dir+"./"+"trimmed.mp3"

    f = open(trimmed_path, "rb")
    sample_bytes = os.path.getsize(trimmed_path)  

    files = [
        ('sample', ('trimmed.mp3', open(trimmed_path, 'rb'), 'audio/mpeg'))
    ]
    data = {'access_key': access_key,
            'sample_bytes': sample_bytes,
            'timestamp': str(timestamp),
            'signature': sign,
            'data_type': data_type,
            "signature_version": signature_version}   

    r = requests.post(requrl, files=files, data=data)    
    r.encoding = "utf-8"    
    jsonString=(r.text)     
    content = json.loads(jsonString)    


    with open(r'/home/ubuntu/Project-NoiseX/Integrated/Audio FingerPrinting/audio_details.json', 'w') as outfile:     
        outfile.write(jsonString)

    print_links=pt.plat()
    
    return print_links
