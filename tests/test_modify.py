import pytest
import string
import random
import os
import pkg_resources

from titanium_rhythm.modify import Song

SONG_FOLDER_PATH = pkg_resources.resource_filename('titanium_rhythm', 'songs/')

def test_modify():
	rand_string = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
	
	# dirpath, dirs, files = next(os.walk(SONG_FOLDER_PATH))
	song_file = os.path.join(SONG_FOLDER_PATH, 'unknown.mp3')
	
	s = Song(song_file)
	s.modify(title = rand_string, artist = rand_string, album = rand_string, genre = 'rock', lyrics = rand_string, image_path = os.path.join(SONG_FOLDER_PATH, 'images.png'))
	s.modify_title(title = rand_string)
	s.modify_artist(artist = rand_string)
	s.modify_genre(genre = 'rock')
	s.modify_lyrics(lyrics = rand_string)
	s.modify_image_path(image_path = os.path.join(SONG_FOLDER_PATH, 'images.png'))
	del(s)
	
	new_s = Song(song_file)
	tag_info = new_s.get_tag()
	
	assert(tag_info['title'] == rand_string)
	assert(tag_info['artist'] == rand_string)
	assert(tag_info['album'] == rand_string)
	assert(tag_info['genre'].name == 'Rock')
	assert(tag_info['lyrics'] == rand_string)
	
