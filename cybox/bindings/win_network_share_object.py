# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class SharedResourceType(cybox_common.BaseObjectPropertyType):
    """SharedResourceType specifies Windows shared resource types via a
    union of the SharedResourceTypeEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""
    
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SharedResourceType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SharedResourceType.subclass:
            return SharedResourceType.subclass(*args_, **kwargs_)
        else:
            return SharedResourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SharedResourceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinNetworkShareObj:', name_='SharedResourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SharedResourceType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinNetworkShareObj:', name_='SharedResourceType'):
        super(SharedResourceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SharedResourceType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinNetworkShareObj:', name_='SharedResourceType', fromsubclass_=False, pretty_print=True):
        super(SharedResourceType, self).exportChildren(lwrite, level, 'WinNetworkShareObj:', name_, True, pretty_print=pretty_print)
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
        super(SharedResourceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SharedResourceType

class WindowsNetworkShareObjectType(cybox_common.ObjectPropertiesType):
    """he WindowsNetworkShareObjectType type is intended to characterize
    Windows network shares."""
    
    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, ACCESS_PERM=None, ACCESS_ATRIB=None, ACCESS_ALL=None, ACCESS_READ=None, ACCESS_DELETE=None, ACCESS_WRITE=None, ACCESS_CREATE=None, ACCESS_EXEC=None, Current_Uses=None, Local_Path=None, Max_Uses=None, Netname=None, Type=None):
        super(WindowsNetworkShareObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.ACCESS_PERM = _cast(bool, ACCESS_PERM)
        self.ACCESS_ATRIB = _cast(bool, ACCESS_ATRIB)
        self.ACCESS_ALL = _cast(bool, ACCESS_ALL)
        self.ACCESS_READ = _cast(bool, ACCESS_READ)
        self.ACCESS_DELETE = _cast(bool, ACCESS_DELETE)
        self.ACCESS_WRITE = _cast(bool, ACCESS_WRITE)
        self.ACCESS_CREATE = _cast(bool, ACCESS_CREATE)
        self.ACCESS_EXEC = _cast(bool, ACCESS_EXEC)
        self.Current_Uses = Current_Uses
        self.Local_Path = Local_Path
        self.Max_Uses = Max_Uses
        self.Netname = Netname
        self.Type = Type
    def factory(*args_, **kwargs_):
        if WindowsNetworkShareObjectType.subclass:
            return WindowsNetworkShareObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsNetworkShareObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Current_Uses(self): return self.Current_Uses
    def set_Current_Uses(self, Current_Uses): self.Current_Uses = Current_Uses
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Local_Path(self): return self.Local_Path
    def set_Local_Path(self, Local_Path): self.Local_Path = Local_Path
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Max_Uses(self): return self.Max_Uses
    def set_Max_Uses(self, Max_Uses): self.Max_Uses = Max_Uses
    def get_Netname(self): return self.Netname
    def set_Netname(self, Netname): self.Netname = Netname
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_SharedResourceType(self, value):
        # Validate type SharedResourceType, a restriction on None.
        pass
    def get_ACCESS_PERM(self): return self.ACCESS_PERM
    def set_ACCESS_PERM(self, ACCESS_PERM): self.ACCESS_PERM = ACCESS_PERM
    def get_ACCESS_ATRIB(self): return self.ACCESS_ATRIB
    def set_ACCESS_ATRIB(self, ACCESS_ATRIB): self.ACCESS_ATRIB = ACCESS_ATRIB
    def get_ACCESS_ALL(self): return self.ACCESS_ALL
    def set_ACCESS_ALL(self, ACCESS_ALL): self.ACCESS_ALL = ACCESS_ALL
    def get_ACCESS_READ(self): return self.ACCESS_READ
    def set_ACCESS_READ(self, ACCESS_READ): self.ACCESS_READ = ACCESS_READ
    def get_ACCESS_DELETE(self): return self.ACCESS_DELETE
    def set_ACCESS_DELETE(self, ACCESS_DELETE): self.ACCESS_DELETE = ACCESS_DELETE
    def get_ACCESS_WRITE(self): return self.ACCESS_WRITE
    def set_ACCESS_WRITE(self, ACCESS_WRITE): self.ACCESS_WRITE = ACCESS_WRITE
    def get_ACCESS_CREATE(self): return self.ACCESS_CREATE
    def set_ACCESS_CREATE(self, ACCESS_CREATE): self.ACCESS_CREATE = ACCESS_CREATE
    def get_ACCESS_EXEC(self): return self.ACCESS_EXEC
    def set_ACCESS_EXEC(self, ACCESS_EXEC): self.ACCESS_EXEC = ACCESS_EXEC
    def hasContent_(self):
        if (
            self.Current_Uses is not None or
            self.Local_Path is not None or
            self.Max_Uses is not None or
            self.Netname is not None or
            self.Type is not None or
            super(WindowsNetworkShareObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinNetworkShareObj:', name_='WindowsNetworkShareObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsNetworkShareObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinNetworkShareObj:', name_='WindowsNetworkShareObjectType'):
        super(WindowsNetworkShareObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsNetworkShareObjectType')
        if self.ACCESS_PERM is not None:

            lwrite(' ACCESS_PERM="%s"' % self.gds_format_boolean(self.ACCESS_PERM, input_name='ACCESS_PERM'))
        if self.ACCESS_ATRIB is not None:

            lwrite(' ACCESS_ATRIB="%s"' % self.gds_format_boolean(self.ACCESS_ATRIB, input_name='ACCESS_ATRIB'))
        if self.ACCESS_ALL is not None:

            lwrite(' ACCESS_ALL="%s"' % self.gds_format_boolean(self.ACCESS_ALL, input_name='ACCESS_ALL'))
        if self.ACCESS_READ is not None:

            lwrite(' ACCESS_READ="%s"' % self.gds_format_boolean(self.ACCESS_READ, input_name='ACCESS_READ'))
        if self.ACCESS_DELETE is not None:

            lwrite(' ACCESS_DELETE="%s"' % self.gds_format_boolean(self.ACCESS_DELETE, input_name='ACCESS_DELETE'))
        if self.ACCESS_WRITE is not None:

            lwrite(' ACCESS_WRITE="%s"' % self.gds_format_boolean(self.ACCESS_WRITE, input_name='ACCESS_WRITE'))
        if self.ACCESS_CREATE is not None:

            lwrite(' ACCESS_CREATE="%s"' % self.gds_format_boolean(self.ACCESS_CREATE, input_name='ACCESS_CREATE'))
        if self.ACCESS_EXEC is not None:

            lwrite(' ACCESS_EXEC="%s"' % self.gds_format_boolean(self.ACCESS_EXEC, input_name='ACCESS_EXEC'))
    def exportChildren(self, lwrite, level, namespace_='WinNetworkShareObj:', name_='WindowsNetworkShareObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsNetworkShareObjectType, self).exportChildren(lwrite, level, 'WinNetworkShareObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Current_Uses is not None:
            self.Current_Uses.export(lwrite, level, 'WinNetworkShareObj:', name_='Current_Uses', pretty_print=pretty_print)
        if self.Local_Path is not None:
            self.Local_Path.export(lwrite, level, 'WinNetworkShareObj:', name_='Local_Path', pretty_print=pretty_print)
        if self.Max_Uses is not None:
            self.Max_Uses.export(lwrite, level, 'WinNetworkShareObj:', name_='Max_Uses', pretty_print=pretty_print)
        if self.Netname is not None:
            self.Netname.export(lwrite, level, 'WinNetworkShareObj:', name_='Netname', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinNetworkShareObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ACCESS_PERM', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_PERM = True
            elif value in ('false', '0'):
                self.ACCESS_PERM = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_ATRIB', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_ATRIB = True
            elif value in ('false', '0'):
                self.ACCESS_ATRIB = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_ALL', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_ALL = True
            elif value in ('false', '0'):
                self.ACCESS_ALL = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_READ', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_READ = True
            elif value in ('false', '0'):
                self.ACCESS_READ = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_DELETE', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_DELETE = True
            elif value in ('false', '0'):
                self.ACCESS_DELETE = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_WRITE', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_WRITE = True
            elif value in ('false', '0'):
                self.ACCESS_WRITE = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_CREATE', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_CREATE = True
            elif value in ('false', '0'):
                self.ACCESS_CREATE = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ACCESS_EXEC', node)
        if value is not None:

            if value in ('true', '1'):
                self.ACCESS_EXEC = True
            elif value in ('false', '0'):
                self.ACCESS_EXEC = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(WindowsNetworkShareObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Current_Uses':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Current_Uses(obj_)
        elif nodeName_ == 'Local_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Local_Path(obj_)
        elif nodeName_ == 'Max_Uses':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Max_Uses(obj_)
        elif nodeName_ == 'Netname':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Netname(obj_)
        elif nodeName_ == 'Type':
            obj_ = SharedResourceType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(WindowsNetworkShareObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsNetworkShareObjectType

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
    'Max_Uses': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Local_Path': cybox_common.StringObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
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
    'Netname': cybox_common.StringObjectPropertyType,
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
    'Current_Uses': cybox_common.NonNegativeIntegerObjectPropertyType,
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
        rootTag = 'Windows_Network_Share'
        rootClass = WindowsNetworkShareObjectType
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
        rootTag = 'Windows_Network_Share'
        rootClass = WindowsNetworkShareObjectType
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
        rootTag = 'Windows_Network_Share'
        rootClass = WindowsNetworkShareObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Network_Share",
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
    "WindowsNetworkShareObjectType",
    "SharedResourceType"
    ]
