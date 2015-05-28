# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Compatibility library for python-cybox.

Only covers things that aren't already present in `six`.
"""

from mixbox.vendor import six

if six.PY2:
    long = long
    def xor(data, key):
        key = int(key)
        return b''.join([chr(ord(c) ^ key) for c in data])

elif six.PY3:
    long = int
    def xor(data, key):
        key = int(key)
        b = bytearray(data)
        for i in range(len(b)):
            b[i] ^= key
        return bytes(b)
