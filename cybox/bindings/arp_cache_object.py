# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object
from . import system_object


class ARPCacheEntryType(GeneratedsSuper):
    """The ARPCacheEntryType type is intended to characterize a single
    entry in a system's ARP cache."""

    subclass = None
    superclass = None
    def __init__(self, IP_Address=None, Physical_Address=None, Type=None, Network_Interface=None):
        self.IP_Address = IP_Address
        self.Physical_Address = Physical_Address
        self.Type = Type
        self.Network_Interface = Network_Interface
    def factory(*args_, **kwargs_):
        if ARPCacheEntryType.subclass:
            return ARPCacheEntryType.subclass(*args_, **kwargs_)
        else:
            return ARPCacheEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def get_Physical_Address(self): return self.Physical_Address
    def set_Physical_Address(self, Physical_Address): self.Physical_Address = Physical_Address
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_ARPCacheEntryTypeType(self, value):
        # Validate type ARPCacheEntryTypeType, a restriction on None.
        pass
    def get_Network_Interface(self): return self.Network_Interface
    def set_Network_Interface(self, Network_Interface): self.Network_Interface = Network_Interface
    def hasContent_(self):
        if (
            self.IP_Address is not None or
            self.Physical_Address is not None or
            self.Type is not None or
            self.Network_Interface is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPCacheEntryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ARPCacheObj:', name_='ARPCacheEntryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_Address is not None:
            self.IP_Address.export(lwrite, level, 'ARPCacheObj:', name_='IP_Address', pretty_print=pretty_print)
        if self.Physical_Address is not None:
            self.Physical_Address.export(lwrite, level, 'ARPCacheObj:', name_='Physical_Address', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'ARPCacheObj:', name_='Type', pretty_print=pretty_print)
        if self.Network_Interface is not None:
            self.Network_Interface.export(lwrite, level, 'ARPCacheObj:', name_='Network_Interface', pretty_print=pretty_print)
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
        if nodeName_ == 'IP_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
        elif nodeName_ == 'Physical_Address':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Physical_Address(obj_)
        elif nodeName_ == 'Type':
            obj_ = ARPCacheEntryTypeType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Network_Interface':
            obj_ = system_object.NetworkInterfaceType.factory()
            obj_.build(child_)
            self.set_Network_Interface(obj_)
# end class ARPCacheEntryType

class ARPCacheEntryTypeType(cybox_common.BaseObjectPropertyType):
    """The ARPCacheEntryTypeType specifies ARP cache entry types via a
    union of the ARPCacheEntryTypeEnum type and the atomic xs:string
    type. Its base type is the CybOX Core cybox_common.BaseObjectPropertyType,
    for permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ARPCacheEntryTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, )
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ARPCacheEntryTypeType.subclass:
            return ARPCacheEntryTypeType.subclass(*args_, **kwargs_)
        else:
            return ARPCacheEntryTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ARPCacheEntryTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheEntryTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPCacheEntryTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ARPCacheObj:', name_='ARPCacheEntryTypeType'):
        super(ARPCacheEntryTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPCacheEntryTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheEntryTypeType', fromsubclass_=False, pretty_print=True):
        super(ARPCacheEntryTypeType, self).exportChildren(lwrite, level, 'ARPCacheObj:', name_, True, pretty_print=pretty_print)
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
        super(ARPCacheEntryTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ARPCacheEntryTypeType

class ARPCacheObjectType(cybox_common.ObjectPropertiesType):
    """The ARPCacheObjectType type is intended to characterize entries in a
    system's address resolution protocol (ARP) cache."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, ARP_Cache_Entry=None):
        super(ARPCacheObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        if ARP_Cache_Entry is None:
            self.ARP_Cache_Entry = []
        else:
            self.ARP_Cache_Entry = ARP_Cache_Entry
    def factory(*args_, **kwargs_):
        if ARPCacheObjectType.subclass:
            return ARPCacheObjectType.subclass(*args_, **kwargs_)
        else:
            return ARPCacheObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ARP_Cache_Entry(self): return self.ARP_Cache_Entry
    def set_ARP_Cache_Entry(self, ARP_Cache_Entry): self.ARP_Cache_Entry = ARP_Cache_Entry
    def add_ARP_Cache_Entry(self, value): self.ARP_Cache_Entry.append(value)
    def insert_ARP_Cache_Entry(self, index, value): self.ARP_Cache_Entry[index] = value
    def hasContent_(self):
        if (
            self.ARP_Cache_Entry or
            super(ARPCacheObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPCacheObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ARPCacheObj:', name_='ARPCacheObjectType'):
        super(ARPCacheObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPCacheObjectType')
    def exportChildren(self, lwrite, level, namespace_='ARPCacheObj:', name_='ARPCacheObjectType', fromsubclass_=False, pretty_print=True):
        super(ARPCacheObjectType, self).exportChildren(lwrite, level, 'ARPCacheObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ARP_Cache_Entry_ in self.ARP_Cache_Entry:
            ARP_Cache_Entry_.export(lwrite, level, 'ARPCacheObj:', name_='ARP_Cache_Entry', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ARPCacheObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ARP_Cache_Entry':
            obj_ = ARPCacheEntryType.factory()
            obj_.build(child_)
            self.ARP_Cache_Entry.append(obj_)
        super(ARPCacheObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class ARPCacheObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'DHCP_Lease_Expires': cybox_common.DateTimeObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Processor_Architecture': system_object.ProcessorArchType,
    'Uptime': cybox_common.DurationObjectPropertyType,
    'DHCP_Server_Address': address_object.AddressObjectType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Network_Interface': system_object.NetworkInterfaceType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Network_Interface_List': system_object.NetworkInterfaceListType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'IP_Gateway_Address': address_object.AddressObjectType,
    'IP_Gateway_List': system_object.IPGatewayListType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'MAC': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'OS': system_object.OSType,
    'Start_Date': cybox_common.DateWithPrecisionType,
    'Physical_Address': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeWithPrecisionType,
    'System': system_object.SystemObjectType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'IP_Address': address_object.AddressObjectType,
    'Adapter': cybox_common.StringObjectPropertyType,
    'Observable_Location': cybox_common.LocationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'BIOS_Info': system_object.BIOSInfoType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Subnet_Mask': address_object.AddressObjectType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'BIOS_Manufacturer': cybox_common.StringObjectPropertyType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Available_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
    'IP_List': system_object.IPInfoListType,
    'Timezone_DST': cybox_common.StringObjectPropertyType,
    'Hostname': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Bitness': system_object.BitnessType,
    'BIOS_Version': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'IP_Info': system_object.IPInfoType,
    'System_Time': cybox_common.TimeObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Build_Number': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Patch_Level': cybox_common.StringObjectPropertyType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'DHCP_Server_List': system_object.DHCPServerListType,
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
    'Install_Date': cybox_common.DateObjectPropertyType,
    'Total_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'DHCP_Lease_Obtained': cybox_common.DateTimeObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'BIOS_Date': cybox_common.DateObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Timezone_Standard': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StringObjectPropertyType,
    'BIOS_Serial_Number': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Local_Time': cybox_common.TimeObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Processor': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'End_Time': cybox_common.DateTimeWithPrecisionType,
    'BIOS_Release_Date': cybox_common.DateObjectPropertyType,
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
        rootTag = 'ARP_Cache'
        rootClass = ARPCacheObjectType
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
        rootTag = 'ARP_Cache'
        rootClass = ARPCacheObjectType
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
        rootTag = 'ARP_Cache'
        rootClass = ARPCacheObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="ARP_Cache",
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
    "ARPCacheObjectType",
    "ARPCacheEntryType",
    "ARPCacheEntryTypeType"
    ]
