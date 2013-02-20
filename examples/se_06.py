#!/usr/bin/env python
"""Creates the CybOX content for Simple Example #6

http://cybox.mitre.org/language/examples/se_06.html
"""

from cybox.common import Hash, String
from cybox.core import Observables
from cybox.objects.address_object import Address
from cybox.objects.email_message_object import EmailMessage, EmailRecipients
from cybox.objects.file_object import File

def main():
    print '<?xml version="1.0" encoding="UTF-8"?>'

    attachment = File()
    attachment.file_name = "FooBar Specification (critical revision).doc"
    attachment.add_hash(Hash("4EC0027BEF4D7E1786A04D021FA8A67F"))

    email = EmailMessage()
    email.attachments.append(attachment)
    # TODO: Make 'email.subject`, `email.to` and `email.from` work 
    # TODO: Make EmailAddress "constructor"
    email.header.subject = String("New modifications to the specification")
    email.header.to = EmailRecipients.from_dict(
                            [Address("victim1@target.com", Address.CAT_EMAIL),
                             Address("victim2@target.com", Address.CAT_EMAIL)])
    email.header.from_ = Address("attacker@example.com", Address.CAT_EMAIL)


    print Observables(email).to_xml()

if __name__ == "__main__":
    main()
