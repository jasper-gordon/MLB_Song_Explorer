#A file that handles music translation and playback for a given MLB "song," a list of five possible interger values
#ranging from 0 to 4.
from playsound import playsound

sample_song = [1, 0, 1, 3, 2, 0, 4, 0, 0, 1, 2, 1, 0, 0, 4]

class Music_Player():

    def __init__(self, song):
        self.song = song

   
    def play_song(self):
        for i in self.song:
            note = "sound_" + str(sample_song[i]) + ".mp3"
            playsound(note)

 