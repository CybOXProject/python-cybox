#!/usr/bin/env python
'''
CybOX Common Indicator API Demo

Demonstrates the use of the Cybox Common Indicator API.
Creates a CybOX Observables document containing a
'''

import sys
from pprint import pprint

from cybox import api
from cybox.core import Observables

def main():
    '''Build a CybOX Observables document and write it to stdout'''
    domain = api.create_domain_name_observable('www.example.com')
    url = api.create_url_observable('http://www.example.com')
    ipv4 = api.create_ipv4_observable('127.0.0.1')
    email = api.create_email_address_observable('cybox@mitre.org')
    file_ = api.create_file_hash_observable('foo.bar','94f93e00fd122466d68a6ae3b8c7f908')

    observables_doc = Observables([
#                                    domain,
#                                    ipv4,
#                                    url,
#                                    email,
                                    file_,
                                  ])
    observables_doc.to_obj().export(sys.stdout, 0)

    pprint(observables_doc.to_dict())

if __name__ == "__main__":
    main()
    sys.exit()
