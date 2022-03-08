from cmath import exp
import os
from re import A
import librosa
import math
import json
DATASET_PATH ="Data"
JSON_PATH =  "data.json"
SAMPLE_RATE = 22050
DURATION = 30 #as per to the data set the average value of the audio length 
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION


def save_mfcc(dataset_path,json_path,n_mfcc=13,n_fft=2048 , hop_length=512 , num_segments=5):
    #creating dictionary to store data
    data = {
        "mapping": [],
        "mfcc": [],
        "labels": []   
    }

    num_sample_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_sample_per_segment / hop_length) #this is to solve the error of audio clips less than 30 aur greater than 30
    #looping through all the genres
    for i , (dirpart ,dirname,filename) in enumerate (os.walk(dataset_path)):
         
        #ensure that we're are not at the root level 
        if dirpart is not dataset_path:
            #Saving The Semantic Label
            dirpart_componet=dirpart.split('\\')     #this is to go the sub folder inside the dataset  (here / means example genre/blue)
            semantic_label=dirpart_componet[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))
            #We need to go to all the audio files in that folder 
            for f in filename:
                file_path = os.path.join(dirpart,f) #this is to give the full directory address of the audio we want to load 
                signal,sr = librosa.load(file_path ,sr = SAMPLE_RATE)
                
                #now we need the audio file split it into the small segments just to increase the number of data set 
                for s in range(num_segments):
                    start_sample = num_sample_per_segment * s
                    finish_sample = start_sample + num_sample_per_segment
                    mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],sr=sr,n_fft=n_fft, n_mfcc=n_mfcc,hop_length=hop_length)
                    mfcc = mfcc.T
                    #we want to store the mfccs for the segment if it has the expected length 
                    if len(mfcc) == expected_num_mfcc_vectors_per_segment : 
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i-1)                    
                        print("{} , segment : {} ".format(file_path,s))
    with open(json_path, 'w') as fp:
        json.dump(data,fp,indent=4)

if __name__ == '__main__':
    save_mfcc(DATASET_PATH,JSON_PATH,num_segments=10)







            
        
         
        

