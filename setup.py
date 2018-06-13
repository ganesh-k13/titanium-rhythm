import setuptools

# with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="titanium-rhythm",
    version="0.0.1",
    author="Ganesh Kathiresan",
    author_email="ganesh3597@gmail.com",
    description="Automatic id3 modifier .mp3 files",
#   long_description=long_description,
#   long_description_content_type="text/markdown",
    url="https://github.com/DarkFate13/titanium-rhythm",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ),
)
