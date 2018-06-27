import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="titanium_rhythm",
    version="0.0.2",
    author="Ganesh Kathiresan",
    author_email="ganesh3597@gmail.com",
    description="Automatic id3 modifier .mp3 files",
	long_description=long_description,
	long_description_content_type="text/markdown",
    url="https://github.com/DarkFate13/titanium-rhythm",
	packages=['titanium_rhythm'],
	package_dir = {'titanium_rhythm': 'titanium_rhythm/'},
	package_data={'titanium_rhythm': ['info/*.*', 'song_info/*.xml']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
	install_requires=[
          'discogs_client',
		  'eyeD3',
		  'pyacoustid',
		  'pytest',
		  'requests',
		  'setuptools',
		  'validators',
      ],
)
