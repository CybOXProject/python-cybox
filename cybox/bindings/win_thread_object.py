# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_handle_object


class ThreadRunningStatusType(cybox_common.BaseObjectPropertyType):
    """ThreadRunningStatusType specifies Windows thread running states via
    a union of the ThreadRunningStatusEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ThreadRunningStatusType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ThreadRunningStatusType.subclass:
            return ThreadRunningStatusType.subclass(*args_, **kwargs_)
        else:
            return ThreadRunningStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ThreadRunningStatusType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinThreadObj:', name_='ThreadRunningStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ThreadRunningStatusType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinThreadObj:', name_='ThreadRunningStatusType'):
        super(ThreadRunningStatusType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ThreadRunningStatusType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinThreadObj:', name_='ThreadRunningStatusType', fromsubclass_=False, pretty_print=True):
        super(ThreadRunningStatusType, self).exportChildren(lwrite, level, 'WinThreadObj:', name_, True, pretty_print=pretty_print)
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
        super(ThreadRunningStatusType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ThreadRunningStatusType

class WindowsThreadObjectType(cybox_common.ObjectPropertiesType):
    """The Windows_ThreadObjectType is intended to characterize Windows
    process threads. See also: http://msdn.microsoft.com/en-
    us/library/windows/desktop/ms684852(v=vs.85).aspx"""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Thread_ID=None, Handle=None, Running_Status=None, Context=None, Priority=None, Creation_Flags=None, Creation_Time=None, Start_Address=None, Parameter_Address=None, Security_Attributes=None, Stack_Size=None):
        super(WindowsThreadObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Thread_ID = Thread_ID
        self.Handle = Handle
        self.Running_Status = Running_Status
        self.Context = Context
        self.Priority = Priority
        self.Creation_Flags = Creation_Flags
        self.Creation_Time = Creation_Time
        self.Start_Address = Start_Address
        self.Parameter_Address = Parameter_Address
        self.Security_Attributes = Security_Attributes
        self.Stack_Size = Stack_Size
    def factory(*args_, **kwargs_):
        if WindowsThreadObjectType.subclass:
            return WindowsThreadObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsThreadObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Thread_ID(self): return self.Thread_ID
    def set_Thread_ID(self, Thread_ID): self.Thread_ID = Thread_ID
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_Running_Status(self): return self.Running_Status
    def set_Running_Status(self, Running_Status): self.Running_Status = Running_Status
    def validate_ThreadRunningStatusType(self, value):
        # Validate type ThreadRunningStatusType, a restriction on None.
        pass
    def get_Context(self): return self.Context
    def set_Context(self, Context): self.Context = Context
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Priority(self): return self.Priority
    def set_Priority(self, Priority): self.Priority = Priority
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Creation_Flags(self): return self.Creation_Flags
    def set_Creation_Flags(self, Creation_Flags): self.Creation_Flags = Creation_Flags
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Creation_Time(self): return self.Creation_Time
    def set_Creation_Time(self, Creation_Time): self.Creation_Time = Creation_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Start_Address(self): return self.Start_Address
    def set_Start_Address(self, Start_Address): self.Start_Address = Start_Address
    def get_Parameter_Address(self): return self.Parameter_Address
    def set_Parameter_Address(self, Parameter_Address): self.Parameter_Address = Parameter_Address
    def get_Security_Attributes(self): return self.Security_Attributes
    def set_Security_Attributes(self, Security_Attributes): self.Security_Attributes = Security_Attributes
    def get_Stack_Size(self): return self.Stack_Size
    def set_Stack_Size(self, Stack_Size): self.Stack_Size = Stack_Size
    def hasContent_(self):
        if (
            self.Thread_ID is not None or
            self.Handle is not None or
            self.Running_Status is not None or
            self.Context is not None or
            self.Priority is not None or
            self.Creation_Flags is not None or
            self.Creation_Time is not None or
            self.Start_Address is not None or
            self.Parameter_Address is not None or
            self.Security_Attributes is not None or
            self.Stack_Size is not None or
            super(WindowsThreadObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinThreadObj:', name_='WindowsThreadObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsThreadObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinThreadObj:', name_='WindowsThreadObjectType'):
        super(WindowsThreadObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsThreadObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinThreadObj:', name_='WindowsThreadObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsThreadObjectType, self).exportChildren(lwrite, level, 'WinThreadObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Thread_ID is not None:
            self.Thread_ID.export(lwrite, level, 'WinThreadObj:', name_='Thread_ID', pretty_print=pretty_print)
        if self.Handle is not None:
            self.Handle.export(lwrite, level, 'WinThreadObj:', name_='Handle', pretty_print=pretty_print)
        if self.Running_Status is not None:
            self.Running_Status.export(lwrite, level, 'WinThreadObj:', name_='Running_Status', pretty_print=pretty_print)
        if self.Context is not None:
            self.Context.export(lwrite, level, 'WinThreadObj:', name_='Context', pretty_print=pretty_print)
        if self.Priority is not None:
            self.Priority.export(lwrite, level, 'WinThreadObj:', name_='Priority', pretty_print=pretty_print)
        if self.Creation_Flags is not None:
            self.Creation_Flags.export(lwrite, level, 'WinThreadObj:', name_='Creation_Flags', pretty_print=pretty_print)
        if self.Creation_Time is not None:
            self.Creation_Time.export(lwrite, level, 'WinThreadObj:', name_='Creation_Time', pretty_print=pretty_print)
        if self.Start_Address is not None:
            self.Start_Address.export(lwrite, level, 'WinThreadObj:', name_='Start_Address', pretty_print=pretty_print)
        if self.Parameter_Address is not None:
            self.Parameter_Address.export(lwrite, level, 'WinThreadObj:', name_='Parameter_Address', pretty_print=pretty_print)
        if self.Security_Attributes is not None:
            self.Security_Attributes.export(lwrite, level, 'WinThreadObj:', name_='Security_Attributes', pretty_print=pretty_print)
        if self.Stack_Size is not None:
            self.Stack_Size.export(lwrite, level, 'WinThreadObj:', name_='Stack_Size', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsThreadObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Thread_ID':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Thread_ID(obj_)
        elif nodeName_ == 'Handle':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_Handle(obj_)
        elif nodeName_ == 'Running_Status':
            obj_ = ThreadRunningStatusType.factory()
            obj_.build(child_)
            self.set_Running_Status(obj_)
        elif nodeName_ == 'Context':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Context(obj_)
        elif nodeName_ == 'Priority':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Priority(obj_)
        elif nodeName_ == 'Creation_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Flags(obj_)
        elif nodeName_ == 'Creation_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Time(obj_)
        elif nodeName_ == 'Start_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Start_Address(obj_)
        elif nodeName_ == 'Parameter_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Parameter_Address(obj_)
        elif nodeName_ == 'Security_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_Attributes(obj_)
        elif nodeName_ == 'Stack_Size':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Stack_Size(obj_)
        super(WindowsThreadObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsThreadObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Thread_ID': cybox_common.NonNegativeIntegerObjectPropertyType,
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
    'Security_Attributes': cybox_common.StringObjectPropertyType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Parameter_Address': cybox_common.HexBinaryObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Priority': cybox_common.UnsignedIntegerObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': win_handle_object.HandleType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Libraries': cybox_common.LibrariesType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Stack_Size': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Start_Address': cybox_common.HexBinaryObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Creation_Flags': cybox_common.HexBinaryObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Context': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
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
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
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
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Thread",
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
    "WindowsThreadObjectType",
    "ThreadRunningStatusType"
    ]
