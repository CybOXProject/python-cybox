"""Common utility methods"""

from .idgen import *
from .nsparser import NamespaceParser, OBJECT_TYPES_DICT


class UnknownObjectTypeError(Exception):
    pass


def get_class_for_object_type(object_type):
    """Gets the class where a given XML Type can be parsed

    Raises an UnknownObjectType if object_type has not been defined in the
        dictionary above.
    Raises an ImportError if the specified module is not available.
    Raises an AttributeError if the specified module does not contain the
         correct class.
    """
    object_type_dict = OBJECT_TYPES_DICT.get(object_type)
    if not object_type_dict:
        raise UnknownObjectTypeError("%s is not a known object type" %
                                        object_type)

    full_class_name = object_type_dict.get('api_class')

    module = ".".join(full_class_name.split('.')[:-1])
    class_name = full_class_name.split('.')[-1]

    # May raise ImportError
    mod = __import__(module, fromlist=[class_name])

    # May raise AttributeError
    return getattr(mod, class_name)


def denormalize_from_xml(value):
    if ',' in value:
        return [x.replace('&comma;', ',').strip() for x in value.split(',')]
    else:
        return str(value).replace('&comma;', ',')


def normalize_to_xml(value):
    if isinstance(value, list):
        return ",".join([x.replace(',', '&comma;') for x in value])
    else:
        return str(value).replace(',', '&comma;')


def test_value(value):
    """
    Test if an input string value is not None and has a length grater than 0 or
    if a dictionary contains a "value" key whose value is not None and has
    a length greater than 0.

    We explicitly want to return True even if the value is False or 0, since
    some parts of the standards are boolean or allow a 0 value, and we want to
    distinguish the case where the "value" key is omitted entirely.
    """
    if isinstance(value, dict):
        v = value.get('value', None)
    elif isinstance(value, str):
        v = value
    elif isinstance(value, unicode):
        v = value
    elif isinstance(value, int):
        v = value
    elif isinstance(value, float):
        v = value
    else:
        v = None
    return (v is not None) and (len(str(v)) > 0)
