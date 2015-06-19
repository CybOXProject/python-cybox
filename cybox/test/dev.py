#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''A collection of functions, etc. that are useful during development.'''


import os
import sys

from mixbox import entities

# This is not in the Python Standard Library before Python 2.7
import importlib


def main():
    import_mods(".")

    subs = list(subclasses(entities.Entity))

#    print("\n".join([str(x) for x in subs]))
#    print(len(subs))

    no_namespace = [x for x in subs if not filter_has_namespace(x)]
    for x in no_namespace:
        print(x)
    print(len(no_namespace))


def filter_has_namespace(cls):
    if hasattr(cls, "_namespace"):
        return True
    return False


#Inpsired by http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/
def subclasses(cls, _seen=None):
    """Generator to return all subclasses of a given class"""

    if _seen is None:
        _seen = set()

    for sub in cls.__subclasses__():
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in subclasses(sub, _seen):
                yield sub


def import_mods(directory):
    """Recursively import all python modules in a given directory"""
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            dirs.remove('.git')

        if 'examples' in dirs:
            dirs.remove('examples')

        for fn in files:
            filename = os.path.join(root, fn)

            if filename.endswith(".py"):
                #print filename

                modname = filename[2:].replace("/", ".")[:-3]
                #print modname

                if modname in ('setup',):
                    continue

                m = importlib.import_module(modname)
                #print m

if __name__ == "__main__":
    main()
