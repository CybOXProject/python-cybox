#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Creates the CybOX content for CybOX_Simple_Email_Pattern.xml
"""

from cybox.core import Observables
from cybox.objects.email_message_object import EmailMessage


def main():
    m = EmailMessage()
    m.from_ = ["attacker@example.com",
               "attacker1@example.com",
               "attacker@bad.example.com"]
    m.from_.condition = "Equals"
    m.subject = "New modifications to the specification"
    m.subject.condition = "Equals"

    print(Observables(m).to_xml(encoding=None))

if __name__ == "__main__":
    main()
