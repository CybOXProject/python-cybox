#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""A test script to parse the existing samples and convert them to JSON.

Not all of the examples currently work.

Example usage:
    python convert_samples.py /path/to/cybox_v2.0_samples
"""

import os
import sys

import cybox.bindings.cybox_core as core_binding
from cybox.core import Observables


def from_file(filename):
    cybox_obj = core_binding.parse(os.path.abspath(filename))
    return Observables.from_obj(cybox_obj)


def main():
    if len(sys.argv) < 2:
        print("Argument required")
        return

    # The argument should be a directory containing XML files.
    d = sys.argv[1]
    output_dir = os.path.join(d, "json")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if not os.path.isdir(output_dir):
        print("{0} exists and is not a directory.".format(output_dir))
        return

    for f in os.listdir(sys.argv[1]):
        orig_file = os.path.join(d, f)
        if not os.path.isfile(orig_file):
            return
        output_fn = "{0}.json".format(os.path.splitext(f)[0])
        output_fn = os.path.join(output_dir, output_fn)
        with open(output_fn, "wt") as f:
            try:
                f.write(from_file(orig_file).to_json())
            except Exception as e:
                print("---------------------------------")
                print("ERROR with {0}".format(orig_file))
                print(e)
                continue

if __name__ == "__main__":
    main()
