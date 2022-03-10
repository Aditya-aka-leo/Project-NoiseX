import mutagen
from mutagen.wave import WAVE


# function to convert the information to seconds
def audio_duration(length):
	hours = length // 3600 # calculate in hours
	length %= 3600
	mins = length // 60 # calculate in minutes
	length %= 60
	seconds = length # calculate in seconds

	return hours, mins, seconds # returns the song duration



audio = WAVE("test.wav") # create a WAVE object, specify the directory address of your wavpack file

# contains all the metadata about the wavpack file
audio_info = audio.info
length = int(audio_info.length)
hours, mins, seconds = audio_duration(length)
print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
