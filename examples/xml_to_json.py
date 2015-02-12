#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import os
import sys

import cybox.bindings.cybox_core as core_binding
from cybox.core import Observables


def from_file(filename):
    cybox_obj = core_binding.parse(os.path.abspath(filename))
    return Observables.from_obj(cybox_obj)


def main():
    if len(sys.argv) < 2:
        print "Argument required"
        return

    print from_file(sys.argv[1]).to_json()

if __name__ == "__main__":
    main()
