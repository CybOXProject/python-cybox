# python-cybox [![Build Status](https://travis-ci.org/CybOXProject/python-cybox.png?branch=master)](https://travis-ci.org/CybOXProject/python-cybox)

A Python library for parsing, manipulating, and generating CybOX content.

For more information about CybOX, see http://cybox.mitre.org.


## Overview

A primary goal of the python-cybox library is to remain faithful to both the
CybOX standard and to customary Python practices. There are places where these
will conflict, and the goal is to make the library intuitive both to those
familiar with the XML schemas (but less familiar with Python) and also to
experienced Python developers who want to add CybOX support to their programs.

There are currently two levels of APIs for dealing with CybOX content:

- A low-level API is provided by auto-generated XML Schema - Python class
  bindings. These bindings were generated using
  [generateDS](http://www.rexx.com/~dkuhlman/generateDS.html). With these,
  any CybOX content can be parsed from or written to XML, but requires a bit
  more knowledge of the actual CybOX schemas. These "binding classes" are all
  located in the `cybox.bindings` package.
- A higher-level API consisting of manually designed Python classes. These
  "native classes" are intended to behave more like Python programmers would
  expect. As they are designed manually, they currently do not support the
  entire CybOX standard, but rather those object types we expect are used most
  frequently. These "native classes" also support exporting their content as
  Python dictionaries and lists, which can easily be converted to JSON.
  Importing from JSON is also supported.


## Versioning

Releases of the python-cybox library will be given `major.minor.revision`
version numbers, where `major` and `minor` correspond to the CybOX version
being supported. The `revision` number is used to indicate new versions of
the Python library itself.


## Installation

The `cybox` package depends on the following Python libraries:
* `lxml` >= 3.1.x
* `python-dateutils`
* `setuptools` (only if installing using setup.py)

For Windows installers of the above libraries, we recommend looking here: http://www.lfd.uci.edu/~gohlke/pythonlibs/

To build `lxml` on Ubuntu, you will need the following packages from the
Ubuntu package repository:

* python-dev
* libxml2-dev
* libxslt1-dev

For more information about installing lxml, see
http://lxml.de/installation.html

## Layout
The structure of the python-cybox structure is as follows:
* cybox/ : the root package
* examples/ : example scripts that leverage the python-cybox library
* cybox/utils/ : utility modules that are leveraged internally by the python-cybox library
* cybox/test/ : unit tests
* cybox/bindings/ : generateDS created xml-to-python bindings (leveraged in parsing and output of CybOX XML content)
* cybox/core/ : APIs for core CybOX constructs (e.g., Observables)
* cybox/common/ : APIs for common CybOX constructs (e.g., Measure Source)
* cybox/object/ : APIs for CybOX objects (e.g., File Object, Address Object)

Please refer to the example scripts for examples of how to use the python-cybox library

## Feedback

Bug reports and feature requests are welcome and encouraged. Pull requests are
especially appreciated. Feel free to use the issue tracker on GitHub or send
an email directly to cybox@mitre.org.
