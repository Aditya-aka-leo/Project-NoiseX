from lib2to3.pgen2.token import LBRACE
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


file = "aud.wav"  #this to load the file in python

#Waveform

signal,sr =librosa.load(file,sr=22050) #signal is vector with values number  =  sr*duration of the audio
#and sr will be equall to the sample provided 
librosa.display.waveplot(signal,sr = sr)   #this is to display the waveform with matplotlib later to print  it out 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Now lets convert this into a spectrum using fourier transform

fft = np.fft.fft(signal)     #this is to create fft with an array that can take data like signal
magnitude = np.abs(fft)      #this is to extract the main values like from the complex values that the signal has

frequency = np.linspace(0,sr,len(magnitude))   #this is frequency  that we expect

print(frequency)
left_frequency =frequency[:int(len(frequency)/2)]   #this is note necessary but it is required to cut the plot into short 
left_magnitude =frequency[:int(len(magnitude)/2)]   #this is note necessary but it is required to cut the plot into short 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Doing STFT
n_fft = 2048    #giving how many samples to stft
hop_length =512 #its the is amount of freq to jump after one fft
stft = librosa.core.stft(signal,hop_length=hop_length,n_fft=n_fft)  #Creating stft 
spectrogram = np.abs(stft)  #getting the magnitude/main values from complex values
log_spectrogram = librosa.amplitude_to_db(spectrogram)  #applying a log to the spectrogram to make it easier to read

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Extracting Mffcs

MFFCs = librosa.feature.mfcc(signal ,n_fft=n_fft,hop_length=hop_length,n_mfcc=13)   #we use the librosa lib to extract the mffc coeficients 
librosa.display.specshow(MFFCs, sr = sr, hop_length=hop_length)  #this is to show the spectrogram that we created
plt.xlabel("Time")
plt.ylabel("MFFCs")
plt.colorbar()
plt.show()









