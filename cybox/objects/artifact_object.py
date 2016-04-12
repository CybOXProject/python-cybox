# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import base64
import bz2
import zlib

from mixbox import entities
from mixbox import fields
from mixbox.vendor import six
from mixbox.compat import xor

import cybox.bindings.artifact_object as artifact_binding
from cybox.common import ObjectProperties, String, HashList


def validate_artifact_type(instance, value):
    if value is None:
        return
    elif value in Artifact.TYPES:
        return
    else:
        err = "Type must be one of %s. Received '%s'." % (Artifact.TYPES, value)
        raise ValueError(err)


class RawArtifact(String):
    _binding_class = artifact_binding.RawArtifactType
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'

    byte_order = fields.TypedField("byte_order")


class Packaging(entities.Entity):
    """An individual packaging layer."""
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.PackagingType

    def pack(self, data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()

    def unpack(self, packed_data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()


class Artifact(ObjectProperties):
    # Warning: Do not attempt to get or set Raw_Artifact directly. Use `data`
    # or `packed_data` respectively. Raw_Artifact will be set on export.
    _binding = artifact_binding
    _binding_class = _binding.ArtifactObjectType
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _XSI_NS = "ArtifactObj"
    _XSI_TYPE = "ArtifactObjectType"

    TYPE_FILE = "File"
    TYPE_MEMORY = "Memory Region"
    TYPE_FILE_SYSTEM = "File System Fragment"
    TYPE_NETWORK = "Network Traffic"
    TYPE_GENERIC = "Generic Data Region"
    TYPES = (TYPE_FILE, TYPE_FILE_SYSTEM, TYPE_GENERIC, TYPE_MEMORY, TYPE_NETWORK)

    hashes = fields.TypedField("Hashes", HashList)
    # packaging = fields.TypedField("Packaging", Packaging, multiple=True)  # TODO: Support this as a TypedField
    type_ =  fields.TypedField("type_", key_name="type", preset_hook=validate_artifact_type)
    content_type = fields.TypedField("content_type")
    content_type_version = fields.TypedField("content_type_version")
    suspected_malicious = fields.TypedField("suspected_malicious")

    def __init__(self, data=None, type_=None):
        super(Artifact, self).__init__()
        self.type_ = type_
        self.packaging = []

        # `data` is the actual binary data that is being encoded in this
        # Artifact. It should use the `str` type on Python 2 or the `bytes`
        # type on Python 3.

        # `packed_data` is the literal character data that comes from (or
        # becomes) the contents of the Raw_Artifact element. It should be a
        # Unicode string (`unicode` on Python 2, `str` on Python 3), and should
        # in general be ASCII-encoded, since any other data should be
        # Base64-encoded.

        # Only one of these two attributes can be set directly. The other can
        # be calculated based on the various `Packaging` types added to this
        # Artifact.

        # We set the private attribute `_packed_data` first, so that the setter
        # for `data` has access to this attribute.
        self._packed_data = None
        self.data = data

    @property
    def data(self):
        """Should return a byte string"""
        if self._data:
            return self._data
        elif self._packed_data:
            tmp_data = self._packed_data.encode('ascii')
            for p in reversed(self.packaging):
                tmp_data = p.unpack(tmp_data)
            return tmp_data
        else:
            return None

    @data.setter
    def data(self, value):
        if self._packed_data:
            raise ValueError("packed_data already set, can't set data")
        if value is not None and not isinstance(value, six.binary_type):
            msg = ("Artifact data must be either None or byte data, not a "
                   "Unicode string.")
            raise ValueError(msg)
        self._data = value

    @property
    def packed_data(self):
        """Should return a Unicode string"""
        if self._packed_data:
            return self._packed_data
        elif self._data:
            tmp_data = self._data
            for p in self.packaging:
                tmp_data = p.pack(tmp_data)
            return tmp_data.decode('ascii')
        else:
            return None

    @packed_data.setter
    def packed_data(self, value):
        if self._data:
            raise ValueError("data already set, can't set packed_data")
        if value is not None and not isinstance(value, six.text_type):
            msg = ("Artifact packed_data must be either None or a Unicode "
                   "string, not byte data.")
            raise ValueError(msg)
        self._packed_data = value

    def to_obj(self, ns_info=None):
        artifact_obj = super(Artifact, self).to_obj(ns_info=ns_info)

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

        return artifact_obj

    def to_dict(self):
        artifact_dict = super(Artifact, self).to_dict()

        if self.packaging:
            artifact_dict['packaging'] = [p.to_dict() for p in self.packaging]
        if self.packed_data:
            artifact_dict['raw_artifact'] = RawArtifact(self.packed_data).to_dict()

        return artifact_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        artifact = super(Artifact, cls).from_obj(cls_obj)
        
        packaging = cls_obj.Packaging
        if packaging:
            for c in packaging.Compression:
                artifact.packaging.append(CompressionFactory.from_obj(c))
            for e in packaging.Encryption:
                artifact.packaging.append(EncryptionFactory.from_obj(e))
            for e in packaging.Encoding:
                artifact.packaging.append(EncodingFactory.from_obj(e))

        raw_artifact = cls_obj.Raw_Artifact
        if raw_artifact:
            data = RawArtifact.from_obj(raw_artifact).value
            artifact.packed_data = six.text_type(data)

        return artifact

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        artifact = super(Artifact, cls).from_dict(cls_dict)
       
        for layer in cls_dict.get('packaging', []):
            if layer.get('packaging_type') == "compression":
                artifact.packaging.append(CompressionFactory.from_dict(layer))
            if layer.get('packaging_type') == "encryption":
                artifact.packaging.append(EncryptionFactory.from_dict(layer))
            if layer.get('packaging_type') == "encoding":
                artifact.packaging.append(EncodingFactory.from_dict(layer))

        raw_artifact = cls_dict.get('raw_artifact')
        if raw_artifact:
            data = RawArtifact.from_dict(raw_artifact).value
            artifact.packed_data = six.text_type(data)

        return artifact


class Compression(Packaging):
    """A Compression packaging layer

    Currently only zlib and bz2 are supported.
    Also, compression_mechanism_ref is not currently supported.
    """
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.CompressionType

    compression_mechanism = fields.TypedField("compression_mechanism")
    compression_mechanism_ref = fields.TypedField("compression_mechanism_ref")

    def __init__(self, compression_mechanism=None):
        super(Compression, self).__init__()
        self.compression_mechanism = compression_mechanism

    def to_dict(self):
        dict_ = super(Compression, self).to_dict()
        dict_['packaging_type'] = 'compression'
        return dict_


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
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.EncryptionType

    encryption_mechanism = fields.TypedField("encryption_mechanism")
    encryption_mechanism_ref = fields.TypedField("encryption_mechanism_ref")
    encryption_key = fields.TypedField("encryption_key")
    encryption_key_ref = fields.TypedField("encryption_key_ref")

    def __init__(self, encryption_mechanism=None, encryption_key=None):
        super(Encryption, self).__init__()
        self.encryption_mechanism = encryption_mechanism
        self.encryption_key = encryption_key

    def to_dict(self):
        dict_ = super(Encryption, self).to_dict()
        dict_['packaging_type'] = 'encryption'
        return dict_


class XOREncryption(Encryption):

    def __init__(self, key=None):
        super(XOREncryption, self).__init__("xor", key)

    def pack(self, data):
        return xor(data, self.encryption_key)

    def unpack(self, packed_data):
        return xor(packed_data, self.encryption_key)


class PasswordProtectedZipEncryption(Encryption):
    def __init__(self, key=None):
        super(PasswordProtectedZipEncryption, self).__init__("PasswordProtected", key)

    # `pack` is not implemented

    def unpack(self, packed_data):
        from zipfile import ZipFile

        buf = six.StringIO(packed_data)
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
    _binding = artifact_binding
    _binding_class = _binding.EncodingType

    algorithm = fields.TypedField("algorithm")

    def to_dict(self):
        dict_ = super(Encoding, self).to_dict()
        dict_['packaging_type'] = 'encoding'
        return dict_


class Base64Encoding(Encoding):

    def pack(self, data):
        return base64.b64encode(data)

    def unpack(self, packed_data):
        return base64.b64decode(packed_data)


class EncryptionFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        if key == "xor":
            return XOREncryption
        elif key == 'PasswordProtected':
            return PasswordProtectedZipEncryption
        else:
            raise ValueError("Unsupported encryption mechanism: %s" % key)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get('encryption_mechanism')

    @classmethod
    def objkey(cls, obj):
        return obj.encryption_mechanism


class CompressionFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        if key == "zlib":
            return ZlibCompression
        elif key == "bz2":
            return Bz2Compression
        else:
            raise ValueError("Unsupported compression mechanism: %s" % key)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get('compression_mechanism')

    @classmethod
    def objkey(cls, obj):
        return obj.compression_mechanism


class EncodingFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        if key == "Base64":
            return Base64Encoding
        else:
            raise ValueError("Unsupported encoding algorithm: %s" % key)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get('algorithm', "Base64")  # default is Base64

    @classmethod
    def objkey(cls, obj):
        return getattr(obj, "algorithm", "Base64")  # default is Base64
