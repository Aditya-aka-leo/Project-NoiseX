from libraries import *
def genre(s_ap):
    SAMPLE_RATE = 22050
    DURATION = 30 
    SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
    def save_mfcc(apath='',n_mfcc=13,n_fft=2048 , hop_length=512 , num_segments=5):
        lis=[]
        num_sample_per_segment = int(SAMPLES_PER_TRACK / num_segments)
        expected_num_mfcc_vectors_per_segment = math.ceil(num_sample_per_segment / hop_length) 
        ap=os.path.join("D:\Project-NoiseX\Integrated\Genre Classification\Songs",apath)
        signal,sr = librosa.load(ap,sr = SAMPLE_RATE)
        for s in range(num_segments):
            start_sample = num_sample_per_segment * s
            finish_sample = start_sample + num_sample_per_segment
            mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],sr=sr,n_fft=n_fft, n_mfcc=n_mfcc,hop_length=hop_length)
            mfcc = mfcc.T
            if len(mfcc) == expected_num_mfcc_vectors_per_segment : 
                lis.append(mfcc)
            return lis
    def predict(s_ap):
        X = save_mfcc(apath=s_ap,num_segments=10)
        X = np.array(X)
        X = X[...,np.newaxis] 
        print(X)
        prediction = model_genre.predict(X)
        prediction_index = np.argmax(prediction,axis=1)
        # print(prediction_index)
        m = prediction_index[0]
        return m
    def genre_gen(s_ap):
        choice = predict(s_ap)
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

    return genre_gen(s_ap)






            
        
         
        

