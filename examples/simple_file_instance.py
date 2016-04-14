#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Creates the CybOX content for CybOX_Simple_File_Instance.xml
"""

from cybox.common import Hash
from cybox.core import Observable, Observables
from cybox.objects.file_object import File


def main():
    h = Hash("a7a0390e99406f8975a1895860f55f2f")

    f = File()
    f.file_name = "bad_file24.exe"
    f.file_path = "AppData\Mozilla"
    f.file_extension = ".exe"
    f.size_in_bytes = 3282
    f.add_hash(h)

    o = Observable(f)
    o.description = "This observable specifies a specific file observation."

    print(Observables(o).to_xml(encoding=None))

if __name__ == "__main__":
    main()
