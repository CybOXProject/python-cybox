# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class WindowsHandleListType(GeneratedsSuper):
    """The WindowsHandleListType type specifies a list of Windows handles,
    for re-use in other objects."""

    subclass = None
    superclass = None
    def __init__(self, Handle=None):
        if Handle is None:
            self.Handle = []
        else:
            self.Handle = Handle
    def factory(*args_, **kwargs_):
        if WindowsHandleListType.subclass:
            return WindowsHandleListType.subclass(*args_, **kwargs_)
        else:
            return WindowsHandleListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def add_Handle(self, value): self.Handle.append(value)
    def insert_Handle(self, index, value): self.Handle[index] = value
    def hasContent_(self):
        if (
            self.Handle
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinHandleObj:', name_='WindowsHandleListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsHandleListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinHandleObj:', name_='WindowsHandleListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinHandleObj:', name_='WindowsHandleListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Handle_ in self.Handle:
            Handle_.export(lwrite, level, 'WinHandleObj:', name_='Handle', pretty_print=pretty_print)
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
        if nodeName_ == 'Handle':
            obj_ = WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.Handle.append(obj_)
# end class WindowsHandleListType

class HandleType(cybox_common.BaseObjectPropertyType):
    """HandleType specifies Windows handle types via a union of the
    HandleTypeEnum type and the atomic xs:string type. Its base type
    is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(HandleType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if HandleType.subclass:
            return HandleType.subclass(*args_, **kwargs_)
        else:
            return HandleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(HandleType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinHandleObj:', name_='HandleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HandleType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinHandleObj:', name_='HandleType'):
        super(HandleType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='HandleType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinHandleObj:', name_='HandleType', fromsubclass_=False, pretty_print=True):
        super(HandleType, self).exportChildren(lwrite, level, 'WinHandleObj:', name_, True, pretty_print=pretty_print)
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
        super(HandleType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class HandleType

class WindowsHandleObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsHandleObjectType type is intended to characterize Windows
    handles."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, ID=None, Name=None, Type=None, Object_Address=None, Access_Mask=None, Pointer_Count=None):
        super(WindowsHandleObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.Object_Address = Object_Address
        self.Access_Mask = Access_Mask
        self.Pointer_Count = Pointer_Count
    def factory(*args_, **kwargs_):
        if WindowsHandleObjectType.subclass:
            return WindowsHandleObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsHandleObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ID(self): return self.ID
    def set_ID(self, ID): self.ID = ID
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_HandleType(self, value):
        # Validate type HandleType, a restriction on None.
        pass
    def get_Object_Address(self): return self.Object_Address
    def set_Object_Address(self, Object_Address): self.Object_Address = Object_Address
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Access_Mask(self): return self.Access_Mask
    def set_Access_Mask(self, Access_Mask): self.Access_Mask = Access_Mask
    def get_Pointer_Count(self): return self.Pointer_Count
    def set_Pointer_Count(self, Pointer_Count): self.Pointer_Count = Pointer_Count
    def hasContent_(self):
        if (
            self.ID is not None or
            self.Name is not None or
            self.Type is not None or
            self.Object_Address is not None or
            self.Access_Mask is not None or
            self.Pointer_Count is not None or
            super(WindowsHandleObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinHandleObj:', name_='WindowsHandleObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsHandleObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinHandleObj:', name_='WindowsHandleObjectType'):
        super(WindowsHandleObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsHandleObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinHandleObj:', name_='WindowsHandleObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsHandleObjectType, self).exportChildren(lwrite, level, 'WinHandleObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ID is not None:
            self.ID.export(lwrite, level, 'WinHandleObj:', name_='ID', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinHandleObj:', name_='Name', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinHandleObj:', name_='Type', pretty_print=pretty_print)
        if self.Object_Address is not None:
            self.Object_Address.export(lwrite, level, 'WinHandleObj:', name_='Object_Address', pretty_print=pretty_print)
        if self.Access_Mask is not None:
            self.Access_Mask.export(lwrite, level, 'WinHandleObj:', name_='Access_Mask', pretty_print=pretty_print)
        if self.Pointer_Count is not None:
            self.Pointer_Count.export(lwrite, level, 'WinHandleObj:', name_='Pointer_Count', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsHandleObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ID(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Type':
            obj_ = HandleType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Object_Address':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Object_Address(obj_)
        elif nodeName_ == 'Access_Mask':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Access_Mask(obj_)
        elif nodeName_ == 'Pointer_Count':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer_Count(obj_)
        super(WindowsHandleObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsHandleObjectType

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
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
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
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
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
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
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
        rootTag = 'Windows_Handle'
        rootClass = WindowsHandleObjectType
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
        rootTag = 'Windows_Handle'
        rootClass = WindowsHandleObjectType
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
        rootTag = 'Windows_Handle'
        rootClass = WindowsHandleObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Handle",
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
    "WindowsHandleObjectType",
    "WindowsHandleListType",
    "HandleType"
    ]
