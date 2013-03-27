#!/usr/bin/env python
"""Creates the CybOX content for Simple Example #5

http://cybox.mitre.org/language/examples/se_05.html
"""

from cybox.common import Hash, String
from cybox.core import Observables
from cybox.objects.address_object import Address, EmailAddress
from cybox.objects.email_message_object import EmailMessage, EmailRecipients
import cybox.utils

def main():
    cybox.utils.set_id_method(cybox.utils.IDGenerator.METHOD_INT)

    print '<?xml version="1.0" encoding="UTF-8"?>'

    email = EmailMessage()
    email.subject = String("New modifications to the specification")
    email.to = EmailRecipients(EmailAddress("victim1@target.com"),
                               EmailAddress("victim2@target.com"))
    email.from_ = EmailAddress("attacker@example.com")


    address = Address("192.168.1.1", Address.CAT_IPV4)

    email.add_related(address, "Received_From", inline=False)

    print Observables([email, address]).to_xml()

if __name__ == "__main__":
    main()
