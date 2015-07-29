# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import process_object


class FileDescriptorListType(GeneratedsSuper):
    """The FileDescriptorListType type specifies a list of Unix file
    descriptors."""

    subclass = None
    superclass = None
    def __init__(self, File_Descriptor=None):
        if File_Descriptor is None:
            self.File_Descriptor = []
        else:
            self.File_Descriptor = File_Descriptor
    def factory(*args_, **kwargs_):
        if FileDescriptorListType.subclass:
            return FileDescriptorListType.subclass(*args_, **kwargs_)
        else:
            return FileDescriptorListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File_Descriptor(self): return self.File_Descriptor
    def set_File_Descriptor(self, File_Descriptor): self.File_Descriptor = File_Descriptor
    def add_File_Descriptor(self, value): self.File_Descriptor.append(value)
    def insert_File_Descriptor(self, index, value): self.File_Descriptor[index] = value
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.File_Descriptor
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixProcessObj:', name_='FileDescriptorListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FileDescriptorListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixProcessObj:', name_='FileDescriptorListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='UnixProcessObj:', name_='FileDescriptorListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for File_Descriptor_ in self.File_Descriptor:
            File_Descriptor_.export(lwrite, level, 'UnixProcessObj:', name_='File_Descriptor', pretty_print=pretty_print)
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
        if nodeName_ == 'File_Descriptor':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.File_Descriptor.append(obj_)
# end class FileDescriptorListType

