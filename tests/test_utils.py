from titanium_rhythm.utils import get_file_type

def test_utils():
	assert(get_file_type('image.png') == 'png')
	assert(get_file_type('path/to/image.jpg') == 'jpg')

