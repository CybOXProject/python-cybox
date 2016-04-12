# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import network_route_entry_object


class NetworkRouteEntriesType(GeneratedsSuper):
    """The NetworkRouteEntriesType type is intended to characterize the set
    of network route segments for this route."""

    subclass = None
    superclass = None
    def __init__(self, Network_Route_Entry=None):
        if Network_Route_Entry is None:
            self.Network_Route_Entry = []
        else:
            self.Network_Route_Entry = Network_Route_Entry
    def factory(*args_, **kwargs_):
        if NetworkRouteEntriesType.subclass:
            return NetworkRouteEntriesType.subclass(*args_, **kwargs_)
        else:
            return NetworkRouteEntriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Route_Entry(self): return self.Network_Route_Entry
    def set_Network_Route_Entry(self, Network_Route_Entry): self.Network_Route_Entry = Network_Route_Entry
    def add_Network_Route_Entry(self, value): self.Network_Route_Entry.append(value)
    def insert_Network_Route_Entry(self, index, value): self.Network_Route_Entry[index] = value
    def hasContent_(self):
        if (
            self.Network_Route_Entry
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkRouteEntriesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Network_Route_Entry_ in self.Network_Route_Entry:
            Network_Route_Entry_.export(lwrite, level, 'NetworkRouteObj:', name_='Network_Route_Entry', pretty_print=pretty_print)
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
        if nodeName_ == 'Network_Route_Entry':
            obj_ = network_route_entry_object.NetworkRouteEntryObjectType.factory()
            obj_.build(child_)
            self.Network_Route_Entry.append(obj_)
# end class NetworkRouteEntriesType

class NetRouteObjectType(cybox_common.ObjectPropertiesType):
    """The NetRouteObjectType type is intended to characterize a specific
    network route.The is_ipv6 field specifies whether or not the
    route uses IPv6 addresses.The is_autoconfigure_address field
    specifies if the IP address is autoconfigured.The is_immortal
    field specifies if the route is immortal.The is_loopback field
    specifies if the route is a loopback route (the gateway is on
    the local host).The is_publish field specifies if the route is
    published."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_publish=None, is_autoconfigure_address=None, is_loopback=None, is_immortal=None, is_ipv6=None, Description=None, Network_Route_Entries=None, Preferred_Lifetime=None, Valid_Lifetime=None, Route_Age=None):
        super(NetRouteObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_publish = _cast(bool, is_publish)
        self.is_autoconfigure_address = _cast(bool, is_autoconfigure_address)
        self.is_loopback = _cast(bool, is_loopback)
        self.is_immortal = _cast(bool, is_immortal)
        self.is_ipv6 = _cast(bool, is_ipv6)
        self.Description = Description
        self.Network_Route_Entries = Network_Route_Entries
        self.Preferred_Lifetime = Preferred_Lifetime
        self.Valid_Lifetime = Valid_Lifetime
        self.Route_Age = Route_Age
    def factory(*args_, **kwargs_):
        if NetRouteObjectType.subclass:
            return NetRouteObjectType.subclass(*args_, **kwargs_)
        else:
            return NetRouteObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Network_Route_Entries(self): return self.Network_Route_Entries
    def set_Network_Route_Entries(self, Network_Route_Entries): self.Network_Route_Entries = Network_Route_Entries
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
            self.Description is not None or
            self.Network_Route_Entries is not None or
            self.Preferred_Lifetime is not None or
            self.Valid_Lifetime is not None or
            self.Route_Age is not None or
            super(NetRouteObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkRouteObj:', name_='NetRouteObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetRouteObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkRouteObj:', name_='NetRouteObjectType'):
        super(NetRouteObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetRouteObjectType')
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
    def exportChildren(self, lwrite, level, namespace_='NetworkRouteObj:', name_='NetRouteObjectType', fromsubclass_=False, pretty_print=True):
        super(NetRouteObjectType, self).exportChildren(lwrite, level, 'NetworkRouteObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'NetworkRouteObj:', name_='Description', pretty_print=pretty_print)
        if self.Network_Route_Entries is not None:
            self.Network_Route_Entries.export(lwrite, level, 'NetworkRouteObj:', name_='Network_Route_Entries', pretty_print=pretty_print)
        if self.Preferred_Lifetime is not None:
            self.Preferred_Lifetime.export(lwrite, level, 'NetworkRouteObj:', name_='Preferred_Lifetime', pretty_print=pretty_print)
        if self.Valid_Lifetime is not None:
            self.Valid_Lifetime.export(lwrite, level, 'NetworkRouteObj:', name_='Valid_Lifetime', pretty_print=pretty_print)
        if self.Route_Age is not None:
            self.Route_Age.export(lwrite, level, 'NetworkRouteObj:', name_='Route_Age', pretty_print=pretty_print)
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
        super(NetRouteObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Network_Route_Entries':
            obj_ = NetworkRouteEntriesType.factory()
            obj_.build(child_)
            self.set_Network_Route_Entries(obj_)
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
        super(NetRouteObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetRouteObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Route_Age': cybox_common.DurationObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
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
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Metric': cybox_common.UnsignedLongObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Network_Route_Entry': network_route_entry_object.NetworkRouteEntryObjectType,
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
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
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
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
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
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Route_Object",
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
    "NetRouteObjectType",
    "NetworkRouteEntriesType"
    ]