class UnixProcessStateType(cybox_common.BaseObjectPropertyType):
    """UnixProcessStateType specifies Unix process states, via a union of
    the UnixProcessStateEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications. See "man ps" for more information.This attribute
    is optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(UnixProcessStateType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if UnixProcessStateType.subclass:
            return UnixProcessStateType.subclass(*args_, **kwargs_)
        else:
            return UnixProcessStateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(UnixProcessStateType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessStateType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessStateType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixProcessObj:', name_='UnixProcessStateType'):
        super(UnixProcessStateType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessStateType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessStateType', fromsubclass_=False, pretty_print=True):
        super(UnixProcessStateType, self).exportChildren(lwrite, level, 'UnixProcessObj:', name_, True, pretty_print=pretty_print)
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
        super(UnixProcessStateType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class UnixProcessStateType

class UnixProcessStatusType(process_object.ProcessStatusType):
    """The UnixProcessStatusType field specifies the current status of the
    running Unix process. It extends the abstract process_object.ProcessStatusType
    from the CybOX Process Object."""

    subclass = None
    superclass = process_object.ProcessStatusType
    def __init__(self, Current_Status=None, Timestamp=None):
        super(UnixProcessStatusType, self).__init__()
        self.Current_Status = Current_Status
        self.Timestamp = Timestamp
    def factory(*args_, **kwargs_):
        if UnixProcessStatusType.subclass:
            return UnixProcessStatusType.subclass(*args_, **kwargs_)
        else:
            return UnixProcessStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Current_Status(self): return self.Current_Status
    def set_Current_Status(self, Current_Status): self.Current_Status = Current_Status
    def validate_UnixProcessStateType(self, value):
        # Validate type UnixProcessStateType, a restriction on None.
        pass
    def get_Timestamp(self): return self.Timestamp
    def set_Timestamp(self, Timestamp): self.Timestamp = Timestamp
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Current_Status is not None or
            self.Timestamp is not None or
            super(UnixProcessStatusType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessStatusType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixProcessObj:', name_='UnixProcessStatusType'):
        super(UnixProcessStatusType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessStatusType')
    def exportChildren(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessStatusType', fromsubclass_=False, pretty_print=True):
        super(UnixProcessStatusType, self).exportChildren(lwrite, level, 'UnixProcessObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Current_Status is not None:
            self.Current_Status.export(lwrite, level, 'UnixProcessObj:', name_='Current_Status', pretty_print=pretty_print)
        if self.Timestamp is not None:
            self.Timestamp.export(lwrite, level, 'UnixProcessObj:', name_='Timestamp', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixProcessStatusType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Current_Status':
            obj_ = UnixProcessStateType.factory()
            obj_.build(child_)
            self.set_Current_Status(obj_)
        elif nodeName_ == 'Timestamp':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Timestamp(obj_)
        super(UnixProcessStatusType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixProcessStatusType

class UnixProcessObjectType(process_object.ProcessObjectType):
    """The UnixProcessObjectType type is intended to characterize Unix
    processes."""

    subclass = None
    superclass = process_object.ProcessObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_hidden=None, PID=None, Name=None, Creation_Time=None, Parent_PID=None, Child_PID_List=None, Image_Info=None, Argument_List=None, Environment_Variable_List=None, Kernel_Time=None, Port_List=None, Network_Connection_List=None, Start_Time=None, Status=None, Username=None, User_Time=None, Extracted_Features=None, Open_File_Descriptor_List=None, Priority=None, RUID=None, Session_ID=None):
        super(UnixProcessObjectType, self).__init__(object_reference, Custom_Properties, is_hidden, PID, Name, Creation_Time, Parent_PID, Child_PID_List, Image_Info, Argument_List, Environment_Variable_List, Kernel_Time, Port_List, Network_Connection_List, Start_Time, Status, Username, User_Time, Extracted_Features, )
        self.Open_File_Descriptor_List = Open_File_Descriptor_List
        self.Priority = Priority
        self.RUID = RUID
        self.Session_ID = Session_ID
    def factory(*args_, **kwargs_):
        if UnixProcessObjectType.subclass:
            return UnixProcessObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixProcessObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Open_File_Descriptor_List(self): return self.Open_File_Descriptor_List
    def set_Open_File_Descriptor_List(self, Open_File_Descriptor_List): self.Open_File_Descriptor_List = Open_File_Descriptor_List
    def get_Priority(self): return self.Priority
    def set_Priority(self, Priority): self.Priority = Priority
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_RUID(self): return self.RUID
    def set_RUID(self, RUID): self.RUID = RUID
    def get_Session_ID(self): return self.Session_ID
    def set_Session_ID(self, Session_ID): self.Session_ID = Session_ID
    def hasContent_(self):
        if (
            self.Open_File_Descriptor_List is not None or
            self.Priority is not None or
            self.RUID is not None or
            self.Session_ID is not None or
            super(UnixProcessObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixProcessObj:', name_='UnixProcessObjectType'):
        super(UnixProcessObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixProcessObjectType')
    def exportChildren(self, lwrite, level, namespace_='UnixProcessObj:', name_='UnixProcessObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixProcessObjectType, self).exportChildren(lwrite, level, 'UnixProcessObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Open_File_Descriptor_List is not None:
            self.Open_File_Descriptor_List.export(lwrite, level, 'UnixProcessObj:', name_='Open_File_Descriptor_List', pretty_print=pretty_print)
        if self.Priority is not None:
            self.Priority.export(lwrite, level, 'UnixProcessObj:', name_='Priority', pretty_print=pretty_print)
        if self.RUID is not None:
            self.RUID.export(lwrite, level, 'UnixProcessObj:', name_='RUID', pretty_print=pretty_print)
        if self.Session_ID is not None:
            self.Session_ID.export(lwrite, level, 'UnixProcessObj:', name_='Session_ID', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixProcessObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Open_File_Descriptor_List':
            obj_ = FileDescriptorListType.factory()
            obj_.build(child_)
            self.set_Open_File_Descriptor_List(obj_)
        elif nodeName_ == 'Priority':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Priority(obj_)
        elif nodeName_ == 'RUID':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_RUID(obj_)
        elif nodeName_ == 'Session_ID':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Session_ID(obj_)
        super(UnixProcessObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixProcessObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Argument_List': process_object.ArgumentListType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Path': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.PositiveIntegerObjectPropertyType,
    'Expect': cybox_common.StringObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'RUID': cybox_common.NonNegativeIntegerObjectPropertyType,
    'File_Descriptor': cybox_common.UnsignedIntegerObjectPropertyType,
    'TE': cybox_common.StringObjectPropertyType,
    'Parent_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'Warning': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Current_Directory': cybox_common.StringObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Priority': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Link': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Server': cybox_common.StringObjectPropertyType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Via': cybox_common.StringObjectPropertyType,
    'X_Requested_For': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Command_Line': cybox_common.StringObjectPropertyType,
    'Argument': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Child_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'User_Time': cybox_common.DurationObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Status': process_object.ProcessStatusType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Timestamp': cybox_common.DateTimeObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Child_PID_List': process_object.ChildPIDListType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Session_ID': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Connection': cybox_common.StringObjectPropertyType,
    'X_Requested_With': cybox_common.StringObjectPropertyType,
    'Kernel_Time': cybox_common.DurationObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'P3P': cybox_common.StringObjectPropertyType,
    'If_Unmodified_Since': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Process': process_object.ProcessObjectType,
    'Imports': cybox_common.ImportsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'Image_Info': process_object.ImageInfoType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Network_Connection_List': process_object.NetworkConnectionListType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Port_List': process_object.PortListType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'ETag': cybox_common.StringObjectPropertyType,
    'Date_Ran': cybox_common.DateTimeObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'If_Match': cybox_common.StringObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
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
        rootTag = 'Unix_Process'
        rootClass = UnixProcessObjectType
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
        rootTag = 'Unix_Process'
        rootClass = UnixProcessObjectType
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
        rootTag = 'Unix_Process'
        rootClass = UnixProcessObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Unix_Process",
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
    "UnixProcessObjectType",
    "UnixProcessStatusType",
    "FileDescriptorListType",
    "UnixProcessStateType"
    ]
