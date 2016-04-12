# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import file_object


class UnixFileType(cybox_common.BaseObjectPropertyType):
    """UnixFileType specifies Unix file types, via a union of the
    UnixFileTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(UnixFileType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if UnixFileType.subclass:
            return UnixFileType.subclass(*args_, **kwargs_)
        else:
            return UnixFileType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(UnixFileType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFileType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFileType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixFileObj:', name_='UnixFileType'):
        super(UnixFileType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFileType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFileType', fromsubclass_=False, pretty_print=True):
        super(UnixFileType, self).exportChildren(lwrite, level, 'UnixFileObj:', name_, True, pretty_print=pretty_print)
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
        super(UnixFileType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class UnixFileType

class UnixFilePermissionsType(file_object.FilePermissionsType):
    """The UnixFilePermissionsType type specifies the specific permissions
    used by the Unix family of operating systems.The suid field
    specifies whether or not the file may be exectued with the
    privileges of the file's owner.The sgid field specifies whether
    or not the file may be executed with the privileges of the
    file's group owner.The uread field specifies whether or not the
    owner of the file can read its contents.The uwrite field
    specifies whether or not the owner of the file can write to
    it.The uexec field specifies whether or not the owner of the
    file can execute it.The gread field specifies whether or not the
    group owner of the file can read its contents.The gwrite field
    specifies whether or not the group owner of the file can write
    to it.The gexec field specifies whether or not the group owner
    of the file can execute it.The oread field specifies whether or
    not all other users can read the contents of the file.The owrite
    field specifies whether or not all other users can write to the
    file.The oexec field specifies whether or not all other users
    can execute the file."""

    subclass = None
    superclass = file_object.FilePermissionsType
    def __init__(self, gwrite=None, suid=None, oexec=None, owrite=None, uwrite=None, gexec=None, gread=None, uexec=None, uread=None, sgid=None, oread=None):
        super(UnixFilePermissionsType, self).__init__()
        self.gwrite = _cast(bool, gwrite)
        self.suid = _cast(bool, suid)
        self.oexec = _cast(bool, oexec)
        self.owrite = _cast(bool, owrite)
        self.uwrite = _cast(bool, uwrite)
        self.gexec = _cast(bool, gexec)
        self.gread = _cast(bool, gread)
        self.uexec = _cast(bool, uexec)
        self.uread = _cast(bool, uread)
        self.sgid = _cast(bool, sgid)
        self.oread = _cast(bool, oread)
        pass
    def factory(*args_, **kwargs_):
        if UnixFilePermissionsType.subclass:
            return UnixFilePermissionsType.subclass(*args_, **kwargs_)
        else:
            return UnixFilePermissionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_gwrite(self): return self.gwrite
    def set_gwrite(self, gwrite): self.gwrite = gwrite
    def get_suid(self): return self.suid
    def set_suid(self, suid): self.suid = suid
    def get_oexec(self): return self.oexec
    def set_oexec(self, oexec): self.oexec = oexec
    def get_owrite(self): return self.owrite
    def set_owrite(self, owrite): self.owrite = owrite
    def get_uwrite(self): return self.uwrite
    def set_uwrite(self, uwrite): self.uwrite = uwrite
    def get_gexec(self): return self.gexec
    def set_gexec(self, gexec): self.gexec = gexec
    def get_gread(self): return self.gread
    def set_gread(self, gread): self.gread = gread
    def get_uexec(self): return self.uexec
    def set_uexec(self, uexec): self.uexec = uexec
    def get_uread(self): return self.uread
    def set_uread(self, uread): self.uread = uread
    def get_sgid(self): return self.sgid
    def set_sgid(self, sgid): self.sgid = sgid
    def get_oread(self): return self.oread
    def set_oread(self, oread): self.oread = oread
    def hasContent_(self):
        if (
            super(UnixFilePermissionsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFilePermissionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFilePermissionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixFileObj:', name_='UnixFilePermissionsType'):
        super(UnixFilePermissionsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFilePermissionsType')
        if self.gwrite is not None:

            lwrite(' gwrite="%s"' % self.gds_format_boolean(self.gwrite, input_name='gwrite'))
        if self.suid is not None:

            lwrite(' suid="%s"' % self.gds_format_boolean(self.suid, input_name='suid'))
        if self.oexec is not None:

            lwrite(' oexec="%s"' % self.gds_format_boolean(self.oexec, input_name='oexec'))
        if self.owrite is not None:

            lwrite(' owrite="%s"' % self.gds_format_boolean(self.owrite, input_name='owrite'))
        if self.uwrite is not None:

            lwrite(' uwrite="%s"' % self.gds_format_boolean(self.uwrite, input_name='uwrite'))
        if self.gexec is not None:

            lwrite(' gexec="%s"' % self.gds_format_boolean(self.gexec, input_name='gexec'))
        if self.gread is not None:

            lwrite(' gread="%s"' % self.gds_format_boolean(self.gread, input_name='gread'))
        if self.uexec is not None:

            lwrite(' uexec="%s"' % self.gds_format_boolean(self.uexec, input_name='uexec'))
        if self.uread is not None:

            lwrite(' uread="%s"' % self.gds_format_boolean(self.uread, input_name='uread'))
        if self.sgid is not None:

            lwrite(' sgid="%s"' % self.gds_format_boolean(self.sgid, input_name='sgid'))
        if self.oread is not None:

            lwrite(' oread="%s"' % self.gds_format_boolean(self.oread, input_name='oread'))
    def exportChildren(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFilePermissionsType', fromsubclass_=False, pretty_print=True):
        super(UnixFilePermissionsType, self).exportChildren(lwrite, level, 'UnixFileObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('gwrite', node)
        if value is not None:

            if value in ('true', '1'):
                self.gwrite = True
            elif value in ('false', '0'):
                self.gwrite = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('suid', node)
        if value is not None:

            if value in ('true', '1'):
                self.suid = True
            elif value in ('false', '0'):
                self.suid = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('oexec', node)
        if value is not None:

            if value in ('true', '1'):
                self.oexec = True
            elif value in ('false', '0'):
                self.oexec = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('owrite', node)
        if value is not None:

            if value in ('true', '1'):
                self.owrite = True
            elif value in ('false', '0'):
                self.owrite = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('uwrite', node)
        if value is not None:

            if value in ('true', '1'):
                self.uwrite = True
            elif value in ('false', '0'):
                self.uwrite = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('gexec', node)
        if value is not None:

            if value in ('true', '1'):
                self.gexec = True
            elif value in ('false', '0'):
                self.gexec = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('gread', node)
        if value is not None:

            if value in ('true', '1'):
                self.gread = True
            elif value in ('false', '0'):
                self.gread = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('uexec', node)
        if value is not None:

            if value in ('true', '1'):
                self.uexec = True
            elif value in ('false', '0'):
                self.uexec = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('uread', node)
        if value is not None:

            if value in ('true', '1'):
                self.uread = True
            elif value in ('false', '0'):
                self.uread = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('sgid', node)
        if value is not None:

            if value in ('true', '1'):
                self.sgid = True
            elif value in ('false', '0'):
                self.sgid = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('oread', node)
        if value is not None:

            if value in ('true', '1'):
                self.oread = True
            elif value in ('false', '0'):
                self.oread = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(UnixFilePermissionsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(UnixFilePermissionsType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class UnixFilePermissionsType

class UnixFileObjectType(file_object.FileObjectType):
    """The UnixFileObjectType type is intended to characterize Unix files."""

    subclass = None
    superclass = file_object.FileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Group_Owner=None, INode=None, Type=None):
        super(UnixFileObjectType, self).__init__(object_reference, Custom_Properties, is_packed, File_Name, File_Path, Device_Path, Full_Path, File_Extension, Size_In_Bytes, Magic_Number, File_Format, Hashes, Digital_Signatures, Modified_Time, Accessed_Time, Created_Time, File_Attributes_List, Permissions, User_Owner, Packer_List, Peak_Entropy, Sym_Links, Byte_Runs, Extracted_Features, )
        self.Group_Owner = Group_Owner
        self.INode = INode
        self.Type = Type
    def factory(*args_, **kwargs_):
        if UnixFileObjectType.subclass:
            return UnixFileObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixFileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group_Owner(self): return self.Group_Owner
    def set_Group_Owner(self, Group_Owner): self.Group_Owner = Group_Owner
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_INode(self): return self.INode
    def set_INode(self, INode): self.INode = INode
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_UnixFileType(self, value):
        # Validate type UnixFileType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Group_Owner is not None or
            self.INode is not None or
            self.Type is not None or
            super(UnixFileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixFileObj:', name_='UnixFileObjectType'):
        super(UnixFileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixFileObjectType')
    def exportChildren(self, lwrite, level, namespace_='UnixFileObj:', name_='UnixFileObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixFileObjectType, self).exportChildren(lwrite, level, 'UnixFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Group_Owner is not None:
            self.Group_Owner.export(lwrite, level, 'UnixFileObj:', name_='Group_Owner', pretty_print=pretty_print)
        if self.INode is not None:
            self.INode.export(lwrite, level, 'UnixFileObj:', name_='INode', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'UnixFileObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixFileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group_Owner':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Group_Owner(obj_)
        elif nodeName_ == 'INode':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_INode(obj_)
        elif nodeName_ == 'Type':
            obj_ = UnixFileType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(UnixFileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixFileObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Device_Path': cybox_common.StringObjectPropertyType,
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
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Type': file_object.PackerClassType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Detected_Entrypoint_Signatures': file_object.EntryPointSignatureListType,
    'Tool_Hashes': cybox_common.HashListType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'File_Path': file_object.FilePathType,
    'Entry_Point_Signature': file_object.EntryPointSignatureType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Strings': cybox_common.ExtractedStringsType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Packer': file_object.PackerType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'File_Attributes_List': file_object.FileAttributeType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Sym_Links': file_object.SymLinksListType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Packer_List': file_object.PackerListType,
    'Import': cybox_common.StringObjectPropertyType,
    'Accessed_Time': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Permissions': file_object.FilePermissionsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'INode': cybox_common.UnsignedLongObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Group_Owner': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'EP_Jump_Codes': file_object.EPJumpCodeType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.StringObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
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
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'File': file_object.FileObjectType,
    'Contributor': cybox_common.ContributorType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
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
        rootTag = 'Unix_File'
        rootClass = UnixFileObjectType
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
        rootTag = 'Unix_File'
        rootClass = UnixFileObjectType
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
        rootTag = 'Unix_File'
        rootClass = UnixFileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Unix_File",
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
    "UnixFileObjectType",
    "UnixFilePermissionsType",
    "UnixFileType"
    ]
