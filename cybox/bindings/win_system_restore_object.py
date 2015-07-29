# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class HiveListType(GeneratedsSuper):

    subclass = None
    superclass = None
    def __init__(self, Hive=None):
        if Hive is None:
            self.Hive = []
        else:
            self.Hive = Hive
    def factory(*args_, **kwargs_):
        if HiveListType.subclass:
            return HiveListType.subclass(*args_, **kwargs_)
        else:
            return HiveListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hive(self): return self.Hive
    def set_Hive(self, Hive): self.Hive = Hive
    def add_Hive(self, value): self.Hive.append(value)
    def insert_Hive(self, index, value): self.Hive[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Hive
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='HiveListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HiveListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemRestoreObj:', name_='HiveListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='HiveListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Hive_ in self.Hive:
            Hive_.export(lwrite, level, 'WinSystemRestoreObj:', name_='Hive', pretty_print=pretty_print)
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
        if nodeName_ == 'Hive':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Hive.append(obj_)
# end class HiveListType

class ChangeLogEntryTypeType(cybox_common.BaseObjectPropertyType):
    """ChangeLogEntryTypeType types, via a union of the
    ChangeLogEntryTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ChangeLogEntryTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ChangeLogEntryTypeType.subclass:
            return ChangeLogEntryTypeType.subclass(*args_, **kwargs_)
        else:
            return ChangeLogEntryTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ChangeLogEntryTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='ChangeLogEntryTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ChangeLogEntryTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemRestoreObj:', name_='ChangeLogEntryTypeType'):
        super(ChangeLogEntryTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ChangeLogEntryTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='ChangeLogEntryTypeType', fromsubclass_=False, pretty_print=True):
        super(ChangeLogEntryTypeType, self).exportChildren(lwrite, level, 'WinSystemRestoreObj:', name_, True, pretty_print=pretty_print)
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
        super(ChangeLogEntryTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ChangeLogEntryTypeType

class WindowsSystemRestoreObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsSystemRestoreObjectType is intended to characterize
    Windows system restore points."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Restore_Point_Description=None, Restore_Point_Full_Path=None, Restore_Point_Name=None, Restore_Point_Type=None, ACL_Change_SID=None, ACL_Change_Username=None, Backup_File_Name=None, Change_Event=None, ChangeLog_Entry_Flags=None, ChangeLog_Entry_Sequence_Number=None, ChangeLog_Entry_Type=None, Change_Log_File_Name=None, Created=None, File_Attributes=None, New_File_Name=None, Original_File_Name=None, Original_Short_File_Name=None, Process_Name=None, Registry_Hive_List=None):
        super(WindowsSystemRestoreObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Restore_Point_Description = Restore_Point_Description
        self.Restore_Point_Full_Path = Restore_Point_Full_Path
        self.Restore_Point_Name = Restore_Point_Name
        self.Restore_Point_Type = Restore_Point_Type
        self.ACL_Change_SID = ACL_Change_SID
        self.ACL_Change_Username = ACL_Change_Username
        self.Backup_File_Name = Backup_File_Name
        self.Change_Event = Change_Event
        self.ChangeLog_Entry_Flags = ChangeLog_Entry_Flags
        self.ChangeLog_Entry_Sequence_Number = ChangeLog_Entry_Sequence_Number
        self.ChangeLog_Entry_Type = ChangeLog_Entry_Type
        self.Change_Log_File_Name = Change_Log_File_Name
        self.Created = Created
        self.File_Attributes = File_Attributes
        self.New_File_Name = New_File_Name
        self.Original_File_Name = Original_File_Name
        self.Original_Short_File_Name = Original_Short_File_Name
        self.Process_Name = Process_Name
        self.Registry_Hive_List = Registry_Hive_List
    def factory(*args_, **kwargs_):
        if WindowsSystemRestoreObjectType.subclass:
            return WindowsSystemRestoreObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsSystemRestoreObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Restore_Point_Description(self): return self.Restore_Point_Description
    def set_Restore_Point_Description(self, Restore_Point_Description): self.Restore_Point_Description = Restore_Point_Description
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Restore_Point_Full_Path(self): return self.Restore_Point_Full_Path
    def set_Restore_Point_Full_Path(self, Restore_Point_Full_Path): self.Restore_Point_Full_Path = Restore_Point_Full_Path
    def get_Restore_Point_Name(self): return self.Restore_Point_Name
    def set_Restore_Point_Name(self, Restore_Point_Name): self.Restore_Point_Name = Restore_Point_Name
    def get_Restore_Point_Type(self): return self.Restore_Point_Type
    def set_Restore_Point_Type(self, Restore_Point_Type): self.Restore_Point_Type = Restore_Point_Type
    def get_ACL_Change_SID(self): return self.ACL_Change_SID
    def set_ACL_Change_SID(self, ACL_Change_SID): self.ACL_Change_SID = ACL_Change_SID
    def get_ACL_Change_Username(self): return self.ACL_Change_Username
    def set_ACL_Change_Username(self, ACL_Change_Username): self.ACL_Change_Username = ACL_Change_Username
    def get_Backup_File_Name(self): return self.Backup_File_Name
    def set_Backup_File_Name(self, Backup_File_Name): self.Backup_File_Name = Backup_File_Name
    def get_Change_Event(self): return self.Change_Event
    def set_Change_Event(self, Change_Event): self.Change_Event = Change_Event
    def validate_ChangeLogEntryTypeType(self, value):
        # Validate type ChangeLogEntryTypeType, a restriction on None.
        pass
    def get_ChangeLog_Entry_Flags(self): return self.ChangeLog_Entry_Flags
    def set_ChangeLog_Entry_Flags(self, ChangeLog_Entry_Flags): self.ChangeLog_Entry_Flags = ChangeLog_Entry_Flags
    def get_ChangeLog_Entry_Sequence_Number(self): return self.ChangeLog_Entry_Sequence_Number
    def set_ChangeLog_Entry_Sequence_Number(self, ChangeLog_Entry_Sequence_Number): self.ChangeLog_Entry_Sequence_Number = ChangeLog_Entry_Sequence_Number
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_ChangeLog_Entry_Type(self): return self.ChangeLog_Entry_Type
    def set_ChangeLog_Entry_Type(self, ChangeLog_Entry_Type): self.ChangeLog_Entry_Type = ChangeLog_Entry_Type
    def get_Change_Log_File_Name(self): return self.Change_Log_File_Name
    def set_Change_Log_File_Name(self, Change_Log_File_Name): self.Change_Log_File_Name = Change_Log_File_Name
    def get_Created(self): return self.Created
    def set_Created(self, Created): self.Created = Created
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_File_Attributes(self): return self.File_Attributes
    def set_File_Attributes(self, File_Attributes): self.File_Attributes = File_Attributes
    def get_New_File_Name(self): return self.New_File_Name
    def set_New_File_Name(self, New_File_Name): self.New_File_Name = New_File_Name
    def get_Original_File_Name(self): return self.Original_File_Name
    def set_Original_File_Name(self, Original_File_Name): self.Original_File_Name = Original_File_Name
    def get_Original_Short_File_Name(self): return self.Original_Short_File_Name
    def set_Original_Short_File_Name(self, Original_Short_File_Name): self.Original_Short_File_Name = Original_Short_File_Name
    def get_Process_Name(self): return self.Process_Name
    def set_Process_Name(self, Process_Name): self.Process_Name = Process_Name
    def get_Registry_Hive_List(self): return self.Registry_Hive_List
    def set_Registry_Hive_List(self, Registry_Hive_List): self.Registry_Hive_List = Registry_Hive_List
    def hasContent_(self):
        if (
            self.Restore_Point_Description is not None or
            self.Restore_Point_Full_Path is not None or
            self.Restore_Point_Name is not None or
            self.Restore_Point_Type is not None or
            self.ACL_Change_SID is not None or
            self.ACL_Change_Username is not None or
            self.Backup_File_Name is not None or
            self.Change_Event is not None or
            self.ChangeLog_Entry_Flags is not None or
            self.ChangeLog_Entry_Sequence_Number is not None or
            self.ChangeLog_Entry_Type is not None or
            self.Change_Log_File_Name is not None or
            self.Created is not None or
            self.File_Attributes is not None or
            self.New_File_Name is not None or
            self.Original_File_Name is not None or
            self.Original_Short_File_Name is not None or
            self.Process_Name is not None or
            self.Registry_Hive_List is not None or
            super(WindowsSystemRestoreObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='WindowsSystemRestoreObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsSystemRestoreObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemRestoreObj:', name_='WindowsSystemRestoreObjectType'):
        super(WindowsSystemRestoreObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsSystemRestoreObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinSystemRestoreObj:', name_='WindowsSystemRestoreObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsSystemRestoreObjectType, self).exportChildren(lwrite, level, 'WinSystemRestoreObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Restore_Point_Description is not None:
            self.Restore_Point_Description.export(lwrite, level, 'WinSystemRestoreObj:', name_='Restore_Point_Description', pretty_print=pretty_print)
        if self.Restore_Point_Full_Path is not None:
            self.Restore_Point_Full_Path.export(lwrite, level, 'WinSystemRestoreObj:', name_='Restore_Point_Full_Path', pretty_print=pretty_print)
        if self.Restore_Point_Name is not None:
            self.Restore_Point_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Restore_Point_Name', pretty_print=pretty_print)
        if self.Restore_Point_Type is not None:
            self.Restore_Point_Type.export(lwrite, level, 'WinSystemRestoreObj:', name_='Restore_Point_Type', pretty_print=pretty_print)
        if self.ACL_Change_SID is not None:
            self.ACL_Change_SID.export(lwrite, level, 'WinSystemRestoreObj:', name_='ACL_Change_SID', pretty_print=pretty_print)
        if self.ACL_Change_Username is not None:
            self.ACL_Change_Username.export(lwrite, level, 'WinSystemRestoreObj:', name_='ACL_Change_Username', pretty_print=pretty_print)
        if self.Backup_File_Name is not None:
            self.Backup_File_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Backup_File_Name', pretty_print=pretty_print)
        if self.Change_Event is not None:
            self.Change_Event.export(lwrite, level, 'WinSystemRestoreObj:', name_='Change_Event', pretty_print=pretty_print)
        if self.ChangeLog_Entry_Flags is not None:
            self.ChangeLog_Entry_Flags.export(lwrite, level, 'WinSystemRestoreObj:', name_='ChangeLog_Entry_Flags', pretty_print=pretty_print)
        if self.ChangeLog_Entry_Sequence_Number is not None:
            self.ChangeLog_Entry_Sequence_Number.export(lwrite, level, 'WinSystemRestoreObj:', name_='ChangeLog_Entry_Sequence_Number', pretty_print=pretty_print)
        if self.ChangeLog_Entry_Type is not None:
            self.ChangeLog_Entry_Type.export(lwrite, level, 'WinSystemRestoreObj:', name_='ChangeLog_Entry_Type', pretty_print=pretty_print)
        if self.Change_Log_File_Name is not None:
            self.Change_Log_File_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Change_Log_File_Name', pretty_print=pretty_print)
        if self.Created is not None:
            self.Created.export(lwrite, level, 'WinSystemRestoreObj:', name_='Created', pretty_print=pretty_print)
        if self.File_Attributes is not None:
            self.File_Attributes.export(lwrite, level, 'WinSystemRestoreObj:', name_='File_Attributes', pretty_print=pretty_print)
        if self.New_File_Name is not None:
            self.New_File_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='New_File_Name', pretty_print=pretty_print)
        if self.Original_File_Name is not None:
            self.Original_File_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Original_File_Name', pretty_print=pretty_print)
        if self.Original_Short_File_Name is not None:
            self.Original_Short_File_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Original_Short_File_Name', pretty_print=pretty_print)
        if self.Process_Name is not None:
            self.Process_Name.export(lwrite, level, 'WinSystemRestoreObj:', name_='Process_Name', pretty_print=pretty_print)
        if self.Registry_Hive_List is not None:
            self.Registry_Hive_List.export(lwrite, level, 'WinSystemRestoreObj:', name_='Registry_Hive_List', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsSystemRestoreObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Restore_Point_Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Restore_Point_Description(obj_)
        elif nodeName_ == 'Restore_Point_Full_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Restore_Point_Full_Path(obj_)
        elif nodeName_ == 'Restore_Point_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Restore_Point_Name(obj_)
        elif nodeName_ == 'Restore_Point_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Restore_Point_Type(obj_)
        elif nodeName_ == 'ACL_Change_SID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ACL_Change_SID(obj_)
        elif nodeName_ == 'ACL_Change_Username':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ACL_Change_Username(obj_)
        elif nodeName_ == 'Backup_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Backup_File_Name(obj_)
        elif nodeName_ == 'Change_Event':
            obj_ = ChangeLogEntryTypeType.factory()
            obj_.build(child_)
            self.set_Change_Event(obj_)
        elif nodeName_ == 'ChangeLog_Entry_Flags':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ChangeLog_Entry_Flags(obj_)
        elif nodeName_ == 'ChangeLog_Entry_Sequence_Number':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ChangeLog_Entry_Sequence_Number(obj_)
        elif nodeName_ == 'ChangeLog_Entry_Type':
            obj_ = ChangeLogEntryTypeType.factory()
            obj_.build(child_)
            self.set_ChangeLog_Entry_Type(obj_)
        elif nodeName_ == 'Change_Log_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Change_Log_File_Name(obj_)
        elif nodeName_ == 'Created':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Created(obj_)
        elif nodeName_ == 'File_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Attributes(obj_)
        elif nodeName_ == 'New_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_New_File_Name(obj_)
        elif nodeName_ == 'Original_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Original_File_Name(obj_)
        elif nodeName_ == 'Original_Short_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Original_Short_File_Name(obj_)
        elif nodeName_ == 'Process_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Process_Name(obj_)
        elif nodeName_ == 'Registry_Hive_List':
            obj_ = HiveListType.factory()
            obj_.build(child_)
            self.set_Registry_Hive_List(obj_)
        super(WindowsSystemRestoreObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsSystemRestoreObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'ACL_Change_Username': cybox_common.StringObjectPropertyType,
    'Original_Short_File_Name': cybox_common.StringObjectPropertyType,
    'Restore_Point_Name': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
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
    'Change_Log_File_Name': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Backup_File_Name': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'ChangeLog_Entry_Flags': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'ChangeLog_Entry_Sequence_Number': cybox_common.LongObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Created': cybox_common.DateTimeObjectPropertyType,
    'Restore_Point_Type': cybox_common.StringObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Restore_Point_Full_Path': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'ACL_Change_SID': cybox_common.StringObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Process_Name': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Original_File_Name': cybox_common.StringObjectPropertyType,
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
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Time': cybox_common.TimeType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'File_Attributes': cybox_common.StringObjectPropertyType,
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
    'Hive': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Restore_Point_Description': cybox_common.StringObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'New_File_Name': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Windows_System_Restore_Entry'
        rootClass = WindowsSystemRestoreObjectType
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
        rootTag = 'Windows_System_Restore_Entry'
        rootClass = WindowsSystemRestoreObjectType
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
        rootTag = 'Windows_System_Restore_Entry'
        rootClass = WindowsSystemRestoreObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_System_Restore_Entry",
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
    "WindowsSystemRestoreObjectType",
    "HiveListType",
    "ChangeLogEntryTypeType"
    ]
