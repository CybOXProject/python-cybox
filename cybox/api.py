#!/usr/bin/env python
'''
CybOX Common Indicator API

An api for creating observables for common indicators:
ipv4 addresses, domain names, file hashes, and urls.
'''

import sys
import uuid

import cybox.bindings.cybox_common_types_1_0 as cybox_common # binding
import cybox.bindings.file_object_1_3 as file_object # binding

from cybox.core import Observables, Observable, StatefulMeasure, Object
from cybox.objects.uri_object import URI
from cybox.objects.address_object import Address

def create_cybox_id(item_type = "guid"):
    '''Returns a unique id to be used by a CybOX entity'''

    return "cybox:" + item_type + "-" + str(uuid.uuid1())


def create_ipv4_observable(ipv4_address):
    '''Creates a CybOX Observable representing an IPv4 address'''
    ipv4_object = Address.from_dict({'address_value':ipv4_address, 'category':'ipv4-addr'})
    observable = Observable(ipv4_object)
    return observable


def create_ipv4_list_observables(list_ipv4_addresses):
    '''Creates a list of CybOX Observables, each representing an IPv4 address'''
    ipv4_objects = []
    list_observables = []
    for ipv4_address in list_ipv4_addresses:
        ipv4_object = create_ipv4_object(ipv4_address)
        observable  = Observable(ipv4_object)
        list_observables.append(observable) 
    return list_observables


def create_email_address_observable(email_address):
    '''Creates a CybOX Observable representing an IPv4 address'''
    email_address_object = Address.from_dict({'address_value':email_address, 'category':'e-mail'})
    observable = Observable(email_address_object)
    return observable


def create_domain_name_observable(domain_name):
    '''Creates a CybOX Observable representing a domain name.'''
    domain_name_object = URI.from_dict({'Value': domain_name,
                                               'type': URI.TYPE_DOMAIN})
    observable = Observable(domain_name_object)
    return observable


def create_file_hash_observable(fn, hash_value, hash_type):
    '''
    Creates a CybOX Observable representing a file hash
    Note: The cybox_helper module for file_object is under
    heavy development at this time and will not be used.  
    '''
    hash_name_type  = cybox_common.HashNameType(valueOf_= hash_type)
    hash_value_type = cybox_common.SimpleHashValueType(valueOf_ = hash_value)
    hash_object     = cybox_common.HashType(Type=hash_name_type, Simple_Hash_Value=hash_value_type)
    hash_list       = cybox_common.HashListType(Hash=[hash_object]) 
    
    file_object_     = file_object.FileObjectType(
                                                        File_Name   = cybox_common.StringObjectAttributeType(valueOf_=fn),
                                                        Hashes      = hash_list
                                                    )
    
    file_object_.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
    observable      = Observable(file_object_)
    
    return observable


def create_url_observable(url):
    url_object = URI.from_dict({'Value': url, 'type': URI.TYPE_URL})
    observable = Observable(url_object)
    return observable

