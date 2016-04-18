#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
CybOX Common Indicator helper Demo

Demonstrates the use of the Cybox Common Indicator helper.
Creates a CybOX Observables document containing a
'''

import sys
from pprint import pprint

from cybox import helper
from cybox.core import Observables


def main():
    '''Build a CybOX Observables document and write it to stdout'''
    domain = helper.create_domain_name_observable('www.example.com')
    url = helper.create_url_observable('http://www.example.com')
    ipv4 = helper.create_ipv4_observable('127.0.0.1')
    email = helper.create_email_address_observable('cybox@mitre.org')
    file_ = helper.create_file_hash_observable('foo.bar',
                                            '94f93e00fd122466d68a6ae3b8c7f908')

    observables_doc = Observables([
                                    domain,
                                    ipv4,
                                    url,
                                    email,
                                    file_,
                                  ])
    print(observables_doc.to_xml(encoding=None))

    pprint(observables_doc.to_dict())

if __name__ == "__main__":
    main()
    sys.exit()
