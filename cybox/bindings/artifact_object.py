# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class RawArtifactType(cybox_common.StringObjectPropertyType):
    """The RawArtifactType is intended to convey, with minimal
    characterization, the content of the Raw Artifact itself."""

    subclass = None
    superclass = None
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, byte_order=None, valueOf_=None):
        super(RawArtifactType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.byte_order = byte_order
    def factory(*args_, **kwargs_):
        if RawArtifactType.subclass:
            return RawArtifactType.subclass(*args_, **kwargs_)
        else:
            return RawArtifactType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_byte_order(self): return self.byte_order
    def set_byte_order(self, byte_order): self.byte_order = byte_order
    def hasContent_(self):
        if (
            super(RawArtifactType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='RawArtifactType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RawArtifactType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='RawArtifactType'):
        super(RawArtifactType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RawArtifactType')
        if self.byte_order is not None:

            lwrite(' byte_order=%s' % (quote_attrib(self.byte_order), ))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='RawArtifactType', fromsubclass_=False, pretty_print=True):
        super(RawArtifactType, self).exportChildren(lwrite, level, 'ArtifactObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('byte_order', node)
        if value is not None:

            self.byte_order = value
        super(RawArtifactType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RawArtifactType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RawArtifactType

class PackagingType(GeneratedsSuper):
    """The PackagingType captures any packaging layers applied to an
    artifact.The is_encrypted field is optional and specifies
    whether the Raw_Artifact content is protected/encrypted.The
    is_compressed field is optional and specifies whether the
    Raw_Artifact content is compressed."""

    subclass = None
    superclass = None
    def __init__(self, is_compressed=None, is_encrypted=None, Compression=None, Encryption=None, Encoding=None):
        self.is_compressed = _cast(bool, is_compressed)
        self.is_encrypted = _cast(bool, is_encrypted)
        if Compression is None:
            self.Compression = []
        else:
            self.Compression = Compression
        if Encryption is None:
            self.Encryption = []
        else:
            self.Encryption = Encryption
        if Encoding is None:
            self.Encoding = []
        else:
            self.Encoding = Encoding
    def factory(*args_, **kwargs_):
        if PackagingType.subclass:
            return PackagingType.subclass(*args_, **kwargs_)
        else:
            return PackagingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Compression(self): return self.Compression
    def set_Compression(self, Compression): self.Compression = Compression
    def add_Compression(self, value): self.Compression.append(value)
    def insert_Compression(self, index, value): self.Compression[index] = value
    def get_Encryption(self): return self.Encryption
    def set_Encryption(self, Encryption): self.Encryption = Encryption
    def add_Encryption(self, value): self.Encryption.append(value)
    def insert_Encryption(self, index, value): self.Encryption[index] = value
    def get_Encoding(self): return self.Encoding
    def set_Encoding(self, Encoding): self.Encoding = Encoding
    def add_Encoding(self, value): self.Encoding.append(value)
    def insert_Encoding(self, index, value): self.Encoding[index] = value
    def get_is_compressed(self): return self.is_compressed
    def set_is_compressed(self, is_compressed): self.is_compressed = is_compressed
    def get_is_encrypted(self): return self.is_encrypted
    def set_is_encrypted(self, is_encrypted): self.is_encrypted = is_encrypted
    def hasContent_(self):
        if (
            self.Compression or
            self.Encryption or
            self.Encoding
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='PackagingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PackagingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='PackagingType'):
        if self.is_compressed is not None:

            lwrite(' is_compressed="%s"' % self.gds_format_boolean(self.is_compressed, input_name='is_compressed'))
        if self.is_encrypted is not None:

            lwrite(' is_encrypted="%s"' % self.gds_format_boolean(self.is_encrypted, input_name='is_encrypted'))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='PackagingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Compression_ in self.Compression:
            Compression_.export(lwrite, level, 'ArtifactObj:', name_='Compression', pretty_print=pretty_print)
        for Encryption_ in self.Encryption:
            Encryption_.export(lwrite, level, 'ArtifactObj:', name_='Encryption', pretty_print=pretty_print)
        for Encoding_ in self.Encoding:
            Encoding_.export(lwrite, level, 'ArtifactObj:', name_='Encoding', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_compressed', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_compressed = True
            elif value in ('false', '0'):
                self.is_compressed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_encrypted', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_encrypted = True
            elif value in ('false', '0'):
                self.is_encrypted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Compression':
            obj_ = CompressionType.factory()
            obj_.build(child_)
            self.Compression.append(obj_)
        elif nodeName_ == 'Encryption':
            obj_ = EncryptionType.factory()
            obj_.build(child_)
            self.Encryption.append(obj_)
        elif nodeName_ == 'Encoding':
            obj_ = EncodingType.factory()
            obj_.build(child_)
            self.Encoding.append(obj_)
# end class PackagingType

class CompressionType(GeneratedsSuper):
    """The CompressionType captures any compression packaging details for
    an artifact.The compression_mechanism field is optional and
    specifies the compression algorithm utilized to protect the
    Raw_Artifact content.The compression_mechanism_ref field is
    optional and conveys a reference to a description of the
    compression algorithm utilized to protect the Raw_Artifact
    content."""

    subclass = None
    superclass = None
    def __init__(self, compression_mechanism=None, compression_mechanism_ref=None):
        self.compression_mechanism = _cast(None, compression_mechanism)
        self.compression_mechanism_ref = _cast(None, compression_mechanism_ref)
        pass
    def factory(*args_, **kwargs_):
        if CompressionType.subclass:
            return CompressionType.subclass(*args_, **kwargs_)
        else:
            return CompressionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_compression_mechanism(self): return self.compression_mechanism
    def set_compression_mechanism(self, compression_mechanism): self.compression_mechanism = compression_mechanism
    def get_compression_mechanism_ref(self): return self.compression_mechanism_ref
    def set_compression_mechanism_ref(self, compression_mechanism_ref): self.compression_mechanism_ref = compression_mechanism_ref
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='CompressionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompressionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='CompressionType'):
        if self.compression_mechanism is not None:

            lwrite(' compression_mechanism=%s' % (self.gds_format_string(quote_attrib(self.compression_mechanism), input_name='compression_mechanism'), ))
        if self.compression_mechanism_ref is not None:

            lwrite(' compression_mechanism_ref=%s' % (self.gds_format_string(quote_attrib(self.compression_mechanism_ref), input_name='compression_mechanism_ref'), ))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='CompressionType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('compression_mechanism', node)
        if value is not None:

            self.compression_mechanism = value
        value = find_attr_value_('compression_mechanism_ref', node)
        if value is not None:

            self.compression_mechanism_ref = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CompressionType

class EncryptionType(GeneratedsSuper):
    """The EncryptionType captures any encryption packaging details for an
    artifact.The encryption_mechanism field is optional and
    specifies the protection/encryption algorithm utilized to
    protect the Raw_Artifact content.The encryption_mechanism_ref
    field is optional and conveys a reference to a description of
    the protection/encryption algorithm utilized to protect the
    Raw_Artifact content.The encryption_key field is optional and
    locally specifies the password for unprotecting/decrypting the
    Raw_Artifact content. The encryption_key_ref field is optional
    and specifies a reference to a remote specification of the
    password for unprotecting/decrypting the Raw_Artifact content."""

    subclass = None
    superclass = None
    def __init__(self, encryption_mechanism=None, encryption_key_ref=None, encryption_key=None, encryption_mechanism_ref=None):
        self.encryption_mechanism = _cast(None, encryption_mechanism)
        self.encryption_key_ref = _cast(None, encryption_key_ref)
        self.encryption_key = _cast(None, encryption_key)
        self.encryption_mechanism_ref = _cast(None, encryption_mechanism_ref)
        pass
    def factory(*args_, **kwargs_):
        if EncryptionType.subclass:
            return EncryptionType.subclass(*args_, **kwargs_)
        else:
            return EncryptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_encryption_mechanism(self): return self.encryption_mechanism
    def set_encryption_mechanism(self, encryption_mechanism): self.encryption_mechanism = encryption_mechanism
    def get_encryption_key_ref(self): return self.encryption_key_ref
    def set_encryption_key_ref(self, encryption_key_ref): self.encryption_key_ref = encryption_key_ref
    def get_encryption_key(self): return self.encryption_key
    def set_encryption_key(self, encryption_key): self.encryption_key = encryption_key
    def get_encryption_mechanism_ref(self): return self.encryption_mechanism_ref
    def set_encryption_mechanism_ref(self, encryption_mechanism_ref): self.encryption_mechanism_ref = encryption_mechanism_ref
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='EncryptionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EncryptionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='EncryptionType'):
        if self.encryption_mechanism is not None:

            lwrite(' encryption_mechanism=%s' % (self.gds_format_string(quote_attrib(self.encryption_mechanism), input_name='encryption_mechanism'), ))
        if self.encryption_key_ref is not None:

            lwrite(' encryption_key_ref=%s' % (self.gds_format_string(quote_attrib(self.encryption_key_ref), input_name='encryption_key_ref'), ))
        if self.encryption_key is not None:

            lwrite(' encryption_key=%s' % (self.gds_format_string(quote_attrib(self.encryption_key), input_name='encryption_key'), ))
        if self.encryption_mechanism_ref is not None:

            lwrite(' encryption_mechanism_ref=%s' % (self.gds_format_string(quote_attrib(self.encryption_mechanism_ref), input_name='encryption_mechanism_ref'), ))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='EncryptionType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('encryption_mechanism', node)
        if value is not None:

            self.encryption_mechanism = value
        value = find_attr_value_('encryption_key_ref', node)
        if value is not None:

            self.encryption_key_ref = value
        value = find_attr_value_('encryption_key', node)
        if value is not None:

            self.encryption_key = value
        value = find_attr_value_('encryption_mechanism_ref', node)
        if value is not None:

            self.encryption_mechanism_ref = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class EncryptionType

class EncodingType(GeneratedsSuper):
    """The EncodingType captures any encoding packaging details for an
    artifact.The algorithm field is optional and specifies the
    encoding algorithm utilized to encode the Raw_Artifact.The
    character_set field is optional and specifies the character set
    utilized in the Raw_Artifact content encoding.The
    custom_character_set_ref field is optional and conveys a
    reference to a specification of the custom character set used to
    encode the Raw_Artifact."""

    subclass = None
    superclass = None
    def __init__(self, custom_character_set_ref=None, character_set=None, algorithm='Base64'):
        self.custom_character_set_ref = _cast(None, custom_character_set_ref)
        self.character_set = _cast(None, character_set)
        self.algorithm = _cast(None, algorithm)
        pass
    def factory(*args_, **kwargs_):
        if EncodingType.subclass:
            return EncodingType.subclass(*args_, **kwargs_)
        else:
            return EncodingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_custom_character_set_ref(self): return self.custom_character_set_ref
    def set_custom_character_set_ref(self, custom_character_set_ref): self.custom_character_set_ref = custom_character_set_ref
    def get_character_set(self): return self.character_set
    def set_character_set(self, character_set): self.character_set = character_set
    def get_algorithm(self): return self.algorithm
    def set_algorithm(self, algorithm): self.algorithm = algorithm
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='EncodingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EncodingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='EncodingType'):
        if self.custom_character_set_ref is not None:

            lwrite(' custom_character_set_ref=%s' % (self.gds_format_string(quote_attrib(self.custom_character_set_ref), input_name='custom_character_set_ref'), ))
        if self.character_set is not None:

            lwrite(' character_set=%s' % (self.gds_format_string(quote_attrib(self.character_set), input_name='character_set'), ))
        if self.algorithm is not None:

            lwrite(' algorithm=%s' % (self.gds_format_string(quote_attrib(self.algorithm), input_name='algorithm'), ))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='EncodingType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('custom_character_set_ref', node)
        if value is not None:

            self.custom_character_set_ref = value
        value = find_attr_value_('character_set', node)
        if value is not None:

            self.character_set = value
        value = find_attr_value_('algorithm', node)
        if value is not None:

            self.algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class EncodingType

class ArtifactObjectType(cybox_common.ObjectPropertiesType):
    """The ArtifactObjectType type is intended to encapsulate and convey
    the content of a Raw Artifact.The type field specifies the
    general type of the artifact contained in this Defined
    Object.The content_type field is optional and specifies the
    Internet Media Type of the artifact contained in this Defined
    Object.The content_type_version field is optional and specifies
    the content type version of the artifact contained in this
    Defined Object.The suspected_malicious field is optional and
    conveys whether the content of the Raw_Artifact is believed to
    be malicoius."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, suspected_malicious=None, content_type_version=None, type_=None, content_type=None, Hashes=None, Packaging=None, Raw_Artifact=None, Raw_Artifact_Reference=None):
        super(ArtifactObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.suspected_malicious = _cast(bool, suspected_malicious)
        self.content_type_version = _cast(None, content_type_version)
        self.type_ = _cast(None, type_)
        self.content_type = _cast(None, content_type)
        self.Hashes = Hashes
        self.Packaging = Packaging
        self.Raw_Artifact = Raw_Artifact
        self.Raw_Artifact_Reference = Raw_Artifact_Reference
    def factory(*args_, **kwargs_):
        if ArtifactObjectType.subclass:
            return ArtifactObjectType.subclass(*args_, **kwargs_)
        else:
            return ArtifactObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Packaging(self): return self.Packaging
    def set_Packaging(self, Packaging): self.Packaging = Packaging
    def get_Raw_Artifact(self): return self.Raw_Artifact
    def set_Raw_Artifact(self, Raw_Artifact): self.Raw_Artifact = Raw_Artifact
    def get_Raw_Artifact_Reference(self): return self.Raw_Artifact_Reference
    def set_Raw_Artifact_Reference(self, Raw_Artifact_Reference): self.Raw_Artifact_Reference = Raw_Artifact_Reference
    def get_suspected_malicious(self): return self.suspected_malicious
    def set_suspected_malicious(self, suspected_malicious): self.suspected_malicious = suspected_malicious
    def get_content_type_version(self): return self.content_type_version
    def set_content_type_version(self, content_type_version): self.content_type_version = content_type_version
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_content_type(self): return self.content_type
    def set_content_type(self, content_type): self.content_type = content_type
    def hasContent_(self):
        if (
            self.Hashes is not None or
            self.Packaging is not None or
            self.Raw_Artifact is not None or
            self.Raw_Artifact_Reference is not None or
            super(ArtifactObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArtifactObj:', name_='ArtifactObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ArtifactObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArtifactObj:', name_='ArtifactObjectType'):
        super(ArtifactObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ArtifactObjectType')
        if self.suspected_malicious is not None:

            lwrite(' suspected_malicious="%s"' % self.gds_format_boolean(self.suspected_malicious, input_name='suspected_malicious'))
        if self.content_type_version is not None:

            lwrite(' content_type_version=%s' % (self.gds_format_string(quote_attrib(self.content_type_version), input_name='content_type_version'), ))
        if self.type_ is not None:

            lwrite(' type=%s' % (quote_attrib(self.type_), ))
        if self.content_type is not None:

            lwrite(' content_type=%s' % (self.gds_format_string(quote_attrib(self.content_type), input_name='content_type'), ))
    def exportChildren(self, lwrite, level, namespace_='ArtifactObj:', name_='ArtifactObjectType', fromsubclass_=False, pretty_print=True):
        super(ArtifactObjectType, self).exportChildren(lwrite, level, 'ArtifactObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'ArtifactObj:', name_='Hashes', pretty_print=pretty_print)
        if self.Packaging is not None:
            self.Packaging.export(lwrite, level, 'ArtifactObj:', name_='Packaging', pretty_print=pretty_print)
        if self.Raw_Artifact is not None:
            if self.Raw_Artifact.get_valueOf_() is not None:
                value = self.Raw_Artifact.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Artifact.set_valueOf_(value)
            self.Raw_Artifact.export(lwrite, level, 'ArtifactObj:', name_='Raw_Artifact', pretty_print=pretty_print)
        if self.Raw_Artifact_Reference is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRaw_Artifact_Reference>%s</%sRaw_Artifact_Reference>%s' % ('ArtifactObj:', self.gds_format_string(quote_xml(self.Raw_Artifact_Reference), input_name='Raw_Artifact_Reference'), 'ArtifactObj:', eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('suspected_malicious', node)
        if value is not None:

            if value in ('true', '1'):
                self.suspected_malicious = True
            elif value in ('false', '0'):
                self.suspected_malicious = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('content_type_version', node)
        if value is not None:

            self.content_type_version = value
        value = find_attr_value_('type', node)
        if value is not None:

            self.type_ = value
        value = find_attr_value_('content_type', node)
        if value is not None:

            self.content_type = value
        super(ArtifactObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Packaging':
            obj_ = PackagingType.factory()
            obj_.build(child_)
            self.set_Packaging(obj_)
        elif nodeName_ == 'Raw_Artifact':
            obj_ = RawArtifactType.factory()
            obj_.build(child_)
            self.set_Raw_Artifact(obj_)
        elif nodeName_ == 'Raw_Artifact_Reference':
            Raw_Artifact_Reference_ = child_.text
            Raw_Artifact_Reference_ = self.gds_validate_string(Raw_Artifact_Reference_, node, 'Raw_Artifact_Reference')
            self.Raw_Artifact_Reference = Raw_Artifact_Reference_
        super(ArtifactObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class ArtifactObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Data_Size': cybox_common.DataSizeType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Artifact'
        rootClass = ArtifactObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Artifact'
        rootClass = ArtifactObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Artifact'
        rootClass = ArtifactObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Artifact",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "ArtifactObjectType",
    "RawArtifactType",
    "PackagingType",
    "CompressionType",
    "EncryptionType",
    "EncodingType"
    ]
