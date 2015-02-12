# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Methods for generating IDs for Objects and Observables"""

import uuid

from cybox.utils.nsparser import Namespace

EXAMPLE_NAMESPACE = Namespace("http://example.com", "example")

__all__ = ['InvalidMethodError', 'IDGenerator', 'set_id_namespace',
           'set_id_method', 'create_id']


class InvalidMethodError(ValueError):

    def __init__(self, method):
        ValueError.__init__(self, "invalid method: %s" % method)


class IDGenerator(object):
    """Utility class for generating CybOX IDs for objects"""
    METHOD_UUID = 1
    METHOD_INT = 2

    METHODS = (METHOD_UUID, METHOD_INT)

    def __init__(self, namespace=EXAMPLE_NAMESPACE, method=METHOD_UUID):
        self.namespace = namespace
        self.method = method
        self.reset()

    def reset(self):
        self.next_int = 1

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        if not isinstance(value, Namespace):
            raise ValueError("Must be a Namespace object")
        self._namespace = value
        self.reset()

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if value not in IDGenerator.METHODS:
            raise InvalidMethodError("invalid method: %s" % value)
        self._method = value
        self.reset()

    def create_id(self, prefix="guid"):
        """Create an ID.

        Note that if `prefix` is not provided, it will be `quid`, even if the
        `method` is `METHOD_INT`.
        """
        if self.method == IDGenerator.METHOD_UUID:
            id_ = str(uuid.uuid4())
        elif self.method == IDGenerator.METHOD_INT:
            id_ = self.next_int
            self.next_int += 1
        else:
            raise InvalidMethodError()

        return "%s:%s-%s" % (self.namespace.prefix, prefix, id_)

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
