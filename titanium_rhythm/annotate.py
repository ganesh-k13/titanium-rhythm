import pickle

from titanium_rhythm.modify import Song
from titanium_rhythm.identify import Identify
from titanium_rhythm.setup_api import Setup

def annotate_file(key, song_file):
    Setup.set_key(key)
    i = Identify(song_file)
    pickle_file = i.aidmatch(pickle_required = True)
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    
    s = Song(song_file)
    s.modify_title(data[0].title)
    s.modify_artist(data[0].artists[0].name)
    s.modify_image_path(data[0].images[0]['uri'])
    s.modify_filename(data[0].title+'.mp3')