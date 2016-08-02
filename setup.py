#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'steam_market',
    packages = ['steam_market'],
    version = '0.2.0',
    description = 'A Python API for getting prices from the Steam market.',
    author = 'Christopher Su',
    author_email = 'chris+gh@christopher.su',
    url = 'https://github.com/csu/PySteamMarket',
    download_url = 'https://github.com/csu/PySteamMarket/archive/master.zip'
)
