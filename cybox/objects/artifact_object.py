# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
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


def validate_byte_order_endianness(instance, value):
    if value is None:
        return
    elif value in RawArtifact.ENDIANNESS:
        return
    else:
        err = "Type must be one of %s. Received '%s'." % (RawArtifact.ENDIANNESS, value)
        raise ValueError(err)


class RawArtifact(String):
    _binding = artifact_binding
    _binding_class = _binding.RawArtifactType
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'

    BIG_ENDIAN = "Big-endian"
    LITTLE_ENDIAN = "Little-endian"
    MIDDLE_ENDIAN = "Middle-endian"
    ENDIANNESS = (BIG_ENDIAN, LITTLE_ENDIAN, MIDDLE_ENDIAN)

    byte_order = fields.TypedField("byte_order", preset_hook=validate_byte_order_endianness)


class Compression(entities.Entity):
    """A Compression packaging layer

    Currently only zlib and bz2 are supported.
    Also, compression_mechanism_ref is not currently supported.
    """
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.CompressionType
    _COMPRESSION_TYPE = None  # overridden by subclasses

    compression_mechanism = fields.TypedField("compression_mechanism")
    compression_mechanism_ref = fields.TypedField("compression_mechanism_ref")

    def __init__(self, compression_mechanism=None, compression_mechanism_ref=None):
        super(Compression, self).__init__()
        self.compression_mechanism = compression_mechanism
        self.compression_mechanism_ref = compression_mechanism_ref

    def pack(self, data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()

    def unpack(self, packed_data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()


class Encryption(entities.Entity):
    """
    An encryption packaging layer.
    """
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.EncryptionType
    _ENCRYPTION_TYPE = None  # overridden by subclasses

    encryption_mechanism = fields.TypedField("encryption_mechanism")
    encryption_mechanism_ref = fields.TypedField("encryption_mechanism_ref")
    encryption_key = fields.TypedField("encryption_key")
    encryption_key_ref = fields.TypedField("encryption_key_ref")

    def __init__(self, encryption_mechanism=None, encryption_key=None,
                 encryption_mechanism_ref=None, encryption_key_ref=None):
        super(Encryption, self).__init__()
        self.encryption_mechanism = encryption_mechanism
        self.encryption_key = encryption_key
        self.encryption_mechanism_ref = encryption_mechanism_ref
        self.encryption_key_ref = encryption_key_ref

    def pack(self, data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()

    def unpack(self, packed_data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()


class Encoding(entities.Entity):
    """
    An encoding packaging layer.

    Currently only base64 with a standard alphabet is supported.
    """
    _binding = artifact_binding
    _binding_class = _binding.EncodingType
    _ENCODING_TYPE = None  # overridden by subclasses

    algorithm = fields.TypedField("algorithm")
    character_set = fields.TypedField("character_set")
    custom_character_set_ref = fields.TypedField("custom_character_set_ref")

    def __init__(self, algorithm=None, character_set=None, custom_character_set_ref=None):
        super(Encoding, self).__init__()
        self.algorithm = algorithm
        self.character_set = character_set
        self.custom_character_set_ref = custom_character_set_ref

    def pack(self, data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()

    def unpack(self, packed_data):
        """This should accept byte data and return byte data"""
        raise NotImplementedError()


class EncryptionFactory(entities.EntityFactory):
    _ENCRYPTION_EXT_MAP = {}

    @classmethod
    def entity_class(cls, key):
        return cls._ENCRYPTION_EXT_MAP.get(key, Encryption)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get("encryption_mechanism")

    @classmethod
    def objkey(cls, obj):
        return obj.encryption_mechanism

    @classmethod
    def register_extension(cls, new_cls):
        cls._ENCRYPTION_EXT_MAP[new_cls._ENCRYPTION_TYPE] = new_cls
        return new_cls


class CompressionFactory(entities.EntityFactory):
    _COMPRESSION_EXT_MAP = {}

    @classmethod
    def entity_class(cls, key):
        return cls._COMPRESSION_EXT_MAP.get(key, Compression)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get("compression_mechanism")

    @classmethod
    def objkey(cls, obj):
        return obj.compression_mechanism

    @classmethod
    def register_extension(cls, new_cls):
        cls._COMPRESSION_EXT_MAP[new_cls._COMPRESSION_TYPE] = new_cls
        return new_cls


class EncodingFactory(entities.EntityFactory):
    _ENCODING_EXT_MAP = {}

    @classmethod
    def entity_class(cls, key):
        return cls._ENCODING_EXT_MAP.get(key, Encoding)

    @classmethod
    def dictkey(cls, mapping):
        return mapping.get("algorithm", "Base64")  # default is Base64

    @classmethod
    def objkey(cls, obj):
        return getattr(obj, "algorithm", "Base64")  # default is Base64

    @classmethod
    def register_extension(cls, new_cls):
        cls._ENCODING_EXT_MAP[new_cls._ENCODING_TYPE] = new_cls
        return new_cls


@CompressionFactory.register_extension
class ZlibCompression(Compression):
    _COMPRESSION_TYPE = "zlib"

    def __init__(self):
        super(ZlibCompression, self).__init__(compression_mechanism="zlib")

    def pack(self, data):
        return zlib.compress(data)

    def unpack(self, packed_data):
        return zlib.decompress(packed_data)


@CompressionFactory.register_extension
class Bz2Compression(Compression):
    _COMPRESSION_TYPE = "bz2"

    def __init__(self):
        super(Bz2Compression, self).__init__(compression_mechanism="bz2")

    def pack(self, data):
        return bz2.compress(data)

    def unpack(self, packed_data):
        return bz2.decompress(packed_data)


@EncryptionFactory.register_extension
class XOREncryption(Encryption):
    _ENCRYPTION_TYPE = "xor"

    def __init__(self, key=None):
        super(XOREncryption, self).__init__(
            encryption_mechanism="xor",
            encryption_key=key
        )

    def pack(self, data):
        return xor(data, self.encryption_key)

    def unpack(self, packed_data):
        return xor(packed_data, self.encryption_key)


@EncryptionFactory.register_extension
class PasswordProtectedZipEncryption(Encryption):
    _ENCRYPTION_TYPE = "PasswordProtected"

    def __init__(self, key=None):
        super(PasswordProtectedZipEncryption, self).__init__(
            encryption_mechanism="PasswordProtected",
            encryption_key=key
        )

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


@EncodingFactory.register_extension
class Base64Encoding(Encoding):
    _ENCODING_TYPE = "Base64"

    def __init__(self):
        super(Base64Encoding, self).__init__(algorithm="Base64")

    def pack(self, data):
        return base64.b64encode(data)

    def unpack(self, packed_data):
        return base64.b64decode(packed_data)


class Packaging(entities.Entity):
    """An individual packaging layer."""
    _namespace = 'http://cybox.mitre.org/objects#ArtifactObject-2'
    _binding = artifact_binding
    _binding_class = _binding.PackagingType

    is_encrypted = fields.BooleanField("is_encrypted")
    is_compressed = fields.BooleanField("is_compressed")
    compression = fields.TypedField("Compression", Compression, factory=CompressionFactory, multiple=True)
    encryption = fields.TypedField("Encryption", Encryption, factory=EncryptionFactory, multiple=True)
    encoding = fields.TypedField("Encoding", Encoding, factory=EncodingFactory, multiple=True)

    def __init__(self, is_encrypted=None, is_compressed=None, compression=None, encryption=None, encoding=None):
        super(Packaging, self).__init__()
        self.is_encrypted = is_encrypted
        self.is_compressed = is_compressed
        self.compression = compression
        self.encryption = encryption
        self.encoding = encoding


class Artifact(ObjectProperties):
    # Warning: Do not attempt to get or set Raw_Artifact directly. Use `data`
    # or `packed_data` respectively. The Raw_Artifact value will be set on
    # export. You can set BaseObjectProperties or PatternFieldGroup attributes.
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
    packaging = fields.TypedField("Packaging", Packaging)
    type_ = fields.TypedField("type_", key_name="type", preset_hook=validate_artifact_type)
    content_type = fields.TypedField("content_type")
    content_type_version = fields.TypedField("content_type_version")
    suspected_malicious = fields.TypedField("suspected_malicious")
    # TODO: xs:choice
    raw_artifact = fields.TypedField("Raw_Artifact", RawArtifact)
    raw_artifact_reference = fields.TypedField("Raw_Artifact_Reference")

    def __init__(self, data=None, type_=None):
        super(Artifact, self).__init__()
        self.type_ = type_

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
            if self.packaging:
                for p in reversed(self.packaging.encoding):
                    tmp_data = p.unpack(tmp_data)
                for p in reversed(self.packaging.encryption):
                    tmp_data = p.unpack(tmp_data)
                for p in reversed(self.packaging.compression):
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
            if self.packaging:
                for p in self.packaging.compression:
                    tmp_data = p.pack(tmp_data)
                for p in self.packaging.encryption:
                    tmp_data = p.pack(tmp_data)
                for p in self.packaging.encoding:
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

        if self.packed_data:
            if not self.raw_artifact:
                self.raw_artifact = RawArtifact()
            self.raw_artifact.value = self.packed_data
            artifact_obj.Raw_Artifact = self.raw_artifact.to_obj(ns_info=ns_info)

        return artifact_obj

    def to_dict(self):
        artifact_dict = super(Artifact, self).to_dict()

        if self.packed_data:
            if not self.raw_artifact:
                self.raw_artifact = RawArtifact()
            self.raw_artifact.value = self.packed_data
            artifact_dict['raw_artifact'] = self.raw_artifact.to_dict()

        return artifact_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        artifact = super(Artifact, cls).from_obj(cls_obj)

        raw_artifact = cls_obj.Raw_Artifact
        if raw_artifact:
            artifact.raw_artifact = RawArtifact.from_obj(raw_artifact)
            artifact.packed_data = six.text_type(artifact.raw_artifact.value)

        return artifact

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        artifact = super(Artifact, cls).from_dict(cls_dict)

        raw_artifact = cls_dict.get('raw_artifact')
        if raw_artifact:
            artifact.raw_artifact = RawArtifact.from_dict(raw_artifact)
            artifact.packed_data = six.text_type(artifact.raw_artifact.value)

        return artifact
