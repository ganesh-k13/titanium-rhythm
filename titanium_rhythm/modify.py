import eyed3
from .utils import get_file_type
import validators
import requests
import os

class Song:
    def __init__(self, filepath):
        self.filepath = filepath
        self.audiofile = eyed3.load(filepath)
    
    def modify(self, title = None, artist = None, album = None, genre = None, lyrics = None, image_path = None, filename = None):
        
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
            if(validators.url(image_path) == True):
                img = requests.get(image_path).content
                self.audiofile.tag.images.set(3, img, 'image/jpeg')
            else:
                self.audiofile.tag.images.set(3, open(image_path, 'rb').read(), 'image/'+get_file_type(image_path))
        
        self.audiofile.tag.save()
        
        if(filename is not None):
            os.rename(self.filepath, os.path.join(os.path.dirname(self.filepath), filename))
        
    def modify_title(self, title):
        self.modify(title = title)
    
    def modify_album(self, album):
        self.modify(album = album)
        
    def modify_artist(self, artist):
        self.modify(artist = artist)
    
    def modify_genre(self, genre):
        self.modify(genre = genre)
        
    def modify_lyrics(self, lyrics):
        self.modify(lyrics = lyrics)
        
    def modify_image_path(self, image_path):
        self.modify(image_path = image_path)
        
    def modify_filename(self, filename):
        self.modify(filename = filename)
    
    # def modify_(self, ):
        # self.modify( = )
    
    def get_tag(self):
        tag_info = dict()
        tag_info['title'] = self.audiofile.tag.title
        tag_info['artist'] = self.audiofile.tag.artist 
        tag_info['album'] = self.audiofile.tag.album 
        tag_info['genre'] = self.audiofile.tag.genre
        tag_info['lyrics'] = self.audiofile.tag.lyrics[0].text
        return tag_info
        