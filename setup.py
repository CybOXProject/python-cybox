# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from setuptools import setup, find_packages

import cybox

setup(
    name="cybox",
    version=cybox.__version__,
    author="CybOX Project, MITRE Corporation",
    author_email="cybox@mitre.org",
    description="A Python library for parsing and generating CybOX content.",
    url="http://cybox.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3', 'python-dateutil'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
