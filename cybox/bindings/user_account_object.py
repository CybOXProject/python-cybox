# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import account_object


class PrivilegeListType(GeneratedsSuper):
    """The PrivilegeListType type specifies the list of privileges that the
    user account has."""

    subclass = None
    superclass = None
    def __init__(self, Privilege=None):
        if Privilege is None:
            self.Privilege = []
        else:
            self.Privilege = Privilege
    def factory(*args_, **kwargs_):
        if PrivilegeListType.subclass:
            return PrivilegeListType.subclass(*args_, **kwargs_)
        else:
            return PrivilegeListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Privilege(self): return self.Privilege
    def set_Privilege(self, Privilege): self.Privilege = Privilege
    def add_Privilege(self, value): self.Privilege.append(value)
    def insert_Privilege(self, index, value): self.Privilege[index] = value
    def hasContent_(self):
        if (
            self.Privilege
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserAccountObj:', name_='PrivilegeListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PrivilegeListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserAccountObj:', name_='PrivilegeListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='UserAccountObj:', name_='PrivilegeListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Privilege_ in self.get_Privilege():
            Privilege_.export(lwrite, level, 'UserAccountObj:', name_='Privilege', pretty_print=pretty_print)
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
        if nodeName_ == 'Privilege':
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
                    'Class not implemented for <Privilege> element')
            self.Privilege.append(obj_)
# end class PrivilegeListType

class PrivilegeType(GeneratedsSuper):
    """The PrivilegeType type specifies a specific privilege that a user
    has. This is an abstract type since user privileges are
    operating-system specific, and is extended as needed in the
    derived CybOX object schemas."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if PrivilegeType.subclass:
            return PrivilegeType.subclass(*args_, **kwargs_)
        else:
            return PrivilegeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserAccountObj:', name_='PrivilegeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PrivilegeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserAccountObj:', name_='PrivilegeType'):
        lwrite(' xsi:type="%s%s"' % (namespace_, name_))
    def exportChildren(self, lwrite, level, namespace_='UserAccountObj:', name_='PrivilegeType', fromsubclass_=False, pretty_print=True):
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
# end class PrivilegeType

class GroupListType(GeneratedsSuper):
    """The GroupListType type specifies the groups that the user account
    belongs to."""

    subclass = None
    superclass = None
    def __init__(self, Group=None):
        if Group is None:
            self.Group = []
        else:
            self.Group = Group
    def factory(*args_, **kwargs_):
        if GroupListType.subclass:
            return GroupListType.subclass(*args_, **kwargs_)
        else:
            return GroupListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group(self): return self.Group
    def set_Group(self, Group): self.Group = Group
    def add_Group(self, value): self.Group.append(value)
    def insert_Group(self, index, value): self.Group[index] = value
    def hasContent_(self):
        if (
            self.Group
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserAccountObj:', name_='GroupListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GroupListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserAccountObj:', name_='GroupListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='UserAccountObj:', name_='GroupListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Group_ in self.get_Group():
            Group_.export(lwrite, level, 'UserAccountObj:', name_='Group', pretty_print=pretty_print)
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
        if nodeName_ == 'Group':
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
                    'Class not implemented for <Group> element')
            self.Group.append(obj_)
# end class GroupListType

class GroupType(GeneratedsSuper):
    """The GroupType type specifies a group that a user account belongs to.
    This is an abstract type since group IDs are operating-system
    specific, and is extended as needed in the derived CybOX object
    schemas."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if GroupType.subclass:
            return GroupType.subclass(*args_, **kwargs_)
        else:
            return GroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserAccountObj:', name_='GroupType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GroupType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserAccountObj:', name_='GroupType'):
        lwrite(' xsi:type="%s%s"' % (namespace_, name_))
    def exportChildren(self, lwrite, level, namespace_='UserAccountObj:', name_='GroupType', fromsubclass_=False, pretty_print=True):
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
# end class GroupType

