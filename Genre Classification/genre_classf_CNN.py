def genre():
    import os
    from re import A
    import librosa
    import math
    import json
    import numpy as np
    import tensorflow
    JSON_PATH =  "bulla.json"
    SAMPLE_RATE = 22050
    DURATION = 30 #as per to the data set the average value of the audio length 
    SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
    def save_mfcc(dataset_path,json_path,n_mfcc=13,n_fft=2048 , hop_length=512 , num_segments=5):
        #creating dictionary to store data
        lis=[]
        num_sample_per_segment = int(SAMPLES_PER_TRACK / num_segments)
        expected_num_mfcc_vectors_per_segment = math.ceil(num_sample_per_segment / hop_length) #this is to solve the error of audio clips less than 30 aur greater than 30
        signal,sr = librosa.load("test1.wav" ,sr = SAMPLE_RATE)
        #now we need the audio file split it into the small segments just to increase the number of data set 
        for s in range(num_segments):
            start_sample = num_sample_per_segment * s
            finish_sample = start_sample + num_sample_per_segment
            mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],sr=sr,n_fft=n_fft, n_mfcc=n_mfcc,hop_length=hop_length)
            mfcc = mfcc.T
            #we want to store the mfccs for the segment if it has the expected length 
            if len(mfcc) == expected_num_mfcc_vectors_per_segment : 
                lis.append(mfcc)
            return lis
    def predict():
        model = tensorflow.keras.models.load_model("saved model")
        X = save_mfcc("gt",JSON_PATH,num_segments=10)
        X = np.array(X)
        X = X[...,np.newaxis] 
        prediction = model.predict(X)
        #extract index with max value in predicion as we are using softmax
        prediction_index = np.argmax(prediction,axis=1)
        # print(prediction_index)
        m = prediction_index[0]
        return m
    def genre_gen():
        choice = predict()
        gen = "none"
        if choice == 0:
            gen = "blues"
        if choice == 1:
            gen = "classical"
        if choice == 2:
            gen = "country"
        if choice == 3:
            gen = "disco"
        if choice == 4:
            gen = "hiphop"
        if choice == 5:
            gen = "jazz"
        if choice == 6:
            gen = "metal"
        if choice == 7:
            gen = "pop"
        if choice == 8:
            gen = "reggae"
        if choice == 9:
            gen = "rock"
        return gen

    print(genre_gen())
genre()











            
        
         
        

