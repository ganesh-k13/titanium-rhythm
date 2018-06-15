import pytest
import string
import random
import os
import pkg_resources

from titanium_rhythm.modify import Song

SONG_FOLDER_PATH = pkg_resources.resource_filename('titanium_rhythm', 'songs/')

def test_modify():
	rand_string = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
	
	dirpath, dirs, files = next(os.walk(SONG_FOLDER_PATH))
	song_file = os.path.join(dirpath, files[0])
	
	s = Song(song_file)
	s.modify(title = rand_string, artist = rand_string, album = rand_string, genre = 'rock', lyrics = rand_string)
	del(s)
	
	new_s = Song(song_file)
	tag_info = new_s.get_tag()
	
	assert(tag_info['title'] == rand_string)
	assert(tag_info['artist'] == rand_string)
	assert(tag_info['album'] == rand_string)
	assert(tag_info['genre'].name == 'Rock')
	# assert(tag_info['lyrics'] == rand_string)

