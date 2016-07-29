#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Creates the CybOX content for CybOX_Simple_Email_Instance.xml
"""

from cybox.core import Observables
from cybox.objects.address_object import Address
from cybox.objects.email_message_object import EmailMessage


def main():
    m = EmailMessage()
    m.to = ["victim1@target.com", "victim2@target.com"]
    m.from_ = "attacker@example.com"
    m.subject = "New modifications to the specification"

    a = Address("192.168.1.1", Address.CAT_IPV4)

    m.add_related(a, "Received_From", inline=False)

    print(Observables([m, a]).to_xml(encoding=None))


if __name__ == "__main__":
    main()
