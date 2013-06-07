# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import json

import cybox.bindings.cybox_core as core_binding
from cybox.core import Observables
import cybox.utils



def assert_equal_ignore(item1, item2, ignore_keys=None):
    """Recursively compare two dictionaries, ignoring differences in some keys.
    """
    if not ignore_keys:
        ignore_keys = []

    if isinstance(item1, dict) and isinstance(item2, dict):
        item1keys = set(item1.keys())
        item2keys = set(item2.keys())
        ignore = set(ignore_keys)
        compare_keys = (item1keys | item2keys) - ignore
        for k in compare_keys:
            assert k in item1, "Item 1 is missing %s" % k
            assert k in item2, "Item 2 is missing %s" % k
            assert_equal_ignore(item1.get(k), item2.get(k), ignore_keys)
    elif isinstance(item1, list) and isinstance(item2, list):
        assert len(item1) == len(item2), "Lists are of different lengths"
        for (x, y) in zip(item1, item2):
            assert_equal_ignore(x, y, ignore_keys)
    else:
        assert item1 == item2, "%s != %s" % (item1, item2)


def round_trip(o, output=False, list_=False):
    """ Performs all four conversions to verify import/export functionality.

    1. Object->JSON
    2. JSON->Object
    3. Object->XML
    4. XML->Object

    It returns the object from the last test, so tests which call this function
    can check to ensure it was not modified during any of the transforms.
    """

    klass = o.__class__

    # object to dict
    if list_:
        d = o.to_list()
    else:
        d = o.to_dict()

    # dict to JSON-string
    json_string = json.dumps(d)
    if output:
        print(json_string)

    # Before parsing the JSON, make sure the cache is clear
    cybox.utils.cache_clear()

    # JSON-string to dict
    d2 = json.loads(json_string)

    # dict to object
    if list_:
        o2 = klass.from_list(d2)
    else:
        o2 = klass.from_dict(d2)

    # object to XML-object
    xobj = o2.to_obj()
    # object to XML string

    # Hack for now to not include namespaces on Observables (they are
    # calculated already)
    include_ns = (type(o) is not Observables)
    print include_ns
    xml_string = o2.to_xml(include_namespaces=include_ns)

    if output:
        print(xml_string)

    # Before parsing the XML, make sure the cache is clear
    cybox.utils.cache_clear()

    xobj2 = klass._binding.parseString(xml_string)

    # XML-object to object
    o3 = klass.from_obj(xobj2)

    return o3


def round_trip_dict(cls, dict_):
    obj = cls.object_from_dict(dict_)
    dict2 = cls.dict_from_object(obj)

    return dict2


def round_trip_list(cls, list_):
    obj = cls.object_from_list(list_)
    list2 = cls.list_from_object(obj)

    return list2
