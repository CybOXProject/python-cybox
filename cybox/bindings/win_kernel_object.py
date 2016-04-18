# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class SSDTEntryListType(GeneratedsSuper):
    """The SSDTEntryListType type specifies a listing of the entries in the
    System Service Descriptor Table (SSDT)."""

    subclass = None
    superclass = None
    def __init__(self, SSDT_Entry=None):
        if SSDT_Entry is None:
            self.SSDT_Entry = []
        else:
            self.SSDT_Entry = SSDT_Entry
    def factory(*args_, **kwargs_):
        if SSDTEntryListType.subclass:
            return SSDTEntryListType.subclass(*args_, **kwargs_)
        else:
            return SSDTEntryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SSDT_Entry(self): return self.SSDT_Entry
    def set_SSDT_Entry(self, SSDT_Entry): self.SSDT_Entry = SSDT_Entry
    def add_SSDT_Entry(self, value): self.SSDT_Entry.append(value)
    def insert_SSDT_Entry(self, index, value): self.SSDT_Entry[index] = value
    def hasContent_(self):
        if (
            self.SSDT_Entry
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelObj:', name_='SSDTEntryListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SSDTEntryListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelObj:', name_='SSDTEntryListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinKernelObj:', name_='SSDTEntryListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SSDT_Entry_ in self.SSDT_Entry:
            SSDT_Entry_.export(lwrite, level, 'WinKernelObj:', name_='SSDT_Entry', pretty_print=pretty_print)
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
        if nodeName_ == 'SSDT_Entry':
            obj_ = SSDTEntryType.factory()
            obj_.build(child_)
            self.SSDT_Entry.append(obj_)
# end class SSDTEntryListType

class SSDTEntryType(GeneratedsSuper):
    """The SSDTEntryType type specifies a single entry in the System
    Service Descriptor Table (SSDT).The hooked attribute specifies
    whether the SSDT entry is hooked."""

    subclass = None
    superclass = None
    def __init__(self, hooked=None, Service_Table_Base=None, Service_Counter_Table_Base=None, Number_Of_Services=None, Argument_Table_Base=None):
        self.hooked = _cast(bool, hooked)
        self.Service_Table_Base = Service_Table_Base
        self.Service_Counter_Table_Base = Service_Counter_Table_Base
        self.Number_Of_Services = Number_Of_Services
        self.Argument_Table_Base = Argument_Table_Base
    def factory(*args_, **kwargs_):
        if SSDTEntryType.subclass:
            return SSDTEntryType.subclass(*args_, **kwargs_)
        else:
            return SSDTEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Service_Table_Base(self): return self.Service_Table_Base
    def set_Service_Table_Base(self, Service_Table_Base): self.Service_Table_Base = Service_Table_Base
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Service_Counter_Table_Base(self): return self.Service_Counter_Table_Base
    def set_Service_Counter_Table_Base(self, Service_Counter_Table_Base): self.Service_Counter_Table_Base = Service_Counter_Table_Base
    def get_Number_Of_Services(self): return self.Number_Of_Services
    def set_Number_Of_Services(self, Number_Of_Services): self.Number_Of_Services = Number_Of_Services
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Argument_Table_Base(self): return self.Argument_Table_Base
    def set_Argument_Table_Base(self, Argument_Table_Base): self.Argument_Table_Base = Argument_Table_Base
    def get_hooked(self): return self.hooked
    def set_hooked(self, hooked): self.hooked = hooked
    def hasContent_(self):
        if (
            self.Service_Table_Base is not None or
            self.Service_Counter_Table_Base is not None or
            self.Number_Of_Services is not None or
            self.Argument_Table_Base is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelObj:', name_='SSDTEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SSDTEntryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelObj:', name_='SSDTEntryType'):
        if self.hooked is not None:

            lwrite(' hooked="%s"' % self.gds_format_boolean(self.hooked, input_name='hooked'))
    def exportChildren(self, lwrite, level, namespace_='WinKernelObj:', name_='SSDTEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Service_Table_Base is not None:
            self.Service_Table_Base.export(lwrite, level, 'WinKernelObj:', name_='Service_Table_Base', pretty_print=pretty_print)
        if self.Service_Counter_Table_Base is not None:
            self.Service_Counter_Table_Base.export(lwrite, level, 'WinKernelObj:', name_='Service_Counter_Table_Base', pretty_print=pretty_print)
        if self.Number_Of_Services is not None:
            self.Number_Of_Services.export(lwrite, level, 'WinKernelObj:', name_='Number_Of_Services', pretty_print=pretty_print)
        if self.Argument_Table_Base is not None:
            self.Argument_Table_Base.export(lwrite, level, 'WinKernelObj:', name_='Argument_Table_Base', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('hooked', node)
        if value is not None:

            if value in ('true', '1'):
                self.hooked = True
            elif value in ('false', '0'):
                self.hooked = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Service_Table_Base':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_Table_Base(obj_)
        elif nodeName_ == 'Service_Counter_Table_Base':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_Counter_Table_Base(obj_)
        elif nodeName_ == 'Number_Of_Services':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Services(obj_)
        elif nodeName_ == 'Argument_Table_Base':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Argument_Table_Base(obj_)
# end class SSDTEntryType

class IDTEntryListType(GeneratedsSuper):
    """The IDTEntryListType type specifies a listing of the entries in the
    Interrupt Descriptor Table (IDT). The IDT is specific to the
    I386 architecture, indicating where the Prtoetcted mode
    Interrupt Service Routines (ISR) are located. See
    http://wiki.osdev.org/Interrupt_Descriptor_Table"""

    subclass = None
    superclass = None
    def __init__(self, IDT_Entry=None):
        if IDT_Entry is None:
            self.IDT_Entry = []
        else:
            self.IDT_Entry = IDT_Entry
    def factory(*args_, **kwargs_):
        if IDTEntryListType.subclass:
            return IDTEntryListType.subclass(*args_, **kwargs_)
        else:
            return IDTEntryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IDT_Entry(self): return self.IDT_Entry
    def set_IDT_Entry(self, IDT_Entry): self.IDT_Entry = IDT_Entry
    def add_IDT_Entry(self, value): self.IDT_Entry.append(value)
    def insert_IDT_Entry(self, index, value): self.IDT_Entry[index] = value
    def hasContent_(self):
        if (
            self.IDT_Entry
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelObj:', name_='IDTEntryListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IDTEntryListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelObj:', name_='IDTEntryListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinKernelObj:', name_='IDTEntryListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for IDT_Entry_ in self.IDT_Entry:
            IDT_Entry_.export(lwrite, level, 'WinKernelObj:', name_='IDT_Entry', pretty_print=pretty_print)
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
        if nodeName_ == 'IDT_Entry':
            obj_ = IDTEntryType.factory()
            obj_.build(child_)
            self.IDT_Entry.append(obj_)
# end class IDTEntryListType

class IDTEntryType(GeneratedsSuper):
    """The IDTEntryType type specifies a single entry in the Interrupt
    Descriptor Table (IDT). Entries can be interrupt gates, task
    gates, and trap gates."""

    subclass = None
    superclass = None
    def __init__(self, Type_Attr=None, Offset_High=None, Offset_Low=None, Offset_Middle=None, Selector=None):
        self.Type_Attr = Type_Attr
        self.Offset_High = Offset_High
        self.Offset_Low = Offset_Low
        self.Offset_Middle = Offset_Middle
        self.Selector = Selector
    def factory(*args_, **kwargs_):
        if IDTEntryType.subclass:
            return IDTEntryType.subclass(*args_, **kwargs_)
        else:
            return IDTEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type_Attr(self): return self.Type_Attr
    def set_Type_Attr(self, Type_Attr): self.Type_Attr = Type_Attr
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Offset_High(self): return self.Offset_High
    def set_Offset_High(self, Offset_High): self.Offset_High = Offset_High
    def get_Offset_Low(self): return self.Offset_Low
    def set_Offset_Low(self, Offset_Low): self.Offset_Low = Offset_Low
    def get_Offset_Middle(self): return self.Offset_Middle
    def set_Offset_Middle(self, Offset_Middle): self.Offset_Middle = Offset_Middle
    def get_Selector(self): return self.Selector
    def set_Selector(self, Selector): self.Selector = Selector
    def hasContent_(self):
        if (
            self.Type_Attr is not None or
            self.Offset_High is not None or
            self.Offset_Low is not None or
            self.Offset_Middle is not None or
            self.Selector is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelObj:', name_='IDTEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IDTEntryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelObj:', name_='IDTEntryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinKernelObj:', name_='IDTEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type_Attr is not None:
            self.Type_Attr.export(lwrite, level, 'WinKernelObj:', name_='Type_Attr', pretty_print=pretty_print)
        if self.Offset_High is not None:
            self.Offset_High.export(lwrite, level, 'WinKernelObj:', name_='Offset_High', pretty_print=pretty_print)
        if self.Offset_Low is not None:
            self.Offset_Low.export(lwrite, level, 'WinKernelObj:', name_='Offset_Low', pretty_print=pretty_print)
        if self.Offset_Middle is not None:
            self.Offset_Middle.export(lwrite, level, 'WinKernelObj:', name_='Offset_Middle', pretty_print=pretty_print)
        if self.Selector is not None:
            self.Selector.export(lwrite, level, 'WinKernelObj:', name_='Selector', pretty_print=pretty_print)
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
        if nodeName_ == 'Type_Attr':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type_Attr(obj_)
        elif nodeName_ == 'Offset_High':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset_High(obj_)
        elif nodeName_ == 'Offset_Low':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset_Low(obj_)
        elif nodeName_ == 'Offset_Middle':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset_Middle(obj_)
        elif nodeName_ == 'Selector':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Selector(obj_)
# end class IDTEntryType

class WindowsKernelObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsKernelObjectType type is intended to characterize Windows
    Kernel structures."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, IDT=None, SSDT=None):
        super(WindowsKernelObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.IDT = IDT
        self.SSDT = SSDT
    def factory(*args_, **kwargs_):
        if WindowsKernelObjectType.subclass:
            return WindowsKernelObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsKernelObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IDT(self): return self.IDT
    def set_IDT(self, IDT): self.IDT = IDT
    def get_SSDT(self): return self.SSDT
    def set_SSDT(self, SSDT): self.SSDT = SSDT
    def hasContent_(self):
        if (
            self.IDT is not None or
            self.SSDT is not None or
            super(WindowsKernelObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelObj:', name_='WindowsKernelObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsKernelObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelObj:', name_='WindowsKernelObjectType'):
        super(WindowsKernelObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsKernelObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinKernelObj:', name_='WindowsKernelObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsKernelObjectType, self).exportChildren(lwrite, level, 'WinKernelObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IDT is not None:
            self.IDT.export(lwrite, level, 'WinKernelObj:', name_='IDT', pretty_print=pretty_print)
        if self.SSDT is not None:
            self.SSDT.export(lwrite, level, 'WinKernelObj:', name_='SSDT', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsKernelObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IDT':
            obj_ = IDTEntryListType.factory()
            obj_.build(child_)
            self.set_IDT(obj_)
        elif nodeName_ == 'SSDT':
            obj_ = SSDTEntryListType.factory()
            obj_.build(child_)
            self.set_SSDT(obj_)
        super(WindowsKernelObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsKernelObjectType

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
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
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
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Selector': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Argument_Table_Base': cybox_common.HexBinaryObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Number_Of_Services': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Type_Attr': cybox_common.HexBinaryObjectPropertyType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Data_Size': cybox_common.DataSizeType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Offset_High': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Offset_Low': cybox_common.HexBinaryObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Offset_Middle': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Service_Counter_Table_Base': cybox_common.HexBinaryObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Service_Table_Base': cybox_common.HexBinaryObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Date': cybox_common.DateRangeType,
    'Dependency_Description': cybox_common.StructuredTextType,
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
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
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
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
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
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Kernel",
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
    "WindowsKernelObjectType",
    "SSDTEntryListType",
    "SSDTEntryType",
    "IDTEntryListType",
    "IDTEntryType"
    ]
