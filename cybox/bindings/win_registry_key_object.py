# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_handle_object


class RegistryValueType(GeneratedsSuper):
    """The RegistryValueType type is intended to characterize Windows
    registry Value name/data pairs."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Data=None, Datatype=None, Byte_Runs=None):
        self.Name = Name
        self.Data = Data
        self.Datatype = Datatype
        self.Byte_Runs = Byte_Runs
    def factory(*args_, **kwargs_):
        if RegistryValueType.subclass:
            return RegistryValueType.subclass(*args_, **kwargs_)
        else:
            return RegistryValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def get_Datatype(self): return self.Datatype
    def set_Datatype(self, Datatype): self.Datatype = Datatype
    def validate_RegistryDatatypeType(self, value):
        # Validate type RegistryDatatypeType, a restriction on None.
        pass
    def get_Byte_Runs(self): return self.Byte_Runs
    def set_Byte_Runs(self, Byte_Runs): self.Byte_Runs = Byte_Runs
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Data is not None or
            self.Datatype is not None or
            self.Byte_Runs is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryValueType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='RegistryValueType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinRegistryKeyObj:', name_='Name', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'WinRegistryKeyObj:', name_='Data', pretty_print=pretty_print)
        if self.Datatype is not None:
            self.Datatype.export(lwrite, level, 'WinRegistryKeyObj:', name_='Datatype', pretty_print=pretty_print)
        if self.Byte_Runs is not None:
            self.Byte_Runs.export(lwrite, level, 'WinRegistryKeyObj:', name_='Byte_Runs', pretty_print=pretty_print)
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
        elif nodeName_ == 'Data':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        elif nodeName_ == 'Datatype':
            obj_ = RegistryDatatypeType.factory()
            obj_.build(child_)
            self.set_Datatype(obj_)
        elif nodeName_ == 'Byte_Runs':
            obj_ = cybox_common.ByteRunsType.factory()
            obj_.build(child_)
            self.set_Byte_Runs(obj_)
# end class RegistryValueType

class RegistryValuesType(GeneratedsSuper):
    """The RegistryValuesType type specifies the values (with their
    name/data pairs) held within the registry key."""

    subclass = None
    superclass = None
    def __init__(self, Value=None):
        if Value is None:
            self.Value = []
        else:
            self.Value = Value
    def factory(*args_, **kwargs_):
        if RegistryValuesType.subclass:
            return RegistryValuesType.subclass(*args_, **kwargs_)
        else:
            return RegistryValuesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def add_Value(self, value): self.Value.append(value)
    def insert_Value(self, index, value): self.Value[index] = value
    def hasContent_(self):
        if (
            self.Value
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryValuesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryValuesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='RegistryValuesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryValuesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Value_ in self.Value:
            Value_.export(lwrite, level, 'WinRegistryKeyObj:', name_='Value', pretty_print=pretty_print)
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
        if nodeName_ == 'Value':
            obj_ = RegistryValueType.factory()
            obj_.build(child_)
            self.Value.append(obj_)
# end class RegistryValuesType

class RegistrySubkeysType(GeneratedsSuper):
    """The RegistrySubkeysType specifies the set of subkeys contained under
    the registry key."""

    subclass = None
    superclass = None
    def __init__(self, Subkey=None):
        if Subkey is None:
            self.Subkey = []
        else:
            self.Subkey = Subkey
    def factory(*args_, **kwargs_):
        if RegistrySubkeysType.subclass:
            return RegistrySubkeysType.subclass(*args_, **kwargs_)
        else:
            return RegistrySubkeysType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Subkey(self): return self.Subkey
    def set_Subkey(self, Subkey): self.Subkey = Subkey
    def add_Subkey(self, value): self.Subkey.append(value)
    def insert_Subkey(self, index, value): self.Subkey[index] = value
    def hasContent_(self):
        if (
            self.Subkey
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistrySubkeysType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistrySubkeysType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='RegistrySubkeysType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistrySubkeysType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Subkey_ in self.Subkey:
            Subkey_.export(lwrite, level, 'WinRegistryKeyObj:', name_='Subkey', pretty_print=pretty_print)
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
        if nodeName_ == 'Subkey':
            obj_ = WindowsRegistryKeyObjectType.factory()
            obj_.build(child_)
            self.Subkey.append(obj_)
# end class RegistrySubkeysType

class RegistryHiveType(cybox_common.BaseObjectPropertyType):
    """RegistryHiveType specifies Windows registry hive types via a union
    of the RegistryHiveEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(RegistryHiveType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if RegistryHiveType.subclass:
            return RegistryHiveType.subclass(*args_, **kwargs_)
        else:
            return RegistryHiveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(RegistryHiveType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryHiveType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryHiveType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='RegistryHiveType'):
        super(RegistryHiveType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryHiveType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryHiveType', fromsubclass_=False, pretty_print=True):
        super(RegistryHiveType, self).exportChildren(lwrite, level, 'WinRegistryKeyObj:', name_, True, pretty_print=pretty_print)
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
        super(RegistryHiveType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class RegistryHiveType

class RegistryDatatypeType(cybox_common.BaseObjectPropertyType):
    """Registry_Datatype specifies Windows registry datatypes via a union
    of the RegistryDataTypesEnum type and the atomic xs:string type.
    Its base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(RegistryDatatypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if RegistryDatatypeType.subclass:
            return RegistryDatatypeType.subclass(*args_, **kwargs_)
        else:
            return RegistryDatatypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(RegistryDatatypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryDatatypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryDatatypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='RegistryDatatypeType'):
        super(RegistryDatatypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RegistryDatatypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='RegistryDatatypeType', fromsubclass_=False, pretty_print=True):
        super(RegistryDatatypeType, self).exportChildren(lwrite, level, 'WinRegistryKeyObj:', name_, True, pretty_print=pretty_print)
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
        super(RegistryDatatypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class RegistryDatatypeType

class WindowsRegistryKeyObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsRegistryObjectType type is intended to characterize
    Windows registry objects, including Keys and Key/Value pairs."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Key=None, Hive=None, Number_Values=None, Values=None, Modified_Time=None, Creator_Username=None, Handle_List=None, Number_Subkeys=None, Subkeys=None, Byte_Runs=None):
        super(WindowsRegistryKeyObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Key = Key
        self.Hive = Hive
        self.Number_Values = Number_Values
        self.Values = Values
        self.Modified_Time = Modified_Time
        self.Creator_Username = Creator_Username
        self.Handle_List = Handle_List
        self.Number_Subkeys = Number_Subkeys
        self.Subkeys = Subkeys
        self.Byte_Runs = Byte_Runs
    def factory(*args_, **kwargs_):
        if WindowsRegistryKeyObjectType.subclass:
            return WindowsRegistryKeyObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsRegistryKeyObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Key(self): return self.Key
    def set_Key(self, Key): self.Key = Key
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Hive(self): return self.Hive
    def set_Hive(self, Hive): self.Hive = Hive
    def validate_RegistryHiveType(self, value):
        # Validate type RegistryHiveType, a restriction on None.
        pass
    def get_Number_Values(self): return self.Number_Values
    def set_Number_Values(self, Number_Values): self.Number_Values = Number_Values
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Values(self): return self.Values
    def set_Values(self, Values): self.Values = Values
    def get_Modified_Time(self): return self.Modified_Time
    def set_Modified_Time(self, Modified_Time): self.Modified_Time = Modified_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Creator_Username(self): return self.Creator_Username
    def set_Creator_Username(self, Creator_Username): self.Creator_Username = Creator_Username
    def get_Handle_List(self): return self.Handle_List
    def set_Handle_List(self, Handle_List): self.Handle_List = Handle_List
    def get_Number_Subkeys(self): return self.Number_Subkeys
    def set_Number_Subkeys(self, Number_Subkeys): self.Number_Subkeys = Number_Subkeys
    def get_Subkeys(self): return self.Subkeys
    def set_Subkeys(self, Subkeys): self.Subkeys = Subkeys
    def get_Byte_Runs(self): return self.Byte_Runs
    def set_Byte_Runs(self, Byte_Runs): self.Byte_Runs = Byte_Runs
    def hasContent_(self):
        if (
            self.Key is not None or
            self.Hive is not None or
            self.Number_Values is not None or
            self.Values is not None or
            self.Modified_Time is not None or
            self.Creator_Username is not None or
            self.Handle_List is not None or
            self.Number_Subkeys is not None or
            self.Subkeys is not None or
            self.Byte_Runs is not None or
            super(WindowsRegistryKeyObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='WindowsRegistryKeyObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsRegistryKeyObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinRegistryKeyObj:', name_='WindowsRegistryKeyObjectType'):
        super(WindowsRegistryKeyObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsRegistryKeyObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinRegistryKeyObj:', name_='WindowsRegistryKeyObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsRegistryKeyObjectType, self).exportChildren(lwrite, level, 'WinRegistryKeyObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Key is not None:
            self.Key.export(lwrite, level, 'WinRegistryKeyObj:', name_='Key', pretty_print=pretty_print)
        if self.Hive is not None:
            self.Hive.export(lwrite, level, 'WinRegistryKeyObj:', name_='Hive', pretty_print=pretty_print)
        if self.Number_Values is not None:
            self.Number_Values.export(lwrite, level, 'WinRegistryKeyObj:', name_='Number_Values', pretty_print=pretty_print)
        if self.Values is not None:
            self.Values.export(lwrite, level, 'WinRegistryKeyObj:', name_='Values', pretty_print=pretty_print)
        if self.Modified_Time is not None:
            self.Modified_Time.export(lwrite, level, 'WinRegistryKeyObj:', name_='Modified_Time', pretty_print=pretty_print)
        if self.Creator_Username is not None:
            self.Creator_Username.export(lwrite, level, 'WinRegistryKeyObj:', name_='Creator_Username', pretty_print=pretty_print)
        if self.Handle_List is not None:
            self.Handle_List.export(lwrite, level, 'WinRegistryKeyObj:', name_='Handle_List', pretty_print=pretty_print)
        if self.Number_Subkeys is not None:
            self.Number_Subkeys.export(lwrite, level, 'WinRegistryKeyObj:', name_='Number_Subkeys', pretty_print=pretty_print)
        if self.Subkeys is not None:
            self.Subkeys.export(lwrite, level, 'WinRegistryKeyObj:', name_='Subkeys', pretty_print=pretty_print)
        if self.Byte_Runs is not None:
            self.Byte_Runs.export(lwrite, level, 'WinRegistryKeyObj:', name_='Byte_Runs', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsRegistryKeyObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Key':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Key(obj_)
        elif nodeName_ == 'Hive':
            obj_ = RegistryHiveType.factory()
            obj_.build(child_)
            self.set_Hive(obj_)
        elif nodeName_ == 'Number_Values':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Values(obj_)
        elif nodeName_ == 'Values':
            obj_ = RegistryValuesType.factory()
            obj_.build(child_)
            self.set_Values(obj_)
        elif nodeName_ == 'Modified_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Modified_Time(obj_)
        elif nodeName_ == 'Creator_Username':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creator_Username(obj_)
        elif nodeName_ == 'Handle_List':
            obj_ = win_handle_object.WindowsHandleListType.factory()
            obj_.build(child_)
            self.set_Handle_List(obj_)
        elif nodeName_ == 'Number_Subkeys':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Subkeys(obj_)
        elif nodeName_ == 'Subkeys':
            obj_ = RegistrySubkeysType.factory()
            obj_.build(child_)
            self.set_Subkeys(obj_)
        elif nodeName_ == 'Byte_Runs':
            obj_ = cybox_common.ByteRunsType.factory()
            obj_.build(child_)
            self.set_Byte_Runs(obj_)
        super(WindowsRegistryKeyObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsRegistryKeyObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Number_Subkeys': cybox_common.UnsignedIntegerObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Tool_Hashes': cybox_common.HashListType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': win_handle_object.HandleType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Key': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Handle_List': win_handle_object.WindowsHandleListType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Data': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.DateTimeObjectPropertyType,
    'Number_Values': cybox_common.UnsignedIntegerObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Creator_Username': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
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
        rootTag = 'Windows_Registry_Key'
        rootClass = WindowsRegistryKeyObjectType
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
        rootTag = 'Windows_Registry_Key'
        rootClass = WindowsRegistryKeyObjectType
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
        rootTag = 'Windows_Registry_Key'
        rootClass = WindowsRegistryKeyObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Registry_Key",
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
    "WindowsRegistryKeyObjectType",
    "RegistryValueType",
    "RegistryDatatypeType",
    "RegistryHiveType",
    "RegistryValuesType",
    "RegistrySubkeysType"
    ]
