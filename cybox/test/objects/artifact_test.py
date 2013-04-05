import base64
import bz2
import zlib
import unittest

from cybox.objects.artifact import (Artifact, Base64Encoding, Bz2Compression,
        ZlibCompression)
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestArtifact(unittest.TestCase, ObjectTestCase):
    object_type = "ArtifactType"
    klass = Artifact

    test_text_data = "Here is a blob of text"
    test_binary_data = "Here is some \x99 binary \xbb data."

    def test_round_trip(self):
        pass

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

        expected_data = base64.b64encode(self.test_binary_data)
        self.assertEqual(base64.b64encode(self.test_binary_data), a2.packed_data)
        print expected_data

    def test_zlib_base64_encoding(self):
        a = Artifact(self.test_binary_data)
        a.packaging.append(ZlibCompression())
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)
        self.assertEqual(self.test_binary_data, a2.data)

        expected_data = base64.b64encode(zlib.compress(self.test_binary_data))
        self.assertEqual(expected_data, a2.packed_data)
        print expected_data


def _set_data(artifact, data):
    artifact.data = data


def _set_packed_data(artifact, packed_data):
    artifact.packed_data = packed_data

if __name__ == "__main__":
    unittest.main()
