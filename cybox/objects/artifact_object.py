# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import base64
import bz2
import zlib

import cybox
import cybox.bindings.artifact_object as artifact_binding
from cybox.common import ObjectProperties, String


class RawArtifact(String):
    _binding_class = artifact_binding.RawArtifactType
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    
    byte_order = cybox.TypedField("byte_order")

class Artifact(ObjectProperties):
    # Warning: Do not attempt to get or set Raw_Artifact directly. Use `data`
    # or `packed_data` respectively. Raw_Artifact will be set on export.
    _binding = artifact_binding
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _XSI_NS = "ArtifactObj"
    _XSI_TYPE = "ArtifactObjectType"

    TYPE_FILE = "File"
    TYPE_MEMORY = "Memory Region"
    TYPE_FILE_SYSTEM = "File System Fragment"
    TYPE_NETWORK = "Network Traffic"
    TYPE_GENERIC = "Generic Data Region"

    def __init__(self, data=None, type_=None):
        super(Artifact, self).__init__()
        self.type_ = type_
        self.packaging = []
        self._packed_data = None
        self.data = data

    @property
    def data(self):
        if self._data:
            return self._data
        elif self._packed_data:
            tmp_data = self._packed_data
            for p in reversed(self.packaging):
                tmp_data = p.unpack(tmp_data)
            return tmp_data
        else:
            return None

    @data.setter
    def data(self, value):
        if self._packed_data:
            raise ValueError("packed_data already set, can't set data")
        self._data = value

    @property
    def packed_data(self):
        if self._packed_data:
            return self._packed_data
        elif self._data:
            tmp_data = self._data
            for p in self.packaging:
                tmp_data = p.pack(tmp_data)
            return tmp_data
        else:
            return None

    @packed_data.setter
    def packed_data(self, value):
        if self._data:
            raise ValueError("data already set, can't set packed_data")
        self._packed_data = value

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        artifact_obj = artifact_binding.ArtifactObjectType()
        super(Artifact, self).to_obj(return_obj=artifact_obj, ns_info=ns_info)

        if self.packaging:
            packaging = artifact_binding.PackagingType()
            for p in self.packaging:
                p_obj = p.to_obj(ns_info=ns_info)
                if isinstance(p, Compression):
                    packaging.add_Compression(p_obj)
                elif isinstance(p, Encryption):
                    packaging.add_Encryption(p_obj)
                elif isinstance(p, Encoding):
                    packaging.add_Encoding(p_obj)
                else:
                    raise ValueError("Unsupported Packaging Type: %s" %
                                        type(p))
            artifact_obj.Packaging = packaging

        if self.packed_data:
            artifact_obj.Raw_Artifact = RawArtifact(self.packed_data).to_obj(ns_info=ns_info)
        artifact_obj.type_ = self.type_

        return artifact_obj

    def to_dict(self):
        artifact_dict = {}
        super(Artifact, self).to_dict(artifact_dict)

        if self.packaging:
            artifact_dict['packaging'] = [p.to_dict() for p in self.packaging]
        if self.packed_data:
            artifact_dict['raw_artifact'] = RawArtifact(self.packed_data).to_dict()
        if self.type_:
            artifact_dict['type'] = self.type_

        return artifact_dict

    @staticmethod
    def from_obj(artifact_obj):
        if not artifact_obj:
            return None

        artifact = Artifact()
        ObjectProperties.from_obj(artifact_obj, artifact)

        packaging = artifact_obj.Packaging
        if packaging:
            for c in packaging.Compression:
                artifact.packaging.append(Compression.from_obj(c))
            for e in packaging.Encryption:
                artifact.packaging.append(Encryption.from_obj(e))
            for e in packaging.Encoding:
                artifact.packaging.append(Encoding.from_obj(e))

        raw_artifact = artifact_obj.Raw_Artifact
        if raw_artifact:
            artifact.packed_data = RawArtifact.from_obj(raw_artifact).value
        artifact.type_ = artifact_obj.type_

        return artifact

    @staticmethod
    def from_dict(artifact_dict):
        if not artifact_dict:
            return None

        artifact = Artifact()
        ObjectProperties.from_dict(artifact_dict, artifact)

        for layer in artifact_dict.get('packaging', []):
            if layer.get('packaging_type') == "compression":
                artifact.packaging.append(Compression.from_dict(layer))
            if layer.get('packaging_type') == "encryption":
                artifact.packaging.append(Encryption.from_dict(layer))
            if layer.get('packaging_type') == "encoding":
                artifact.packaging.append(Encoding.from_dict(layer))

        raw_artifact = artifact_dict.get('raw_artifact')
        if raw_artifact:
            artifact.packed_data = RawArtifact.from_dict(raw_artifact).value
        artifact.type_ = artifact_dict.get('type')

        return artifact


class Packaging(cybox.Entity):
    """An individual packaging layer."""
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'

    def pack(self, data):
        raise NotImplementedError()

    def unpack(self, packed_data):
        raise NotImplementedError()


