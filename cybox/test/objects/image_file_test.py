# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.image_file_object import ImageFile

from cybox.common import Hash, String
from cybox.compat import long
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase

class TestImageFile(ObjectTestCase, unittest.TestCase):
    object_type = "ImageFileObjectType"
    klass = ImageFile

    _full_dict = {
        'image_is_compressed': True,
        'image_file_format': u("JPG"),
        'image_height': 10000,
        'image_width': 3000,
        'bits_per_pixel': 9000,
        'compression_algorithm': u("An algorithm"),

        'is_packed': False,
        'is_masqueraded': True,
        'file_name': u("example.txt"),
        'file_path': {'value': u("C:\\Temp"),
                      'fully_qualified': True},
        'device_path': u("\\Device\\CdRom0"),
        'full_path': u("C:\\Temp\\example.txt"),
        'file_extension': u("txt"),
        'size_in_bytes': long(1024),
        'magic_number': u("D0CF11E0"),
        'file_format': u("ASCII Text"),
        'hashes': [
            {
                'type': Hash.TYPE_MD5,
                'simple_hash_value': u("0123456789abcdef0123456789abcdef")
            }
        ],
        'digital_signatures': [
            {
                'certificate_issuer': u("Microsoft"),
                'certificate_subject': u("Notepad"),
            }
        ],
        'modified_time': "2010-11-06T02:02:02+08:00",
        'accessed_time': "2010-11-07T02:03:02+09:00",
        'created_time': "2010-11-08T02:04:02+10:00",
        'user_owner': u("sballmer"),
        'packer_list': [
            {
                'name': u("UPX"),
                'version': u("3.91"),
            }
        ],
        'peak_entropy': 7.454352453,
        'sym_links': [u("../link_destination")],
        'byte_runs': [{'offset': 16, 'byte_run_data': u("1A2B3C4D")}],
        'extracted_features': {
            'strings': [{'string_value': u("string from the file")}],
        },
        'encryption_algorithm': u("RC4"),
        'compression_method': u("deflate"),
        'compression_version': u("1.0"),
        'compression_comment': u("This has been compressed"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
