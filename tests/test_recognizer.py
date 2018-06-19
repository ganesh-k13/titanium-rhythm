import pytest
import pkg_resources
import os
import sys

from titanium_rhythm.setup_api import Setup
from titanium_rhythm.identify import Identify

SONG_FILE = pkg_resources.resource_filename('titanium_rhythm', os.path.join('songs', 'unknown.mp3'))

@pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on osx yet")
def test_identify():
	Setup.set_key('PMaILC8xG3')
	i = Identify(SONG_FILE)
	i.aidmatch()
	

