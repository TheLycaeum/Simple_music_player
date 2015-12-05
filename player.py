import json

import tracks

class Playlist(object):
    def __init__(self, playlist_filename = None):
        if playlist_filename:
            with open(playlist_filename, "r") as f:
                self.songs = json.loads(f.read())
        else:
            self.songs = []
    
    def get_song_list(self):
        return self.songs

    def add_song(self, song):
        self.songs.append(song)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.songs))
            
    def play(self, filename):
        track = tracks.get_track(filename)
        track.play()
            

    def play_all(self):
        for i in self.songs:
            try:
                self.play(i)
            except tracks.UnknownFormat as e:
                print "Skipping {}".format(i)


        
        
        
        

    
