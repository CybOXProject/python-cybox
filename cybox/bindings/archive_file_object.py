# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import file_object


class ArchiveFileFormatType(cybox_common.BaseObjectPropertyType):
    """The ArchiveFileFormatType specifies archive file formats via a union
    of the ArchiveFileFormatEnum type and the atomic xs:string type.
    Its base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ArchiveFileFormatType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, )
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ArchiveFileFormatType.subclass:
            return ArchiveFileFormatType.subclass(*args_, **kwargs_)
        else:
            return ArchiveFileFormatType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ArchiveFileFormatType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArchiveFileObj:', name_='ArchiveFileFormatType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ArchiveFileFormatType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArchiveFileObj:', name_='ArchiveFileFormatType'):
        super(ArchiveFileFormatType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ArchiveFileFormatType')
    def exportChildren(self, lwrite, level, namespace_='ArchiveFileObj:', name_='ArchiveFileFormatType', fromsubclass_=False, pretty_print=True):
        super(ArchiveFileFormatType, self).exportChildren(lwrite, level, 'ArchiveFileObj:', name_, True, pretty_print=pretty_print)
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
        super(ArchiveFileFormatType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ArchiveFileFormatType

class ArchiveFileObjectType(file_object.FileObjectType):
    """The ArchiveFileObjectType type is intended to characterize archive
    files."""

    subclass = None
    superclass = file_object.FileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, is_masqueraded=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Encryption_Algorithm=None, Decryption_Key=None, Compression_Method=None, Compression_Version=None, Compression_Comment=None, Archive_Format=None, Version=None, File_Count=None, Comment=None, Archived_File=None):
        super(ArchiveFileObjectType, self).__init__(object_reference, Custom_Properties, xsi_type, is_packed, is_masqueraded, File_Name, File_Path, Device_Path, Full_Path, File_Extension, Size_In_Bytes, Magic_Number, File_Format, Hashes, Digital_Signatures, Modified_Time, Accessed_Time, Created_Time, File_Attributes_List, Permissions, User_Owner, Packer_List, Peak_Entropy, Sym_Links, Byte_Runs, Extracted_Features, Encryption_Algorithm, Decryption_Key, Compression_Method, Compression_Version, Compression_Comment, )
        self.Archive_Format = Archive_Format
        self.Version = Version
        self.File_Count = File_Count
        self.Encryption_Algorithm = Encryption_Algorithm
        self.Decryption_Key = Decryption_Key
        self.Comment = Comment
        if Archived_File is None:
            self.Archived_File = []
        else:
            self.Archived_File = Archived_File
    def factory(*args_, **kwargs_):
        if ArchiveFileObjectType.subclass:
            return ArchiveFileObjectType.subclass(*args_, **kwargs_)
        else:
            return ArchiveFileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Archive_Format(self): return self.Archive_Format
    def set_Archive_Format(self, Archive_Format): self.Archive_Format = Archive_Format
    def validate_ArchiveFileFormatType(self, value):
        # Validate type ArchiveFileFormatType, a restriction on None.
        pass
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_File_Count(self): return self.File_Count
    def set_File_Count(self, File_Count): self.File_Count = File_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Encryption_Algorithm(self): return self.Encryption_Algorithm
    def set_Encryption_Algorithm(self, Encryption_Algorithm): self.Encryption_Algorithm = Encryption_Algorithm
    def validate_CipherType(self, value):
        # Validate type cybox_common.CipherType, a restriction on None.
        pass
    def get_Decryption_Key(self): return self.Decryption_Key
    def set_Decryption_Key(self, Decryption_Key): self.Decryption_Key = Decryption_Key
    def get_Comment(self): return self.Comment
    def set_Comment(self, Comment): self.Comment = Comment
    def get_Archived_File(self): return self.Archived_File
    def set_Archived_File(self, Archived_File): self.Archived_File = Archived_File
    def add_Archived_File(self, value): self.Archived_File.append(value)
    def insert_Archived_File(self, index, value): self.Archived_File[index] = value
    def hasContent_(self):
        if (
            self.Archive_Format is not None or
            self.Version is not None or
            self.File_Count is not None or
            self.Encryption_Algorithm is not None or
            self.Decryption_Key is not None or
            self.Comment is not None or
            self.Archived_File or
            super(ArchiveFileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ArchiveFileObj:', name_='ArchiveFileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ArchiveFileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ArchiveFileObj:', name_='ArchiveFileObjectType'):
        super(ArchiveFileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ArchiveFileObjectType')
    def exportChildren(self, lwrite, level, namespace_='ArchiveFileObj:', name_='ArchiveFileObjectType', fromsubclass_=False, pretty_print=True):
        super(ArchiveFileObjectType, self).exportChildren(lwrite, level, 'ArchiveFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Archive_Format is not None:
            self.Archive_Format.export(lwrite, level, 'ArchiveFileObj:', name_='Archive_Format', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(lwrite, level, 'ArchiveFileObj:', name_='Version', pretty_print=pretty_print)
        if self.File_Count is not None:
            self.File_Count.export(lwrite, level, 'ArchiveFileObj:', name_='File_Count', pretty_print=pretty_print)
        if self.Encryption_Algorithm is not None:
            self.Encryption_Algorithm.export(lwrite, level, 'ArchiveFileObj:', name_='Encryption_Algorithm', pretty_print=pretty_print)
        if self.Decryption_Key is not None:
            self.Decryption_Key.export(lwrite, level, 'ArchiveFileObj:', name_='Decryption_Key', pretty_print=pretty_print)
        if self.Comment is not None:
            self.Comment.export(lwrite, level, 'ArchiveFileObj:', name_='Comment', pretty_print=pretty_print)
        for Archived_File_ in self.Archived_File:
            Archived_File_.export(lwrite, level, 'ArchiveFileObj:', name_='Archived_File', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ArchiveFileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Archive_Format':
            obj_ = ArchiveFileFormatType.factory()
            obj_.build(child_)
            self.set_Archive_Format(obj_)
        elif nodeName_ == 'Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'File_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Count(obj_)
        elif nodeName_ == 'Encryption_Algorithm':
            obj_ = cybox_common.CipherType.factory()
            obj_.build(child_)
            self.set_Encryption_Algorithm(obj_)
        elif nodeName_ == 'Decryption_Key':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Decryption_Key(obj_)
        elif nodeName_ == 'Comment':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Comment(obj_)
        elif nodeName_ == 'Archived_File':
            obj_ = file_object.FileObjectType.factory()
            obj_.build(child_)
            self.Archived_File.append(obj_)
        super(ArchiveFileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class ArchiveFileObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Sym_Links': file_object.SymLinksListType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Compression_Version': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Device_Path': cybox_common.StringObjectPropertyType,
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
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Type': file_object.PackerClassType,
    'Accessed_Time': cybox_common.DateTimeObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Detected_Entrypoint_Signatures': file_object.EntryPointSignatureListType,
    'Tool_Hashes': cybox_common.HashListType,
    'File_Path': file_object.FilePathType,
    'Observable_Location': cybox_common.LocationType,
    'Entry_Point_Signature': file_object.EntryPointSignatureType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Comment': cybox_common.StringObjectPropertyType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Packer': file_object.PackerType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'File_Attributes_List': file_object.FileAttributeType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Packer_List': file_object.PackerListType,
    'Import': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
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
    'Permissions': file_object.FilePermissionsType,
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
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Archived_File': file_object.FileObjectType,
    'References': cybox_common.ToolReferencesType,
    'Encryption_Algorithm': cybox_common.CipherType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'EP_Jump_Codes': file_object.EPJumpCodeType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'Modified_Time': cybox_common.DateTimeObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
    'Decryption_Key': cybox_common.StringObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Full_Path': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Depth': cybox_common.IntegerObjectPropertyType,
    'Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compression_Comment': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Compression_Method': cybox_common.StringObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'File_Count': cybox_common.IntegerObjectPropertyType,
    'End_Time': cybox_common.DateTimeWithPrecisionType,
    'File': file_object.FileObjectType,
    'Contributor': cybox_common.ContributorType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
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
        rootTag = 'Archive_File'
        rootClass = ArchiveFileObjectType
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
        rootTag = 'Archive_File'
        rootClass = ArchiveFileObjectType
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
        rootTag = 'Archive_File'
        rootClass = ArchiveFileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="Archive_File",
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
    "ArchiveFileObjectType",
    "ArchiveFileFormatType"
    ]
