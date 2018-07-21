# Titanium-Rhythm

[![Build Status](https://travis-ci.org/ganesh-k13/titanium-rhythm.svg?branch=master)](https://travis-ci.org/ganesh-k13/titanium-rhythm) ![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)  [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)  


Titanium_Rhythm is a python package that recognizes mp3 files and automatically modifies its ID3.

### Installation

This package requires:
- python-gst0.10-dev
- gstreamer1.0
- libchromaprint-tools
- libchromaprint-dev
- python-gst-1.0
- ffmpeg

Install the above dependencies and required packages by:

```sh
$ apt-get update
$ apt-get install <PACKAGES>
$ pip3 install titanium-rhythm
```

### Tests

```sh
$ pytest
```

### Usage

```
>>> from titanium_rhythm.annotate import annotate_file
>>> annotate_file('PMaILC8xG3', filepath)
```
or

```
$ sudo python3 main.py
```
 

### License: MIT

