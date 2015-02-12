# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import base64
import bz2
import zlib
import unittest

from cybox.objects.artifact_object import (Artifact, Base64Encoding,
        Bz2Compression, RawArtifact, XOREncryption, ZlibCompression)
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestRawArtifact(unittest.TestCase):

    def test_xml_output(self):
        data = "0123456789abcdef"
        ra = RawArtifact(data)

        self.assertTrue(data in ra.to_xml())


class TestArtifact(ObjectTestCase, unittest.TestCase):
    object_type = "ArtifactObjectType"
    klass = Artifact

    test_text_data = "Here is a blob of text"
    test_binary_data = "Here is some \x99 binary \xbb data."

    #TODO: Test with binary data as well.
    _full_dict = {
        'raw_artifact': test_text_data,
        'type': Artifact.TYPE_NETWORK,
        'xsi:type': object_type,
    }

    def test_set_data_and_packed_data(self):
        a = Artifact()
        self.assertEqual(a.data, None)
        self.assertEqual(a.packed_data, None)

        a.data = "Blob"
        self.assertRaises(ValueError, _set_packed_data, a, "blob")
        a.data = None

        a.packed_data = "Blob"
        self.assertRaises(ValueError, _set_data, a, "blob")
        a.packed_data = None

    def test_round_trip(self):
        a = Artifact(self.test_text_data, Artifact.TYPE_GENERIC)
        a2 = round_trip(a, Artifact)
        self.assertEqual(a.to_dict(), a2.to_dict())

    def test_base64_encoding(self):
        a = Artifact(self.test_binary_data)
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)
        self.assertEqual(self.test_binary_data, a2.data)

        expected = base64.b64encode(self.test_binary_data)
        self.assertEqual(expected, a2.packed_data)

    def test_zlib_base64_encoding(self):
        a = Artifact(self.test_binary_data)
        a.packaging.append(ZlibCompression())
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)
        self.assertEqual(self.test_binary_data, a2.data)

        expected = base64.b64encode(zlib.compress(self.test_binary_data))
        self.assertEqual(expected, a2.packed_data)

    def test_encryption(self):
        a = Artifact(self.test_binary_data)
        a.packaging.append(XOREncryption(0x4a))
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)

        self.assertEqual(self.test_binary_data, a2.data)


def _set_data(artifact, data):
    artifact.data = data


def _set_packed_data(artifact, packed_data):
    artifact.packed_data = packed_data

if __name__ == "__main__":
    unittest.main()
