#!/usr/bin/env python

# Copyright (c) 2015 - The MITRE Corporation
# For license information, see the LICENSE.txt file

from os.path import abspath, dirname, join


from setuptools import setup, find_packages

BASE_DIR = dirname(abspath(__file__))
VERSION_FILE = join(BASE_DIR, 'cybox', 'version.py')


def get_version():
    with open(VERSION_FILE) as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")


with open('README.rst') as f:
    readme = f.read()

install_requires = [
    'lxml>=2.2.3',
    'mixbox>=1.0.2',
    'python-dateutil',
]

try:
    import importlib
except ImportError:
    install_requires.append('importlib')

setup(
    name="cybox",
    version=get_version(),
    author="CybOX Project, MITRE Corporation",
    author_email="cybox@mitre.org",
    description="A Python library for parsing and generating CybOX content.",
    long_description=readme,
    url="http://cybox.mitre.org",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
