#!/usr/bin/env python
"""Creates the CybOX content for Simple Example #3

http://cybox.mitre.org/language/examples/se_03.html
"""

from cybox.common import Hash
from cybox.core import Observables
from cybox.objects.file_object import File

def main():
    print '<?xml version="1.0" encoding="UTF-8"?>'

    h1 = Hash("59a7078444ee3c862e4c08b601ed7e01", exact=True)
    h2 = Hash("98e969b49ff2aedf66b94eb82c54b916f1a634cd", exact=True)
    h3 = Hash("1706c7cd14a5c9bbf674b21f9c4f873ac04b7a6f1f2202cd0c5977c48968d188", exact=True)

    f = File()
    f.file_name = "notepad.exe"
    f.file_path = "C:\Temp"
    f.add_hash(h1)
    f.add_hash(h2)
    f.add_hash(h3)

    print Observables(f).to_xml()

if __name__ == "__main__":
    main()
