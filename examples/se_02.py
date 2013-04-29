#!/usr/bin/env python
"""Creates the CybOX content for Simple Example #2

http://cybox.mitre.org/language/examples/se_02.html
"""

from cybox.common import Hash, HexBinary
from cybox.core import Observables
from cybox.objects.file_object import File

def main():
    print '<?xml version="1.0" encoding="UTF-8"?>'

    s = HexBinary()
    s.condition = "Equals"
    s.value = ["4EC0027BEF4D7E1786A04D021FA8A67F",
               "21F0027ACF4D9017861B1D021FA8CF76",
               "2B4D027BEF4D7E1786A04D021FA8CC01"]

    f = File()
    h = Hash(s, Hash.TYPE_MD5)
    f.add_hash(h)

    print Observables(f).to_xml()

if __name__ == "__main__":
    main()
