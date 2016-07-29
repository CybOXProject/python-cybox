# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class AuthenticationType(GeneratedsSuper):
    """The AuthenticationType type specifies authentication information for
    an account."""
    subclass = None
    superclass = None
    def __init__(self, Authentication_Type=None, Authentication_Data=None, Authentication_Token_Protection_Mechanism=None, Structured_Authentication_Mechanism=None):
        self.Authentication_Type = Authentication_Type
        self.Authentication_Data = Authentication_Data
        self.Authentication_Token_Protection_Mechanism = Authentication_Token_Protection_Mechanism
        self.Structured_Authentication_Mechanism = Structured_Authentication_Mechanism
    def factory(*args_, **kwargs_):
        if AuthenticationType.subclass:
            return AuthenticationType.subclass(*args_, **kwargs_)
        else:
            return AuthenticationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Authentication_Type(self): return self.Authentication_Type
    def set_Authentication_Type(self, Authentication_Type): self.Authentication_Type = Authentication_Type
    def get_Authentication_Data(self): return self.Authentication_Data
    def set_Authentication_Data(self, Authentication_Data): self.Authentication_Data = Authentication_Data
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Authentication_Token_Protection_Mechanism(self): return self.Authentication_Token_Protection_Mechanism
    def set_Authentication_Token_Protection_Mechanism(self, Authentication_Token_Protection_Mechanism): self.Authentication_Token_Protection_Mechanism = Authentication_Token_Protection_Mechanism
    def get_Structured_Authentication_Mechanism(self): return self.Structured_Authentication_Mechanism
    def set_Structured_Authentication_Mechanism(self, Structured_Authentication_Mechanism): self.Structured_Authentication_Mechanism = Structured_Authentication_Mechanism
    def hasContent_(self):
        if (
            self.Authentication_Type is not None or
            self.Authentication_Data is not None or
            self.Authentication_Token_Protection_Mechanism is not None or
            self.Structured_Authentication_Mechanism is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='AccountObj:', name_='AuthenticationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AuthenticationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AccountObj:', name_='AuthenticationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='AccountObj:', name_='AuthenticationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Authentication_Type is not None:
            self.Authentication_Type.export(lwrite, level, 'AccountObj:', name_='Authentication_Type', pretty_print=pretty_print)
        if self.Authentication_Data is not None:
            self.Authentication_Data.export(lwrite, level, 'AccountObj:', name_='Authentication_Data', pretty_print=pretty_print)
        if self.Authentication_Token_Protection_Mechanism is not None:
            self.Authentication_Token_Protection_Mechanism.export(lwrite, level, 'AccountObj:', name_='Authentication_Token_Protection_Mechanism', pretty_print=pretty_print)
        if self.Structured_Authentication_Mechanism is not None:
            self.Structured_Authentication_Mechanism.export(lwrite, level, 'AccountObj:', name_='Structured_Authentication_Mechanism', pretty_print=pretty_print)
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
        if nodeName_ == 'Authentication_Type':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Authentication_Type(obj_)
        elif nodeName_ == 'Authentication_Data':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Authentication_Data(obj_)
        elif nodeName_ == 'Authentication_Token_Protection_Mechanism':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Authentication_Token_Protection_Mechanism(obj_)
        elif nodeName_ == 'Structured_Authentication_Mechanism':
            obj_ = StructuredAuthenticationMechanismType.factory()
            obj_.build(child_)
            self.set_Structured_Authentication_Mechanism(obj_)
# end class AuthenticationType

class StructuredAuthenticationMechanismType(GeneratedsSuper):
    """Characterizes the description of an authentication mechanism, such
    as biometrics-based authentication.In addition to capturing
    basic information, this type is intended to be extended to
    enable the structured description of an authentication mechanism
    using the XML Schema extension feature. No extension is provided
    by CybOX to support this, however those wishing to represent
    structured authentication mechanism information may develop such
    an extension."""
    subclass = None
    superclass = None
    def __init__(self, Description=None):
        self.Description = Description
    def factory(*args_, **kwargs_):
        if StructuredAuthenticationMechanismType.subclass:
            return StructuredAuthenticationMechanismType.subclass(*args_, **kwargs_)
        else:
            return StructuredAuthenticationMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def hasContent_(self):
        if (
            self.Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='AccountObj:', name_='StructuredAuthenticationMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StructuredAuthenticationMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AccountObj:', name_='StructuredAuthenticationMechanismType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='AccountObj:', name_='StructuredAuthenticationMechanismType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'AccountObj:', name_='Description', pretty_print=pretty_print)
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
        if nodeName_ == 'Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
# end class StructuredAuthenticationMechanismType


class AccountObjectType(cybox_common.ObjectPropertiesType):
    """The AccountObjectType type is intended to characterize generic
    accounts.The disabled field specifies whether or not the account
    is disabled.The locked_out field specifies whether or not the
    account is locked out."""
    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, disabled=None, locked_out=None, Description=None, Domain=None, Authentication=None, Creation_Date=None, Modified_Date=None, Last_Accessed_Time=None):
        super(AccountObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.disabled = _cast(bool, disabled)
        self.locked_out = _cast(bool, locked_out)
        self.Description = Description
        self.Domain = Domain
        if Authentication is None:
            self.Authentication = []
        else:
            self.Authentication = Authentication
        self.Creation_Date = Creation_Date
        self.Modified_Date = Modified_Date
        self.Last_Accessed_Time = Last_Accessed_Time
    def factory(*args_, **kwargs_):
        if AccountObjectType.subclass:
            return AccountObjectType.subclass(*args_, **kwargs_)
        else:
            return AccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Domain(self): return self.Domain
    def set_Domain(self, Domain): self.Domain = Domain
    def get_Authentication(self): return self.Authentication
    def set_Authentication(self, Authentication): self.Authentication = Authentication
    def add_Authentication(self, value): self.Authentication.append(value)
    def insert_Authentication(self, index, value): self.Authentication[index] = value
    def get_Creation_Date(self): return self.Creation_Date
    def set_Creation_Date(self, Creation_Date): self.Creation_Date = Creation_Date
    def get_Modified_Date(self): return self.Modified_Date
    def set_Modified_Date(self, Modified_Date): self.Modified_Date = Modified_Date
    def get_Last_Accessed_Time(self): return self.Last_Accessed_Time
    def set_Last_Accessed_Time(self, Last_Accessed_Time): self.Last_Accessed_Time = Last_Accessed_Time
    def get_disabled(self): return self.disabled
    def set_disabled(self, disabled): self.disabled = disabled
    def get_locked_out(self): return self.locked_out
    def set_locked_out(self, locked_out): self.locked_out = locked_out
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Domain is not None or
            self.Authentication or
            self.Creation_Date is not None or
            self.Modified_Date is not None or
            self.Last_Accessed_Time is not None or
            super(AccountObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='AccountObj:', name_='AccountObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AccountObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AccountObj:', name_='AccountObjectType'):
        super(AccountObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AccountObjectType')
        if self.disabled is not None:

            lwrite(' disabled="%s"' % self.gds_format_boolean(self.disabled, input_name='disabled'))
        if self.locked_out is not None:

            lwrite(' locked_out="%s"' % self.gds_format_boolean(self.locked_out, input_name='locked_out'))
    def exportChildren(self, lwrite, level, namespace_='AccountObj:', name_='AccountObjectType', fromsubclass_=False, pretty_print=True):
        super(AccountObjectType, self).exportChildren(lwrite, level, 'AccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'AccountObj:', name_='Description', pretty_print=pretty_print)
        if self.Domain is not None:
            self.Domain.export(lwrite, level, 'AccountObj:', name_='Domain', pretty_print=pretty_print)
        for Authentication_ in self.Authentication:
            Authentication_.export(lwrite, level, 'AccountObj:', name_='Authentication', pretty_print=pretty_print)
        if self.Creation_Date is not None:
            self.Creation_Date.export(lwrite, level, 'AccountObj:', name_='Creation_Date', pretty_print=pretty_print)
        if self.Modified_Date is not None:
            self.Modified_Date.export(lwrite, level, 'AccountObj:', name_='Modified_Date', pretty_print=pretty_print)
        if self.Last_Accessed_Time is not None:
            self.Last_Accessed_Time.export(lwrite, level, 'AccountObj:', name_='Last_Accessed_Time', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('disabled', node)
        if value is not None:

            if value in ('true', '1'):
                self.disabled = True
            elif value in ('false', '0'):
                self.disabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('locked_out', node)
        if value is not None:

            if value in ('true', '1'):
                self.locked_out = True
            elif value in ('false', '0'):
                self.locked_out = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(AccountObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Domain':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Domain(obj_)
        elif nodeName_ == 'Authentication':
            obj_ = AuthenticationType.factory()
            obj_.build(child_)
            self.Authentication.append(obj_)
        elif nodeName_ == 'Creation_Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Date(obj_)
        elif nodeName_ == 'Modified_Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Modified_Date(obj_)
        elif nodeName_ == 'Last_Accessed_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Accessed_Time(obj_)
        super(AccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class AccountObjectType

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
    'Identifier': cybox_common.PlatformIdentifierType,
    'Strings': cybox_common.ExtractedStringsType,
    'Domain': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
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
        rootTag = 'Account'
        rootClass = AccountObjectType
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
        rootTag = 'Account'
        rootClass = AccountObjectType
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
        rootTag = 'Account'
        rootClass = AccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Account",
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
    "AccountObjectType"
    ]
