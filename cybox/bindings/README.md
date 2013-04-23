CybOX v2.0 Python Bindings
--------------------------------
These are the latest Python bindings for CybOX v2.0.

-cybox_core: the CybOX Core Schema bindings.

-cybox_common: the CybOX Common Types bindings. 

-*_object_* : the CybOX defined object bindings. 

Dependencies
------------
For parsing of CybOX XML instances (using the parse() method),
these bindings require version 2.3+ of the Python LXML module to be installed. 

Please see:
http://lxml.de/installation.html
or
http://pypi.python.org/pypi/lxml/2.3 (for Windows)

Usage
-----
For parsing of input CybOX XML files, call the parse() method from the cybox_core bindings. E.g,

import cybox_core as cybox

cybox.parse('some_input_file.xml')

Similarly, for export of CybOX XML to a file, create and open a file and then pass it to the export method of the Observables object you're using.  The latest version of the core bindings will write out all of the namespaces and schema locations for you, so you don't need to declare them (via the namespacedef_ parameter).
E.g.,

import cybox_core_1_0 as cybox

observables = cybox.ObservablesType()
...
output_file = file('some_file.xml', 'w')

observables.export(output_file, 0)

Examples
-----
For up-to-date examples of how to use the Bindings, please see the Tools wiki:

https://github.com/CybOXProject/Tools/wiki