class UserAccountObjectType(account_object.AccountObjectType):
    """The UserAccountObjectType type is intended to characterize generic
    user accounts.The password_required field specifies whether a
    password is required for this user account."""

    subclass = None
    superclass = account_object.AccountObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, disabled=None, locked_out=None, Description=None, Domain=None, password_required=None, Full_Name=None, Group_List=None, Home_Directory=None, Last_Login=None, Privilege_List=None, Script_Path=None, Username=None, User_Password_Age=None):
        super(UserAccountObjectType, self).__init__(object_reference, Custom_Properties, disabled, locked_out, Description, Domain, )
        self.password_required = _cast(bool, password_required)
        self.Full_Name = Full_Name
        self.Group_List = Group_List
        self.Home_Directory = Home_Directory
        self.Last_Login = Last_Login
        self.Privilege_List = Privilege_List
        self.Script_Path = Script_Path
        self.Username = Username
        self.User_Password_Age = User_Password_Age
    def factory(*args_, **kwargs_):
        if UserAccountObjectType.subclass:
            return UserAccountObjectType.subclass(*args_, **kwargs_)
        else:
            return UserAccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Full_Name(self): return self.Full_Name
    def set_Full_Name(self, Full_Name): self.Full_Name = Full_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Group_List(self): return self.Group_List
    def set_Group_List(self, Group_List): self.Group_List = Group_List
    def get_Home_Directory(self): return self.Home_Directory
    def set_Home_Directory(self, Home_Directory): self.Home_Directory = Home_Directory
    def get_Last_Login(self): return self.Last_Login
    def set_Last_Login(self, Last_Login): self.Last_Login = Last_Login
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Privilege_List(self): return self.Privilege_List
    def set_Privilege_List(self, Privilege_List): self.Privilege_List = Privilege_List
    def get_Script_Path(self): return self.Script_Path
    def set_Script_Path(self, Script_Path): self.Script_Path = Script_Path
    def get_Username(self): return self.Username
    def set_Username(self, Username): self.Username = Username
    def get_User_Password_Age(self): return self.User_Password_Age
    def set_User_Password_Age(self, User_Password_Age): self.User_Password_Age = User_Password_Age
    def validate_DurationObjectPropertyType(self, value):
        # Validate type cybox_common.DurationObjectPropertyType, a restriction on None.
        pass
    def get_password_required(self): return self.password_required
    def set_password_required(self, password_required): self.password_required = password_required
    def hasContent_(self):
        if (
            self.Full_Name is not None or
            self.Group_List is not None or
            self.Home_Directory is not None or
            self.Last_Login is not None or
            self.Privilege_List is not None or
            self.Script_Path is not None or
            self.Username is not None or
            self.User_Password_Age is not None or
            super(UserAccountObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UserAccountObj:', name_='UserAccountObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UserAccountObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UserAccountObj:', name_='UserAccountObjectType'):
        super(UserAccountObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UserAccountObjectType')
        if self.password_required is not None:

            lwrite(' password_required="%s"' % self.gds_format_boolean(self.password_required, input_name='password_required'))
    def exportChildren(self, lwrite, level, namespace_='UserAccountObj:', name_='UserAccountObjectType', fromsubclass_=False, pretty_print=True):
        super(UserAccountObjectType, self).exportChildren(lwrite, level, 'UserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Full_Name is not None:
            self.Full_Name.export(lwrite, level, 'UserAccountObj:', name_='Full_Name', pretty_print=pretty_print)
        if self.Group_List is not None:
            self.Group_List.export(lwrite, level, 'UserAccountObj:', name_='Group_List', pretty_print=pretty_print)
        if self.Home_Directory is not None:
            self.Home_Directory.export(lwrite, level, 'UserAccountObj:', name_='Home_Directory', pretty_print=pretty_print)
        if self.Last_Login is not None:
            self.Last_Login.export(lwrite, level, 'UserAccountObj:', name_='Last_Login', pretty_print=pretty_print)
        if self.Privilege_List is not None:
            self.Privilege_List.export(lwrite, level, 'UserAccountObj:', name_='Privilege_List', pretty_print=pretty_print)
        if self.Script_Path is not None:
            self.Script_Path.export(lwrite, level, 'UserAccountObj:', name_='Script_Path', pretty_print=pretty_print)
        if self.Username is not None:
            self.Username.export(lwrite, level, 'UserAccountObj:', name_='Username', pretty_print=pretty_print)
        if self.User_Password_Age is not None:
            self.User_Password_Age.export(lwrite, level, 'UserAccountObj:', name_='User_Password_Age', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('password_required', node)
        if value is not None:

            if value in ('true', '1'):
                self.password_required = True
            elif value in ('false', '0'):
                self.password_required = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(UserAccountObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Full_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Full_Name(obj_)
        elif nodeName_ == 'Group_List':
            obj_ = GroupListType.factory()
            obj_.build(child_)
            self.set_Group_List(obj_)
        elif nodeName_ == 'Home_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Home_Directory(obj_)
        elif nodeName_ == 'Last_Login':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Login(obj_)
        elif nodeName_ == 'Privilege_List':
            obj_ = PrivilegeListType.factory()
            obj_.build(child_)
            self.set_Privilege_List(obj_)
        elif nodeName_ == 'Script_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Script_Path(obj_)
        elif nodeName_ == 'Username':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Username(obj_)
        elif nodeName_ == 'User_Password_Age':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Password_Age(obj_)
        super(UserAccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UserAccountObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'User_Password_Age': cybox_common.DurationObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Home_Directory': cybox_common.StringObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Account': account_object.AccountObjectType,
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
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Domain': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Name': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
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
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Last_Login': cybox_common.DateTimeObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
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
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
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
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
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
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="User_Account",
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
    "UserAccountObjectType",
    "PrivilegeListType",
    "PrivilegeType",
    "GroupListType",
    "GroupType"
    ]
