# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import dns_record_object
from . import uri_object


class DNSQuestionType(GeneratedsSuper):
    """The DNSQuestionType specifies the components of a DNS Question,
    including the domain name queried, type, and class."""

    subclass = None
    superclass = None
    def __init__(self, QName=None, QType=None, QClass=None):
        self.QName = QName
        self.QType = QType
        self.QClass = QClass
    def factory(*args_, **kwargs_):
        if DNSQuestionType.subclass:
            return DNSQuestionType.subclass(*args_, **kwargs_)
        else:
            return DNSQuestionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_QName(self): return self.QName
    def set_QName(self, QName): self.QName = QName
    def get_QType(self): return self.QType
    def set_QType(self, QType): self.QType = QType
    def validate_DNSRecordType(self, value):
        # Validate type DNSRecordType, a restriction on None.
        pass
    def get_QClass(self): return self.QClass
    def set_QClass(self, QClass): self.QClass = QClass
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.QName is not None or
            self.QType is not None or
            self.QClass is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSQuestionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSQuestionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DNSQueryObj:', name_='DNSQuestionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSQuestionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.QName is not None:
            self.QName.export(lwrite, level, 'DNSQueryObj:', name_='QName', pretty_print=pretty_print)
        if self.QType is not None:
            self.QType.export(lwrite, level, 'DNSQueryObj:', name_='QType', pretty_print=pretty_print)
        if self.QClass is not None:
            self.QClass.export(lwrite, level, 'DNSQueryObj:', name_='QClass', pretty_print=pretty_print)
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
        if nodeName_ == 'QName':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_QName(obj_)
        elif nodeName_ == 'QType':
            obj_ = DNSRecordType.factory()
            obj_.build(child_)
            self.set_QType(obj_)
        elif nodeName_ == 'QClass':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_QClass(obj_)
# end class DNSQuestionType

