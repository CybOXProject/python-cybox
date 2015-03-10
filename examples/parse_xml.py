#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Example script for parsing CybOX XML documents.

Usage: parse_xml.py example.xml

The CybOX XML document is parsed into a python-cybox Observables instance. Once
parsed, the dictionary representation of the object is printed to stdout.
"""

import sys
import cybox.bindings.cybox_core as cybox_core_binding
from cybox.core import Observables


def parse(xml_file):
    # create binding object from xml file
    observables_obj = cybox_core_binding.parse(xml_file)

    # convert binding object into python-cybox object
    observables = Observables.from_obj(observables_obj)
    return observables


def main():
    if len(sys.argv) != 2:
        print("[!] Please provide an xml file")
        exit(1)

    xml_file = sys.argv[-1]
    observables = parse(xml_file)
    print(observables.to_dict())  # example to_dict() call on returned object


if __name__ == "__main__":
    main()
