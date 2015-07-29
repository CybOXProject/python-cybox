# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class UnformattedMessageListType(GeneratedsSuper):
    """The UnformattedMessageListType type is a list of unformatted
    messages in the event log entry."""

    subclass = None
    superclass = None
    def __init__(self, Unformatted_Message=None):
        if Unformatted_Message is None:
            self.Unformatted_Message = []
        else:
            self.Unformatted_Message = Unformatted_Message
    def factory(*args_, **kwargs_):
        if UnformattedMessageListType.subclass:
            return UnformattedMessageListType.subclass(*args_, **kwargs_)
        else:
            return UnformattedMessageListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Unformatted_Message(self): return self.Unformatted_Message
    def set_Unformatted_Message(self, Unformatted_Message): self.Unformatted_Message = Unformatted_Message
    def add_Unformatted_Message(self, value): self.Unformatted_Message.append(value)
    def insert_Unformatted_Message(self, index, value): self.Unformatted_Message[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Unformatted_Message
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinEventLogObj:', name_='UnformattedMessageListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnformattedMessageListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinEventLogObj:', name_='UnformattedMessageListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinEventLogObj:', name_='UnformattedMessageListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Unformatted_Message_ in self.Unformatted_Message:
            Unformatted_Message_.export(lwrite, level, 'WinEventLogObj:', name_='Unformatted_Message', pretty_print=pretty_print)
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
        if nodeName_ == 'Unformatted_Message':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Unformatted_Message.append(obj_)
# end class UnformattedMessageListType

class WindowsEventLogObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsEventLogObjectType type is intended to characterize
    entries in the Windows event log."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, EID=None, Type=None, Log=None, Message=None, Category_Num=None, Category=None, Generation_Time=None, Source=None, Machine=None, User=None, Blob=None, Correlation_Activity_ID=None, Correlation_Related_Activity_ID=None, Execution_Process_ID=None, Execution_Thread_ID=None, Index=None, Reserved=None, Unformatted_Message_List=None, Write_Time=None):
        super(WindowsEventLogObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.EID = EID
        self.Type = Type
        self.Log = Log
        self.Message = Message
        self.Category_Num = Category_Num
        self.Category = Category
        self.Generation_Time = Generation_Time
        self.Source = Source
        self.Machine = Machine
        self.User = User
        self.Blob = Blob
        self.Correlation_Activity_ID = Correlation_Activity_ID
        self.Correlation_Related_Activity_ID = Correlation_Related_Activity_ID
        self.Execution_Process_ID = Execution_Process_ID
        self.Execution_Thread_ID = Execution_Thread_ID
        self.Index = Index
        self.Reserved = Reserved
        self.Unformatted_Message_List = Unformatted_Message_List
        self.Write_Time = Write_Time
    def factory(*args_, **kwargs_):
        if WindowsEventLogObjectType.subclass:
            return WindowsEventLogObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsEventLogObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_EID(self): return self.EID
    def set_EID(self, EID): self.EID = EID
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Log(self): return self.Log
    def set_Log(self, Log): self.Log = Log
    def get_Message(self): return self.Message
    def set_Message(self, Message): self.Message = Message
    def get_Category_Num(self): return self.Category_Num
    def set_Category_Num(self, Category_Num): self.Category_Num = Category_Num
    def get_Category(self): return self.Category
    def set_Category(self, Category): self.Category = Category
    def get_Generation_Time(self): return self.Generation_Time
    def set_Generation_Time(self, Generation_Time): self.Generation_Time = Generation_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Source(self): return self.Source
    def set_Source(self, Source): self.Source = Source
    def get_Machine(self): return self.Machine
    def set_Machine(self, Machine): self.Machine = Machine
    def get_User(self): return self.User
    def set_User(self, User): self.User = User
    def get_Blob(self): return self.Blob
    def set_Blob(self, Blob): self.Blob = Blob
    def validate_Base64BinaryObjectPropertyType(self, value):
        # Validate type cybox_common.Base64BinaryObjectPropertyType, a restriction on None.
        pass
    def get_Correlation_Activity_ID(self): return self.Correlation_Activity_ID
    def set_Correlation_Activity_ID(self, Correlation_Activity_ID): self.Correlation_Activity_ID = Correlation_Activity_ID
    def get_Correlation_Related_Activity_ID(self): return self.Correlation_Related_Activity_ID
    def set_Correlation_Related_Activity_ID(self, Correlation_Related_Activity_ID): self.Correlation_Related_Activity_ID = Correlation_Related_Activity_ID
    def get_Execution_Process_ID(self): return self.Execution_Process_ID
    def set_Execution_Process_ID(self, Execution_Process_ID): self.Execution_Process_ID = Execution_Process_ID
    def get_Execution_Thread_ID(self): return self.Execution_Thread_ID
    def set_Execution_Thread_ID(self, Execution_Thread_ID): self.Execution_Thread_ID = Execution_Thread_ID
    def get_Index(self): return self.Index
    def set_Index(self, Index): self.Index = Index
    def get_Reserved(self): return self.Reserved
    def set_Reserved(self, Reserved): self.Reserved = Reserved
    def get_Unformatted_Message_List(self): return self.Unformatted_Message_List
    def set_Unformatted_Message_List(self, Unformatted_Message_List): self.Unformatted_Message_List = Unformatted_Message_List
    def get_Write_Time(self): return self.Write_Time
    def set_Write_Time(self, Write_Time): self.Write_Time = Write_Time
    def hasContent_(self):
        if (
            self.EID is not None or
            self.Type is not None or
            self.Log is not None or
            self.Message is not None or
            self.Category_Num is not None or
            self.Category is not None or
            self.Generation_Time is not None or
            self.Source is not None or
            self.Machine is not None or
            self.User is not None or
            self.Blob is not None or
            self.Correlation_Activity_ID is not None or
            self.Correlation_Related_Activity_ID is not None or
            self.Execution_Process_ID is not None or
            self.Execution_Thread_ID is not None or
            self.Index is not None or
            self.Reserved is not None or
            self.Unformatted_Message_List is not None or
            self.Write_Time is not None or
            super(WindowsEventLogObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinEventLogObj:', name_='WindowsEventLogObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsEventLogObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinEventLogObj:', name_='WindowsEventLogObjectType'):
        super(WindowsEventLogObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsEventLogObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinEventLogObj:', name_='WindowsEventLogObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsEventLogObjectType, self).exportChildren(lwrite, level, 'WinEventLogObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EID is not None:
            self.EID.export(lwrite, level, 'WinEventLogObj:', name_='EID', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinEventLogObj:', name_='Type', pretty_print=pretty_print)
        if self.Log is not None:
            self.Log.export(lwrite, level, 'WinEventLogObj:', name_='Log', pretty_print=pretty_print)
        if self.Message is not None:
            self.Message.export(lwrite, level, 'WinEventLogObj:', name_='Message', pretty_print=pretty_print)
        if self.Category_Num is not None:
            self.Category_Num.export(lwrite, level, 'WinEventLogObj:', name_='Category_Num', pretty_print=pretty_print)
        if self.Category is not None:
            self.Category.export(lwrite, level, 'WinEventLogObj:', name_='Category', pretty_print=pretty_print)
        if self.Generation_Time is not None:
            self.Generation_Time.export(lwrite, level, 'WinEventLogObj:', name_='Generation_Time', pretty_print=pretty_print)
        if self.Source is not None:
            self.Source.export(lwrite, level, 'WinEventLogObj:', name_='Source', pretty_print=pretty_print)
        if self.Machine is not None:
            self.Machine.export(lwrite, level, 'WinEventLogObj:', name_='Machine', pretty_print=pretty_print)
        if self.User is not None:
            self.User.export(lwrite, level, 'WinEventLogObj:', name_='User', pretty_print=pretty_print)
        if self.Blob is not None:
            self.Blob.export(lwrite, level, 'WinEventLogObj:', name_='Blob', pretty_print=pretty_print)
        if self.Correlation_Activity_ID is not None:
            self.Correlation_Activity_ID.export(lwrite, level, 'WinEventLogObj:', name_='Correlation_Activity_ID', pretty_print=pretty_print)
        if self.Correlation_Related_Activity_ID is not None:
            self.Correlation_Related_Activity_ID.export(lwrite, level, 'WinEventLogObj:', name_='Correlation_Related_Activity_ID', pretty_print=pretty_print)
        if self.Execution_Process_ID is not None:
            self.Execution_Process_ID.export(lwrite, level, 'WinEventLogObj:', name_='Execution_Process_ID', pretty_print=pretty_print)
        if self.Execution_Thread_ID is not None:
            self.Execution_Thread_ID.export(lwrite, level, 'WinEventLogObj:', name_='Execution_Thread_ID', pretty_print=pretty_print)
        if self.Index is not None:
            self.Index.export(lwrite, level, 'WinEventLogObj:', name_='Index', pretty_print=pretty_print)
        if self.Reserved is not None:
            self.Reserved.export(lwrite, level, 'WinEventLogObj:', name_='Reserved', pretty_print=pretty_print)
        if self.Unformatted_Message_List is not None:
            self.Unformatted_Message_List.export(lwrite, level, 'WinEventLogObj:', name_='Unformatted_Message_List', pretty_print=pretty_print)
        if self.Write_Time is not None:
            self.Write_Time.export(lwrite, level, 'WinEventLogObj:', name_='Write_Time', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsEventLogObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'EID':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_EID(obj_)
        elif nodeName_ == 'Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Log':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Log(obj_)
        elif nodeName_ == 'Message':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Message(obj_)
        elif nodeName_ == 'Category_Num':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Category_Num(obj_)
        elif nodeName_ == 'Category':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Category(obj_)
        elif nodeName_ == 'Generation_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Generation_Time(obj_)
        elif nodeName_ == 'Source':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Source(obj_)
        elif nodeName_ == 'Machine':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Machine(obj_)
        elif nodeName_ == 'User':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User(obj_)
        elif nodeName_ == 'Blob':
            obj_ = cybox_common.Base64BinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Blob(obj_)
        elif nodeName_ == 'Correlation_Activity_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Correlation_Activity_ID(obj_)
        elif nodeName_ == 'Correlation_Related_Activity_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Correlation_Related_Activity_ID(obj_)
        elif nodeName_ == 'Execution_Process_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Execution_Process_ID(obj_)
        elif nodeName_ == 'Execution_Thread_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Execution_Thread_ID(obj_)
        elif nodeName_ == 'Index':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Index(obj_)
        elif nodeName_ == 'Reserved':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reserved(obj_)
        elif nodeName_ == 'Unformatted_Message_List':
            obj_ = UnformattedMessageListType.factory()
            obj_.build(child_)
            self.set_Unformatted_Message_List(obj_)
        elif nodeName_ == 'Write_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Write_Time(obj_)
        super(WindowsEventLogObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsEventLogObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Correlation_Related_Activity_ID': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Write_Time': cybox_common.DateTimeObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Execution_Thread_ID': cybox_common.StringObjectPropertyType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Unformatted_Message': cybox_common.StringObjectPropertyType,
    'Index': cybox_common.LongObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Source': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Generation_Time': cybox_common.DateTimeObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Correlation_Activity_ID': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Category': cybox_common.StringObjectPropertyType,
    'Log': cybox_common.StringObjectPropertyType,
    'Category_Num': cybox_common.LongObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'User': cybox_common.StringObjectPropertyType,
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
    'Libraries': cybox_common.LibrariesType,
    'Contributors': cybox_common.PersonnelType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Blob': cybox_common.Base64BinaryObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Machine': cybox_common.StringObjectPropertyType,
    'EID': cybox_common.LongObjectPropertyType,
    'Execution_Process_ID': cybox_common.StringObjectPropertyType,
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
    'Message': cybox_common.StringObjectPropertyType,
    'Reserved': cybox_common.LongObjectPropertyType,
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
        rootTag = 'Windows_Event_Log'
        rootClass = WindowsEventLogObjectType
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
        rootTag = 'Windows_Event_Log'
        rootClass = WindowsEventLogObjectType
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
        rootTag = 'Windows_Event_Log'
        rootClass = WindowsEventLogObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Event_Log",
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
    "WindowsEventLogObjectType",
    "UnformattedMessageListType"
    ]
