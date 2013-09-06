# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
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

    def to_obj(self):
        artifact_obj = artifact_binding.ArtifactObjectType()
        super(Artifact, self).to_obj(artifact_obj)

        if self.packaging:
            packaging = artifact_binding.PackagingType()
            for p in self.packaging:
                p_obj = p.to_obj()
                if isinstance(p, Compression):
                    packaging.add_Compression(p_obj)
                elif isinstance(p, Encryption):
                    packaging.add_Encryption(p_obj)
                elif isinstance(p, Encoding):
                    packaging.add_Encoding(p_obj)
                else:
                    raise ValueError("Unsupported Packaging Type: %s" %
                                        type(p))
            artifact_obj.set_Packaging(packaging)

        if self.packed_data:
            artifact_obj.set_Raw_Artifact(RawArtifact(self.packed_data).to_obj())

        return artifact_obj

    def to_dict(self):
        artifact_dict = {}
        super(Artifact, self).to_dict(artifact_dict)

        if self.packaging:
            artifact_dict['packaging'] = [p.to_dict() for p in self.packaging]
        if self.packed_data:
            artifact_dict['raw_artifact'] = RawArtifact(self.packed_data).to_dict()

        return artifact_dict

    @staticmethod
    def from_obj(artifact_obj):
        if not artifact_obj:
            return None

        artifact = Artifact()
        ObjectProperties.from_obj(artifact_obj, artifact)

        packaging = artifact_obj.get_Packaging()
        if packaging:
            for c in packaging.get_Compression():
                artifact.packaging.append(Compression.from_obj(c))
            for e in packaging.get_Encryption():
                artifact.packaging.append(Encryption.from_obj(e))
            for e in packaging.get_Encoding():
                artifact.packaging.append(Encoding.from_obj(e))

        raw_artifact = artifact_obj.get_Raw_Artifact()
        if raw_artifact:
            artifact.packed_data = RawArtifact.from_obj(raw_artifact).value

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

    def to_obj(self):
        obj = artifact_binding.CompressionType()
        if self.compression_mechanism:
            obj.set_compression_mechanism(self.compression_mechanism)

        return obj

    def to_dict(self):
        dict_ = {}
        dict_['packaging_type'] = 'compression'
        if self.compression_mechanism:
            dict_['compression_mechanism'] = self.compression_mechanism

        return dict_

    @staticmethod
    def from_obj(compression_obj):
        mechanism = compression_obj.get_compression_mechanism()
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
    pass


class Encoding(Packaging):
    """
    An encoding packaging layer.

    Currently only base64 with a standard alphabet is supported.
    Also, compression_mechanism_ref is not currently supported.
    """

    def to_obj(self):
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
