"""Common utility methods"""

import uuid

# Maps an ObjectType name to a tuple (module, class_name) where the class
# can be found
OBJECTS = {
            "AddressObjectType": 'cybox.objects.address_object.Address',
            "URIObjectType": 'cybox.objects.uri_object.URI',
            "EmailMessageObjectType": 'cybox.objects.email_message_object.EmailMessage',
            "FileObjectType": 'cybox.objects.file_object.File',

            # These are just for testing. Please don't attempt to use!
            "!!ObjectTestCase": 'cybox.utils.IDGenerator',
            "!!MissingModule": 'some.nonexistent.module',
            "!!BadClassName": 'cybox.utils.NonexistentClass',
          }

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
    full_class_name = OBJECTS.get(object_type)
    if not full_class_name:
        raise UnknownObjectTypeError("%s is not a known object type" %
                                        object_type)

    module = ".".join(full_class_name.split('.')[:-1])
    class_name = full_class_name.split('.')[-1]
    print (module, class_name)

    # May raise ImportError
    mod = __import__(module, fromlist=[class_name])

    # May raise AttributeError
    return getattr(mod, class_name)


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





class InvalidMethodError(ValueError):

    def __init__(self, method):
        ValueError.__init__(self, "invalid method: %s" % method)


class IDGenerator(object):
    """Utility class for generating CybOX IDs for objects"""
    METHOD_UUID = 1
    METHOD_INT = 2

    METHODS = (METHOD_UUID, METHOD_INT,)

    def __init__(self, namespace="cybox", method=METHOD_UUID):
        self.namespace = namespace
        self.method = method
        self.next_int = 1

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        self._namespace = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if value not in IDGenerator.METHODS:
            raise InvalidMethodError("invalid method: %s" % value)
        self._method = value

    def create_id(self, prefix="guid"):
        """Create an ID.

        Note that if `prefix` is not provided, it will be `quid`, even if the
        `method` is `METHOD_INT`.
        """
        if self.method == IDGenerator.METHOD_UUID:
            id_ = str(uuid.uuid1())
        elif self.method == IDGenerator.METHOD_INT:
            id_ = self.next_int
            self.next_int += 1
        else:
            raise InvalidMethodError()

        return "%s:%s-%s" % (self.namespace, prefix, id_)

# Singleton instance within this module. It is lazily instantiated, so simply
# importing the utils module will not create the object.
__generator = None


def _get_generator():
    """Return the `cybox.utils` module's generator object.

    Only under rare circumstances should this function be called by external
    code. More likely, external code should initialize its own IDGenerator or
    use the `set_id_namespace`, `set_id_method`, or `create_id` functions of
    the `cybox.utils` module.
    """
    global __generator
    if not __generator:
        __generator = IDGenerator()
    return __generator


def set_id_namespace(namespace):
    """ Set the namespace for the module-level ID Generator"""
    _get_generator().namespace = namespace


def set_id_method(method):
    """ Set the method for the module-level ID Generator"""
    _get_generator().method = method


def create_id(prefix=None):
    """ Create an ID using the module-level ID Generator"""
    if not prefix:
        return _get_generator().create_id()
    else:
        return _get_generator().create_id(prefix)