class Compression(Packaging):
    """A Compression packaging layer

    Currently only zlib and bz2 are supported.
    Also, compression_mechanism_ref is not currently supported.
    """

    def __init__(self, compression_mechanism=None):
        super(Compression, self).__init__()
        self.compression_mechanism = compression_mechanism

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        obj = artifact_binding.CompressionType()
        if self.compression_mechanism:
            obj.compression_mechanism = self.compression_mechanism

        return obj

    def to_dict(self):
        dict_ = {}
        dict_['packaging_type'] = 'compression'
        if self.compression_mechanism:
            dict_['compression_mechanism'] = self.compression_mechanism

        return dict_

    @staticmethod
    def from_obj(compression_obj):
        mechanism = compression_obj.compression_mechanism
        return Compression.get_object(mechanism)

    @staticmethod
    def from_dict(compression_dict):
        mechanism = compression_dict.get('compression_mechanism')
        return Compression.get_object(mechanism)

    @staticmethod
    def get_object(mechanism):
        if mechanism == 'zlib':
            return ZlibCompression()
        elif mechanism == "bz2":
            return Bz2Compression()
        else:
            raise ValueError("Unsupported compression mechanism: %s" % mechanism)


class ZlibCompression(Compression):

    def __init__(self):
        super(ZlibCompression, self).__init__("zlib")

    def pack(self, data):
        return zlib.compress(data)

    def unpack(self, packed_data):
        return zlib.decompress(packed_data)


class Bz2Compression(Compression):

    def __init__(self):
        super(Bz2Compression, self).__init__("bz2")

    def pack(self, data):
        return bz2.compress(data)

    def unpack(self, packed_data):
        return bz2.decompress(packed_data)


class Encryption(Packaging):
    """
    An encryption packaging layer.
    """

    def __init__(self, encryption_mechanism=None, encryption_key=None):
        super(Encryption, self).__init__()
        self.encryption_mechanism = encryption_mechanism
        self.encryption_key = encryption_key

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        obj = artifact_binding.EncryptionType()
        if self.encryption_mechanism:
            obj.encryption_mechanism = self.encryption_mechanism
        if self.encryption_key:
            obj.encryption_key = self.encryption_key

        return obj

    def to_dict(self):
        dict_ = {}
        dict_['packaging_type'] = 'encryption'
        if self.encryption_mechanism:
            dict_['encryption_mechanism'] = self.encryption_mechanism
        if self.encryption_key:
            dict_['encryption_key'] = self.encryption_key

        return dict_

    @staticmethod
    def from_obj(encryption_obj):
        mechanism = encryption_obj.encryption_mechanism
        key = encryption_obj.encryption_key
        return Encryption.get_object(mechanism, key)

    @staticmethod
    def from_dict(encryption_dict):
        mechanism = encryption_dict.get('encryption_mechanism')
        key = encryption_dict.get('encryption_key')
        return Encryption.get_object(mechanism, key)

    @staticmethod
    def get_object(mechanism, key):
        if mechanism == 'xor':
            return XOREncryption(key)
        if mechanism == 'PasswordProtected':
            return PasswordProtectedZipEncryption(key)
        else:
            raise ValueError("Unsupported encryption mechanism: %s" % mechanism)


def xor(data, key):
    key = int(key)
    return ''.join([chr(ord(c) ^ key) for c in data])


class XOREncryption(Encryption):

    def __init__(self, key):
        super(XOREncryption, self).__init__("xor", key)

    def pack(self, data):
        return xor(data, self.encryption_key)

    def unpack(self, packed_data):
        return xor(packed_data, self.encryption_key)


class PasswordProtectedZipEncryption(Encryption):

    def __init__(self, key):
        super(PasswordProtectedZipEncryption, self).__init__("PasswordProtected", key)

    # `pack` is not implemented

    def unpack(self, packed_data):
        from zipfile import ZipFile
        from StringIO import StringIO

        buf = StringIO(packed_data)
        with ZipFile(buf, 'r') as myzip:
            # Assume there is only one member in the archive, and that it
            # contains the artifact data. Ignore the name.
            filename = myzip.namelist()[0]
            data = myzip.read(filename, self.encryption_key)

        return data


class Encoding(Packaging):
    """
    An encoding packaging layer.

    Currently only base64 with a standard alphabet is supported.
    """

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        # Defaults to "Base64" algorithm
        obj = artifact_binding.EncodingType()

        return obj

    def to_dict(self):
        dict_ = {}
        dict_['packaging_type'] = 'encoding'
        dict_['algorithm'] = 'Base64'

        return dict_

    @staticmethod
    def from_obj(encoding_obj):
        if encoding_obj:
            return Base64Encoding()

    @staticmethod
    def from_dict(encoding_dict):
        if encoding_dict:
            return Base64Encoding()


class Base64Encoding(Encoding):

    def pack(self, data):
        return base64.b64encode(data)

    def unpack(self, packed_data):
        return base64.b64decode(packed_data)
