# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
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


class TestArtifactInstance(ObjectTestCase, unittest.TestCase):
    object_type = "ArtifactObjectType"
    klass = Artifact

    _full_dict = {
        "packaging": [
            {
                "packaging_type": "encoding",
                "algorithm": "Base64"
            }
        ],
        "xsi:type": object_type,
        "raw_artifact": "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAsmdKQq6RBwBGAAAARgAAAADAnzJBjADg"
                        "GLEMrQgARQAAOAAAQABAEWVHwKiqCMCoqhSAGwA1ACSF7RAyAQAAAQAAAAAAAAZn"
                        "b29nbGUDY29tAAAQAAGyZ0pCwJMHAGIAAABiAAAAAOAYsQytAMCfMkGMCABFAABU"
                        "y+wAAIARmT7AqKoUwKiqCAA1gBsAQMclEDKBgAABAAEAAAAABmdvb2dsZQNjb20A"
                        "ABAAAcAMABAAAQAAAQ4AEA92PXNwZjEgcHRyID9hbGy2Z0pCFKYHAEYAAABGAAAA"
                        "AMCfMkGMAOAYsQytCABFAAA4AABAAEARZUfAqKoIwKiqFIAbADUAJJ6w928BAAAB"
                        "AAAAAAAABmdvb2dsZQNjb20AAA8AAbdnSkJZFgUAKgEAACoBAAAA4BixDK0AwJ8y"
                        "QYwIAEUAARzMuwAAgBGXp8CoqhTAqKoIADWAGwEI1vP3b4GAAAEABgAAAAYGZ29v"
                        "Z2xlA2NvbQAADwABwAwADwABAAACKAAKACgFc210cDTADMAMAA8AAQAAAigACgAK"
                        "BXNtdHA1wAzADAAPAAEAAAIoAAoACgVzbXRwNsAMwAwADwABAAACKAAKAAoFc210"
                        "cDHADMAMAA8AAQAAAigACgAKBXNtdHAywAzADAAPAAEAAAIoAAoAKAVzbXRwM8AM"
                        "wCoAAQABAAACWAAE2O8lGsBAAAEAAQAAAlgABEDppxnAVgABAAEAAAJYAARCZgkZ"
                        "wGwAAQABAAACWAAE2O85GcCCAAEAAQAAAlgABNjvJRnAmAABAAEAAAJYAATY7zka"
                        "v2dKQo/HBABGAAAARgAAAADAnzJBjADgGLEMrQgARQAAOAAAQABAEWVHwKiqCMCo"
                        "qhSAGwA1ACRMcUmhAQAAAQAAAAAAAAZnb29nbGUDY29tAAAdAAG/Z0pCn+YGAEYA"
                        "AABGAAAAAOAYsQytAMCfMkGMCABFAAA4zM0AAIARmHnAqKoUwKiqCAA1gBsAJMvw"
                        "SaGBgAABAAAAAAAABmdvb2dsZQNjb20AAB0AAcdnSkJp5QQAVQAAAFUAAAAAwJ8y"
                        "QYwA4BixDK0IAEUAAEcAAEAAQBFlOMCoqgjAqKoUgBsANQAzF8KbuwEAAAEAAAAA"
                        "AAADMTA0ATkDMTkyAjY2B2luLWFkZHIEYXJwYQAADAABx2dKQmPnBACBAAAAgQAA"
                        "AADgGLEMrQDAnzJBjAgARQAAc80bAACAEZfwwKiqFMCoqggANYAbAF+CtZu7gYAA"
                        "AQABAAAAAAMxMDQBOQMxOTICNjYHaW4tYWRkcgRhcnBhAAAMAAHADAAMAAEAAVEl"
                        "ACAMNjYtMTkyLTktMTA0A2dlbgl0d3RlbGVjb20DbmV0AA5oSkJ/dwoASgAAAEoA"
                        "AAAAwJ8yQYwA4BixDK0IAEUAADwAAEAAQBFlQ8CoqgjAqKoUgBsANQAor2F1wAEA"
                        "AAEAAAAAAAADd3d3Bm5ldGJzZANvcmcAAAEAAQ5oSkKONgsAWgAAAFoAAAAA4Bix"
                        "DK0AwJ8yQYwIAEUAAEzP+QAAgBGVOcCoqhTAqKoIADWAGwA4oxd1wIGAAAEAAQAA"
                        "AAADd3d3Bm5ldGJzZANvcmcAAAEAAcAMAAEAAQABQO8ABMyYvgwfaEpCfQkHAEoA"
                        "AABKAAAAAMCfMkGMAOAYsQytCABFAAA8b0xAAEAR9fbAqKoIwKiqFIAbADUAKDQy"
                        "8NQBAAABAAAAAAAAA3d3dwZuZXRic2QDb3JnAAAcAAEfaEpC4akKAGYAAABmAAAA"
                        "AOAYsQytAMCfMkGMCABFAABY0FoAAIARlMzAqKoUwKiqCAA1gBsARF8b8NSBgAAB"
                        "AAEAAAAAA3d3dwZuZXRic2QDb3JnAAAcAAHADAAcAAEAAVGAABAgAQT4AAQABwLg"
                        "gf/+UpprW2hKQrD8BwBKAAAASgAAAADAnzJBjADgGLEMrQgARQAAPAAAQABAEWVD"
                        "wKiqCMCoqhSAGwA1ACilzX85AQAAAQAAAAAAAAN3d3cGbmV0YnNkA29yZwAAHAAB"
                        "W2hKQjP+BwBmAAAAZgAAAADgGLEMrQDAnzJBjAgARQAAWNRPAACAEZDXwKiqFMCo"
                        "qggANYAbAETQ8n85gYAAAQABAAAAAAN3d3cGbmV0YnNkA29yZwAAHAABwAwAHAAB"
                        "AAFRRAAQIAEE+AAEAAcC4IH//lKaa2RoSkKSOgsASgAAAEoAAAAAwJ8yQYwA4Bix"
                        "DK0IAEUAADwAAEAAQBFlQ8CoqgjAqKoUgBsANQAojWmNswEAAAEAAAAAAAADd3d3"
                        "Bmdvb2dsZQNjb20AABwAAWRoSkIsewsAXgAAAF4AAAAA4BixDK0AwJ8yQYwIAEUA"
                        "AFDUbQAAgBGQwcCoqhTAqKoIADWAGwA8DcGNs4GAAAEAAQAAAAADd3d3Bmdvb2ds"
                        "ZQNjb20AABwAAcAMAAUAAQAAAnkACAN3d3cBbMAQbmhKQqZWBQBMAAAATAAAAADA"
                        "nzJBjADgGLEMrQgARQAAPgAAQABAEWVBwKiqCMCoqhSAGwA1ACo9CtyiAQAAAQAA"
                        "AAAAAAN3d3cBbAZnb29nbGUDY29tAAAcAAFuaEpCv5cFAEwAAABMAAAAAOAYsQyt"
                        "AMCfMkGMCABFAAA+1TkAAIARkAfAqKoUwKiqCAA1gBsAKryJ3KKBgAABAAAAAAAA"
                        "A3d3dwFsBmdvb2dsZQNjb20AABwAAZdoSkI8HgMASwAAAEsAAAAAwJ8yQYwA4Bix"
                        "DK0IAEUAAD0AAEAAQBFlQsCoqgjAqKoUgBsANQApiGG8HwEAAAEAAAAAAAADd3d3"
                        "B2V4YW1wbGUDY29tAAAcAAGXaEpC86wGAEsAAABLAAAAAOAYsQytAMCfMkGMCABF"
                        "AAA91p8AAIARjqLAqKoUwKiqCAA1gBsAKQfhvB+BgAABAAAAAAAAA3d3dwdleGFt"
                        "cGxlA2NvbQAAHAABomhKQhCDDABPAAAATwAAAADAnzJBjADgGLEMrQgARQAAQQAA"
                        "QABAEWU+wKiqCMCoqhSAGwA1AC1EKCZtAQAAAQAAAAAAAAN3d3cHZXhhbXBsZQdu"
                        "b3RnaW5oAAAcAAGjaEpC0IAAAE8AAABPAAAAAOAYsQytAMCfMkGMCABFAABB1y4A"
                        "AIARjg/AqKoUwKiqCAA1gBsALb+kJm2FgwABAAAAAAAAA3d3dwdleGFtcGxlB25v"
                        "dGdpbmgAABwAAcFoSkIsFQoARwAAAEcAAAAAwJ8yQYwA4BixDK0IAEUAADkAAEAA"
                        "QBFlRsCoqgjAqKoUgBsANQAlQm7+4wEAAAEAAAAAAAADd3d3A2lzYwNvcmcAAP8A"
                        "AcFoSkLIMAsAcwAAAHMAAAAA4BixDK0AwJ8yQYwIAEUAAGXY9AAAgBGMJcCoqhTA"
                        "qKoIADWAGwBRy2T+44GAAAEAAgAAAAADd3d3A2lzYwNvcmcAAP8AAcAMABwAAQAA"
                        "AlgAECABBPgAAAACAAAAAAAAAA3ADAABAAEAAAJYAATMmLhYwWhKQrQ/CwBSAAAA"
                        "UgAAAADAnzJBjADgGLEMrQgARQAARAAAQABAEWU7wKiqCMCoqhSAHAA1ADACNVpT"
                        "AQAAAQAAAAAAAAExATABMAMxMjcHaW4tYWRkcgRhcnBhAAAMAAHBaEpCAEILAGkA"
                        "AABpAAAAAOAYsQytAMCfMkGMCABFAABb2PUAAIARjC7AqKoUwKiqCAA1gBwAR/kw"
                        "WlOFgAABAAEAAAAAATEBMAEwAzEyNwdpbi1hZGRyBGFycGEAAAwAAcAMAAwAAQAA"
                        "DhAACwlsb2NhbGhvc3QAwWhKQkZLCwBDAAAAQwAAAADAnzJBjADgGLEMrQgARQAA"
                        "NQAAQABAEWVKwKiqCMCoqhSAHQA1ACGYvSCKAQAAAQAAAAAAAANpc2MDb3JnAAAC"
                        "AAHBaEpC2ogLAIEAAACBAAAAABKpADIjAGAIReRVCABFAABzh94AAIARapXAqKo4"
                        "2Q0EGAarADUAXznwMm4BAAABAAAAAAAABV9sZGFwBF90Y3AXRGVmYXVsdC1GaXJz"
                        "dC1TaXRlLU5hbWUGX3NpdGVzAmRjBl9tc2Rjcwt1dGVsc3lzdGVtcwVsb2NhbAAA"
                        "IQABwWhKQrWSCwCmAAAApgAAAADgGLEMrQDAnzJBjAgARQAAmNj3AACAEYvvwKiq"
                        "FMCoqggANYAdAIR72CCKgYAAAQAEAAAAAANpc2MDb3JnAAACAAHADAACAAEAAA4Q"
                        "AA4GbnMtZXh0BG5ydDHADMAMAAIAAQAADhAADgZucy1leHQEc3RoMcAMwAwAAgAB"
                        "AAAOEAAJBm5zLWV4dMAMwAwAAgABAAAOEAAOBm5zLWV4dARsZ2ExwAzBaEpCPdYL"
                        "AIEAAACBAAAAAGAIReRVABKpADIjCABFAABzAABAADoR+HPZDQQYwKiqOAA1BqsA"
                        "X7VsMm6FgwABAAAAAAAABV9sZGFwBF90Y3AXRGVmYXVsdC1GaXJzdC1TaXRlLU5h"
                        "bWUGX3NpdGVzAmRjBl9tc2Rjcwt1dGVsc3lzdGVtcwVsb2NhbAAAIQABwWhKQszY"
                        "CwBiAAAAYgAAAAASqQAyIwBgCEXkVQgARQAAVIfwAACAEWqiwKiqONkNBBgGrAA1"
                        "AEB8UfFhAQAAAQAAAAAAAAVfbGRhcARfdGNwAmRjBl9tc2Rjcwt1dGVsc3lzdGVt"
                        "cwVsb2NhbAAAIQABwWhKQmEcDABiAAAAYgAAAABgCEXkVQASqQAyIwgARQAAVAAA"
                        "QAA6EfiS2Q0EGMCoqjgANQasAED3zfFhhYMAAQAAAAAAAAVfbGRhcARfdGNwAmRj"
                        "Bl9tc2Rjcwt1dGVsc3lzdGVtcwVsb2NhbAAAIQABwWhKQoAeDACMAAAAjAAAAAAS"
                        "qQAyIwBgCEXkVQgARQAAfofxAACAEWp3wKiqONkNBBgGrQA1AGp3mINhAQAAAQAA"
                        "AAAAAAVfbGRhcARfdGNwJDA1YjUyOTJiLTM0YjgtNGZiNy04NWEzLThiZWVmNWZk"
                        "MjA2OQdkb21haW5zBl9tc2Rjcwt1dGVsc3lzdGVtcwVsb2NhbAAAIQABwWhKQmRr"
                        "DACMAAAAjAAAAABgCEXkVQASqQAyIwgARQAAfgAAQAA6Efho2Q0EGMCoqjgANQat"
                        "AGrzFINhhYMAAQAAAAAAAAVfbGRhcARfdGNwJDA1YjUyOTJiLTM0YjgtNGZiNy04"
                        "NWEzLThiZWVmNWZkMjA2OQdkb21haW5zBl9tc2Rjcwt1dGVsc3lzdGVtcwVsb2Nh"
                        "bAAAIQABwWhKQvn4DQBTAAAAUwAAAAASqQAyIwBgCEXkVQgARQAARYf1AACAEWqs"
                        "wKiqONkNBBgGrgA1ADEajdBgAQAAAQAAAAAAAAVHUklNTQt1dGVsc3lzdGVtcwVs"
                        "b2NhbAAAAQABwWhKQhU7DgBTAAAAUwAAAABgCEXkVQASqQAyIwgARQAARQAAQAA6"
                        "Efih2Q0EGMCoqjgANQauADGWCdBghYMAAQAAAAAAAAVHUklNTQt1dGVsc3lzdGVt"
                        "cwVsb2NhbAAAAQAByWhKQuJzBQBTAAAAUwAAAAASqQAyIwBgCEXkVQgARQAARYf7"
                        "AACAEWqmwKiqONkNBBgGrwA1ADF0iXZjAQAAAQAAAAAAAAVHUklNTQt1dGVsc3lz"
                        "dGVtcwVsb2NhbAAAAQAByWhKQj+6BQBTAAAAUwAAAABgCEXkVQASqQAyIwgARQAA"
                        "RQAAQAA6Efih2Q0EGMCoqjgANQavADHwBXZjhYMAAQAAAAAAAAVHUklNTQt1dGVs"
                        "c3lzdGVtcwVsb2NhbAAAAQAB",
        "type": "Network Traffic"
    }


class TestArtifactPattern(ObjectTestCase, unittest.TestCase):
    object_type = "ArtifactObjectType"
    klass = Artifact

    _full_dict = {
        "xsi:type": object_type,
        "raw_artifact": {
            "value": "777777076578616D706C6503636F6D",
            "condition": "Contains"
        },
        "type": "Network Traffic"
    }


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
