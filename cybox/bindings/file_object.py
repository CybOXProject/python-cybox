# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class FilePathType(cybox_common.StringObjectPropertyType):
    """The FilePathType type specifies the path to the file, not including
    the device. Whether the path is relative or fully-qualified can
    be specified via the 'fully_qualified' attribute.The
    fully_qualified field specifies whether the path is fully
    qualified."""

    subclass = None
    superclass = None
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, fully_qualified=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(FilePathType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.fully_qualified = _cast(bool, fully_qualified)
    def factory(*args_, **kwargs_):
        if FilePathType.subclass:
            return FilePathType.subclass(*args_, **kwargs_)
        else:
            return FilePathType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_fully_qualified(self): return self.fully_qualified
    def set_fully_qualified(self, fully_qualified): self.fully_qualified = fully_qualified
    def hasContent_(self):
        if (
            super(FilePathType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='FilePathType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FilePathType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='FilePathType'):
        super(FilePathType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='FilePathType')
        if self.fully_qualified is not None:

            lwrite(' fully_qualified="%s"' % self.gds_format_boolean(self.fully_qualified, input_name='fully_qualified'))
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='FilePathType', fromsubclass_=False, pretty_print=True):
        super(FilePathType, self).exportChildren(lwrite, level, 'FileObj:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('fully_qualified', node)
        if value is not None:

            if value in ('true', '1'):
                self.fully_qualified = True
            elif value in ('false', '0'):
                self.fully_qualified = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(FilePathType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(FilePathType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class FilePathType

class FileAttributeType(GeneratedsSuper):
    """The FileAttributeType type specifies attribute(s) of a file. Since
    this Object property(ies) is platform-specific, it is defined
    here as an abstract type."""

    subclass = None
    superclass = None
    def __init__(self, xsi_type = None):
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if FileAttributeType.subclass:
            return FileAttributeType.subclass(*args_, **kwargs_)
        else:
            return FileAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='FileAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FileAttributeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='FileAttributeType'):
        lwrite(' xsi:type="%s%s"' % (namespace_, name_))
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='FileAttributeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.xsi_type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class FileAttributeType

class FilePermissionsType(GeneratedsSuper):
    """The FilePermissionsType type specifies a permission of a file. Since
    this is a platform-specific Object property, it is defined here
    as an abstract type and then implemented in any platform
    specific derived file objects."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if FilePermissionsType.subclass:
            return FilePermissionsType.subclass(*args_, **kwargs_)
        else:
            return FilePermissionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='FilePermissionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FilePermissionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='FilePermissionsType'):
        lwrite(' xsi:type="%s%s"' % (namespace_, name_))
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='FilePermissionsType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class FilePermissionsType

class PackerListType(GeneratedsSuper):
    """The PackerListType type specifies a list of file packers."""

    subclass = None
    superclass = None
    def __init__(self, Packer=None):
        if Packer is None:
            self.Packer = []
        else:
            self.Packer = Packer
    def factory(*args_, **kwargs_):
        if PackerListType.subclass:
            return PackerListType.subclass(*args_, **kwargs_)
        else:
            return PackerListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Packer(self): return self.Packer
    def set_Packer(self, Packer): self.Packer = Packer
    def add_Packer(self, value): self.Packer.append(value)
    def insert_Packer(self, index, value): self.Packer[index] = value
    def hasContent_(self):
        if (
            self.Packer
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='PackerListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PackerListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='PackerListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='PackerListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Packer_ in self.Packer:
            Packer_.export(lwrite, level, 'FileObj:', name_='Packer', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Packer':
            obj_ = PackerType.factory()
            obj_.build(child_)
            self.Packer.append(obj_)
# end class PackerListType

class PackerType(GeneratedsSuper):
    """The PackerType specifies the fields that characterize a particular
    file packer, such as name and version."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Version=None, Entry_Point=None, Signature=None, Type=None, Detected_Entrypoint_Signatures=None, EP_Jump_Codes=None):
        self.Name = Name
        self.Version = Version
        self.Entry_Point = Entry_Point
        self.Signature = Signature
        self.Type = Type
        self.Detected_Entrypoint_Signatures = Detected_Entrypoint_Signatures
        self.EP_Jump_Codes = EP_Jump_Codes
    def factory(*args_, **kwargs_):
        if PackerType.subclass:
            return PackerType.subclass(*args_, **kwargs_)
        else:
            return PackerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def get_Entry_Point(self): return self.Entry_Point
    def set_Entry_Point(self, Entry_Point): self.Entry_Point = Entry_Point
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Signature(self): return self.Signature
    def set_Signature(self, Signature): self.Signature = Signature
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_PackerClassType(self, value):
        # Validate type PackerClassType, a restriction on None.
        pass
    def get_Detected_Entrypoint_Signatures(self): return self.Detected_Entrypoint_Signatures
    def set_Detected_Entrypoint_Signatures(self, Detected_Entrypoint_Signatures): self.Detected_Entrypoint_Signatures = Detected_Entrypoint_Signatures
    def get_EP_Jump_Codes(self): return self.EP_Jump_Codes
    def set_EP_Jump_Codes(self, EP_Jump_Codes): self.EP_Jump_Codes = EP_Jump_Codes
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Version is not None or
            self.Entry_Point is not None or
            self.Signature is not None or
            self.Type is not None or
            self.Detected_Entrypoint_Signatures is not None or
            self.EP_Jump_Codes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='PackerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PackerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='PackerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='PackerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'FileObj:', name_='Name', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(lwrite, level, 'FileObj:', name_='Version', pretty_print=pretty_print)
        if self.Entry_Point is not None:
            self.Entry_Point.export(lwrite, level, 'FileObj:', name_='Entry_Point', pretty_print=pretty_print)
        if self.Signature is not None:
            self.Signature.export(lwrite, level, 'FileObj:', name_='Signature', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'FileObj:', name_='Type', pretty_print=pretty_print)
        if self.Detected_Entrypoint_Signatures is not None:
            self.Detected_Entrypoint_Signatures.export(lwrite, level, 'FileObj:', name_='Detected_Entrypoint_Signatures', pretty_print=pretty_print)
        if self.EP_Jump_Codes is not None:
            self.EP_Jump_Codes.export(lwrite, level, 'FileObj:', name_='EP_Jump_Codes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Entry_Point':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Entry_Point(obj_)
        elif nodeName_ == 'Signature':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature(obj_)
        elif nodeName_ == 'Type':
            obj_ = PackerClassType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Detected_Entrypoint_Signatures':
            obj_ = EntryPointSignatureListType.factory()
            obj_.build(child_)
            self.set_Detected_Entrypoint_Signatures(obj_)
        elif nodeName_ == 'EP_Jump_Codes':
            obj_ = EPJumpCodeType.factory()
            obj_.build(child_)
            self.set_EP_Jump_Codes(obj_)
# end class PackerType

class EPJumpCodeType(GeneratedsSuper):
    """Specifies an entry-point jump code used by a packer."""

    subclass = None
    superclass = None
    def __init__(self, Depth=None, Opcodes=None):
        self.Depth = Depth
        self.Opcodes = Opcodes
    def factory(*args_, **kwargs_):
        if EPJumpCodeType.subclass:
            return EPJumpCodeType.subclass(*args_, **kwargs_)
        else:
            return EPJumpCodeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Depth(self): return self.Depth
    def set_Depth(self, Depth): self.Depth = Depth
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Opcodes(self): return self.Opcodes
    def set_Opcodes(self, Opcodes): self.Opcodes = Opcodes
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Depth is not None or
            self.Opcodes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='EPJumpCodeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EPJumpCodeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='EPJumpCodeType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='EPJumpCodeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Depth is not None:
            self.Depth.export(lwrite, level, 'FileObj:', name_='Depth', pretty_print=pretty_print)
        if self.Opcodes is not None:
            self.Opcodes.export(lwrite, level, 'FileObj:', name_='Opcodes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Depth':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Depth(obj_)
        elif nodeName_ == 'Opcodes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Opcodes(obj_)
# end class EPJumpCodeType

class EntryPointSignatureType(GeneratedsSuper):
    """Specifies an entry point signature for a packer."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
    def factory(*args_, **kwargs_):
        if EntryPointSignatureType.subclass:
            return EntryPointSignatureType.subclass(*args_, **kwargs_)
        else:
            return EntryPointSignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_DetectedTypeEnum(self, value):
        # Validate type DetectedTypeEnum, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Type is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='EntryPointSignatureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EntryPointSignatureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='EntryPointSignatureType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='EntryPointSignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'FileObj:', name_='Name', pretty_print=pretty_print)
        if self.Type is not None:
            lwrite('<%sType>%s</%sType>%s' % ('FileObj:', self.gds_format_string(quote_xml(self.Type), input_name='Type'), 'FileObj:', eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Type':
            Type = child_.text
            Type = self.gds_validate_string(Type, node, 'Type')
            self.Type = Type
# end class EntryPointSignatureType

class EntryPointSignatureListType(GeneratedsSuper):
    """Species a list of entry point signatures for a packer."""

    subclass = None
    superclass = None
    def __init__(self, Entry_Point_Signature=None):
        if Entry_Point_Signature is None:
            self.Entry_Point_Signature = []
        else:
            self.Entry_Point_Signature = Entry_Point_Signature
    def factory(*args_, **kwargs_):
        if EntryPointSignatureListType.subclass:
            return EntryPointSignatureListType.subclass(*args_, **kwargs_)
        else:
            return EntryPointSignatureListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Entry_Point_Signature(self): return self.Entry_Point_Signature
    def set_Entry_Point_Signature(self, Entry_Point_Signature): self.Entry_Point_Signature = Entry_Point_Signature
    def add_Entry_Point_Signature(self, value): self.Entry_Point_Signature.append(value)
    def insert_Entry_Point_Signature(self, index, value): self.Entry_Point_Signature[index] = value
    def hasContent_(self):
        if (
            self.Entry_Point_Signature
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='EntryPointSignatureListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EntryPointSignatureListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='EntryPointSignatureListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='EntryPointSignatureListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Entry_Point_Signature_ in self.Entry_Point_Signature:
            Entry_Point_Signature_.export(lwrite, level, 'FileObj:', name_='Entry_Point_Signature', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Entry_Point_Signature':
            obj_ = EntryPointSignatureType.factory()
            obj_.build(child_)
            self.Entry_Point_Signature.append(obj_)
# end class EntryPointSignatureListType

class SymLinksListType(GeneratedsSuper):
    """The SymLinksListType specifies a list of symbolic links."""

    subclass = None
    superclass = None
    def __init__(self, Sym_Link=None):
        if Sym_Link is None:
            self.Sym_Link = []
        else:
            self.Sym_Link = Sym_Link
    def factory(*args_, **kwargs_):
        if SymLinksListType.subclass:
            return SymLinksListType.subclass(*args_, **kwargs_)
        else:
            return SymLinksListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Sym_Link(self): return self.Sym_Link
    def set_Sym_Link(self, Sym_Link): self.Sym_Link = Sym_Link
    def add_Sym_Link(self, value): self.Sym_Link.append(value)
    def insert_Sym_Link(self, index, value): self.Sym_Link[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Sym_Link
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='SymLinksListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SymLinksListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='SymLinksListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='SymLinksListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Sym_Link_ in self.Sym_Link:
            Sym_Link_.export(lwrite, level, 'FileObj:', name_='Sym_Link', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Sym_Link':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Sym_Link.append(obj_)
# end class SymLinksListType

class PackerClassType(cybox_common.BaseObjectPropertyType):
    """PackerCassType specifies packer classes, via a union of the
    PackerTypeEnum type and the atomic xs:string type. Its base type
    is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This field is
    optional and specifies the expected type for the value of the
    specified field."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(PackerClassType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PackerClassType.subclass:
            return PackerClassType.subclass(*args_, **kwargs_)
        else:
            return PackerClassType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PackerClassType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='PackerClassType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PackerClassType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='PackerClassType'):
        super(PackerClassType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PackerClassType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='PackerClassType', fromsubclass_=False, pretty_print=True):
        super(PackerClassType, self).exportChildren(lwrite, level, 'FileObj:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(PackerClassType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PackerClassType

class FileObjectType(cybox_common.ObjectPropertiesType):
    """The File_ObjectType type is intended to characterize generic
    files.The ispacked field is used to indicate whether the file is
    packed or not."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, is_masqueraded=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Encryption_Algorithm=None, Decryption_Key=None, Compression_Method=None, Compression_Version=None, Compression_Comment=None):
        super(FileObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.is_packed = _cast(bool, is_packed)
        self.is_masqueraded = _cast(bool, is_masqueraded)
        self.File_Name = File_Name
        self.File_Path = File_Path
        self.Device_Path = Device_Path
        self.Full_Path = Full_Path
        self.File_Extension = File_Extension
        self.Size_In_Bytes = Size_In_Bytes
        self.Magic_Number = Magic_Number
        self.File_Format = File_Format
        self.Hashes = Hashes
        self.Digital_Signatures = Digital_Signatures
        self.Modified_Time = Modified_Time
        self.Accessed_Time = Accessed_Time
        self.Created_Time = Created_Time
        self.File_Attributes_List = File_Attributes_List
        self.Permissions = Permissions
        self.User_Owner = User_Owner
        self.Packer_List = Packer_List
        self.Peak_Entropy = Peak_Entropy
        self.Sym_Links = Sym_Links
        self.Byte_Runs = Byte_Runs
        self.Extracted_Features = Extracted_Features
        self.Encryption_Algorithm = Encryption_Algorithm
        self.Decryption_Key = Decryption_Key
        self.Compression_Method = Compression_Method
        self.Compression_Version = Compression_Version
        self.Compression_Comment = Compression_Comment
    def factory(*args_, **kwargs_):
        if FileObjectType.subclass:
            return FileObjectType.subclass(*args_, **kwargs_)
        else:
            return FileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File_Name(self): return self.File_Name
    def set_File_Name(self, File_Name): self.File_Name = File_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_File_Path(self): return self.File_Path
    def set_File_Path(self, File_Path): self.File_Path = File_Path
    def get_Device_Path(self): return self.Device_Path
    def set_Device_Path(self, Device_Path): self.Device_Path = Device_Path
    def get_Full_Path(self): return self.Full_Path
    def set_Full_Path(self, Full_Path): self.Full_Path = Full_Path
    def get_File_Extension(self): return self.File_Extension
    def set_File_Extension(self, File_Extension): self.File_Extension = File_Extension
    def get_Size_In_Bytes(self): return self.Size_In_Bytes
    def set_Size_In_Bytes(self, Size_In_Bytes): self.Size_In_Bytes = Size_In_Bytes
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Magic_Number(self): return self.Magic_Number
    def set_Magic_Number(self, Magic_Number): self.Magic_Number = Magic_Number
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_File_Format(self): return self.File_Format
    def set_File_Format(self, File_Format): self.File_Format = File_Format
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Digital_Signatures(self): return self.Digital_Signatures
    def set_Digital_Signatures(self, Digital_Signatures): self.Digital_Signatures = Digital_Signatures
    def get_Modified_Time(self): return self.Modified_Time
    def set_Modified_Time(self, Modified_Time): self.Modified_Time = Modified_Time
    def get_Accessed_Time(self): return self.Accessed_Time
    def set_Accessed_Time(self, Accessed_Time): self.Accessed_Time = Accessed_Time
    def get_Created_Time(self): return self.Created_Time
    def set_Created_Time(self, Created_Time): self.Created_Time = Created_Time
    def get_File_Attributes_List(self): return self.File_Attributes_List
    def set_File_Attributes_List(self, File_Attributes_List): self.File_Attributes_List = File_Attributes_List
    def get_Permissions(self): return self.Permissions
    def set_Permissions(self, Permissions): self.Permissions = Permissions
    def get_User_Owner(self): return self.User_Owner
    def set_User_Owner(self, User_Owner): self.User_Owner = User_Owner
    def get_Packer_List(self): return self.Packer_List
    def set_Packer_List(self, Packer_List): self.Packer_List = Packer_List
    def get_Peak_Entropy(self): return self.Peak_Entropy
    def set_Peak_Entropy(self, Peak_Entropy): self.Peak_Entropy = Peak_Entropy
    def validate_DoubleObjectPropertyType(self, value):
        # Validate type cybox_common.DoubleObjectPropertyType, a restriction on None.
        pass
    def get_Sym_Links(self): return self.Sym_Links
    def set_Sym_Links(self, Sym_Links): self.Sym_Links = Sym_Links
    def get_Byte_Runs(self): return self.Byte_Runs
    def set_Byte_Runs(self, Byte_Runs): self.Byte_Runs = Byte_Runs
    def get_Extracted_Features(self): return self.Extracted_Features
    def set_Extracted_Features(self, Extracted_Features): self.Extracted_Features = Extracted_Features
    def get_Encryption_Algorithm(self): return self.Encryption_Algorithm
    def set_Encryption_Algorithm(self, Encryption_Algorithm): self.Encryption_Algorithm = Encryption_Algorithm
    def validate_CipherType(self, value):
        # Validate type cybox_common.CipherType, a restriction on None.
        pass
    def get_Decryption_Key(self): return self.Decryption_Key
    def set_Decryption_Key(self, Decryption_Key): self.Decryption_Key = Decryption_Key
    def get_Compression_Method(self): return self.Compression_Method
    def set_Compression_Method(self, Compression_Method): self.Compression_Method = Compression_Method
    def get_Compression_Version(self): return self.Compression_Version
    def set_Compression_Version(self, Compression_Version): self.Compression_Version = Compression_Version
    def get_Compression_Comment(self): return self.Compression_Comment
    def set_Compression_Comment(self, Compression_Comment): self.Compression_Comment = Compression_Comment
    def get_is_packed(self): return self.is_packed
    def set_is_packed(self, is_packed): self.is_packed = is_packed
    def get_is_masqueraded(self): return self.is_masqueraded
    def set_is_masqueraded(self, is_masqueraded): self.is_masqueraded = is_masqueraded
    def hasContent_(self):
        if (
            self.File_Name is not None or
            self.File_Path is not None or
            self.Device_Path is not None or
            self.Full_Path is not None or
            self.File_Extension is not None or
            self.Size_In_Bytes is not None or
            self.Magic_Number is not None or
            self.File_Format is not None or
            self.Hashes is not None or
            self.Digital_Signatures is not None or
            self.Modified_Time is not None or
            self.Accessed_Time is not None or
            self.Created_Time is not None or
            self.File_Attributes_List is not None or
            self.Permissions is not None or
            self.User_Owner is not None or
            self.Packer_List is not None or
            self.Peak_Entropy is not None or
            self.Sym_Links is not None or
            self.Byte_Runs is not None or
            self.Extracted_Features is not None or
            self.Encryption_Algorithm is not None or
            self.Decryption_Key is not None or
            self.Compression_Method is not None or
            self.Compression_Version is not None or
            self.Compression_Comment is not None or
            super(FileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='FileObj:', name_='FileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='FileObj:', name_='FileObjectType'):
        super(FileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='FileObjectType')
        if self.is_packed is not None:

            lwrite(' is_packed="%s"' % self.gds_format_boolean(self.is_packed, input_name='is_packed'))
        if self.is_masqueraded is not None:

            lwrite(' is_masqueraded="%s"' % self.gds_format_boolean(self.is_masqueraded, input_name='is_masqueraded'))
    def exportChildren(self, lwrite, level, namespace_='FileObj:', name_='FileObjectType', fromsubclass_=False, pretty_print=True):
        super(FileObjectType, self).exportChildren(lwrite, level, 'FileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.File_Name is not None:
            self.File_Name.export(lwrite, level, 'FileObj:', name_='File_Name', pretty_print=pretty_print)
        if self.File_Path is not None:
            self.File_Path.export(lwrite, level, 'FileObj:', name_='File_Path', pretty_print=pretty_print)
        if self.Device_Path is not None:
            self.Device_Path.export(lwrite, level, 'FileObj:', name_='Device_Path', pretty_print=pretty_print)
        if self.Full_Path is not None:
            self.Full_Path.export(lwrite, level, 'FileObj:', name_='Full_Path', pretty_print=pretty_print)
        if self.File_Extension is not None:
            self.File_Extension.export(lwrite, level, 'FileObj:', name_='File_Extension', pretty_print=pretty_print)
        if self.Size_In_Bytes is not None:
            self.Size_In_Bytes.export(lwrite, level, 'FileObj:', name_='Size_In_Bytes', pretty_print=pretty_print)
        if self.Magic_Number is not None:
            self.Magic_Number.export(lwrite, level, 'FileObj:', name_='Magic_Number', pretty_print=pretty_print)
        if self.File_Format is not None:
            self.File_Format.export(lwrite, level, 'FileObj:', name_='File_Format', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'FileObj:', name_='Hashes', pretty_print=pretty_print)
        if self.Digital_Signatures is not None:
            self.Digital_Signatures.export(lwrite, level, 'FileObj:', name_='Digital_Signatures', pretty_print=pretty_print)
        if self.Modified_Time is not None:
            self.Modified_Time.export(lwrite, level, 'FileObj:', name_='Modified_Time', pretty_print=pretty_print)
        if self.Accessed_Time is not None:
            self.Accessed_Time.export(lwrite, level, 'FileObj:', name_='Accessed_Time', pretty_print=pretty_print)
        if self.Created_Time is not None:
            self.Created_Time.export(lwrite, level, 'FileObj:', name_='Created_Time', pretty_print=pretty_print)
        if self.File_Attributes_List is not None:
            self.File_Attributes_List.export(lwrite, level, 'FileObj:', name_='File_Attributes_List', pretty_print=pretty_print)
        if self.Permissions is not None:
            self.Permissions.export(lwrite, level, 'FileObj:', name_='Permissions', pretty_print=pretty_print)
        if self.User_Owner is not None:
            self.User_Owner.export(lwrite, level, 'FileObj:', name_='User_Owner', pretty_print=pretty_print)
        if self.Packer_List is not None:
            self.Packer_List.export(lwrite, level, 'FileObj:', name_='Packer_List', pretty_print=pretty_print)
        if self.Peak_Entropy is not None:
            self.Peak_Entropy.export(lwrite, level, 'FileObj:', name_='Peak_Entropy', pretty_print=pretty_print)
        if self.Sym_Links is not None:
            self.Sym_Links.export(lwrite, level, 'FileObj:', name_='Sym_Links', pretty_print=pretty_print)
        if self.Byte_Runs is not None:
            self.Byte_Runs.export(lwrite, level, 'FileObj:', name_='Byte_Runs', pretty_print=pretty_print)
        if self.Extracted_Features is not None:
            self.Extracted_Features.export(lwrite, level, 'FileObj:', name_='Extracted_Features', pretty_print=pretty_print)
        if self.Encryption_Algorithm is not None:
            self.Encryption_Algorithm.export(lwrite, level, 'FileObj:', name_='Encryption_Algorithm', pretty_print=pretty_print)
        if self.Decryption_Key is not None:
            self.Decryption_Key.export(lwrite, level, 'FileObj:', name_='Decryption_Key', pretty_print=pretty_print)
        if self.Compression_Method is not None:
            self.Compression_Method.export(lwrite, level, 'FileObj:', name_='Compression_Method', pretty_print=pretty_print)
        if self.Compression_Version is not None:
            self.Compression_Version.export(lwrite, level, 'FileObj:', name_='Compression_Version', pretty_print=pretty_print)
        if self.Compression_Comment is not None:
            self.Compression_Comment.export(lwrite, level, 'FileObj:', name_='Compression_Comment', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_packed', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_packed = True
            elif value in ('false', '0'):
                self.is_packed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_masqueraded', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_masqueraded = True
            elif value in ('false', '0'):
                self.is_masqueraded = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(FileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Name(obj_)
        elif nodeName_ == 'File_Path':
            obj_ = FilePathType.factory()
            obj_.build(child_)
            self.set_File_Path(obj_)
        elif nodeName_ == 'Device_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Device_Path(obj_)
        elif nodeName_ == 'Full_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Full_Path(obj_)
        elif nodeName_ == 'File_Extension':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Extension(obj_)
        elif nodeName_ == 'Size_In_Bytes':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_In_Bytes(obj_)
        elif nodeName_ == 'Magic_Number':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Magic_Number(obj_)
        elif nodeName_ == 'File_Format':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Format(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Digital_Signatures':
            obj_ = cybox_common.DigitalSignaturesType.factory()
            obj_.build(child_)
            self.set_Digital_Signatures(obj_)
        elif nodeName_ == 'Modified_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Modified_Time(obj_)
        elif nodeName_ == 'Accessed_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accessed_Time(obj_)
        elif nodeName_ == 'Created_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Created_Time(obj_)
        elif nodeName_ == 'File_Attributes_List':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <File_Attributes_List> element')
            self.set_File_Attributes_List(obj_)
        elif nodeName_ == 'Permissions':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Permissions> element')
            self.set_Permissions(obj_)
        elif nodeName_ == 'User_Owner':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Owner(obj_)
        elif nodeName_ == 'Packer_List':
            obj_ = PackerListType.factory()
            obj_.build(child_)
            self.set_Packer_List(obj_)
        elif nodeName_ == 'Peak_Entropy':
            obj_ = cybox_common.DoubleObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Peak_Entropy(obj_)
        elif nodeName_ == 'Sym_Links':
            obj_ = SymLinksListType.factory()
            obj_.build(child_)
            self.set_Sym_Links(obj_)
        elif nodeName_ == 'Byte_Runs':
            obj_ = cybox_common.ByteRunsType.factory()
            obj_.build(child_)
            self.set_Byte_Runs(obj_)
        elif nodeName_ == 'Extracted_Features':
            obj_ = cybox_common.ExtractedFeaturesType.factory()
            obj_.build(child_)
            self.set_Extracted_Features(obj_)
        elif nodeName_ == 'Encryption_Algorithm':
            obj_ = cybox_common.CipherType.factory()
            obj_.build(child_)
            self.set_Encryption_Algorithm(obj_)
        elif nodeName_ == 'Decryption_Key':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Decryption_Key(obj_)
        elif nodeName_ == 'Compression_Method':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Compression_Method(obj_)
        elif nodeName_ == 'Compression_Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Compression_Version(obj_)
        elif nodeName_ == 'Compression_Comment':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Compression_Comment(obj_)
        super(FileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class FileObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Errors': cybox_common.ErrorsType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'String': cybox_common.ExtractedStringType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Accessed_Time': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Time': cybox_common.TimeType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.StringObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Full_Path': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Depth': cybox_common.IntegerObjectPropertyType,
    'Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Tool': cybox_common.ToolInformationType,
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
        rootTag = 'File'
        rootClass = FileObjectType
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
        rootTag = 'File'
        rootClass = FileObjectType
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
        rootTag = 'File'
        rootClass = FileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="File",
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
    "FileObjectType",
    "FilePathType",
    "FileAttributeType",
    "FilePermissionsType",
    "PackerListType",
    "PackerType",
    "PackerClassType",
    "EPJumpCodeType",
    "EntryPointSignatureType",
    "EntryPointSignatureListType",
    "SymLinksListType"
    ]
