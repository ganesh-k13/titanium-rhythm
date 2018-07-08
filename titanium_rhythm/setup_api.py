import json
import pkg_resources
import os

DATA_PATH = pkg_resources.resource_filename('titanium_rhythm', 'info/')
JSON_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('info', 'info.json'))

info = dict()
info['api_key'] = ''
info['discogs_key'] = ''

class Setup():
    def __init__(self):
        pass
    
    @staticmethod
    def set_key(key):
        info['api_key'] = key
        with open(JSON_FILE, 'w') as f:
            json.dump(info, f, indent = 4)
    
    @staticmethod
    def get_key():
        with open(JSON_FILE, 'r') as f:
            info = json.load(f)
        
        return info

    @staticmethod
    def set_discogs_key(key):
        info['discogs_key'] = key
        with open(JSON_FILE, 'w') as f:
            json.dump(info, f, indent = 4)

    @staticmethod
    def get_disogs_key():
        with open(JSON_FILE, 'r') as f:
            info = json.load(f)

        return info
            