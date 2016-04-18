# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import network_route_entry_object


class UnixNetworkRouteEntryObjectType(network_route_entry_object.NetworkRouteEntryObjectType):
    """The UnixNetworkRouteEntryObjectType type is intended to characterize
    entries in the network routing table of a Unix system."""

    subclass = None
    superclass = network_route_entry_object.NetworkRouteEntryObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_publish=None, is_autoconfigure_address=None, is_loopback=None, is_immortal=None, is_ipv6=None, Destination_Address=None, Origin=None, Netmask=None, Gateway_Address=None, Metric=None, Type=None, Protocol=None, Interface=None, Preferred_Lifetime=None, Valid_Lifetime=None, Route_Age=None, Flags=None, MSS=None, Ref=None, Use=None, Window=None):
        super(UnixNetworkRouteEntryObjectType, self).__init__(object_reference, Custom_Properties, is_publish, is_autoconfigure_address, is_loopback, is_immortal, is_ipv6, Destination_Address, Origin, Netmask, Gateway_Address, Metric, Type, Protocol, Interface, Preferred_Lifetime, Valid_Lifetime, Route_Age, )
        self.Flags = Flags
        self.MSS = MSS
        self.Ref = Ref
        self.Use = Use
        self.Window = Window
    def factory(*args_, **kwargs_):
        if UnixNetworkRouteEntryObjectType.subclass:
            return UnixNetworkRouteEntryObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixNetworkRouteEntryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flags(self): return self.Flags
    def set_Flags(self, Flags): self.Flags = Flags
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_MSS(self): return self.MSS
    def set_MSS(self, MSS): self.MSS = MSS
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Ref(self): return self.Ref
    def set_Ref(self, Ref): self.Ref = Ref
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Use(self): return self.Use
    def set_Use(self, Use): self.Use = Use
    def get_Window(self): return self.Window
    def set_Window(self, Window): self.Window = Window
    def hasContent_(self):
        if (
            self.Flags is not None or
            self.MSS is not None or
            self.Ref is not None or
            self.Use is not None or
            self.Window is not None or
            super(UnixNetworkRouteEntryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixNetworkRouteEntryObj:', name_='UnixNetworkRouteEntryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixNetworkRouteEntryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixNetworkRouteEntryObj:', name_='UnixNetworkRouteEntryObjectType'):
        super(UnixNetworkRouteEntryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixNetworkRouteEntryObjectType')
    def exportChildren(self, lwrite, level, namespace_='UnixNetworkRouteEntryObj:', name_='UnixNetworkRouteEntryObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixNetworkRouteEntryObjectType, self).exportChildren(lwrite, level, 'UnixNetworkRouteEntryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flags is not None:
            self.Flags.export(lwrite, level, 'UnixNetworkRouteEntryObj:', name_='Flags', pretty_print=pretty_print)
        if self.MSS is not None:
            self.MSS.export(lwrite, level, 'UnixNetworkRouteEntryObj:', name_='MSS', pretty_print=pretty_print)
        if self.Ref is not None:
            self.Ref.export(lwrite, level, 'UnixNetworkRouteEntryObj:', name_='Ref', pretty_print=pretty_print)
        if self.Use is not None:
            self.Use.export(lwrite, level, 'UnixNetworkRouteEntryObj:', name_='Use', pretty_print=pretty_print)
        if self.Window is not None:
            self.Window.export(lwrite, level, 'UnixNetworkRouteEntryObj:', name_='Window', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixNetworkRouteEntryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flags':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flags(obj_)
        elif nodeName_ == 'MSS':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_MSS(obj_)
        elif nodeName_ == 'Ref':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Ref(obj_)
        elif nodeName_ == 'Use':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Use(obj_)
        elif nodeName_ == 'Window':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Window(obj_)
        super(UnixNetworkRouteEntryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixNetworkRouteEntryObjectType

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
    'Use': cybox_common.UnsignedLongObjectPropertyType,
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
    'Internal_Strings': cybox_common.InternalStringsType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'MSS': cybox_common.UnsignedIntegerObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Window': cybox_common.UnsignedIntegerObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Ref': cybox_common.UnsignedLongObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Valid_Lifetime': cybox_common.DurationObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Flags': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Unix_Network_Route_Entry'
        rootClass = UnixNetworkRouteEntryObjectType
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
        rootTag = 'Unix_Network_Route_Entry'
        rootClass = UnixNetworkRouteEntryObjectType
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
        rootTag = 'Unix_Network_Route_Entry'
        rootClass = UnixNetworkRouteEntryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Unix_Network_Route_Entry",
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
    "UnixNetworkRouteEntryObjectType"
    ]
