# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class SMSMessageObjectType(cybox_common.ObjectPropertiesType):
    """The SMSMessageObjectType is intended to characterize Short Message
    Service (SMS) messages.The is_premium field specifies whether
    the SMS message is a premium (i.e. fee-collecting) message."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_premium=None, Sender_Phone_Number=None, Recipient_Phone_Number=None, Sent_DateTime=None, Body=None, Length=None, Size=None, Encoding=None, Bits_Per_Character=None, User_Data_Header=None):
        super(SMSMessageObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.is_premium = _cast(bool, is_premium)
        self.Sender_Phone_Number = Sender_Phone_Number
        self.Recipient_Phone_Number = Recipient_Phone_Number
        self.Sent_DateTime = Sent_DateTime
        self.Body = Body
        self.Length = Length
        self.Size = Size
        self.Encoding = Encoding
        self.Bits_Per_Character = Bits_Per_Character
        self.User_Data_Header = User_Data_Header
    def factory(*args_, **kwargs_):
        if SMSMessageObjectType.subclass:
            return SMSMessageObjectType.subclass(*args_, **kwargs_)
        else:
            return SMSMessageObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Sender_Phone_Number(self): return self.Sender_Phone_Number
    def set_Sender_Phone_Number(self, Sender_Phone_Number): self.Sender_Phone_Number = Sender_Phone_Number
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Recipient_Phone_Number(self): return self.Recipient_Phone_Number
    def set_Recipient_Phone_Number(self, Recipient_Phone_Number): self.Recipient_Phone_Number = Recipient_Phone_Number
    def get_Sent_DateTime(self): return self.Sent_DateTime
    def set_Sent_DateTime(self, Sent_DateTime): self.Sent_DateTime = Sent_DateTime
    def get_Body(self): return self.Body
    def set_Body(self, Body): self.Body = Body
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Size(self): return self.Size
    def set_Size(self, Size): self.Size = Size
    def get_Encoding(self): return self.Encoding
    def set_Encoding(self, Encoding): self.Encoding = Encoding
    def get_Bits_Per_Character(self): return self.Bits_Per_Character
    def set_Bits_Per_Character(self, Bits_Per_Character): self.Bits_Per_Character = Bits_Per_Character
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_User_Data_Header(self): return self.User_Data_Header
    def set_User_Data_Header(self, User_Data_Header): self.User_Data_Header = User_Data_Header
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_is_premium(self): return self.is_premium
    def set_is_premium(self, is_premium): self.is_premium = is_premium
    def hasContent_(self):
        if (
            self.Sender_Phone_Number is not None or
            self.Recipient_Phone_Number is not None or
            self.Sent_DateTime is not None or
            self.Body is not None or
            self.Length is not None or
            self.Size is not None or
            self.Encoding is not None or
            self.Bits_Per_Character is not None or
            self.User_Data_Header is not None or
            super(SMSMessageObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SMSMessageObj:', name_='SMSMessageObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SMSMessageObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SMSMessageObj:', name_='SMSMessageObjectType'):
        super(SMSMessageObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SMSMessageObjectType')
        if self.is_premium is not None:

            lwrite(' is_premium="%s"' % self.gds_format_boolean(self.is_premium, input_name='is_premium'))
    def exportChildren(self, lwrite, level, namespace_='SMSMessageObj:', name_='SMSMessageObjectType', fromsubclass_=False, pretty_print=True):
        super(SMSMessageObjectType, self).exportChildren(lwrite, level, 'SMSMessageObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Sender_Phone_Number is not None:
            self.Sender_Phone_Number.export(lwrite, level, 'SMSMessageObj:', name_='Sender_Phone_Number', pretty_print=pretty_print)
        if self.Recipient_Phone_Number is not None:
            self.Recipient_Phone_Number.export(lwrite, level, 'SMSMessageObj:', name_='Recipient_Phone_Number', pretty_print=pretty_print)
        if self.Sent_DateTime is not None:
            self.Sent_DateTime.export(lwrite, level, 'SMSMessageObj:', name_='Sent_DateTime', pretty_print=pretty_print)
        if self.Body is not None:
            self.Body.export(lwrite, level, 'SMSMessageObj:', name_='Body', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'SMSMessageObj:', name_='Length', pretty_print=pretty_print)
        if self.Size is not None:
            self.Size.export(lwrite, level, 'SMSMessageObj:', name_='Size', pretty_print=pretty_print)
        if self.Encoding is not None:
            self.Encoding.export(lwrite, level, 'SMSMessageObj:', name_='Encoding', pretty_print=pretty_print)
        if self.Bits_Per_Character is not None:
            self.Bits_Per_Character.export(lwrite, level, 'SMSMessageObj:', name_='Bits_Per_Character', pretty_print=pretty_print)
        if self.User_Data_Header is not None:
            self.User_Data_Header.export(lwrite, level, 'SMSMessageObj:', name_='User_Data_Header', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_premium', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_premium = True
            elif value in ('false', '0'):
                self.is_premium = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(SMSMessageObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Sender_Phone_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sender_Phone_Number(obj_)
        elif nodeName_ == 'Recipient_Phone_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Recipient_Phone_Number(obj_)
        elif nodeName_ == 'Sent_DateTime':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sent_DateTime(obj_)
        elif nodeName_ == 'Body':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Body(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Size':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size(obj_)
        elif nodeName_ == 'Encoding':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Encoding(obj_)
        elif nodeName_ == 'Bits_Per_Character':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Bits_Per_Character(obj_)
        elif nodeName_ == 'User_Data_Header':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Data_Header(obj_)
        super(SMSMessageObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class SMSMessageObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Body': cybox_common.StringObjectPropertyType,
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
    'Sent_DateTime': cybox_common.DateTimeObjectPropertyType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Start_Date': cybox_common.DateWithPrecisionType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeWithPrecisionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'User_Data_Header': cybox_common.HexBinaryObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Observable_Location': cybox_common.LocationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Recipient_Phone_Number': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
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
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Size': cybox_common.IntegerObjectPropertyType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Sender_Phone_Number': cybox_common.StringObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Bits_Per_Character': cybox_common.PositiveIntegerObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'End_Time': cybox_common.DateTimeWithPrecisionType,
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
        rootTag = 'SMS_Message'
        rootClass = SMSMessageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SMS_Message'
        rootClass = SMSMessageObjectType
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
        rootTag = 'SMS_Message'
        rootClass = SMSMessageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="SMS_Message",
        namespacedef_='')
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
    "SMSMessageObjectType"
    ]
