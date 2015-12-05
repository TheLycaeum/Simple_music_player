import pytest

import tracks

def test_get_track_mp3():
    sample_file = "foo.mp3"
    track = tracks.get_track(sample_file)
    assert isinstance(track, tracks.MP3Track)

def test_get_track_ogg():
    sample_file = "foo.ogg"
    track = tracks.get_track(sample_file)
    assert isinstance(track, tracks.OGGTrack)

def test_get_track_unknown_format():
    sample_file = "foo.blah"
    with pytest.raises(tracks.UnknownFormat):
        track = tracks.get_track(sample_file)

