#!/usr/bin/env python
"""Creates the CybOX content for CybOX_URL_Instance.xml
"""

from cybox.common import AnyURI
from cybox.core import Observables
from cybox.objects.uri_object import URI

def main():
    v = AnyURI("http://www.example.com/index1.html")

    u = URI()
    u.value = v
    u.type_ = URI.TYPE_URL

    o = Observables(u)
    print o.to_xml()

if __name__ == "__main__":
    main()
