# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class PartitionType(cybox_common.BaseObjectPropertyType):
    """PartitionType specifies partition types, via a union of the
    PartitionTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(PartitionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PartitionType.subclass:
            return PartitionType.subclass(*args_, **kwargs_)
        else:
            return PartitionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PartitionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DiskPartitionObj:', name_='PartitionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PartitionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DiskPartitionObj:', name_='PartitionType'):
        super(PartitionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PartitionType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='DiskPartitionObj:', name_='PartitionType', fromsubclass_=False, pretty_print=True):
        super(PartitionType, self).exportChildren(lwrite, level, 'DiskPartitionObj:', name_, True, pretty_print=pretty_print)
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
        super(PartitionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PartitionType

class DiskPartitionObjectType(cybox_common.ObjectPropertiesType):
    """The DiskPartitionType type is intended to characterize partitions of
    disk drives."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Created=None, Device_Name=None, Mount_Point=None, Partition_ID=None, Partition_Length=None, Partition_Offset=None, Space_Left=None, Space_Used=None, Total_Space=None, Type=None):
        super(DiskPartitionObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Created = Created
        self.Device_Name = Device_Name
        self.Mount_Point = Mount_Point
        self.Partition_ID = Partition_ID
        self.Partition_Length = Partition_Length
        self.Partition_Offset = Partition_Offset
        self.Space_Left = Space_Left
        self.Space_Used = Space_Used
        self.Total_Space = Total_Space
        self.Type = Type
    def factory(*args_, **kwargs_):
        if DiskPartitionObjectType.subclass:
            return DiskPartitionObjectType.subclass(*args_, **kwargs_)
        else:
            return DiskPartitionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Created(self): return self.Created
    def set_Created(self, Created): self.Created = Created
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Device_Name(self): return self.Device_Name
    def set_Device_Name(self, Device_Name): self.Device_Name = Device_Name
    def validate_NameObjectPropertyType(self, value):
        # Validate type cybox_common.NameObjectPropertyType, a restriction on None.
        pass
    def get_Mount_Point(self): return self.Mount_Point
    def set_Mount_Point(self, Mount_Point): self.Mount_Point = Mount_Point
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Partition_ID(self): return self.Partition_ID
    def set_Partition_ID(self, Partition_ID): self.Partition_ID = Partition_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Partition_Length(self): return self.Partition_Length
    def set_Partition_Length(self, Partition_Length): self.Partition_Length = Partition_Length
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Partition_Offset(self): return self.Partition_Offset
    def set_Partition_Offset(self, Partition_Offset): self.Partition_Offset = Partition_Offset
    def get_Space_Left(self): return self.Space_Left
    def set_Space_Left(self, Space_Left): self.Space_Left = Space_Left
    def get_Space_Used(self): return self.Space_Used
    def set_Space_Used(self, Space_Used): self.Space_Used = Space_Used
    def get_Total_Space(self): return self.Total_Space
    def set_Total_Space(self, Total_Space): self.Total_Space = Total_Space
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_PartitionType(self, value):
        # Validate type PartitionType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Created is not None or
            self.Device_Name is not None or
            self.Mount_Point is not None or
            self.Partition_ID is not None or
            self.Partition_Length is not None or
            self.Partition_Offset is not None or
            self.Space_Left is not None or
            self.Space_Used is not None or
            self.Total_Space is not None or
            self.Type is not None or
            super(DiskPartitionObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DiskPartitionObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType'):
        super(DiskPartitionObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DiskPartitionObjectType')
    def exportChildren(self, lwrite, level, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType', fromsubclass_=False, pretty_print=True):
        super(DiskPartitionObjectType, self).exportChildren(lwrite, level, 'DiskPartitionObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Created is not None:
            self.Created.export(lwrite, level, 'DiskPartitionObj:', name_='Created', pretty_print=pretty_print)
        if self.Device_Name is not None:
            self.Device_Name.export(lwrite, level, 'DiskPartitionObj:', name_='Device_Name', pretty_print=pretty_print)
        if self.Mount_Point is not None:
            self.Mount_Point.export(lwrite, level, 'DiskPartitionObj:', name_='Mount_Point', pretty_print=pretty_print)
        if self.Partition_ID is not None:
            self.Partition_ID.export(lwrite, level, 'DiskPartitionObj:', name_='Partition_ID', pretty_print=pretty_print)
        if self.Partition_Length is not None:
            self.Partition_Length.export(lwrite, level, 'DiskPartitionObj:', name_='Partition_Length', pretty_print=pretty_print)
        if self.Partition_Offset is not None:
            self.Partition_Offset.export(lwrite, level, 'DiskPartitionObj:', name_='Partition_Offset', pretty_print=pretty_print)
        if self.Space_Left is not None:
            self.Space_Left.export(lwrite, level, 'DiskPartitionObj:', name_='Space_Left', pretty_print=pretty_print)
        if self.Space_Used is not None:
            self.Space_Used.export(lwrite, level, 'DiskPartitionObj:', name_='Space_Used', pretty_print=pretty_print)
        if self.Total_Space is not None:
            self.Total_Space.export(lwrite, level, 'DiskPartitionObj:', name_='Total_Space', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'DiskPartitionObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DiskPartitionObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Created':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Created(obj_)
        elif nodeName_ == 'Device_Name':
            obj_ = cybox_common.NameObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Device_Name(obj_)
        elif nodeName_ == 'Mount_Point':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Mount_Point(obj_)
        elif nodeName_ == 'Partition_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Partition_ID(obj_)
        elif nodeName_ == 'Partition_Length':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Partition_Length(obj_)
        elif nodeName_ == 'Partition_Offset':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Partition_Offset(obj_)
        elif nodeName_ == 'Space_Left':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Space_Left(obj_)
        elif nodeName_ == 'Space_Used':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Space_Used(obj_)
        elif nodeName_ == 'Total_Space':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Total_Space(obj_)
        elif nodeName_ == 'Type':
            obj_ = PartitionType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(DiskPartitionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DiskPartitionObjectType

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
    'Mount_Point': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Created': cybox_common.DateTimeObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Partition_Length': cybox_common.UnsignedLongObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Partition_ID': cybox_common.IntegerObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
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
    'Total_Space': cybox_common.UnsignedLongObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Partition_Offset': cybox_common.UnsignedLongObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Space_Left': cybox_common.UnsignedLongObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Device_Name': cybox_common.NameObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Space_Used': cybox_common.UnsignedLongObjectPropertyType,
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
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
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
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
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
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Disk_Partition",
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
    "DiskPartitionObjectType",
    "PartitionType"
    ]