class DNSResourceRecordsType(GeneratedsSuper):
    """The DNSAnswersType encompasses one or more resource records returned
    for a DNS query."""

    subclass = None
    superclass = None
    def __init__(self, Resource_Record=None):
        if Resource_Record is None:
            self.Resource_Record = []
        else:
            self.Resource_Record = Resource_Record
    def factory(*args_, **kwargs_):
        if DNSResourceRecordsType.subclass:
            return DNSResourceRecordsType.subclass(*args_, **kwargs_)
        else:
            return DNSResourceRecordsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Resource_Record(self): return self.Resource_Record
    def set_Resource_Record(self, Resource_Record): self.Resource_Record = Resource_Record
    def add_Resource_Record(self, value): self.Resource_Record.append(value)
    def insert_Resource_Record(self, index, value): self.Resource_Record[index] = value
    def hasContent_(self):
        if (
            self.Resource_Record
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSResourceRecordsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSResourceRecordsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DNSQueryObj:', name_='DNSResourceRecordsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSResourceRecordsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Resource_Record_ in self.Resource_Record:
            Resource_Record_.export(lwrite, level, 'DNSQueryObj:', name_='Resource_Record', pretty_print=pretty_print)
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
        if nodeName_ == 'Resource_Record':
            obj_ = dns_record_object.DNSRecordObjectType.factory()
            obj_.build(child_)
            self.Resource_Record.append(obj_)
# end class DNSResourceRecordsType

class DNSRecordType(cybox_common.BaseObjectPropertyType):
    """DNSRecordType specifies DNS record types, via a union of the
    DNSRecordTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(DNSRecordType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DNSRecordType.subclass:
            return DNSRecordType.subclass(*args_, **kwargs_)
        else:
            return DNSRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DNSRecordType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSRecordType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DNSQueryObj:', name_='DNSRecordType'):
        super(DNSRecordType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSRecordType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSRecordType', fromsubclass_=False, pretty_print=True):
        super(DNSRecordType, self).exportChildren(lwrite, level, 'DNSQueryObj:', name_, True, pretty_print=pretty_print)
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
        super(DNSRecordType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DNSRecordType

class DNSQueryObjectType(cybox_common.ObjectPropertiesType):
    """The DNSQueryType is intended to characterize a single DNS query and
    its components.The successful field specifies whether or not the
    DNS Query was successful."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, successful=None, Transaction_ID=None, Question=None, Answer_Resource_Records=None, Authority_Resource_Records=None, Additional_Records=None, Date_Ran=None, Service_Used=None):
        super(DNSQueryObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.successful = _cast(bool, successful)
        self.Transaction_ID = Transaction_ID
        self.Question = Question
        self.Answer_Resource_Records = Answer_Resource_Records
        self.Authority_Resource_Records = Authority_Resource_Records
        self.Additional_Records = Additional_Records
        self.Date_Ran = Date_Ran
        self.Service_Used = Service_Used
    def factory(*args_, **kwargs_):
        if DNSQueryObjectType.subclass:
            return DNSQueryObjectType.subclass(*args_, **kwargs_)
        else:
            return DNSQueryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Transaction_ID(self): return self.Transaction_ID
    def set_Transaction_ID(self, Transaction_ID): self.Transaction_ID = Transaction_ID
    def get_Question(self): return self.Question
    def set_Question(self, Question): self.Question = Question
    def get_Answer_Resource_Records(self): return self.Answer_Resource_Records
    def set_Answer_Resource_Records(self, Answer_Resource_Records): self.Answer_Resource_Records = Answer_Resource_Records
    def get_Authority_Resource_Records(self): return self.Authority_Resource_Records
    def set_Authority_Resource_Records(self, Authority_Resource_Records): self.Authority_Resource_Records = Authority_Resource_Records
    def get_Additional_Records(self): return self.Additional_Records
    def set_Additional_Records(self, Additional_Records): self.Additional_Records = Additional_Records
    def get_Date_Ran(self): return self.Date_Ran
    def set_Date_Ran(self, Date_Ran): self.Date_Ran = Date_Ran
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Service_Used(self): return self.Service_Used
    def set_Service_Used(self, Service_Used): self.Service_Used = Service_Used
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_successful(self): return self.successful
    def set_successful(self, successful): self.successful = successful
    def hasContent_(self):
        if (
            self.Transaction_ID is not None or
            self.Question is not None or
            self.Answer_Resource_Records is not None or
            self.Authority_Resource_Records is not None or
            self.Additional_Records is not None or
            self.Date_Ran is not None or
            self.Service_Used is not None or
            super(DNSQueryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSQueryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSQueryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DNSQueryObj:', name_='DNSQueryObjectType'):
        super(DNSQueryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DNSQueryObjectType')
        if self.successful is not None:

            lwrite(' successful="%s"' % self.gds_format_boolean(self.successful, input_name='successful'))
    def exportChildren(self, lwrite, level, namespace_='DNSQueryObj:', name_='DNSQueryObjectType', fromsubclass_=False, pretty_print=True):
        super(DNSQueryObjectType, self).exportChildren(lwrite, level, 'DNSQueryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transaction_ID is not None:
            self.Transaction_ID.export(lwrite, level, 'DNSQueryObj:', name_='Transaction_ID', pretty_print=pretty_print)
        if self.Question is not None:
            self.Question.export(lwrite, level, 'DNSQueryObj:', name_='Question', pretty_print=pretty_print)
        if self.Answer_Resource_Records is not None:
            self.Answer_Resource_Records.export(lwrite, level, 'DNSQueryObj:', name_='Answer_Resource_Records', pretty_print=pretty_print)
        if self.Authority_Resource_Records is not None:
            self.Authority_Resource_Records.export(lwrite, level, 'DNSQueryObj:', name_='Authority_Resource_Records', pretty_print=pretty_print)
        if self.Additional_Records is not None:
            self.Additional_Records.export(lwrite, level, 'DNSQueryObj:', name_='Additional_Records', pretty_print=pretty_print)
        if self.Date_Ran is not None:
            self.Date_Ran.export(lwrite, level, 'DNSQueryObj:', name_='Date_Ran', pretty_print=pretty_print)
        if self.Service_Used is not None:
            self.Service_Used.export(lwrite, level, 'DNSQueryObj:', name_='Service_Used', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('successful', node)
        if value is not None:

            if value in ('true', '1'):
                self.successful = True
            elif value in ('false', '0'):
                self.successful = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(DNSQueryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Transaction_ID':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Transaction_ID(obj_)
        elif nodeName_ == 'Question':
            obj_ = DNSQuestionType.factory()
            obj_.build(child_)
            self.set_Question(obj_)
        elif nodeName_ == 'Answer_Resource_Records':
            obj_ = DNSResourceRecordsType.factory()
            obj_.build(child_)
            self.set_Answer_Resource_Records(obj_)
        elif nodeName_ == 'Authority_Resource_Records':
            obj_ = DNSResourceRecordsType.factory()
            obj_.build(child_)
            self.set_Authority_Resource_Records(obj_)
        elif nodeName_ == 'Additional_Records':
            obj_ = DNSResourceRecordsType.factory()
            obj_.build(child_)
            self.set_Additional_Records(obj_)
        elif nodeName_ == 'Date_Ran':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Date_Ran(obj_)
        elif nodeName_ == 'Service_Used':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_Used(obj_)
        super(DNSQueryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DNSQueryObjectType

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
    'DNS_Record': dns_record_object.DNSRecordObjectType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Resource_Record': dns_record_object.DNSRecordObjectType,
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
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'QName': uri_object.URIObjectType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
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
    'Date_Ran': cybox_common.DateTimeObjectPropertyType,
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
        rootTag = 'DNS_Query'
        rootClass = DNSQueryObjectType
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
        rootTag = 'DNS_Query'
        rootClass = DNSQueryObjectType
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
        rootTag = 'DNS_Query'
        rootClass = DNSQueryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="DNS_Query",
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
    "DNSQueryObjectType",
    "DNSQuestionType",
    "DNSResourceRecordsType",
    "DNSRecordType"
    ]
