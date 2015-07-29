# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class UserSessionObjectType(cybox_common.ObjectPropertiesType):
    """The UserSessionObjectType type is intended to characterize user
    sessions."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Effective_Group=None, Effective_Group_ID=None, Effective_User=None, Effective_User_ID=None, Login_Time=None, Logout_Time=None):
        super(UserSessionObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Effective_Group = Effective_Group
        self.Effective_Group_ID = Effective_Group_ID
        self.Effective_User = Effective_User
        self.Effective_User_ID = Effective_User_ID
        self.Login_Time = Login_Time
        self.Logout_Time = Logout_Time
    def factory(*args_, **kwargs_):
        if UserSessionObjectType.subclass:
            return UserSessionObjectType.subclass(*args_, **kwargs_)
        else:
            return UserSessionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Effective_Group(self): return self.Effective_Group
    def set_Effective_Group(self, Effective_Group): self.Effective_Group = Effective_Group
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Effective_Group_ID(self): return self.Effective_Group_ID
    def set_Effective_Group_ID(self, Effective_Group_ID): self.Effective_Group_ID = Effective_Group_ID
    def get_Effective_User(self): return self.Effective_User
    def set_Effective_User(self, Effective_User): self.Effective_User = Effective_User
    def get_Effective_User_ID(self): return self.Effective_User_ID
    def set_Effective_User_ID(self, Effective_User_ID): self.Effective_User_ID = Effective_User_ID
    def get_Login_Time(self): return self.Login_Time
    def set_Login_Time(self, Login_Time): self.Login_Time = Login_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Logout_Time(self): return self.Logout_Time
    def set_Logout_Time(self, Logout_Time): self.Logout_Time = Logout_Time
    def hasContent_(self):
        if (
            self.Effective_Group is not None or
            self.Effective_Group_ID is not None or
            self.Effective_User is not None or
            self.Effective_User_ID is not None or
            self.Login_Time is not None or
            self.Logout_Time is not None or
            super(UserSessionObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserSessionObj:', name_='UserSessionObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UserSessionObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserSessionObj:', name_='UserSessionObjectType'):
        super(UserSessionObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UserSessionObjectType')
    def exportChildren(self, lwrite, level, namespace_='UserSessionObj:', name_='UserSessionObjectType', fromsubclass_=False, pretty_print=True):
        super(UserSessionObjectType, self).exportChildren(lwrite, level, 'UserSessionObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Effective_Group is not None:
            self.Effective_Group.export(lwrite, level, 'UserSessionObj:', name_='Effective_Group', pretty_print=pretty_print)
        if self.Effective_Group_ID is not None:
            self.Effective_Group_ID.export(lwrite, level, 'UserSessionObj:', name_='Effective_Group_ID', pretty_print=pretty_print)
        if self.Effective_User is not None:
            self.Effective_User.export(lwrite, level, 'UserSessionObj:', name_='Effective_User', pretty_print=pretty_print)
        if self.Effective_User_ID is not None:
            self.Effective_User_ID.export(lwrite, level, 'UserSessionObj:', name_='Effective_User_ID', pretty_print=pretty_print)
        if self.Login_Time is not None:
            self.Login_Time.export(lwrite, level, 'UserSessionObj:', name_='Login_Time', pretty_print=pretty_print)
        if self.Logout_Time is not None:
            self.Logout_Time.export(lwrite, level, 'UserSessionObj:', name_='Logout_Time', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UserSessionObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Effective_Group':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Effective_Group(obj_)
        elif nodeName_ == 'Effective_Group_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Effective_Group_ID(obj_)
        elif nodeName_ == 'Effective_User':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Effective_User(obj_)
        elif nodeName_ == 'Effective_User_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Effective_User_ID(obj_)
        elif nodeName_ == 'Login_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Login_Time(obj_)
        elif nodeName_ == 'Logout_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Logout_Time(obj_)
        super(UserSessionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UserSessionObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Error': cybox_common.ErrorType,
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
    'Compiler': cybox_common.CompilerType,
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
    'Login_Time': cybox_common.DateTimeObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Logout_Time': cybox_common.DateTimeObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Effective_User_ID': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Effective_Group': cybox_common.StringObjectPropertyType,
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
    'Effective_User': cybox_common.StringObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Effective_Group_ID': cybox_common.StringObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Time': cybox_common.TimeType,
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
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
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
        rootTag = 'User_Session'
        rootClass = UserSessionObjectType
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
        rootTag = 'User_Session'
        rootClass = UserSessionObjectType
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
        rootTag = 'User_Session'
        rootClass = UserSessionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="User_Session",
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
    "UserSessionObjectType"
    ]
