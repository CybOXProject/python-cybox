# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.linux_package_object as linux_package_binding
from cybox.common import ObjectProperties, String, StructuredText


class LinuxPackage(ObjectProperties):
    _binding = linux_package_binding
    _binding_class = linux_package_binding.LinuxPackageObjectType
    _namespace = "http://cybox.mitre.org/objects#LinuxPackageObject-2"
    _XSI_NS = "LinuxPackageObj"
    _XSI_TYPE = "LinuxPackageObjectType"

    #architecture = cybox.TypedField("Architecture", Architecture) TODO
    category = cybox.TypedField("Category", String)
    description = cybox.TypedField("Description", String)
    epoch = cybox.TypedField("Epoch", String)
    evr = cybox.TypedField("EVR", String)
    name = cybox.TypedField("Name", String)
    release = cybox.TypedField("Release", String)
    vendor = cybox.TypedField("Vendor", String)
    version = cybox.TypedField("Version", String)
