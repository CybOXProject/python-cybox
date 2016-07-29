# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object


class RouteType(cybox_common.BaseObjectPropertyType):
    """RouteType specifies route types, via a union of the RouteTypeEnum
    type and the atomic xs:string type. Its base type is the CybOX
    Core cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(RouteType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if RouteType.subclass:
            return RouteType.subclass(*args_, **kwargs_)
        else:
            return RouteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(RouteType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkRouteEntryObj:', name_='RouteType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RouteType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkRouteEntryObj:', name_='RouteType'):
        super(RouteType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RouteType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkRouteEntryObj:', name_='RouteType', fromsubclass_=False, pretty_print=True):
        super(RouteType, self).exportChildren(lwrite, level, 'NetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
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
        super(RouteType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class RouteType

class NetworkRouteEntryObjectType(cybox_common.ObjectPropertiesType):
    """The NetworkRouteEntryObjectType type is intended to characterize
    generic system network routing table entries.The is_ipv6 field
    specifies whether the route uses IPv6 addresses.The
    is_autoconfigure_address field specifies whether the destination
    IP address for the route is automatically configured.The
    is_immortal field specifies whether the lifetimes for the route
    prefixes are infinite.The is_loopback field specifies whether
    the route is the default for all packets sent to local network
    addresses.The is_publish field specifies whether the route is
    published."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_publish=None, is_autoconfigure_address=None, is_loopback=None, is_immortal=None, is_ipv6=None, Destination_Address=None, Origin=None, Netmask=None, Gateway_Address=None, Metric=None, Type=None, Protocol=None, Interface=None, Preferred_Lifetime=None, Valid_Lifetime=None, Route_Age=None):
        super(NetworkRouteEntryObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_publish = _cast(bool, is_publish)
        self.is_autoconfigure_address = _cast(bool, is_autoconfigure_address)
        self.is_loopback = _cast(bool, is_loopback)
        self.is_immortal = _cast(bool, is_immortal)
        self.is_ipv6 = _cast(bool, is_ipv6)
        self.Destination_Address = Destination_Address
        self.Origin = Origin
        self.Netmask = Netmask
        self.Gateway_Address = Gateway_Address
        self.Metric = Metric
        self.Type = Type
        self.Protocol = Protocol
        self.Interface = Interface
        self.Preferred_Lifetime = Preferred_Lifetime
        self.Valid_Lifetime = Valid_Lifetime
        self.Route_Age = Route_Age
    def factory(*args_, **kwargs_):
        if NetworkRouteEntryObjectType.subclass:
            return NetworkRouteEntryObjectType.subclass(*args_, **kwargs_)
        else:
            return NetworkRouteEntryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Destination_Address(self): return self.Destination_Address
    def set_Destination_Address(self, Destination_Address): self.Destination_Address = Destination_Address
    def get_Origin(self): return self.Origin
    def set_Origin(self, Origin): self.Origin = Origin
    def get_Netmask(self): return self.Netmask
    def set_Netmask(self, Netmask): self.Netmask = Netmask
    def get_Gateway_Address(self): return self.Gateway_Address
    def set_Gateway_Address(self, Gateway_Address): self.Gateway_Address = Gateway_Address
    def get_Metric(self): return self.Metric
    def set_Metric(self, Metric): self.Metric = Metric
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_RouteType(self, value):
        # Validate type RouteType, a restriction on None.
        pass
    def get_Protocol(self): return self.Protocol
    def set_Protocol(self, Protocol): self.Protocol = Protocol
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Interface(self): return self.Interface
    def set_Interface(self, Interface): self.Interface = Interface
    def get_Preferred_Lifetime(self): return self.Preferred_Lifetime
    def set_Preferred_Lifetime(self, Preferred_Lifetime): self.Preferred_Lifetime = Preferred_Lifetime
    def validate_DurationObjectPropertyType(self, value):
        # Validate type cybox_common.DurationObjectPropertyType, a restriction on None.
        pass
    def get_Valid_Lifetime(self): return self.Valid_Lifetime
    def set_Valid_Lifetime(self, Valid_Lifetime): self.Valid_Lifetime = Valid_Lifetime
    def get_Route_Age(self): return self.Route_Age
    def set_Route_Age(self, Route_Age): self.Route_Age = Route_Age
    def get_is_publish(self): return self.is_publish
    def set_is_publish(self, is_publish): self.is_publish = is_publish
    def get_is_autoconfigure_address(self): return self.is_autoconfigure_address
    def set_is_autoconfigure_address(self, is_autoconfigure_address): self.is_autoconfigure_address = is_autoconfigure_address
    def get_is_loopback(self): return self.is_loopback
    def set_is_loopback(self, is_loopback): self.is_loopback = is_loopback
    def get_is_immortal(self): return self.is_immortal
    def set_is_immortal(self, is_immortal): self.is_immortal = is_immortal
    def get_is_ipv6(self): return self.is_ipv6
    def set_is_ipv6(self, is_ipv6): self.is_ipv6 = is_ipv6
    def hasContent_(self):
        if (
            self.Destination_Address is not None or
            self.Origin is not None or
            self.Netmask is not None or
            self.Gateway_Address is not None or
            self.Metric is not None or
            self.Type is not None or
            self.Protocol is not None or
            self.Interface is not None or
            self.Preferred_Lifetime is not None or
            self.Valid_Lifetime is not None or
            self.Route_Age is not None or
            super(NetworkRouteEntryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkRouteEntryObj:', name_='NetworkRouteEntryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkRouteEntryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkRouteEntryObj:', name_='NetworkRouteEntryObjectType'):
        super(NetworkRouteEntryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkRouteEntryObjectType')
        if self.is_publish is not None:

            lwrite(' is_publish="%s"' % self.gds_format_boolean(self.is_publish, input_name='is_publish'))
        if self.is_autoconfigure_address is not None:

            lwrite(' is_autoconfigure_address="%s"' % self.gds_format_boolean(self.is_autoconfigure_address, input_name='is_autoconfigure_address'))
        if self.is_loopback is not None:

            lwrite(' is_loopback="%s"' % self.gds_format_boolean(self.is_loopback, input_name='is_loopback'))
        if self.is_immortal is not None:

            lwrite(' is_immortal="%s"' % self.gds_format_boolean(self.is_immortal, input_name='is_immortal'))
        if self.is_ipv6 is not None:

            lwrite(' is_ipv6="%s"' % self.gds_format_boolean(self.is_ipv6, input_name='is_ipv6'))
    def exportChildren(self, lwrite, level, namespace_='NetworkRouteEntryObj:', name_='NetworkRouteEntryObjectType', fromsubclass_=False, pretty_print=True):
        super(NetworkRouteEntryObjectType, self).exportChildren(lwrite, level, 'NetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Destination_Address is not None:
            self.Destination_Address.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Destination_Address', pretty_print=pretty_print)
        if self.Origin is not None:
            self.Origin.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Origin', pretty_print=pretty_print)
        if self.Netmask is not None:
            self.Netmask.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Netmask', pretty_print=pretty_print)
        if self.Gateway_Address is not None:
            self.Gateway_Address.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Gateway_Address', pretty_print=pretty_print)
        if self.Metric is not None:
            self.Metric.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Metric', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Type', pretty_print=pretty_print)
        if self.Protocol is not None:
            self.Protocol.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Protocol', pretty_print=pretty_print)
        if self.Interface is not None:
            self.Interface.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Interface', pretty_print=pretty_print)
        if self.Preferred_Lifetime is not None:
            self.Preferred_Lifetime.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Preferred_Lifetime', pretty_print=pretty_print)
        if self.Valid_Lifetime is not None:
            self.Valid_Lifetime.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Valid_Lifetime', pretty_print=pretty_print)
        if self.Route_Age is not None:
            self.Route_Age.export(lwrite, level, 'NetworkRouteEntryObj:', name_='Route_Age', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_publish', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_publish = True
            elif value in ('false', '0'):
                self.is_publish = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_autoconfigure_address', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_autoconfigure_address = True
            elif value in ('false', '0'):
                self.is_autoconfigure_address = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_loopback', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_loopback = True
            elif value in ('false', '0'):
                self.is_loopback = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_immortal', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_immortal = True
            elif value in ('false', '0'):
                self.is_immortal = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_ipv6', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_ipv6 = True
            elif value in ('false', '0'):
                self.is_ipv6 = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(NetworkRouteEntryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Destination_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Destination_Address(obj_)
        elif nodeName_ == 'Origin':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Origin(obj_)
        elif nodeName_ == 'Netmask':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Netmask(obj_)
        elif nodeName_ == 'Gateway_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Gateway_Address(obj_)
        elif nodeName_ == 'Metric':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Metric(obj_)
        elif nodeName_ == 'Type':
            obj_ = RouteType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Protocol':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Protocol(obj_)
        elif nodeName_ == 'Interface':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Interface(obj_)
        elif nodeName_ == 'Preferred_Lifetime':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Preferred_Lifetime(obj_)
        elif nodeName_ == 'Valid_Lifetime':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Valid_Lifetime(obj_)
        elif nodeName_ == 'Route_Age':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Route_Age(obj_)
        super(NetworkRouteEntryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkRouteEntryObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Gateway_Address': address_object.AddressObjectType,
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
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Preferred_Lifetime': cybox_common.DurationObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Interface': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Hash': cybox_common.HashType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Metric': cybox_common.UnsignedLongObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
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
    'Destination_Address': address_object.AddressObjectType,
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
    'Valid_Lifetime': cybox_common.DurationObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
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
        rootTag = 'Network_Route_Entry'
        rootClass = NetworkRouteEntryObjectType
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
        rootTag = 'Network_Route_Entry'
        rootClass = NetworkRouteEntryObjectType
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
        rootTag = 'Network_Route_Entry'
        rootClass = NetworkRouteEntryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Route_Entry",
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
    "NetworkRouteEntryObjectType",
    "RouteType"
    ]
