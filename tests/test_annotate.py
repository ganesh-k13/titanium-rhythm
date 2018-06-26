# Consumer Key	vGjWQytoJdVnmCueiIsE
# Consumer Secret	wYYPlTcELQvfVORHjIkurHDEHLefltru
# Request Token URL	https://api.discogs.com/oauth/request_token
# Authorize URL	https://www.discogs.com/oauth/authorize
# Access Token URL	https://api.discogs.com/oauth/access_token

import pytest
import pkg_resources
import os
import sys

from titanium_rhythm.annotate import annotate_file

SONG_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('songs', 'unknown.mp3'))

@pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on osx yet")
def test_annotate():
	annotate_file('PMaILC8xG3', SONG_FILE)
	

