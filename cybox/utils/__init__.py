# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Common utility methods"""

#importlib is imported below
import os

from .caches import *
from .idgen import *
from .nsparser import *

import xml.sax.saxutils

PROPERTY_LIST_DELIMITER = "##comma##"


def get_class_for_object_type(object_type):
    return META.get_class_for_object_type(object_type)


def denormalize_from_xml(value):
    # This is probably not necessary since the parser will have removed
    # the CDATA already.
    denormalized = unwrap_cdata(value)

    if PROPERTY_LIST_DELIMITER in value:
        return [unescape(x) for x in
                denormalized.split(PROPERTY_LIST_DELIMITER)]
    else:
        return unescape(denormalized)


def normalize_to_xml(value):
    normalized = value

    if isinstance(value, list):
        normalized = PROPERTY_LIST_DELIMITER.join(
                                    [escape(unicode(x)) for x in value])
    else:
        normalized = escape(unicode(value))

    return normalized


def escape(value):
    return xml.sax.saxutils.escape(value)


def unescape(value):
    return xml.sax.saxutils.unescape(value)


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
