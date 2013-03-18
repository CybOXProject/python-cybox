import json


def round_trip(o, cls, output=False):
    """ Performs all four conversions to verify import/export functionality.

    1. Object->JSON
    2. JSON->Object
    3. Object->XML
    4. XML->Object

    It returns the object from the last test, so tests which call this function
    can check to ensure it was not modified during any of the transforms.
    """

    # object to dict
    d = o.to_dict()
    # dict to JSON-string
    s = json.dumps(d)
    if output:
        print(s)
    # JSON-string to dict
    d2 = json.loads(s)
    # dict to object
    o2 = cls.from_dict(d2)
    # object to XML-object
    xobj = o2.to_obj()
    # object to XML string
    if output:
        print(o2.to_xml())

    # TODO: XML-string to XML-object.

    # XML-object to object
    o3 = cls.from_obj(xobj)

    return o3
