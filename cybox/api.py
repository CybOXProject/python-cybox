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

import cybox.core.observable
import cybox.core.observables
import cybox.core.object
import cybox.core.stateful_measure
from cybox.objects.uri_object import Uri
from cybox.objects.address_object import Address

def create_cybox_id(item_type = "guid"):
    '''Returns a unique id to be used by a CybOX entity'''

    return "cybox:" + item_type + "-" + str(uuid.uuid1())



def create_observables_document(list_observables):
    '''Creates a CybOX Observables element for the given list of Observables'''    

    observables = cybox.core.observables.Observables()
    for obs in list_observables:
        observables.add_observable(obs)
    return observables


def create_observable(cybox_object):
    '''Creates a CybOX Observable for the given CybOX object'''
    # TODO: modify constructors so this is easier
    object_ = cybox.core.object.Object()
    object_.defined_object = cybox_object
    sm = cybox.core.stateful_measure.StatefulMeasure()
    sm.object_ = object_
    observable = cybox.core.observable.Observable()
    observable.stateful_measure = sm
    return observable


def create_ipv4_observable(ipv4_address):
    '''Creates a CybOX Observable representing an IPv4 address'''
    ipv4_object = Address.from_dict({'address_value':ipv4_address, 'category':'ipv4-addr'})
    observable = create_observable(ipv4_object)
    return observable


def create_ipv4_list_observables(list_ipv4_addresses):
    '''Creates a list of CybOX Observables, each representing an IPv4 address'''
    ipv4_objects = []
    list_observables = []
    for ipv4_address in list_ipv4_addresses:
        ipv4_object = create_ipv4_object(ipv4_address)
        observable  = create_observable(ipv4_object)
        list_observables.append(observable) 
    return list_observables


def create_email_address_observable(email_address):
    '''Creates a CybOX Observable representing an IPv4 address'''
    email_address_object = Address.from_dict({'address_value':email_address, 'category':'e-mail'})
    observable = create_observable(email_address_object)
    return observable


def create_domain_name_observable(domain_name):
    '''Creates a CybOX Observable representing a domain name.'''
    domain_name_object = Uri.from_dict({'Value': domain_name,
                                               'type': Uri.TYPE_DOMAIN})
    observable = create_observable(domain_name_object)
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
    observable      = create_observable(file_object_)
    
    return observable


def create_url_observable(url):
    url_object = Uri.from_dict({'Value': url, 'type': Uri.TYPE_URL})
    observable = create_observable(url_object)
    return observable

