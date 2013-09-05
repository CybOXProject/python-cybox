class _type_base(object):
    """A base class for all of these types"""

    # TODO: get this working with python magic __new__ or __init__
    @classmethod
    def make(cls, val):
        if val is None:
            return None
        return cls._pytype(val)

    @classmethod
    def istypeof(self, obj):
        return isinstance(obj, self._pytype)


class QName(_type_base):
    """A class to use in TypedFields where a QName is required.

    For now, there is no checking and we only require it to be a string.
    Additional checking may be added in the future.
    """
    _pytype = str


class Enum(_type_base):
    """A class to use in TypedFields where an enumerated type is required.

    So far, our approach has been to not enforce enumerated values. If we
    choose to do so, this is a natural extension point.
    """
    _pytype = str


class Any(_type_base):
    """A class to use in TypedFields whose XML type is xs:anyType."""
    #For now, treat them as bytestrings. Later we'll want to see about
    #changing _pytype to "object".
    _pytype = str


class string(_type_base):
    """A class to use in TypedField whose XML type is xs:string."""
    _pytype = unicode


class boolean(_type_base):
    """A class to use in TypedFields whose XML type is xs:boolean."""
    _pytype = bool
