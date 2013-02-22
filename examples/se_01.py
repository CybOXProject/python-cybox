#!/usr/bin/env python
"""Creates the CybOX content for Simple Example #1

http://cybox.mitre.org/language/examples/se_01.html
"""

from cybox.common import AnyURI
from cybox.core import Observables
from cybox.objects.uri_object import URI

def main():
    print '<?xml version="1.0" encoding="UTF-8"?>'

    v = AnyURI("www.sample1.com/index.html")
    v.condition = "Equals"

    u = URI()
    u.value = v
    u.type_ = URI.TYPE_URL

    o = Observables(u)
    print o.to_xml()

if __name__ == "__main__":
    main()
