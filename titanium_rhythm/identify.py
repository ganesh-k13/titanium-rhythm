import acoustid
import sys
import urllib.request
import pkg_resources
import os
import json
import ntpath
import discogs_client
import pickle

DATA_PATH = pkg_resources.resource_filename('titanium_rhythm', 'song_info/')
JSON_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('info', 'info.json'))


class Identify():
    def __init__(self, filename):
        self.get_info()
        self.filename = filename
    
    def get_info(self):
        with open(JSON_FILE, 'r') as f:
            self.info = json.load(f)
        self.api_key = self.info['api_key']
        
    def aidmatch(self, xml_required = False, pickle_required = False):
        try:
            results = acoustid.match(self.api_key, self.filename)
        except acoustid.NoBackendError:
            print("chromaprint library/tool not found", file=sys.stderr)
            sys.exit(1)
        except acoustid.FingerprintGenerationError:
            print("fingerprint could not be calculated", file=sys.stderr)
            sys.exit(1)
        except acoustid.WebServiceError as exc:
            print("web service request failed:", exc.message, file=sys.stderr)
            sys.exit(1)
        
        if(xml_required == True):
            for score, rid, title, artist in results:
                url = "https://musicbrainz.org/ws/2/recording/{0}?inc=aliases%2Bartist-credits%2Breleases".format(rid)
                response = urllib.request.urlopen(url)
                data = response.read()      # a `bytes` object
                text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
                basename = ntpath.basename(self.filename)
                XML_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('song_info', basename[:-4]+'.xml'))
                with open(XML_FILE, 'w') as f:
                    print(text, file = f)
        
        if(pickle_required == True):
            d = discogs_client.Client('ExampleApplication/0.1', user_token="vqhbRQaPOlwDSVqSNXovPSgwltksFddGjifKGNRS")
            for score, rid, title, artist in results:
                results = d.search(title+' '+artist, type = 'release')
                basename = ntpath.basename(self.filename)
                PICKLE_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('song_info', basename[:-4]+'.pkl'))
                with open(PICKLE_FILE, 'wb') as f:
                    pickle.dump(results, f, pickle.HIGHEST_PROTOCOL)
                return PICKLE_FILE

if __name__ == '__main__':
    i = Identify(sys.argv[1])
    i.aidmatch()
    # PMaILC8xG3
