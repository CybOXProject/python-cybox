# CybOX Python Bindings

This directory contains low-level Python bindings for CybOX that were 
generated from the CybOX XML schemas by generateDS. 

## Layout

* `cybox_core.py`: CybOX Core Schema bindings.
* `cybox_common.py`: CybOX Common Types bindings. 
* `*_object_*.py` : CybOX defined object bindings. 
* `extensions/*`: CybOX extension bindings.

## Dependencies

For parsing of CybOX XML instances (using the `parse()` method),
these bindings require version 2.3+ of the Python LXML module to be installed. 

Please see:
http://lxml.de/installation.html
or
http://pypi.python.org/pypi/lxml/2.3 (for Windows)

## Usage

For parsing of input CybOX XML files, call the `parse()` method from the 
`cybox_core.py` binding.

### Example

The following code snippet demonstrates how to parse a CybOX XML document
via the binding `parse()` method.

```python
import cybox.bindings.cybox_core as cybox

binding_observables = cybox.parse('cybox-document.xml')

# Iterate over the contained Observable instances
# and print the title of each.
for observable in binding_observables.get_Observable():
    print observable.get_Title()

# Or create a python-cybox object from the binding
# object!
from cybox.core import Observables
observables = Observables.from_obj(binding_observables)

for observable in observables.observables:
  print observable.title

```
