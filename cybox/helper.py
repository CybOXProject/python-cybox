#!/usr/bin/env python

# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
CybOX Common Indicator API

An api for creating observables for common indicators:
ipv4 addresses, domain names, file hashes, and urls.
'''

from cybox.core import Observable
from cybox.common import Hash
from cybox.objects.address_object import Address
from cybox.objects.file_object import File
from cybox.objects.uri_object import URI


def create_ipv4_observable(ipv4_address):
    '''Create a CybOX Observable representing an IPv4 address'''
    ipv4_object = Address.from_dict({'address_value': ipv4_address,
                                     'category': Address.CAT_IPV4})
    return Observable(ipv4_object)


def create_ipv4_list_observables(list_ipv4_addresses):
    '''Create a list of CybOX Observables, each representing an IPv4 address'''
    list_observables = []
    for ipv4_address in list_ipv4_addresses:
        ipv4_observable = create_ipv4_observable(ipv4_address)
        observable = Observable(ipv4_observable)
        list_observables.append(observable)
    return list_observables


def create_email_address_observable(email_address):
    '''Create a CybOX Observable representing an IPv4 address'''
    email_address_object = Address.from_dict({'address_value': email_address,
                                              'category': Address.CAT_EMAIL})
    return Observable(email_address_object)


def create_domain_name_observable(domain_name):
    '''Create a CybOX Observable representing a domain name.'''
    domain_name_object = URI.from_dict({'value': domain_name,
                                        'type': URI.TYPE_DOMAIN})
    return Observable(domain_name_object)


def create_file_hash_observable(fn, hash_value):
    '''Create a CybOX Observable representing a file hash.'''
    hash_ = Hash(hash_value)
    file_ = File()
    file_.file_name = fn
    file_.add_hash(hash_)
    return Observable(file_)


def create_url_observable(url):
    url_object = URI.from_dict({'value': url, 'type': URI.TYPE_URL})
    return Observable(url_object)
