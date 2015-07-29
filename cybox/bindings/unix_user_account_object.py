# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import user_account_object


class UnixPrivilegeType(user_account_object.PrivilegeType):
    """The UnixPrivilegeType type is used to specify Unix privileges. It
    extends the abstract user_account_object.PrivilegeType from the CybOX UserAccount
    object."""

    subclass = None
    superclass = user_account_object.PrivilegeType
    def __init__(self, Permissions_Mask=None):
        super(UnixPrivilegeType, self).__init__()
        self.Permissions_Mask = Permissions_Mask
    def factory(*args_, **kwargs_):
        if UnixPrivilegeType.subclass:
            return UnixPrivilegeType.subclass(*args_, **kwargs_)
        else:
            return UnixPrivilegeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Permissions_Mask(self): return self.Permissions_Mask
    def set_Permissions_Mask(self, Permissions_Mask): self.Permissions_Mask = Permissions_Mask
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Permissions_Mask is not None or
            super(UnixPrivilegeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixPrivilegeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType'):
        super(UnixPrivilegeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixPrivilegeType')
    def exportChildren(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType', fromsubclass_=False, pretty_print=True):
        super(UnixPrivilegeType, self).exportChildren(lwrite, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Permissions_Mask is not None:
            self.Permissions_Mask.export(lwrite, level, 'UnixUserAccountObj:', name_='Permissions_Mask', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixPrivilegeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Permissions_Mask':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Permissions_Mask(obj_)
        super(UnixPrivilegeType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixPrivilegeType

class UnixGroupType(user_account_object.GroupType):
    """The UnixGroupType type is used for specifying Unix groups. It
    extends the abstract user_account_object.GroupType from the Cybox UserAccount
    construct."""

    subclass = None
    superclass = user_account_object.GroupType
    def __init__(self, Group_ID=None):
        super(UnixGroupType, self).__init__()
        self.Group_ID = Group_ID
    def factory(*args_, **kwargs_):
        if UnixGroupType.subclass:
            return UnixGroupType.subclass(*args_, **kwargs_)
        else:
            return UnixGroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group_ID(self): return self.Group_ID
    def set_Group_ID(self, Group_ID): self.Group_ID = Group_ID
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Group_ID is not None or
            super(UnixGroupType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixGroupType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixGroupType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixGroupType'):
        super(UnixGroupType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixGroupType')
    def exportChildren(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixGroupType', fromsubclass_=False, pretty_print=True):
        super(UnixGroupType, self).exportChildren(lwrite, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Group_ID is not None:
            self.Group_ID.export(lwrite, level, 'UnixUserAccountObj:', name_='Group_ID', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixGroupType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group_ID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Group_ID(obj_)
        super(UnixGroupType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixGroupType

class UnixUserAccountObjectType(user_account_object.UserAccountObjectType):
    """The UnixUserAccountType type is intended to characterize Unix user
    accounts."""

    subclass = None
    superclass = user_account_object.UserAccountObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, disabled=None, locked_out=None, Description=None, Domain=None, password_required=None, Full_Name=None, Group_List=None, Home_Directory=None, Last_Login=None, Privilege_List=None, Script_Path=None, Username=None, User_Password_Age=None, Group_ID=None, User_ID=None, Login_Shell=None):
        super(UnixUserAccountObjectType, self).__init__(object_reference, Custom_Properties, disabled, locked_out, Description, Domain, password_required, Full_Name, Group_List, Home_Directory, Last_Login, Privilege_List, Script_Path, Username, User_Password_Age, )
        self.Group_ID = Group_ID
        self.User_ID = User_ID
        self.Login_Shell = Login_Shell
    def factory(*args_, **kwargs_):
        if UnixUserAccountObjectType.subclass:
            return UnixUserAccountObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixUserAccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group_ID(self): return self.Group_ID
    def set_Group_ID(self, Group_ID): self.Group_ID = Group_ID
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_User_ID(self): return self.User_ID
    def set_User_ID(self, User_ID): self.User_ID = User_ID
    def get_Login_Shell(self): return self.Login_Shell
    def set_Login_Shell(self, Login_Shell): self.Login_Shell = Login_Shell
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Group_ID is not None or
            self.User_ID is not None or
            self.Login_Shell is not None or
            super(UnixUserAccountObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixUserAccountObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType'):
        super(UnixUserAccountObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixUserAccountObjectType')
    def exportChildren(self, lwrite, level, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixUserAccountObjectType, self).exportChildren(lwrite, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Group_ID is not None:
            self.Group_ID.export(lwrite, level, 'UnixUserAccountObj:', name_='Group_ID', pretty_print=pretty_print)
        if self.User_ID is not None:
            self.User_ID.export(lwrite, level, 'UnixUserAccountObj:', name_='User_ID', pretty_print=pretty_print)
        if self.Login_Shell is not None:
            self.Login_Shell.export(lwrite, level, 'UnixUserAccountObj:', name_='Login_Shell', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixUserAccountObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group_ID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Group_ID(obj_)
        elif nodeName_ == 'User_ID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_ID(obj_)
        elif nodeName_ == 'Login_Shell':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Login_Shell(obj_)
        super(UnixUserAccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixUserAccountObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Group_List': user_account_object.GroupListType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'User_Password_Age': cybox_common.DurationObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Home_Directory': cybox_common.StringObjectPropertyType,
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
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Domain': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Permissions_Mask': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Group': user_account_object.GroupType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Name': cybox_common.StringObjectPropertyType,
    'Privilege': user_account_object.PrivilegeType,
    'Import': cybox_common.StringObjectPropertyType,
    'Group_ID': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Login_Shell': cybox_common.StringObjectPropertyType,
    'User_ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Full_Name': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Script_Path': cybox_common.StringObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Privilege_List': user_account_object.PrivilegeListType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StringObjectPropertyType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Last_Login': cybox_common.DateTimeObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'User_Account': user_account_object.UserAccountObjectType,
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
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
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
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
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
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Unix_User_Account",
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
    "UnixUserAccountObjectType",
    "UnixGroupType",
    "UnixPrivilegeType"
    ]
