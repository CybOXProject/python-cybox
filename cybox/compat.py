import sys

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)


if is_py2:
    from StringIO import StringIO
    basestring = basestring
    bytes = str
    long = long
    str = unicode

elif is_py3:
    from io import StringIO
    basestring = (str, bytes)
    bytes = bytes
    long = int
    str = str
