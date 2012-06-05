'''
Created on 12-mei-2012

@author: Erik Vandeputte
'''
import pylast
from pyechonest import song

#API_KEY and API_SECRET
API_KEY = "23d4d080ab66300840b2f6cc49151fbb"
API_SECRET = "02b5d7e670df35c99b0c09f50e365239"

def get_tempo(artist, title):
    "gets the tempo for a song"
    results = song.search(artist=artist, title=title, results=1, buckets=['audio_summary'])
    if len(results) > 0:
        return results[0].audio_summary['tempo']
    else:
        return None

def get_data():
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
    user = network.get_user("perikvdp");
    return user.get_loved_tracks();

if __name__ == '__main__':
    artist = "Lady Gaga"
    title = "Poker face"
    print artist,title, "tempo: ",get_tempo(artist,title)
    '''tracks = get_data()
    for lovedtrack in tracks:
        track = lovedtrack[0]
        artist = track.artist
        title = track.title
        print artist,title, "tempo: ",get_tempo(artist,title)'''