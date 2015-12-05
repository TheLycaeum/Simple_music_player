#interface.py

import sys

import player
import tracks

def load_playlist(filename):
    f = player.Playlist(filename)
    return f


def main():
    try:
        playlist_file = sys.argv[1]
    except IndexError:
        playlist_file = None

    playlist = load_playlist(playlist_file)
    while True:
        command = raw_input("What should I do?")
        if command.startswith("load"):
            song = command.split()[1]
            playlist.add_song(song)
        elif command.startswith("playall"):
            print playlist.play_all()
        elif command.startswith("play"):
            song = command.split()[1]
            playlist.play(song)
        elif command.startswith("save"):
            playlist_file = command.split()[1]
            playlist.save(playlist_file)
        elif command.startswith("show"):
            print playlist.get_song_list()
        else:
            print "I don't understand that command"

if __name__ == '__main__':
    main() 


