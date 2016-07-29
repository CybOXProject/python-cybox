# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import hostname_object
from . import uri_object


class URLHistoryEntryType(GeneratedsSuper):
    """The URLHistoryEntryType captures the properties of a URL history
    entry for a particular browser."""

    subclass = None
    superclass = None
    def __init__(self, URL=None, Hostname=None, Referrer_URL=None, Page_Title=None, User_Profile_Name=None, Visit_Count=None, Manually_Entered_Count=None, Modification_DateTime=None, Expiration_DateTime=None, First_Visit_DateTime=None, Last_Visit_DateTime=None):
        self.URL = URL
        self.Hostname = Hostname
        self.Referrer_URL = Referrer_URL
        self.Page_Title = Page_Title
        self.User_Profile_Name = User_Profile_Name
        self.Visit_Count = Visit_Count
        self.Manually_Entered_Count = Manually_Entered_Count
        self.Modification_DateTime = Modification_DateTime
        self.Expiration_DateTime = Expiration_DateTime
        self.First_Visit_DateTime = First_Visit_DateTime
        self.Last_Visit_DateTime = Last_Visit_DateTime
    def factory(*args_, **kwargs_):
        if URLHistoryEntryType.subclass:
            return URLHistoryEntryType.subclass(*args_, **kwargs_)
        else:
            return URLHistoryEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_URL(self): return self.URL
    def set_URL(self, URL): self.URL = URL
    def get_Hostname(self): return self.Hostname
    def set_Hostname(self, Hostname): self.Hostname = Hostname
    def get_Referrer_URL(self): return self.Referrer_URL
    def set_Referrer_URL(self, Referrer_URL): self.Referrer_URL = Referrer_URL
    def get_Page_Title(self): return self.Page_Title
    def set_Page_Title(self, Page_Title): self.Page_Title = Page_Title
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_User_Profile_Name(self): return self.User_Profile_Name
    def set_User_Profile_Name(self, User_Profile_Name): self.User_Profile_Name = User_Profile_Name
    def get_Visit_Count(self): return self.Visit_Count
    def set_Visit_Count(self, Visit_Count): self.Visit_Count = Visit_Count
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Manually_Entered_Count(self): return self.Manually_Entered_Count
    def set_Manually_Entered_Count(self, Manually_Entered_Count): self.Manually_Entered_Count = Manually_Entered_Count
    def get_Modification_DateTime(self): return self.Modification_DateTime
    def set_Modification_DateTime(self, Modification_DateTime): self.Modification_DateTime = Modification_DateTime
    def get_Expiration_DateTime(self): return self.Expiration_DateTime
    def set_Expiration_DateTime(self, Expiration_DateTime): self.Expiration_DateTime = Expiration_DateTime
    def get_First_Visit_DateTime(self): return self.First_Visit_DateTime
    def set_First_Visit_DateTime(self, First_Visit_DateTime): self.First_Visit_DateTime = First_Visit_DateTime
    def get_Last_Visit_DateTime(self): return self.Last_Visit_DateTime
    def set_Last_Visit_DateTime(self, Last_Visit_DateTime): self.Last_Visit_DateTime = Last_Visit_DateTime
    def hasContent_(self):
        if (
            self.URL is not None or
            self.Hostname is not None or
            self.Referrer_URL is not None or
            self.Page_Title is not None or
            self.User_Profile_Name is not None or
            self.Visit_Count is not None or
            self.Manually_Entered_Count is not None or
            self.Modification_DateTime is not None or
            self.Expiration_DateTime is not None or
            self.First_Visit_DateTime is not None or
            self.Last_Visit_DateTime is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='URLHistoryObj:', name_='URLHistoryEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='URLHistoryEntryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='URLHistoryObj:', name_='URLHistoryEntryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='URLHistoryObj:', name_='URLHistoryEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.URL is not None:
            self.URL.export(lwrite, level, 'URLHistoryObj:', name_='URL', pretty_print=pretty_print)
        if self.Hostname is not None:
            self.Hostname.export(lwrite, level, 'URLHistoryObj:', name_='Hostname', pretty_print=pretty_print)
        if self.Referrer_URL is not None:
            self.Referrer_URL.export(lwrite, level, 'URLHistoryObj:', name_='Referrer_URL', pretty_print=pretty_print)
        if self.Page_Title is not None:
            self.Page_Title.export(lwrite, level, 'URLHistoryObj:', name_='Page_Title', pretty_print=pretty_print)
        if self.User_Profile_Name is not None:
            self.User_Profile_Name.export(lwrite, level, 'URLHistoryObj:', name_='User_Profile_Name', pretty_print=pretty_print)
        if self.Visit_Count is not None:
            self.Visit_Count.export(lwrite, level, 'URLHistoryObj:', name_='Visit_Count', pretty_print=pretty_print)
        if self.Manually_Entered_Count is not None:
            self.Manually_Entered_Count.export(lwrite, level, 'URLHistoryObj:', name_='Manually_Entered_Count', pretty_print=pretty_print)
        if self.Modification_DateTime is not None:
            self.Modification_DateTime.export(lwrite, level, 'URLHistoryObj:', name_='Modification_DateTime', pretty_print=pretty_print)
        if self.Expiration_DateTime is not None:
            self.Expiration_DateTime.export(lwrite, level, 'URLHistoryObj:', name_='Expiration_DateTime', pretty_print=pretty_print)
        if self.First_Visit_DateTime is not None:
            self.First_Visit_DateTime.export(lwrite, level, 'URLHistoryObj:', name_='First_Visit_DateTime', pretty_print=pretty_print)
        if self.Last_Visit_DateTime is not None:
            self.Last_Visit_DateTime.export(lwrite, level, 'URLHistoryObj:', name_='Last_Visit_DateTime', pretty_print=pretty_print)
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
        if nodeName_ == 'URL':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_URL(obj_)
        elif nodeName_ == 'Hostname':
            obj_ = hostname_object.HostnameObjectType.factory()
            obj_.build(child_)
            self.set_Hostname(obj_)
        elif nodeName_ == 'Referrer_URL':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Referrer_URL(obj_)
        elif nodeName_ == 'Page_Title':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Page_Title(obj_)
        elif nodeName_ == 'User_Profile_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Profile_Name(obj_)
        elif nodeName_ == 'Visit_Count':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Visit_Count(obj_)
        elif nodeName_ == 'Manually_Entered_Count':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Manually_Entered_Count(obj_)
        elif nodeName_ == 'Modification_DateTime':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Modification_DateTime(obj_)
        elif nodeName_ == 'Expiration_DateTime':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Expiration_DateTime(obj_)
        elif nodeName_ == 'First_Visit_DateTime':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_First_Visit_DateTime(obj_)
        elif nodeName_ == 'Last_Visit_DateTime':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Visit_DateTime(obj_)
# end class URLHistoryEntryType

class URLHistoryObjectType(cybox_common.ObjectPropertiesType):
    """The URLHistoryObject type is intended to characterize the stored URL
    history for a particular web browser."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Browser_Information=None, URL_History_Entry=None):
        super(URLHistoryObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.Browser_Information = Browser_Information
        if URL_History_Entry is None:
            self.URL_History_Entry = []
        else:
            self.URL_History_Entry = URL_History_Entry
    def factory(*args_, **kwargs_):
        if URLHistoryObjectType.subclass:
            return URLHistoryObjectType.subclass(*args_, **kwargs_)
        else:
            return URLHistoryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Browser_Information(self): return self.Browser_Information
    def set_Browser_Information(self, Browser_Information): self.Browser_Information = Browser_Information
    def get_URL_History_Entry(self): return self.URL_History_Entry
    def set_URL_History_Entry(self, URL_History_Entry): self.URL_History_Entry = URL_History_Entry
    def add_URL_History_Entry(self, value): self.URL_History_Entry.append(value)
    def insert_URL_History_Entry(self, index, value): self.URL_History_Entry[index] = value
    def hasContent_(self):
        if (
            self.Browser_Information is not None or
            self.URL_History_Entry or
            super(URLHistoryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='URLHistoryObj:', name_='URLHistoryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='URLHistoryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='URLHistoryObj:', name_='URLHistoryObjectType'):
        super(URLHistoryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='URLHistoryObjectType')
    def exportChildren(self, lwrite, level, namespace_='URLHistoryObj:', name_='URLHistoryObjectType', fromsubclass_=False, pretty_print=True):
        super(URLHistoryObjectType, self).exportChildren(lwrite, level, 'URLHistoryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Browser_Information is not None:
            self.Browser_Information.export(lwrite, level, 'URLHistoryObj:', name_='Browser_Information', pretty_print=pretty_print)
        for URL_History_Entry_ in self.URL_History_Entry:
            URL_History_Entry_.export(lwrite, level, 'URLHistoryObj:', name_='URL_History_Entry', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(URLHistoryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Browser_Information':
            obj_ = cybox_common.ToolInformationType.factory()
            obj_.build(child_)
            self.set_Browser_Information(obj_)
        elif nodeName_ == 'URL_History_Entry':
            obj_ = URLHistoryEntryType.factory()
            obj_.build(child_)
            self.URL_History_Entry.append(obj_)
        super(URLHistoryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class URLHistoryObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Last_Visit_DateTime': cybox_common.DateTimeObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'URL': uri_object.URIObjectType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'URI': uri_object.URIObjectType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Hostname_Value': cybox_common.StringObjectPropertyType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
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
    'Page_Title': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Naming_System': cybox_common.StringObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Modification_DateTime': cybox_common.DateTimeObjectPropertyType,
    'Observable_Location': cybox_common.LocationType,
    'Expiration_DateTime': cybox_common.DateTimeObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
    'Hostname': hostname_object.HostnameObjectType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Manually_Entered_Count': cybox_common.NonNegativeIntegerObjectPropertyType,
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
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'Libraries': cybox_common.LibrariesType,
    'Visit_Count': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'User_Profile_Name': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Browser_Information': cybox_common.ToolInformationType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Referrer_URL': uri_object.URIObjectType,
    'End_Time': cybox_common.DateTimeWithPrecisionType,
    'First_Visit_DateTime': cybox_common.DateTimeObjectPropertyType,
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
        rootTag = 'URL_History'
        rootClass = URLHistoryObjectType
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
        rootTag = 'URL_History'
        rootClass = URLHistoryObjectType
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
        rootTag = 'URL_History'
        rootClass = URLHistoryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="URL_History",
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
    "URLHistoryObjectType",
    "URLHistoryEntryType"
    ]
