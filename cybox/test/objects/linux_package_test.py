# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.linux_package_object import LinuxPackage
from cybox.test.objects import ObjectTestCase


class TestLinuxPackage(ObjectTestCase, unittest.TestCase):
    object_type = "LinuxPackageObjectType"
    klass = LinuxPackage

    _full_dict = {
        'architecture': "Some test arch",
        'category': "test category",
        'description': "A linux package",
        'epoch': "the epoch",
        'evr': "evr evr evr",
        'name': "sample package",
        'release': "release text",
        'vendor': "some vendor",
        'version': "v2",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
