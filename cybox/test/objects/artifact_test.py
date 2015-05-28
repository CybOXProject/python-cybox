# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from base64 import b64encode
import unittest
from zlib import compress

from mixbox.vendor import six
from mixbox.vendor.six import u

from cybox.objects.artifact_object import (Artifact, Base64Encoding,
        Bz2Compression, RawArtifact, XOREncryption, ZlibCompression)
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestRawArtifact(unittest.TestCase):

    def test_xml_output(self):
        # A RawArtifact stores a Unicode string, even though it typically
        # consists only of valid Base64 characters.
        data = u("0123456789abcdef")
        ra = RawArtifact(data)

        expected_data = data.encode('utf-8')
        self.assertTrue(expected_data in ra.to_xml())


class TestArtifactEncoding(unittest.TestCase):

    def test_cannot_create_artifact_from_unicode_data(self):
        self.assertRaises(ValueError, Artifact, u("abc123"))

    def test_setting_ascii_artifact_data_no_packaging(self):
        a = Artifact()
        a.data = b"abc123"
        self.assertEqual(six.binary_type, type(a.data))
        self.assertEqual(six.text_type, type(a.packed_data))

    def test_cannot_set_nonascii_data_with_no_packaging(self):
        a = Artifact()
        # You can set this data, but if you don't add any packaging, you should
        # get an error when trying to get the packed data, since it can't be
        # encoded as ASCII.
        a.data = b"\x00abc123\xff"
        self.assertEqual(six.binary_type, type(a.data))
        self.assertRaises(ValueError, _get_packed_data, a)

        # With Base64 encoding, we can retrieve this.
        a.packaging.append(Base64Encoding())
        self.assertEqual("AGFiYzEyM/8=", a.packed_data)

    def test_setting_ascii_artifact_packed_data_no_packaging(self):
        a = Artifact()
        a.packed_data = u("abc123")
        self.assertEqual(six.binary_type, type(a.data))
        self.assertEqual(six.text_type, type(a.packed_data))

    def test_cannot_set_nonascii_artifact_packed_data(self):
        a = Artifact()
        a.packed_data = u("\x00abc123\xff")
        self.assertEqual(six.text_type, type(a.packed_data))

        #TODO: Should this raise an error sooner, since there's nothing we can
        # do at this point? There's no reason that the packed_data should
        # contain non-ascii characters.
        self.assertRaises(UnicodeEncodeError, _get_data, a)


class TestArtifact(ObjectTestCase, unittest.TestCase):
    object_type = "ArtifactObjectType"
    klass = Artifact

    ascii_data = b"ABCDEFGHIJKLMNOPQRSTUVWZYZ0123456879"
    binary_data = b"\xde\xad\xbe\xef Dead Beef"

    # The raw_artifact data in a JSON/dict representation should always be
    # ASCII byte data (typically Base64-encoded, but this is not required).
    _full_dict = {
        'raw_artifact': "Here is a blob of text.",
        'type': Artifact.TYPE_NETWORK,
        'xsi:type': object_type,
    }

    def test_set_data_and_packed_data(self):
        a = Artifact()
        self.assertEqual(a.data, None)
        self.assertEqual(a.packed_data, None)

        a.data = b"Blob"
        self.assertRaises(ValueError, _set_packed_data, a, u("blob"))
        a.data = None

        a.packed_data = u("Blob")
        self.assertRaises(ValueError, _set_data, a, b"blob")
        a.packed_data = None

    def test_round_trip(self):
        # Without any packaging, the only data an Artifact can encode
        # successfully is ASCII data.
        a = Artifact(self.ascii_data, Artifact.TYPE_GENERIC)
        a2 = round_trip(a, Artifact)
        self.assertEqual(a.to_dict(), a2.to_dict())

    def test_non_ascii_round_trip_raises_error(self):
        a = Artifact(self.binary_data, Artifact.TYPE_GENERIC)
        # Since the data is non-ASCII, this should raise an error.
        self.assertRaises(ValueError, round_trip, a, Artifact)

    def test_base64_encoding(self):
        a = Artifact(self.binary_data)
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)
        self.assertEqual(self.binary_data, a2.data)

        expected = b64encode(self.binary_data).decode('ascii')
        self.assertEqual(expected, a2.packed_data)

    def test_zlib_base64_encoding(self):
        a = Artifact(self.binary_data)
        a.packaging.append(ZlibCompression())
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)
        self.assertEqual(self.binary_data, a2.data)

        expected = b64encode(compress(self.binary_data)).decode('ascii')
        self.assertEqual(expected, a2.packed_data)

    def test_encryption(self):
        a = Artifact(self.binary_data)
        a.packaging.append(XOREncryption(0x4a))
        a.packaging.append(Base64Encoding())
        a2 = round_trip(a, Artifact)

        self.assertEqual(self.binary_data, a2.data)


def _get_data(artifact):
    return artifact.data


def _set_data(artifact, data):
    artifact.data = data


def _get_packed_data(artifact):
    return artifact.packed_data


def _set_packed_data(artifact, packed_data):
    artifact.packed_data = packed_data


if __name__ == "__main__":
    unittest.main()
