# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from cybox.bindings import *
import cybox_common

import address_object
import network_route_entry_object


class NLRouteProtocolType(cybox_common.BaseObjectPropertyType):
    """NLRouteProtocolType specifies Windows-centric network routing
    protocol values via a union of the NLRouteProtocolEnum type and
    the atomic xs:string type. Its base type is the CybOX
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""
    
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(NLRouteProtocolType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if NLRouteProtocolType.subclass:
            return NLRouteProtocolType.subclass(*args_, **kwargs_)
        else:
            return NLRouteProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NLRouteProtocolType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NLRouteProtocolType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteProtocolType'):
        super(NLRouteProtocolType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NLRouteProtocolType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteProtocolType', fromsubclass_=False, pretty_print=True):
        super(NLRouteProtocolType, self).exportChildren(lwrite, level, 'WinNetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(NLRouteProtocolType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NLRouteProtocolType

class NLRouteOriginType(cybox_common.BaseObjectPropertyType):
    """NLRouteOriginType specifies Windows-centric network route
    origination values via a union of the RouteOriginEnum type and
    the atomic xs:string type. Its base type is the CybOX
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""
    
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(NLRouteOriginType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if NLRouteOriginType.subclass:
            return NLRouteOriginType.subclass(*args_, **kwargs_)
        else:
            return NLRouteOriginType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NLRouteOriginType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteOriginType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NLRouteOriginType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteOriginType'):
        super(NLRouteOriginType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NLRouteOriginType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='NLRouteOriginType', fromsubclass_=False, pretty_print=True):
        super(NLRouteOriginType, self).exportChildren(lwrite, level, 'WinNetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(NLRouteOriginType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NLRouteOriginType

class WindowsNetworkRouteEntryObjectType(network_route_entry_object.NetworkRouteEntryObjectType):
    """The WindowsNetworkRouteEntryObjectType type is intended to
    characterize Windows network routing table entries."""
    
    subclass = None
    superclass = network_route_entry_object.NetworkRouteEntryObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_publish=None, is_autoconfigure_address=None, is_loopback=None, is_immortal=None, is_ipv6=None, Destination_Address=None, Origin=None, Netmask=None, Gateway_Address=None, Metric=None, Type=None, Protocol=None, Interface=None, Preferred_Lifetime=None, Valid_Lifetime=None, Route_Age=None, NL_ROUTE_PROTOCOL=None, NL_ROUTE_ORIGIN=None):
        super(WindowsNetworkRouteEntryObjectType, self).__init__(object_reference, Custom_Properties, is_publish, is_autoconfigure_address, is_loopback, is_immortal, is_ipv6, Destination_Address, Origin, Netmask, Gateway_Address, Metric, Type, Protocol, Interface, Preferred_Lifetime, Valid_Lifetime, Route_Age, )
        self.NL_ROUTE_PROTOCOL = NL_ROUTE_PROTOCOL
        self.NL_ROUTE_ORIGIN = NL_ROUTE_ORIGIN
    def factory(*args_, **kwargs_):
        if WindowsNetworkRouteEntryObjectType.subclass:
            return WindowsNetworkRouteEntryObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsNetworkRouteEntryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_NL_ROUTE_PROTOCOL(self): return self.NL_ROUTE_PROTOCOL
    def set_NL_ROUTE_PROTOCOL(self, NL_ROUTE_PROTOCOL): self.NL_ROUTE_PROTOCOL = NL_ROUTE_PROTOCOL
    def validate_NLRouteProtocolType(self, value):
        # Validate type NLRouteProtocolType, a restriction on None.
        pass
    def get_NL_ROUTE_ORIGIN(self): return self.NL_ROUTE_ORIGIN
    def set_NL_ROUTE_ORIGIN(self, NL_ROUTE_ORIGIN): self.NL_ROUTE_ORIGIN = NL_ROUTE_ORIGIN
    def validate_NLRouteOriginType(self, value):
        # Validate type NLRouteOriginType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.NL_ROUTE_PROTOCOL is not None or
            self.NL_ROUTE_ORIGIN is not None or
            super(WindowsNetworkRouteEntryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='WindowsNetworkRouteEntryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsNetworkRouteEntryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinNetworkRouteEntryObj:', name_='WindowsNetworkRouteEntryObjectType'):
        super(WindowsNetworkRouteEntryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsNetworkRouteEntryObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinNetworkRouteEntryObj:', name_='WindowsNetworkRouteEntryObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsNetworkRouteEntryObjectType, self).exportChildren(lwrite, level, 'WinNetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NL_ROUTE_PROTOCOL is not None:
            self.NL_ROUTE_PROTOCOL.export(lwrite, level, 'WinNetworkRouteEntryObj:', name_='NL_ROUTE_PROTOCOL', pretty_print=pretty_print)
        if self.NL_ROUTE_ORIGIN is not None:
            self.NL_ROUTE_ORIGIN.export(lwrite, level, 'WinNetworkRouteEntryObj:', name_='NL_ROUTE_ORIGIN', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsNetworkRouteEntryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'NL_ROUTE_PROTOCOL':
            obj_ = NLRouteProtocolType.factory()
            obj_.build(child_)
            self.set_NL_ROUTE_PROTOCOL(obj_)
        elif nodeName_ == 'NL_ROUTE_ORIGIN':
            obj_ = NLRouteOriginType.factory()
            obj_.build(child_)
            self.set_NL_ROUTE_ORIGIN(obj_)
        super(WindowsNetworkRouteEntryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsNetworkRouteEntryObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Netmask': address_object.AddressObjectType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Route_Age': cybox_common.DurationObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Origin': address_object.AddressObjectType,
    'Protocol': cybox_common.StringObjectPropertyType,
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
    'Type': network_route_entry_object.RouteType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Preferred_Lifetime': cybox_common.DurationObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Interface': cybox_common.StringObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Gateway_Address': address_object.AddressObjectType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Metric': cybox_common.UnsignedLongObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Network_Route_Entry': network_route_entry_object.NetworkRouteEntryObjectType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
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
    'Internal_Strings': cybox_common.InternalStringsType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Destination_Address': address_object.AddressObjectType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Valid_Lifetime': cybox_common.DurationObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
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
    print USAGE_TEXT
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
        rootTag = 'Windows_Network_Route_Entry'
        rootClass = WindowsNetworkRouteEntryObjectType
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
        rootTag = 'Windows_Network_Route_Entry'
        rootClass = WindowsNetworkRouteEntryObjectType
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
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Network_Route_Entry'
        rootClass = WindowsNetworkRouteEntryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Network_Route_Entry",
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
    "WindowsNetworkRouteEntryObjectType",
    "NLRouteOriginType",
    "NLRouteProtocolType"
    ]
