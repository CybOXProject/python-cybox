#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Creates the CybOX content for CybOX_Artifact_Instance.xml
"""

import os

from cybox.core import Observable, Observables
from cybox.objects.artifact_object import Artifact, Base64Encoding


def main():
    test_file = os.path.join(os.path.dirname(__file__), "test.pcap")

    with open(test_file, "rb") as f:
        data = f.read()

    a = Artifact(data, Artifact.TYPE_NETWORK)
    a.packaging.append(Base64Encoding())

    o = Observable(a)

    o.description = ("This Observable specifies an instance of an Artifact "
                     "object, specifically some network traffic that was "
                     "captured in a PCAP file and then base64 encoded for "
                     "transport.")

    print(Observables(o).to_xml(encoding=None))


if __name__ == "__main__":
    main()
