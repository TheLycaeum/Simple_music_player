import os

class UnknownFormat(Exception):
    pass

def get_track(filename):
    track_types = {"mp3" : MP3Track,
                   "ogg" : OGGTrack}
    
    name, extension = os.path.splitext(filename)
    extension = extension[1:]

    try:
        return track_types[extension](filename)
    except KeyError:
        raise UnknownFormat("Cannot play track of type {}".format(extension))

class Track(object):
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    def get_metadata(self):
        raise NotImplementedError()


class MP3Track(Track):
    def play(self):
        # Actual code to decode an mp3
        print "Now playing using MP3 codec"
    
    def stop(self):
        print "Now stopping MP3 playback"

    def get_metadata(self):
        return "MP3 : {}".format(self.filename)


class OGGTrack(Track):
    def play(self):
        # Actual code to decode an OGG
        print "Now playing using OGG codec"
    
    def stop(self):
        print "Now stopping OGG playback"

    def get_metadata(self):
        return "OGG : {}".format(self.filename)

        
    
