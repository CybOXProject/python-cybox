# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import system_object
from . import win_handle_object


class GlobalFlagListType(GeneratedsSuper):
    """The GlobalFlagListType type is a listing of all Windows global
    flags."""

    subclass = None
    superclass = None
    def __init__(self, Global_Flag=None):
        if Global_Flag is None:
            self.Global_Flag = []
        else:
            self.Global_Flag = Global_Flag
    def factory(*args_, **kwargs_):
        if GlobalFlagListType.subclass:
            return GlobalFlagListType.subclass(*args_, **kwargs_)
        else:
            return GlobalFlagListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Global_Flag(self): return self.Global_Flag
    def set_Global_Flag(self, Global_Flag): self.Global_Flag = Global_Flag
    def add_Global_Flag(self, value): self.Global_Flag.append(value)
    def insert_Global_Flag(self, index, value): self.Global_Flag[index] = value
    def hasContent_(self):
        if (
            self.Global_Flag
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemObj:', name_='GlobalFlagListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GlobalFlagListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemObj:', name_='GlobalFlagListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinSystemObj:', name_='GlobalFlagListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Global_Flag_ in self.Global_Flag:
            Global_Flag_.export(lwrite, level, 'WinSystemObj:', name_='Global_Flag', pretty_print=pretty_print)
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
        if nodeName_ == 'Global_Flag':
            obj_ = GlobalFlagType.factory()
            obj_.build(child_)
            self.Global_Flag.append(obj_)
# end class GlobalFlagListType

class GlobalFlagType(GeneratedsSuper):
    """The GlobalFlagType type is intended to characterize Windows global
    flags."""

    subclass = None
    superclass = None
    def __init__(self, Abbreviation=None, Destination=None, Hexadecimal_Value=None, Symbolic_Name=None):
        self.Abbreviation = Abbreviation
        self.Destination = Destination
        self.Hexadecimal_Value = Hexadecimal_Value
        self.Symbolic_Name = Symbolic_Name
    def factory(*args_, **kwargs_):
        if GlobalFlagType.subclass:
            return GlobalFlagType.subclass(*args_, **kwargs_)
        else:
            return GlobalFlagType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Abbreviation(self): return self.Abbreviation
    def set_Abbreviation(self, Abbreviation): self.Abbreviation = Abbreviation
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Destination(self): return self.Destination
    def set_Destination(self, Destination): self.Destination = Destination
    def get_Hexadecimal_Value(self): return self.Hexadecimal_Value
    def set_Hexadecimal_Value(self, Hexadecimal_Value): self.Hexadecimal_Value = Hexadecimal_Value
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Symbolic_Name(self): return self.Symbolic_Name
    def set_Symbolic_Name(self, Symbolic_Name): self.Symbolic_Name = Symbolic_Name
    def hasContent_(self):
        if (
            self.Abbreviation is not None or
            self.Destination is not None or
            self.Hexadecimal_Value is not None or
            self.Symbolic_Name is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemObj:', name_='GlobalFlagType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GlobalFlagType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemObj:', name_='GlobalFlagType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinSystemObj:', name_='GlobalFlagType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Abbreviation is not None:
            self.Abbreviation.export(lwrite, level, 'WinSystemObj:', name_='Abbreviation', pretty_print=pretty_print)
        if self.Destination is not None:
            self.Destination.export(lwrite, level, 'WinSystemObj:', name_='Destination', pretty_print=pretty_print)
        if self.Hexadecimal_Value is not None:
            self.Hexadecimal_Value.export(lwrite, level, 'WinSystemObj:', name_='Hexadecimal_Value', pretty_print=pretty_print)
        if self.Symbolic_Name is not None:
            self.Symbolic_Name.export(lwrite, level, 'WinSystemObj:', name_='Symbolic_Name', pretty_print=pretty_print)
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
        if nodeName_ == 'Abbreviation':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Abbreviation(obj_)
        elif nodeName_ == 'Destination':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Destination(obj_)
        elif nodeName_ == 'Hexadecimal_Value':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hexadecimal_Value(obj_)
        elif nodeName_ == 'Symbolic_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Symbolic_Name(obj_)
# end class GlobalFlagType

class WindowsSystemObjectType(system_object.SystemObjectType):
    """The WindowsSystemObjectType type is intended to characterize Windows
    systems."""

    subclass = None
    superclass = system_object.SystemObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Available_Physical_Memory=None, BIOS_Info=None, Date=None, Hostname=None, Local_Time=None, Network_Interface_List=None, OS=None, Processor=None, Processor_Architecture=None, System_Time=None, Timezone_DST=None, Timezone_Standard=None, Total_Physical_Memory=None, Uptime=None, Username=None, Domain=None, Global_Flag_List=None, NetBIOS_Name=None, Open_Handle_List=None, Product_ID=None, Product_Name=None, Registered_Organization=None, Registered_Owner=None, Windows_Directory=None, Windows_System_Directory=None, Windows_Temp_Directory=None):
        super(WindowsSystemObjectType, self).__init__(object_reference, Custom_Properties, xsi_type, Available_Physical_Memory, BIOS_Info, Date, Hostname, Local_Time, Network_Interface_List, OS, Processor, Processor_Architecture, System_Time, Timezone_DST, Timezone_Standard, Total_Physical_Memory, Uptime, Username, )
        if Domain is None:
            self.Domain = []
        else:
            self.Domain = Domain
        self.Global_Flag_List = Global_Flag_List
        self.NetBIOS_Name = NetBIOS_Name
        self.Open_Handle_List = Open_Handle_List
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.Registered_Organization = Registered_Organization
        self.Registered_Owner = Registered_Owner
        self.Windows_Directory = Windows_Directory
        self.Windows_System_Directory = Windows_System_Directory
        self.Windows_Temp_Directory = Windows_Temp_Directory
    def factory(*args_, **kwargs_):
        if WindowsSystemObjectType.subclass:
            return WindowsSystemObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsSystemObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Domain(self): return self.Domain
    def set_Domain(self, Domain): self.Domain = Domain
    def add_Domain(self, value): self.Domain.append(value)
    def insert_Domain(self, index, value): self.Domain[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Global_Flag_List(self): return self.Global_Flag_List
    def set_Global_Flag_List(self, Global_Flag_List): self.Global_Flag_List = Global_Flag_List
    def get_NetBIOS_Name(self): return self.NetBIOS_Name
    def set_NetBIOS_Name(self, NetBIOS_Name): self.NetBIOS_Name = NetBIOS_Name
    def get_Open_Handle_List(self): return self.Open_Handle_List
    def set_Open_Handle_List(self, Open_Handle_List): self.Open_Handle_List = Open_Handle_List
    def get_Product_ID(self): return self.Product_ID
    def set_Product_ID(self, Product_ID): self.Product_ID = Product_ID
    def get_Product_Name(self): return self.Product_Name
    def set_Product_Name(self, Product_Name): self.Product_Name = Product_Name
    def get_Registered_Organization(self): return self.Registered_Organization
    def set_Registered_Organization(self, Registered_Organization): self.Registered_Organization = Registered_Organization
    def get_Registered_Owner(self): return self.Registered_Owner
    def set_Registered_Owner(self, Registered_Owner): self.Registered_Owner = Registered_Owner
    def get_Windows_Directory(self): return self.Windows_Directory
    def set_Windows_Directory(self, Windows_Directory): self.Windows_Directory = Windows_Directory
    def get_Windows_System_Directory(self): return self.Windows_System_Directory
    def set_Windows_System_Directory(self, Windows_System_Directory): self.Windows_System_Directory = Windows_System_Directory
    def get_Windows_Temp_Directory(self): return self.Windows_Temp_Directory
    def set_Windows_Temp_Directory(self, Windows_Temp_Directory): self.Windows_Temp_Directory = Windows_Temp_Directory
    def hasContent_(self):
        if (
            self.Domain or
            self.Global_Flag_List is not None or
            self.NetBIOS_Name is not None or
            self.Open_Handle_List is not None or
            self.Product_ID is not None or
            self.Product_Name is not None or
            self.Registered_Organization is not None or
            self.Registered_Owner is not None or
            self.Windows_Directory is not None or
            self.Windows_System_Directory is not None or
            self.Windows_Temp_Directory is not None or
            super(WindowsSystemObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinSystemObj:', name_='WindowsSystemObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsSystemObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinSystemObj:', name_='WindowsSystemObjectType'):
        super(WindowsSystemObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsSystemObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinSystemObj:', name_='WindowsSystemObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsSystemObjectType, self).exportChildren(lwrite, level, 'WinSystemObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Domain_ in self.Domain:
            Domain_.export(lwrite, level, 'WinSystemObj:', name_='Domain', pretty_print=pretty_print)
        if self.Global_Flag_List is not None:
            self.Global_Flag_List.export(lwrite, level, 'WinSystemObj:', name_='Global_Flag_List', pretty_print=pretty_print)
        if self.NetBIOS_Name is not None:
            self.NetBIOS_Name.export(lwrite, level, 'WinSystemObj:', name_='NetBIOS_Name', pretty_print=pretty_print)
        if self.Open_Handle_List is not None:
            self.Open_Handle_List.export(lwrite, level, 'WinSystemObj:', name_='Open_Handle_List', pretty_print=pretty_print)
        if self.Product_ID is not None:
            self.Product_ID.export(lwrite, level, 'WinSystemObj:', name_='Product_ID', pretty_print=pretty_print)
        if self.Product_Name is not None:
            self.Product_Name.export(lwrite, level, 'WinSystemObj:', name_='Product_Name', pretty_print=pretty_print)
        if self.Registered_Organization is not None:
            self.Registered_Organization.export(lwrite, level, 'WinSystemObj:', name_='Registered_Organization', pretty_print=pretty_print)
        if self.Registered_Owner is not None:
            self.Registered_Owner.export(lwrite, level, 'WinSystemObj:', name_='Registered_Owner', pretty_print=pretty_print)
        if self.Windows_Directory is not None:
            self.Windows_Directory.export(lwrite, level, 'WinSystemObj:', name_='Windows_Directory', pretty_print=pretty_print)
        if self.Windows_System_Directory is not None:
            self.Windows_System_Directory.export(lwrite, level, 'WinSystemObj:', name_='Windows_System_Directory', pretty_print=pretty_print)
        if self.Windows_Temp_Directory is not None:
            self.Windows_Temp_Directory.export(lwrite, level, 'WinSystemObj:', name_='Windows_Temp_Directory', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsSystemObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Domain':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Domain.append(obj_)
        elif nodeName_ == 'Global_Flag_List':
            obj_ = GlobalFlagListType.factory()
            obj_.build(child_)
            self.set_Global_Flag_List(obj_)
        elif nodeName_ == 'NetBIOS_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_NetBIOS_Name(obj_)
        elif nodeName_ == 'Open_Handle_List':
            obj_ = win_handle_object.WindowsHandleListType.factory()
            obj_.build(child_)
            self.set_Open_Handle_List(obj_)
        elif nodeName_ == 'Product_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Product_ID(obj_)
        elif nodeName_ == 'Product_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Product_Name(obj_)
        elif nodeName_ == 'Registered_Organization':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Registered_Organization(obj_)
        elif nodeName_ == 'Registered_Owner':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Registered_Owner(obj_)
        elif nodeName_ == 'Windows_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Windows_Directory(obj_)
        elif nodeName_ == 'Windows_System_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Windows_System_Directory(obj_)
        elif nodeName_ == 'Windows_Temp_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Windows_Temp_Directory(obj_)
        super(WindowsSystemObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsSystemObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Open_Handle_List': win_handle_object.WindowsHandleListType,
    'DHCP_Lease_Expires': cybox_common.DateTimeObjectPropertyType,
    'Destination': cybox_common.StringObjectPropertyType,
    'Processor_Architecture': system_object.ProcessorArchType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Hexadecimal_Value': cybox_common.HexBinaryObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'BIOS_Date': cybox_common.DateObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Network_Interface_List': system_object.NetworkInterfaceListType,
    'NetBIOS_Name': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'IP_Gateway_List': system_object.IPGatewayListType,
    'Windows_System_Directory': cybox_common.StringObjectPropertyType,
    'Registered_Owner': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Abbreviation': cybox_common.StringObjectPropertyType,
    'MAC': cybox_common.StringObjectPropertyType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'OS': system_object.OSType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
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
    'Product_Name': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'BIOS_Info': system_object.BIOSInfoType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Registered_Organization': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Domain': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'BIOS_Manufacturer': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Available_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Uptime': cybox_common.DurationObjectPropertyType,
    'IP_List': system_object.IPInfoListType,
    'Timezone_DST': cybox_common.StringObjectPropertyType,
    'Hostname': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Bitness': system_object.BitnessType,
    'BIOS_Version': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
    'IP_Info': system_object.IPInfoType,
    'System_Time': cybox_common.TimeObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Build_Number': cybox_common.StringObjectPropertyType,
    'Adapter': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Patch_Level': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Windows_Directory': cybox_common.StringObjectPropertyType,
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
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Install_Date': cybox_common.DateObjectPropertyType,
    'Total_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'DHCP_Lease_Obtained': cybox_common.DateTimeObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Network_Interface': system_object.NetworkInterfaceType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Time': cybox_common.TimeType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Timezone_Standard': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StringObjectPropertyType,
    'BIOS_Serial_Number': cybox_common.StringObjectPropertyType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Symbolic_Name': cybox_common.StringObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Local_Time': cybox_common.TimeObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Processor': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Windows_Temp_Directory': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'BIOS_Release_Date': cybox_common.DateObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'Product_ID': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Windows_System'
        rootClass = WindowsSystemObjectType
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
        rootTag = 'Windows_System'
        rootClass = WindowsSystemObjectType
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
        rootTag = 'Windows_System'
        rootClass = WindowsSystemObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_System",
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
    "WindowsSystemObjectType",
    "GlobalFlagListType",
    "GlobalFlagType"
    ]
