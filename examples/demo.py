#!/usr/bin/env python
'''
CybOX Common Indicator API Demo

Demonstrates the use of the Cybox Common Indicator API.
Creates a CybOX Observables document containing a
'''

import sys
from cybox import api

def main():
    '''Build a CybOX Observables document and write it to stdout'''
    domain_name_observable  = api.create_domain_name_observable('www.example.com')
    ipv4_observable         = api.create_ipv4_observable('127.0.0.1')
    hash_observable         = api.create_file_hash_observable('foo.bar','94f93e00fd122466d68a6ae3b8c7f908','MD5')
    url_observable          = api.create_url_observable('http://www.example.com')

    observables_doc = api.create_observables_document( [domain_name_observable,
                                                        ipv4_observable,
                                                        hash_observable,
                                                        url_observable] )
    observables_doc.export(sys.stdout, 0)

if __name__ == "__main__":
    main()
    sys.exit()
