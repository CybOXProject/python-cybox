#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Creates the CybOX content for CybOX_URL_Pattern.xml
"""

from cybox.common import AnyURI
from cybox.core import Observables
from cybox.objects.uri_object import URI


def main():
    v = AnyURI("http://www.example.com/index1.html")
    v.condition = "Equals"

    u = URI()
    u.value = v
    u.type_ = URI.TYPE_URL

    print(Observables(u).to_xml(encoding=None))

if __name__ == "__main__":
    main()
