import eyed3
from .utils import get_file_type

class Song:
	def __init__(self, filepath):
		self.filepath = filepath
		self.audiofile = eyed3.load(filepath)
	
	def modify(self, title = None, artist = None, album = None, genre = None, lyrics = None, image_path = None):
		
		if(title is not None):
			self.audiofile.tag.title = title
		if(artist is not None):
			self.audiofile.tag.artist = artist
		if(album is not None):
			self.audiofile.tag.album = album
		if(genre is not None):
			self.audiofile.tag.genre = genre
		if(lyrics is not None):
			self.audiofile.tag.lyrics.set(lyrics)		
		if(image_path is not None):
			self.audiofile.tag.images.set(3, open(image_path, 'rb').read(), 'image/'+get_file_type(image_path))
		self.audiofile.tag.save()
		
	def get_tag(self):
		tag_info = dict()
		tag_info['title'] = self.audiofile.tag.title
		tag_info['artist'] = self.audiofile.tag.artist 
		tag_info['album'] = self.audiofile.tag.album 
		tag_info['genre'] = self.audiofile.tag.genre
		tag_info['lyrics'] = self.audiofile.tag.lyrics[0].text
		return tag_info
		