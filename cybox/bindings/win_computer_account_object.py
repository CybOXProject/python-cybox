# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import account_object
from . import port_object


class FullyQualifiedNameType(GeneratedsSuper):
    """The FullyQualifiedNameType type refers to the fully qualified
    name(s) of the Windows computer account."""

    subclass = None
    superclass = None
    def __init__(self, NetBEUI_Name=None, Full_Name=None):
        self.NetBEUI_Name = NetBEUI_Name
        self.Full_Name = Full_Name
    def factory(*args_, **kwargs_):
        if FullyQualifiedNameType.subclass:
            return FullyQualifiedNameType.subclass(*args_, **kwargs_)
        else:
            return FullyQualifiedNameType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_NetBEUI_Name(self): return self.NetBEUI_Name
    def set_NetBEUI_Name(self, NetBEUI_Name): self.NetBEUI_Name = NetBEUI_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Full_Name(self): return self.Full_Name
    def set_Full_Name(self, Full_Name): self.Full_Name = Full_Name
    def hasContent_(self):
        if (
            self.NetBEUI_Name is not None or
            self.Full_Name is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='FullyQualifiedNameType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FullyQualifiedNameType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinComputerAccountObj:', name_='FullyQualifiedNameType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='FullyQualifiedNameType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NetBEUI_Name is not None:
            self.NetBEUI_Name.export(lwrite, level, 'WinComputerAccountObj:', name_='NetBEUI_Name', pretty_print=pretty_print)
        if self.Full_Name is not None:
            self.Full_Name.export(lwrite, level, 'WinComputerAccountObj:', name_='Full_Name', pretty_print=pretty_print)
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
        if nodeName_ == 'NetBEUI_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_NetBEUI_Name(obj_)
        elif nodeName_ == 'Full_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Full_Name(obj_)
# end class FullyQualifiedNameType

class KerberosType(GeneratedsSuper):
    """The KerberosType type specifies the Kerberos authentication protocol
    specific Object properties for the Windows computer account."""

    subclass = None
    superclass = None
    def __init__(self, Delegation=None, Ticket=None):
        self.Delegation = Delegation
        self.Ticket = Ticket
    def factory(*args_, **kwargs_):
        if KerberosType.subclass:
            return KerberosType.subclass(*args_, **kwargs_)
        else:
            return KerberosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Delegation(self): return self.Delegation
    def set_Delegation(self, Delegation): self.Delegation = Delegation
    def get_Ticket(self): return self.Ticket
    def set_Ticket(self, Ticket): self.Ticket = Ticket
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Delegation is not None or
            self.Ticket is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KerberosType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinComputerAccountObj:', name_='KerberosType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Delegation is not None:
            self.Delegation.export(lwrite, level, 'WinComputerAccountObj:', name_='Delegation', pretty_print=pretty_print)
        if self.Ticket is not None:
            self.Ticket.export(lwrite, level, 'WinComputerAccountObj:', name_='Ticket', pretty_print=pretty_print)
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
        if nodeName_ == 'Delegation':
            obj_ = KerberosDelegationType.factory()
            obj_.build(child_)
            self.set_Delegation(obj_)
        elif nodeName_ == 'Ticket':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Ticket(obj_)
# end class KerberosType

class KerberosDelegationType(GeneratedsSuper):
    """The Delegation field specifies the Kerberos delegation used for the
    Windows computer account."""

    subclass = None
    superclass = None
    def __init__(self, Bitmask=None, Service=None):
        self.Bitmask = Bitmask
        self.Service = Service
    def factory(*args_, **kwargs_):
        if KerberosDelegationType.subclass:
            return KerberosDelegationType.subclass(*args_, **kwargs_)
        else:
            return KerberosDelegationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Bitmask(self): return self.Bitmask
    def set_Bitmask(self, Bitmask): self.Bitmask = Bitmask
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Service(self): return self.Service
    def set_Service(self, Service): self.Service = Service
    def hasContent_(self):
        if (
            self.Bitmask is not None or
            self.Service is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosDelegationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KerberosDelegationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinComputerAccountObj:', name_='KerberosDelegationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosDelegationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Bitmask is not None:
            self.Bitmask.export(lwrite, level, 'WinComputerAccountObj:', name_='Bitmask', pretty_print=pretty_print)
        if self.Service is not None:
            self.Service.export(lwrite, level, 'WinComputerAccountObj:', name_='Service', pretty_print=pretty_print)
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
        if nodeName_ == 'Bitmask':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Bitmask(obj_)
        elif nodeName_ == 'Service':
            obj_ = KerberosServiceType.factory()
            obj_.build(child_)
            self.set_Service(obj_)
# end class KerberosDelegationType

class KerberosServiceType(GeneratedsSuper):
    """The KerberosServiceType specifies the properties of the Kerberos
    delegation service for the Windows computer account."""

    subclass = None
    superclass = None
    def __init__(self, Computer=None, Name=None, Port=None, User=None):
        self.Computer = Computer
        self.Name = Name
        self.Port = Port
        self.User = User
    def factory(*args_, **kwargs_):
        if KerberosServiceType.subclass:
            return KerberosServiceType.subclass(*args_, **kwargs_)
        else:
            return KerberosServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Computer(self): return self.Computer
    def set_Computer(self, Computer): self.Computer = Computer
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Port(self): return self.Port
    def set_Port(self, Port): self.Port = Port
    def get_User(self): return self.User
    def set_User(self, User): self.User = User
    def hasContent_(self):
        if (
            self.Computer is not None or
            self.Name is not None or
            self.Port is not None or
            self.User is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosServiceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KerberosServiceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinComputerAccountObj:', name_='KerberosServiceType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='KerberosServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Computer is not None:
            self.Computer.export(lwrite, level, 'WinComputerAccountObj:', name_='Computer', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinComputerAccountObj:', name_='Name', pretty_print=pretty_print)
        if self.Port is not None:
            self.Port.export(lwrite, level, 'WinComputerAccountObj:', name_='Port', pretty_print=pretty_print)
        if self.User is not None:
            self.User.export(lwrite, level, 'WinComputerAccountObj:', name_='User', pretty_print=pretty_print)
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
        if nodeName_ == 'Computer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Computer(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Port':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_Port(obj_)
        elif nodeName_ == 'User':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User(obj_)
# end class KerberosServiceType

class WindowsComputerAccountObjectType(account_object.AccountObjectType):
    """The WinComputerAccountObject type is intended to characterize
    Windows computer accounts."""

    subclass = None
    superclass = account_object.AccountObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, disabled=None, locked_out=None, Description=None, Domain=None, Fully_Qualified_Name=None, Kerberos=None, Security_ID=None, Security_Type=None, Type=None):
        super(WindowsComputerAccountObjectType, self).__init__(object_reference, Custom_Properties, disabled, locked_out, Description, Domain, )
        self.Fully_Qualified_Name = Fully_Qualified_Name
        self.Kerberos = Kerberos
        self.Security_ID = Security_ID
        self.Security_Type = Security_Type
        self.Type = Type
    def factory(*args_, **kwargs_):
        if WindowsComputerAccountObjectType.subclass:
            return WindowsComputerAccountObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsComputerAccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Fully_Qualified_Name(self): return self.Fully_Qualified_Name
    def set_Fully_Qualified_Name(self, Fully_Qualified_Name): self.Fully_Qualified_Name = Fully_Qualified_Name
    def get_Kerberos(self): return self.Kerberos
    def set_Kerberos(self, Kerberos): self.Kerberos = Kerberos
    def get_Security_ID(self): return self.Security_ID
    def set_Security_ID(self, Security_ID): self.Security_ID = Security_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Security_Type(self): return self.Security_Type
    def set_Security_Type(self, Security_Type): self.Security_Type = Security_Type
    def validate_SIDType(self, value):
        # Validate type cybox_common.SIDType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def hasContent_(self):
        if (
            self.Fully_Qualified_Name is not None or
            self.Kerberos is not None or
            self.Security_ID is not None or
            self.Security_Type is not None or
            self.Type is not None or
            super(WindowsComputerAccountObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='WindowsComputerAccountObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsComputerAccountObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinComputerAccountObj:', name_='WindowsComputerAccountObjectType'):
        super(WindowsComputerAccountObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsComputerAccountObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinComputerAccountObj:', name_='WindowsComputerAccountObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsComputerAccountObjectType, self).exportChildren(lwrite, level, 'WinComputerAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Fully_Qualified_Name is not None:
            self.Fully_Qualified_Name.export(lwrite, level, 'WinComputerAccountObj:', name_='Fully_Qualified_Name', pretty_print=pretty_print)
        if self.Kerberos is not None:
            self.Kerberos.export(lwrite, level, 'WinComputerAccountObj:', name_='Kerberos', pretty_print=pretty_print)
        if self.Security_ID is not None:
            self.Security_ID.export(lwrite, level, 'WinComputerAccountObj:', name_='Security_ID', pretty_print=pretty_print)
        if self.Security_Type is not None:
            self.Security_Type.export(lwrite, level, 'WinComputerAccountObj:', name_='Security_Type', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinComputerAccountObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsComputerAccountObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Fully_Qualified_Name':
            obj_ = FullyQualifiedNameType.factory()
            obj_.build(child_)
            self.set_Fully_Qualified_Name(obj_)
        elif nodeName_ == 'Kerberos':
            obj_ = KerberosType.factory()
            obj_.build(child_)
            self.set_Kerberos(obj_)
        elif nodeName_ == 'Security_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_ID(obj_)
        elif nodeName_ == 'Security_Type':
            obj_ = cybox_common.SIDType.factory()
            obj_.build(child_)
            self.set_Security_Type(obj_)
        elif nodeName_ == 'Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(WindowsComputerAccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsComputerAccountObjectType

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
    'Account': account_object.AccountObjectType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Compiler': cybox_common.CompilerType,
    'Layer4_Protocol': port_object.Layer4ProtocolType,
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
    'NetBEUI_Name': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Bitmask': cybox_common.HexBinaryObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Domain': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Security_Type': cybox_common.SIDType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Computer': cybox_common.StringObjectPropertyType,
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
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'User': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Full_Name': cybox_common.StringObjectPropertyType,
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
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Libraries': cybox_common.LibrariesType,
    'Security_ID': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Ticket': cybox_common.UnsignedLongObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Port': port_object.PortObjectType,
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
        rootTag = 'Windows_Computer_Account'
        rootClass = WindowsComputerAccountObjectType
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
        rootTag = 'Windows_Computer_Account'
        rootClass = WindowsComputerAccountObjectType
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
        rootTag = 'Windows_Computer_Account'
        rootClass = WindowsComputerAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Computer_Account",
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
    "WindowsComputerAccountObjectType",
    "FullyQualifiedNameType",
    "KerberosType",
    "KerberosDelegationType",
    "KerberosServiceType"
    ]
