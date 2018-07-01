import pytest
import string
import random

from titanium_rhythm.setup_api import Setup

def test_api_key():
    rand_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    Setup.set_key(rand_key)
    assert(Setup.get_key()['api_key'] == rand_key)

