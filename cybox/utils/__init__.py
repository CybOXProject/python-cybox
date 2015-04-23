# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Common utility methods"""

#importlib is imported below
import os

from .caches import *
from .idgen import *
from .nsparser import *


def get_class_for_object_type(object_type):
    return META.get_class_for_object_type(object_type)


def denormalize_from_xml(value, delimiter):
    if not delimiter:
        raise ValueError("delimiter must not be None")

    # This is probably not necessary since the parser will have removed
    # the CDATA already.
    denormalized = unwrap_cdata(value)

    if delimiter in denormalized:
        return denormalized.split(delimiter)
    else:
        return denormalized


def normalize_to_xml(value, delimiter):
    if not delimiter:
        raise ValueError("delimiter must not be None")

    if isinstance(value, list):
        normalized_list = [unicode(x) for x in value]
        if any(delimiter in x for x in normalized_list):
            raise ValueError("list items cannot contain delimiter")
        normalized = delimiter.join(normalized_list)
    else:
        normalized = unicode(value)
        if delimiter in normalized:
            raise ValueError("value cannot contain delimiter")

    return normalized


def wrap_cdata(value):
    return "<![CDATA[" + value + "]]>"


def unwrap_cdata(value):
    """Remove CDATA wrapping from `value` if present"""
    if value.startswith("<![CDATA[") and value.endswith("]]>"):
        return value[9:-3]
    else:
        return value


def _import_submodules(pkg):
    import importlib
    filename = pkg.__file__
    if "__init__.py" not in filename:
        return

    for module in os.listdir(os.path.dirname(filename)):
        if "__init__.py" in module or not module.endswith(".py"):
            continue
        mod_name = "%s.%s" % (pkg.__name__, module[:-3])
        importlib.import_module(mod_name)


def is_sequence(item):
    """Returns ``True`` if `value` is a sequence type (e.g., ``list``, or
    ``tuple``). String types will return ``False``.

    """
    return hasattr(item, "__iter__")


def _import_all():
    """Import all modules in the core, common and objects packages.

    This is useful when we want to check all classes for some property.
    """

    # Everything in common should be imported by cybox.common.__init__
    import cybox.common
    # Everything in core should be imported by cybox.core.__init__
    import cybox.core
    import cybox.objects
    _import_submodules(cybox.objects)
