import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="titanium_rhythm",
    version="1.0.0",
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
          'discogs_client == 2.2.1',
          'eyeD3 == 0.8.7',
          'pyacoustid == 1.1.5',
          'pytest == 3.6.1',
          'requests == 2.18.4',
          'setuptools == 38.6.0',
          'validators == 0.12.2',
      ],
)
