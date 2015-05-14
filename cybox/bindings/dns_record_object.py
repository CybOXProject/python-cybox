# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object
from . import uri_object


class DNSRecordObjectType(cybox_common.ObjectPropertiesType):
    """The DNSRecordObjectType type is intended to characterize an
    individual DNS record."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Description=None, Queried_Date=None, Domain_Name=None, IP_Address=None, Address_Class=None, Entry_Type=None, Record_Name=None, Record_Type=None, TTL=None, Flags=None, Data_Length=None, Record_Data=None):
        super(DNSRecordObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Description = Description
        self.Queried_Date = Queried_Date
        self.Domain_Name = Domain_Name
        self.IP_Address = IP_Address
        self.Address_Class = Address_Class
        self.Entry_Type = Entry_Type
        self.Record_Name = Record_Name
        self.Record_Type = Record_Type
        self.TTL = TTL
        self.Flags = Flags
        self.Data_Length = Data_Length
        self.Record_Data = Record_Data
    def factory(*args_, **kwargs_):
        if DNSRecordObjectType.subclass:
            return DNSRecordObjectType.subclass(*args_, **kwargs_)
        else:
            return DNSRecordObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Queried_Date(self): return self.Queried_Date
    def set_Queried_Date(self, Queried_Date): self.Queried_Date = Queried_Date
    def get_Domain_Name(self): return self.Domain_Name
    def set_Domain_Name(self, Domain_Name): self.Domain_Name = Domain_Name
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def get_Address_Class(self): return self.Address_Class
    def set_Address_Class(self, Address_Class): self.Address_Class = Address_Class
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Entry_Type(self): return self.Entry_Type
    def set_Entry_Type(self, Entry_Type): self.Entry_Type = Entry_Type
    def get_Record_Name(self): return self.Record_Name
    def set_Record_Name(self, Record_Name): self.Record_Name = Record_Name
    def get_Record_Type(self): return self.Record_Type
    def set_Record_Type(self, Record_Type): self.Record_Type = Record_Type
    def get_TTL(self): return self.TTL
    def set_TTL(self, TTL): self.TTL = TTL
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Flags(self): return self.Flags
    def set_Flags(self, Flags): self.Flags = Flags
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Data_Length(self): return self.Data_Length
    def set_Data_Length(self, Data_Length): self.Data_Length = Data_Length
    def get_Record_Data(self): return self.Record_Data
    def set_Record_Data(self, Record_Data): self.Record_Data = Record_Data
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Queried_Date is not None or
            self.Domain_Name is not None or
            self.IP_Address is not None or
            self.Address_Class is not None or
            self.Entry_Type is not None or
            self.Record_Name is not None or
            self.Record_Type is not None or
            self.TTL is not None or
            self.Flags is not None or
            self.Data_Length is not None or
            self.Record_Data is not None or
            super(DNSRecordObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DNSRecordObj:', name_='DNSRecordObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSRecordObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DNSRecordObj:', name_='DNSRecordObjectType'):
        super(DNSRecordObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSRecordObjectType')
    def exportChildren(self, lwrite, level, namespace_='DNSRecordObj:', name_='DNSRecordObjectType', fromsubclass_=False, pretty_print=True):
        super(DNSRecordObjectType, self).exportChildren(lwrite, level, 'DNSRecordObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'DNSRecordObj:', name_='Description', pretty_print=pretty_print)
        if self.Queried_Date is not None:
            self.Queried_Date.export(lwrite, level, 'DNSRecordObj:', name_='Queried_Date', pretty_print=pretty_print)
        if self.Domain_Name is not None:
            self.Domain_Name.export(lwrite, level, 'DNSRecordObj:', name_='Domain_Name', pretty_print=pretty_print)
        if self.IP_Address is not None:
            self.IP_Address.export(lwrite, level, 'DNSRecordObj:', name_='IP_Address', pretty_print=pretty_print)
        if self.Address_Class is not None:
            self.Address_Class.export(lwrite, level, 'DNSRecordObj:', name_='Address_Class', pretty_print=pretty_print)
        if self.Entry_Type is not None:
            self.Entry_Type.export(lwrite, level, 'DNSRecordObj:', name_='Entry_Type', pretty_print=pretty_print)
        if self.Record_Name is not None:
            self.Record_Name.export(lwrite, level, 'DNSRecordObj:', name_='Record_Name', pretty_print=pretty_print)
        if self.Record_Type is not None:
            self.Record_Type.export(lwrite, level, 'DNSRecordObj:', name_='Record_Type', pretty_print=pretty_print)
        if self.TTL is not None:
            self.TTL.export(lwrite, level, 'DNSRecordObj:', name_='TTL', pretty_print=pretty_print)
        if self.Flags is not None:
            self.Flags.export(lwrite, level, 'DNSRecordObj:', name_='Flags', pretty_print=pretty_print)
        if self.Data_Length is not None:
            self.Data_Length.export(lwrite, level, 'DNSRecordObj:', name_='Data_Length', pretty_print=pretty_print)
        if self.Record_Data is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRecord_Data>%s</%sRecord_Data>%s' % ('DNSRecordObj:', self.gds_format_string(quote_xml(self.Record_Data), input_name='Record_Data'), 'DNSRecordObj:', eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DNSRecordObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Queried_Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Queried_Date(obj_)
        elif nodeName_ == 'Domain_Name':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Domain_Name(obj_)
        elif nodeName_ == 'IP_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
        elif nodeName_ == 'Address_Class':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address_Class(obj_)
        elif nodeName_ == 'Entry_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Entry_Type(obj_)
        elif nodeName_ == 'Record_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Record_Name(obj_)
        elif nodeName_ == 'Record_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Record_Type(obj_)
        elif nodeName_ == 'TTL':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TTL(obj_)
        elif nodeName_ == 'Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flags(obj_)
        elif nodeName_ == 'Data_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data_Length(obj_)
        elif nodeName_ == 'Record_Data':
            Record_Data_ = child_.text
            Record_Data_ = self.gds_validate_string(Record_Data_, node, 'Record_Data')
            self.Record_Data = Record_Data_
        super(DNSRecordObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DNSRecordObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'URI': uri_object.URIObjectType,
    'Value': cybox_common.AnyURIObjectPropertyType,
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
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'IP_Address': address_object.AddressObjectType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Domain_Name': uri_object.URIObjectType,
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
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Tool': cybox_common.ToolInformationType,
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
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
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
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
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
    from six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="DNS_Record",
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
    "DNSRecordObjectType"
    ]
