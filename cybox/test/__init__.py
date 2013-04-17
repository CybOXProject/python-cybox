import json

def assert_equal_ignore(item1, item2, ignore_keys=None):
    """Recursively compare two dictionaries, ignoring differences in some keys.
    """
    if not ignore_keys:
        ignore_keys = []

    if not (isinstance(item1, dict) and isinstance(item2, dict)):
        assert item1 ==  item2
    else:
        item1keys = set(item1.keys())
        item2keys = set(item2.keys())
        ignore = set(ignore_keys)
        compare_keys = (item1keys | item2keys) - ignore
        for k in compare_keys:
            assert k in item1
            assert k in item2
            assert_equal_ignore(item1.get(k), item2.get(k), ignore_keys)


def round_trip(o, output=False):
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
    d = o.to_dict()
    # dict to JSON-string
    s = json.dumps(d)
    if output:
        print(s)
    # JSON-string to dict
    d2 = json.loads(s)
    # dict to object
    o2 = klass.from_dict(d2)
    # object to XML-object
    xobj = o2.to_obj()
    # object to XML string
    if output:
        print(o2.to_xml())

    # TODO: XML-string to XML-object.

    # XML-object to object
    o3 = klass.from_obj(xobj)

    return o3


def round_trip_dict(cls, dict_):
    obj = cls.object_from_dict(dict_)
    dict2 = cls.dict_from_object(obj)

    return dict2


def round_trip_list(cls, list_):
    obj = cls.object_from_list(list_)
    list2 = cls.list_from_object(obj)

    return list2
