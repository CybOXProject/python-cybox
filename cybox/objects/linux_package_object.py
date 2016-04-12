# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.linux_package_object as linux_package_binding
from cybox.common import ObjectProperties, String, VocabString
from cybox.common.vocabs import VocabField


class LinuxPackageArchitecture(VocabString):
    pass


class LinuxPackage(ObjectProperties):
    _binding = linux_package_binding
    _binding_class = linux_package_binding.LinuxPackageObjectType
    _namespace = "http://cybox.mitre.org/objects#LinuxPackageObject-2"
    _XSI_NS = "LinuxPackageObj"
    _XSI_TYPE = "LinuxPackageObjectType"

    architecture = VocabField("Architecture", LinuxPackageArchitecture)
    category = fields.TypedField("Category", String)
    description = fields.TypedField("Description", String)
    epoch = fields.TypedField("Epoch", String)
    evr = fields.TypedField("EVR", String)
    name = fields.TypedField("Name", String)
    release = fields.TypedField("Release", String)
    vendor = fields.TypedField("Vendor", String)
    version = fields.TypedField("Version", String)
