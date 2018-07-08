# Consumer Key  vGjWQytoJdVnmCueiIsE
# Consumer Secret   wYYPlTcELQvfVORHjIkurHDEHLefltru
# Request Token URL https://api.discogs.com/oauth/request_token
# Authorize URL https://www.discogs.com/oauth/authorize
# Access Token URL  https://api.discogs.com/oauth/access_token

import pytest
import pkg_resources
import os
import sys

from titanium_rhythm.setup_api import Setup
from titanium_rhythm.identify import Identify

SONG_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('songs', '23.mp3'))

@pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on osx yet")
def test_identify():
    Setup.set_key('PMaILC8xG3')
    i = Identify(SONG_FILE)
    i.aidmatch(pickle_required = True)
    

