# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_file_object


class PEChecksumType(GeneratedsSuper):
    """The PECheckSumType records the checksum of the PE file, both as
    found in the file and computed."""

    subclass = None
    superclass = None
    def __init__(self, PE_Computed_API=None, PE_File_API=None, PE_File_Raw=None):
        self.PE_Computed_API = PE_Computed_API
        self.PE_File_API = PE_File_API
        self.PE_File_Raw = PE_File_Raw
    def factory(*args_, **kwargs_):
        if PEChecksumType.subclass:
            return PEChecksumType.subclass(*args_, **kwargs_)
        else:
            return PEChecksumType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PE_Computed_API(self): return self.PE_Computed_API
    def set_PE_Computed_API(self, PE_Computed_API): self.PE_Computed_API = PE_Computed_API
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_PE_File_API(self): return self.PE_File_API
    def set_PE_File_API(self, PE_File_API): self.PE_File_API = PE_File_API
    def get_PE_File_Raw(self): return self.PE_File_Raw
    def set_PE_File_Raw(self, PE_File_Raw): self.PE_File_Raw = PE_File_Raw
    def hasContent_(self):
        if (
            self.PE_Computed_API is not None or
            self.PE_File_API is not None or
            self.PE_File_Raw is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEChecksumType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEChecksumType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEChecksumType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEChecksumType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PE_Computed_API is not None:
            self.PE_Computed_API.export(lwrite, level, 'WinExecutableFileObj:', name_='PE_Computed_API', pretty_print=pretty_print)
        if self.PE_File_API is not None:
            self.PE_File_API.export(lwrite, level, 'WinExecutableFileObj:', name_='PE_File_API', pretty_print=pretty_print)
        if self.PE_File_Raw is not None:
            self.PE_File_Raw.export(lwrite, level, 'WinExecutableFileObj:', name_='PE_File_Raw', pretty_print=pretty_print)
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
        if nodeName_ == 'PE_Computed_API':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_PE_Computed_API(obj_)
        elif nodeName_ == 'PE_File_API':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_PE_File_API(obj_)
        elif nodeName_ == 'PE_File_Raw':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_PE_File_Raw(obj_)
# end class PEChecksumType

class PEExportsType(GeneratedsSuper):
    """PEExportsType specifies the PE File exports data section. The
    exports data section contains information about symbols exported
    by the PE File (a DLL) which can be dynamically loaded by other
    executables. This type abstracts, and its components, abstract
    the Windows structures."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Exported_Functions=None, Number_Of_Functions=None, Exports_Time_Stamp=None, Number_Of_Addresses=None, Number_Of_Names=None):
        self.Name = Name
        self.Exported_Functions = Exported_Functions
        self.Number_Of_Functions = Number_Of_Functions
        self.Exports_Time_Stamp = Exports_Time_Stamp
        self.Number_Of_Addresses = Number_Of_Addresses
        self.Number_Of_Names = Number_Of_Names
    def factory(*args_, **kwargs_):
        if PEExportsType.subclass:
            return PEExportsType.subclass(*args_, **kwargs_)
        else:
            return PEExportsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Exported_Functions(self): return self.Exported_Functions
    def set_Exported_Functions(self, Exported_Functions): self.Exported_Functions = Exported_Functions
    def get_Number_Of_Functions(self): return self.Number_Of_Functions
    def set_Number_Of_Functions(self, Number_Of_Functions): self.Number_Of_Functions = Number_Of_Functions
    def get_Exports_Time_Stamp(self): return self.Exports_Time_Stamp
    def set_Exports_Time_Stamp(self, Exports_Time_Stamp): self.Exports_Time_Stamp = Exports_Time_Stamp
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Addresses(self): return self.Number_Of_Addresses
    def set_Number_Of_Addresses(self, Number_Of_Addresses): self.Number_Of_Addresses = Number_Of_Addresses
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Names(self): return self.Number_Of_Names
    def set_Number_Of_Names(self, Number_Of_Names): self.Number_Of_Names = Number_Of_Names
    def hasContent_(self):
        if (
            self. Name is not None or
            self.Exported_Functions is not None or
            self.Number_Of_Functions is not None or
            self.Exports_Time_Stamp is not None or
            self.Number_Of_Addresses is not None or
            self.Number_Of_Names is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEExportsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEExportsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Name', pretty_print=pretty_print)
        if self.Exported_Functions is not None:
            self.Exported_Functions.export(lwrite, level, 'WinExecutableFileObj:', name_='Exported_Functions', pretty_print=pretty_print)
        if self.Number_Of_Functions is not None:
            self.Number_Of_Functions.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Functions', pretty_print=pretty_print)
        if self.Exports_Time_Stamp is not None:
            self.Exports_Time_Stamp.export(lwrite, level, 'WinExecutableFileObj:', name_='Exports_Time_Stamp', pretty_print=pretty_print)
        if self.Number_Of_Addresses is not None:
            self.Number_Of_Addresses.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Addresses', pretty_print=pretty_print)
        if self.Number_Of_Names is not None:
            self.Number_Of_Names.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Names', pretty_print=pretty_print)
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
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Exported_Functions':
            obj_ = PEExportedFunctionsType.factory()
            obj_.build(child_)
            self.set_Exported_Functions(obj_)
        elif nodeName_ == 'Number_Of_Functions':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Functions(obj_)
        elif nodeName_ == 'Exports_Time_Stamp':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exports_Time_Stamp(obj_)
        elif nodeName_ == 'Number_Of_Addresses':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Addresses(obj_)
        elif nodeName_ == 'Number_Of_Names':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Names(obj_)
# end class PEExportsType

class PEExportedFunctionsType(GeneratedsSuper):
    """PEExportedFunctionsType specifies a list of PE exported functions"""

    subclass = None
    superclass = None
    def __init__(self, Exported_Function=None):
        if Exported_Function is None:
            self.Exported_Function = []
        else:
            self.Exported_Function = Exported_Function
    def factory(*args_, **kwargs_):
        if PEExportedFunctionsType.subclass:
            return PEExportedFunctionsType.subclass(*args_, **kwargs_)
        else:
            return PEExportedFunctionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Exported_Function(self): return self.Exported_Function
    def set_Exported_Function(self, Exported_Function): self.Exported_Function = Exported_Function
    def add_Exported_Function(self, value): self.Exported_Function.append(value)
    def insert_Exported_Function(self, index, value): self.Exported_Function[index] = value
    def hasContent_(self):
        if (
            self.Exported_Function
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEExportedFunctionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Exported_Function_ in self.Exported_Function:
            Exported_Function_.export(lwrite, level, 'WinExecutableFileObj:', name_='Exported_Function', pretty_print=pretty_print)
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
        if nodeName_ == 'Exported_Function':
            obj_ = PEExportedFunctionType.factory()
            obj_.build(child_)
            self.Exported_Function.append(obj_)
# end class PEExportedFunctionsType

class PESectionListType(GeneratedsSuper):
    """Specifies a list of sections that appear in the PE file."""

    subclass = None
    superclass = None
    def __init__(self, Section=None):
        if Section is None:
            self.Section = []
        else:
            self.Section = Section
    def factory(*args_, **kwargs_):
        if PESectionListType.subclass:
            return PESectionListType.subclass(*args_, **kwargs_)
        else:
            return PESectionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Section(self): return self.Section
    def set_Section(self, Section): self.Section = Section
    def add_Section(self, value): self.Section.append(value)
    def insert_Section(self, index, value): self.Section[index] = value
    def hasContent_(self):
        if (
            self.Section
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PESectionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PESectionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Section_ in self.Section:
            Section_.export(lwrite, level, 'WinExecutableFileObj:', name_='Section', pretty_print=pretty_print)
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
        if nodeName_ == 'Section':
            obj_ = PESectionType.factory()
            obj_.build(child_)
            self.Section.append(obj_)
# end class PESectionListType

class EntropyType(GeneratedsSuper):
    """Specifies the result of an entropy computation."""

    subclass = None
    superclass = None
    def __init__(self, Value=None, Min=None, Max=None):
        self.Value = Value
        self.Min = Min
        self.Max = Max
    def factory(*args_, **kwargs_):
        if EntropyType.subclass:
            return EntropyType.subclass(*args_, **kwargs_)
        else:
            return EntropyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def validate_FloatObjectPropertyType(self, value):
        # Validate type cybox_common.FloatObjectPropertyType, a restriction on None.
        pass
    def get_Min(self): return self.Min
    def set_Min(self, Min): self.Min = Min
    def get_Max(self): return self.Max
    def set_Max(self, Max): self.Max = Max
    def hasContent_(self):
        if (
            self.Value is not None or
            self.Min is not None or
            self.Max is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='EntropyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EntropyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='EntropyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='EntropyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            self.Value.export(lwrite, level, 'WinExecutableFileObj:', name_='Value', pretty_print=pretty_print)
        if self.Min is not None:
            self.Min.export(lwrite, level, 'WinExecutableFileObj:', name_='Min', pretty_print=pretty_print)
        if self.Max is not None:
            self.Max.export(lwrite, level, 'WinExecutableFileObj:', name_='Max', pretty_print=pretty_print)
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
        if nodeName_ == 'Value':
            obj_ = cybox_common.FloatObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Value(obj_)
        elif nodeName_ == 'Min':
            obj_ = cybox_common.FloatObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Min(obj_)
        elif nodeName_ == 'Max':
            obj_ = cybox_common.FloatObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Max(obj_)
# end class EntropyType

class PEImportType(GeneratedsSuper):
    """The PEImportType type is intended as container for the properties
    relevant to PE binary imports.The delay_load field is a boolean
    value that is intended to describe whether a PE binary import is
    delay-load or not.The initially_visible field refers to whether
    the import is initially visible, with regards to being initially
    visible or hidden in relation to PE binary packing. A packed
    binary will typically have few initially visible imports, and
    thus it is necessary to make the distinction between those that
    are visible initially or only after the binary is unpacked."""

    subclass = None
    superclass = None
    def __init__(self, initially_visible=None, delay_load=None, File_Name=None, Imported_Functions=None, Virtual_Address=None):
        self.initially_visible = _cast(bool, initially_visible)
        self.delay_load = _cast(bool, delay_load)
        self.File_Name = File_Name
        self.Imported_Functions = Imported_Functions
        self.Virtual_Address = Virtual_Address
    def factory(*args_, **kwargs_):
        if PEImportType.subclass:
            return PEImportType.subclass(*args_, **kwargs_)
        else:
            return PEImportType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File_Name(self): return self.File_Name
    def set_File_Name(self, File_Name): self.File_Name = File_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Imported_Functions(self): return self.Imported_Functions
    def set_Imported_Functions(self, Imported_Functions): self.Imported_Functions = Imported_Functions
    def get_Virtual_Address(self): return self.Virtual_Address
    def set_Virtual_Address(self, Virtual_Address): self.Virtual_Address = Virtual_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_initially_visible(self): return self.initially_visible
    def set_initially_visible(self, initially_visible): self.initially_visible = initially_visible
    def get_delay_load(self): return self.delay_load
    def set_delay_load(self, delay_load): self.delay_load = delay_load
    def hasContent_(self):
        if (
            self.File_Name is not None or
            self.Imported_Functions is not None or
            self.Virtual_Address is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEImportType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEImportType'):
        if self.initially_visible is not None:

            lwrite(' initially_visible="%s"' % self.gds_format_boolean(self.initially_visible, input_name='initially_visible'))
        if self.delay_load is not None:

            lwrite(' delay_load="%s"' % self.gds_format_boolean(self.delay_load, input_name='delay_load'))
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.File_Name is not None:
            self.File_Name.export(lwrite, level, 'WinExecutableFileObj:', name_='File_Name', pretty_print=pretty_print)
        if self.Imported_Functions is not None:
            self.Imported_Functions.export(lwrite, level, 'WinExecutableFileObj:', name_='Imported_Functions', pretty_print=pretty_print)
        if self.Virtual_Address is not None:
            self.Virtual_Address.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Address', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('initially_visible', node)
        if value is not None:

            if value in ('true', '1'):
                self.initially_visible = True
            elif value in ('false', '0'):
                self.initially_visible = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('delay_load', node)
        if value is not None:

            if value in ('true', '1'):
                self.delay_load = True
            elif value in ('false', '0'):
                self.delay_load = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Name(obj_)
        elif nodeName_ == 'Imported_Functions':
            obj_ = PEImportedFunctionsType.factory()
            obj_.build(child_)
            self.set_Imported_Functions(obj_)
        elif nodeName_ == 'Virtual_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Address(obj_)
# end class PEImportType

class PEImportedFunctionsType(GeneratedsSuper):
    """A list of PE imported functions"""

    subclass = None
    superclass = None
    def __init__(self, Imported_Function=None):
        if Imported_Function is None:
            self.Imported_Function = []
        else:
            self.Imported_Function = Imported_Function
    def factory(*args_, **kwargs_):
        if PEImportedFunctionsType.subclass:
            return PEImportedFunctionsType.subclass(*args_, **kwargs_)
        else:
            return PEImportedFunctionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Imported_Function(self): return self.Imported_Function
    def set_Imported_Function(self, Imported_Function): self.Imported_Function = Imported_Function
    def add_Imported_Function(self, value): self.Imported_Function.append(value)
    def insert_Imported_Function(self, index, value): self.Imported_Function[index] = value
    def hasContent_(self):
        if (
            self.Imported_Function
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEImportedFunctionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Imported_Function_ in self.Imported_Function:
            Imported_Function_.export(lwrite, level, 'WinExecutableFileObj:', name_='Imported_Function', pretty_print=pretty_print)
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
        if nodeName_ == 'Imported_Function':
            obj_ = PEImportedFunctionType.factory()
            obj_.build(child_)
            self.Imported_Function.append(obj_)
# end class PEImportedFunctionsType

class PEResourceContentType(cybox_common.BaseObjectPropertyType):
    """The PEResourceContentType specifies PE resource types via a union of
    the PEResourceTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(PEResourceContentType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PEResourceContentType.subclass:
            return PEResourceContentType.subclass(*args_, **kwargs_)
        else:
            return PEResourceContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PEResourceContentType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceContentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEResourceContentType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEResourceContentType'):
        super(PEResourceContentType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PEResourceContentType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceContentType', fromsubclass_=False, pretty_print=True):
        super(PEResourceContentType, self).exportChildren(lwrite, level, 'WinExecutableFileObj:', name_, True, pretty_print=pretty_print)
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
        super(PEResourceContentType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PEResourceContentType

class PEResourceType(GeneratedsSuper):
    """The PEResourceType type is intended as container for the properties
    relevant to PE binary resources."""

    subclass = None
    superclass = None
    def __init__(self, Type=None, Name=None, Size=None, Virtual_Address=None, Language=None, Sub_Language=None, Hashes=None, Data=None, extensiontype_=None):
        self.Type = Type
        self.Name = Name
        self.Size = Size
        self.Virtual_Address = Virtual_Address
        self.Language = Language
        self.Sub_Language = Sub_Language
        self.Hashes = Hashes
        self.Data = Data
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if PEResourceType.subclass:
            return PEResourceType.subclass(*args_, **kwargs_)
        else:
            return PEResourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_PEResourceTypeEnum(self, value):
        # Validate type PEResourceTypeEnum, a restriction on xs:string.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Size(self): return self.Size
    def set_Size(self, Size): self.Size = Size
    def get_Virtual_Address(self): return self.Virtual_Address
    def set_Virtual_Address(self, Virtual_Address): self.Virtual_Address = Virtual_Address
    def get_Language(self): return self.Language
    def set_Language(self, Language): self.Language = Language
    def get_Sub_Language(self): return self.Sub_Language
    def set_Sub_Language(self, Sub_Language): self.Sub_Language = Sub_Language
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Name is not None or
            self.Size is not None or
            self.Virtual_Address is not None or
            self.Language is not None or
            self.Sub_Language is not None or
            self.Hashes is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEResourceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEResourceType'):
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinExecutableFileObj:', name_='Type', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Name', pretty_print=pretty_print)
        if self.Size is not None:
            self.Size.export(lwrite, level, 'WinExecutableFileObj:', name_='Size', pretty_print=pretty_print)
        if self.Virtual_Address is not None:
            self.Virtual_Address.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Address', pretty_print=pretty_print)
        if self.Language is not None:
            self.Language.export(lwrite, level, 'WinExecutableFileObj:', name_='Language', pretty_print=pretty_print)
        if self.Sub_Language is not None:
            self.Sub_Language.export(lwrite, level, 'WinExecutableFileObj:', name_='Sub_Language', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Hashes', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Data', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = PEResourceContentType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Size':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size(obj_)
        elif nodeName_ == 'Virtual_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Address(obj_)
        elif nodeName_ == 'Language':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Language(obj_)
        elif nodeName_ == 'Sub_Language':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sub_Language(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Data':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class PEResourceType

class PEVersionInfoResourceType(PEResourceType):
    """The PEVersionInfoResourceType characterizes the special VERSIONINFO
    resource type. For more information please see:
    http://msdn.microsoft.com/en-
    us/library/windows/desktop/aa381058(v=vs.85).aspx"""

    subclass = None
    superclass = PEResourceType
    def __init__(self, Type=None, Name=None, Hashes=None, Comments=None, CompanyName=None, FileDescription=None, FileVersion=None, InternalName=None, LangID=None, LegalCopyright=None, LegalTrademarks=None, OriginalFilename=None, PrivateBuild=None, ProductName=None, ProductVersion=None, SpecialBuild=None):
        super(PEVersionInfoResourceType, self).__init__(Type, Name, Hashes, )
        self.Comments = Comments
        self.CompanyName = CompanyName
        self.FileDescription = FileDescription
        self.FileVersion = FileVersion
        self.InternalName = InternalName
        self.LangID = LangID
        self.LegalCopyright = LegalCopyright
        self.LegalTrademarks = LegalTrademarks
        self.OriginalFilename = OriginalFilename
        self.PrivateBuild = PrivateBuild
        self.ProductName = ProductName
        self.ProductVersion = ProductVersion
        self.SpecialBuild = SpecialBuild
    def factory(*args_, **kwargs_):
        if PEVersionInfoResourceType.subclass:
            return PEVersionInfoResourceType.subclass(*args_, **kwargs_)
        else:
            return PEVersionInfoResourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Comments(self): return self.Comments
    def set_Comments(self, Comments): self.Comments = Comments
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_CompanyName(self): return self.CompanyName
    def set_CompanyName(self, CompanyName): self.CompanyName = CompanyName
    def get_FileDescription(self): return self.FileDescription
    def set_FileDescription(self, FileDescription): self.FileDescription = FileDescription
    def get_FileVersion(self): return self.FileVersion
    def set_FileVersion(self, FileVersion): self.FileVersion = FileVersion
    def get_InternalName(self): return self.InternalName
    def set_InternalName(self, InternalName): self.InternalName = InternalName
    def get_LangID(self): return self.LangID
    def set_LangID(self, LangID): self.LangID = LangID
    def get_LegalCopyright(self): return self.LegalCopyright
    def set_LegalCopyright(self, LegalCopyright): self.LegalCopyright = LegalCopyright
    def get_LegalTrademarks(self): return self.LegalTrademarks
    def set_LegalTrademarks(self, LegalTrademarks): self.LegalTrademarks = LegalTrademarks
    def get_OriginalFilename(self): return self.OriginalFilename
    def set_OriginalFilename(self, OriginalFilename): self.OriginalFilename = OriginalFilename
    def get_PrivateBuild(self): return self.PrivateBuild
    def set_PrivateBuild(self, PrivateBuild): self.PrivateBuild = PrivateBuild
    def get_ProductName(self): return self.ProductName
    def set_ProductName(self, ProductName): self.ProductName = ProductName
    def get_ProductVersion(self): return self.ProductVersion
    def set_ProductVersion(self, ProductVersion): self.ProductVersion = ProductVersion
    def get_SpecialBuild(self): return self.SpecialBuild
    def set_SpecialBuild(self, SpecialBuild): self.SpecialBuild = SpecialBuild
    def hasContent_(self):
        if (
            self.Comments is not None or
            self.CompanyName is not None or
            self.FileDescription is not None or
            self.FileVersion is not None or
            self.InternalName is not None or
            self.LangID is not None or
            self.LegalCopyright is not None or
            self.LegalTrademarks is not None or
            self.OriginalFilename is not None or
            self.PrivateBuild is not None or
            self.ProductName is not None or
            self.ProductVersion is not None or
            self.SpecialBuild is not None or
            super(PEVersionInfoResourceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEVersionInfoResourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEVersionInfoResourceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEVersionInfoResourceType'):
        super(PEVersionInfoResourceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PEVersionInfoResourceType')
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEVersionInfoResourceType', fromsubclass_=False, pretty_print=True):
        super(PEVersionInfoResourceType, self).exportChildren(lwrite, level, 'WinExecutableFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Comments is not None:
            self.Comments.export(lwrite, level, 'WinExecutableFileObj:', name_='Comments', pretty_print=pretty_print)
        if self.CompanyName is not None:
            self.CompanyName.export(lwrite, level, 'WinExecutableFileObj:', name_='CompanyName', pretty_print=pretty_print)
        if self.FileDescription is not None:
            self.FileDescription.export(lwrite, level, 'WinExecutableFileObj:', name_='FileDescription', pretty_print=pretty_print)
        if self.FileVersion is not None:
            self.FileVersion.export(lwrite, level, 'WinExecutableFileObj:', name_='FileVersion', pretty_print=pretty_print)
        if self.InternalName is not None:
            self.InternalName.export(lwrite, level, 'WinExecutableFileObj:', name_='InternalName', pretty_print=pretty_print)
        if self.LangID is not None:
            self.LangID.export(lwrite, level, 'WinExecutableFileObj:', name_='LangID', pretty_print=pretty_print)
        if self.LegalCopyright is not None:
            self.LegalCopyright.export(lwrite, level, 'WinExecutableFileObj:', name_='LegalCopyright', pretty_print=pretty_print)
        if self.LegalTrademarks is not None:
            self.LegalTrademarks.export(lwrite, level, 'WinExecutableFileObj:', name_='LegalTrademarks', pretty_print=pretty_print)
        if self.OriginalFilename is not None:
            self.OriginalFilename.export(lwrite, level, 'WinExecutableFileObj:', name_='OriginalFilename', pretty_print=pretty_print)
        if self.PrivateBuild is not None:
            self.PrivateBuild.export(lwrite, level, 'WinExecutableFileObj:', name_='PrivateBuild', pretty_print=pretty_print)
        if self.ProductName is not None:
            self.ProductName.export(lwrite, level, 'WinExecutableFileObj:', name_='ProductName', pretty_print=pretty_print)
        if self.ProductVersion is not None:
            self.ProductVersion.export(lwrite, level, 'WinExecutableFileObj:', name_='ProductVersion', pretty_print=pretty_print)
        if self.SpecialBuild is not None:
            self.SpecialBuild.export(lwrite, level, 'WinExecutableFileObj:', name_='SpecialBuild', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PEVersionInfoResourceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Comments':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Comments(obj_)
        elif nodeName_ == 'CompanyName':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_CompanyName(obj_)
        elif nodeName_ == 'FileDescription':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_FileDescription(obj_)
        elif nodeName_ == 'FileVersion':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_FileVersion(obj_)
        elif nodeName_ == 'InternalName':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_InternalName(obj_)
        elif nodeName_ == 'LangID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_LangID(obj_)
        elif nodeName_ == 'LegalCopyright':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_LegalCopyright(obj_)
        elif nodeName_ == 'LegalTrademarks':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_LegalTrademarks(obj_)
        elif nodeName_ == 'OriginalFilename':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_OriginalFilename(obj_)
        elif nodeName_ == 'PrivateBuild':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_PrivateBuild(obj_)
        elif nodeName_ == 'ProductName':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ProductName(obj_)
        elif nodeName_ == 'ProductVersion':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ProductVersion(obj_)
        elif nodeName_ == 'SpecialBuild':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SpecialBuild(obj_)
        super(PEVersionInfoResourceType, self).buildChildren(child_, node, nodeName_, True)
# end class PEVersionInfoResourceType

class PEExportedFunctionType(GeneratedsSuper):
    """PEExportType sepcifies the type describing exported functions."""

    subclass = None
    superclass = None
    def __init__(self, Function_Name=None, Entry_Point=None, Ordinal=None):
        self.Function_Name = Function_Name
        self.Entry_Point = Entry_Point
        self.Ordinal = Ordinal
    def factory(*args_, **kwargs_):
        if PEExportedFunctionType.subclass:
            return PEExportedFunctionType.subclass(*args_, **kwargs_)
        else:
            return PEExportedFunctionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Function_Name(self): return self.Function_Name
    def set_Function_Name(self, Function_Name): self.Function_Name = Function_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Entry_Point(self): return self.Entry_Point
    def set_Entry_Point(self, Entry_Point): self.Entry_Point = Entry_Point
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Ordinal(self): return self.Ordinal
    def set_Ordinal(self, Ordinal): self.Ordinal = Ordinal
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Function_Name is not None or
            self.Entry_Point is not None or
            self.Ordinal is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEExportedFunctionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEExportedFunctionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Function_Name is not None:
            self.Function_Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Function_Name', pretty_print=pretty_print)
        if self.Entry_Point is not None:
            self.Entry_Point.export(lwrite, level, 'WinExecutableFileObj:', name_='Entry_Point', pretty_print=pretty_print)
        if self.Ordinal is not None:
            self.Ordinal.export(lwrite, level, 'WinExecutableFileObj:', name_='Ordinal', pretty_print=pretty_print)
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
        if nodeName_ == 'Function_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Function_Name(obj_)
        elif nodeName_ == 'Entry_Point':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Entry_Point(obj_)
        elif nodeName_ == 'Ordinal':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Ordinal(obj_)
# end class PEExportedFunctionType

class PEResourceListType(GeneratedsSuper):
    """PEResourceListType specifies a list of resources found in the PE
    file."""

    subclass = None
    superclass = None
    def __init__(self, Resource=None):
        if Resource is None:
            self.Resource = []
        else:
            self.Resource = Resource
    def factory(*args_, **kwargs_):
        if PEResourceListType.subclass:
            return PEResourceListType.subclass(*args_, **kwargs_)
        else:
            return PEResourceListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Resource(self): return self.Resource
    def set_Resource(self, Resource): self.Resource = Resource
    def add_Resource(self, value): self.Resource.append(value)
    def insert_Resource(self, index, value): self.Resource[index] = value
    def hasContent_(self):
        if (
            self.Resource
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEResourceListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEResourceListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEResourceListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Resource_ in self.Resource:
            if isinstance(Resource_, PEVersionInfoResourceType):
                Resource_.export(lwrite, level, 'WinExecutableFileObj:', name_='VersionInfoResource', pretty_print=pretty_print)
            elif isinstance(Resource_, PEResourceType):
                Resource_.export(lwrite, level, 'WinExecutableFileObj:', name_='Resource', pretty_print=pretty_print)
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
        if nodeName_ == 'Resource':
            obj_ = PEResourceType.factory()
            obj_.build(child_)
            self.add_Resource(obj_)
        elif nodeName_ == 'VersionInfoResource':
            obj_ = PEVersionInfoResourceType.factory()
            obj_.build(child_)
            self.add_Resource(obj_)
# end class PEResourceListType

class PEImportedFunctionType(GeneratedsSuper):
    """PEImportedFunctionType specifies the type describing imported
    functions."""

    subclass = None
    superclass = None
    def __init__(self, Function_Name=None, Hint=None, Ordinal=None, Bound=None, Virtual_Address=None):
        self.Function_Name = Function_Name
        self.Hint = Hint
        self.Ordinal = Ordinal
        self.Bound = Bound
        self.Virtual_Address = Virtual_Address
    def factory(*args_, **kwargs_):
        if PEImportedFunctionType.subclass:
            return PEImportedFunctionType.subclass(*args_, **kwargs_)
        else:
            return PEImportedFunctionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Function_Name(self): return self.Function_Name
    def set_Function_Name(self, Function_Name): self.Function_Name = Function_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Hint(self): return self.Hint
    def set_Hint(self, Hint): self.Hint = Hint
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Ordinal(self): return self.Ordinal
    def set_Ordinal(self, Ordinal): self.Ordinal = Ordinal
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Bound(self): return self.Bound
    def set_Bound(self, Bound): self.Bound = Bound
    def get_Virtual_Address(self): return self.Virtual_Address
    def set_Virtual_Address(self, Virtual_Address): self.Virtual_Address = Virtual_Address
    def hasContent_(self):
        if (
            self.Function_Name is not None or
            self.Hint is not None or
            self.Ordinal is not None or
            self.Bound is not None or
            self.Virtual_Address is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEImportedFunctionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportedFunctionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Function_Name is not None:
            self.Function_Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Function_Name', pretty_print=pretty_print)
        if self.Hint is not None:
            self.Hint.export(lwrite, level, 'WinExecutableFileObj:', name_='Hint', pretty_print=pretty_print)
        if self.Ordinal is not None:
            self.Ordinal.export(lwrite, level, 'WinExecutableFileObj:', name_='Ordinal', pretty_print=pretty_print)
        if self.Bound is not None:
            self.Bound.export(lwrite, level, 'WinExecutableFileObj:', name_='Bound', pretty_print=pretty_print)
        if self.Virtual_Address is not None:
            self.Virtual_Address.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Address', pretty_print=pretty_print)
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
        if nodeName_ == 'Function_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Function_Name(obj_)
        elif nodeName_ == 'Hint':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hint(obj_)
        elif nodeName_ == 'Ordinal':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Ordinal(obj_)
        elif nodeName_ == 'Bound':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Bound(obj_)
        elif nodeName_ == 'Virtual_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Address(obj_)
# end class PEImportedFunctionType

class PEImportListType(GeneratedsSuper):
    """PEImportListType specifies a list of functions in an import data
    section."""

    subclass = None
    superclass = None
    def __init__(self, Import=None):
        if Import is None:
            self.Import = []
        else:
            self.Import = Import
    def factory(*args_, **kwargs_):
        if PEImportListType.subclass:
            return PEImportListType.subclass(*args_, **kwargs_)
        else:
            return PEImportListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Import(self): return self.Import
    def set_Import(self, Import): self.Import = Import
    def add_Import(self, value): self.Import.append(value)
    def insert_Import(self, index, value): self.Import[index] = value
    def hasContent_(self):
        if (
            self.Import
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEImportListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEImportListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEImportListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Import_ in self.Import:
            Import_.export(lwrite, level, 'WinExecutableFileObj:', name_='Import', pretty_print=pretty_print)
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
        if nodeName_ == 'Import':
            obj_ = PEImportType.factory()
            obj_.build(child_)
            self.Import.append(obj_)
# end class PEImportListType

class PESectionType(GeneratedsSuper):
    """The PESectionType type is intended as container for the properties
    relevant to PE binary sections. A PE Section consists of a
    header and data. The PESectionType contains properties that
    describe the Section Header and metadata computed about the
    section (e.g., hashes, entropy)."""

    subclass = None
    superclass = None
    def __init__(self, Section_Header=None, Data_Hashes=None, Entropy=None, Header_Hashes=None):
        self.Section_Header = Section_Header
        self.Data_Hashes = Data_Hashes
        self.Entropy = Entropy
        self.Header_Hashes = Header_Hashes
    def factory(*args_, **kwargs_):
        if PESectionType.subclass:
            return PESectionType.subclass(*args_, **kwargs_)
        else:
            return PESectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Section_Header(self): return self.Section_Header
    def set_Section_Header(self, Section_Header): self.Section_Header = Section_Header
    def get_Data_Hashes(self): return self.Data_Hashes
    def set_Data_Hashes(self, Data_Hashes): self.Data_Hashes = Data_Hashes
    def get_Entropy(self): return self.Entropy
    def set_Entropy(self, Entropy): self.Entropy = Entropy
    def get_Header_Hashes(self): return self.Header_Hashes
    def set_Header_Hashes(self, Header_Hashes): self.Header_Hashes = Header_Hashes
    def validate_SectionType(self, value):
        # Validate type SectionType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Section_Header is not None or
            self.Data_Hashes is not None or
            self.Entropy is not None or
            self.Header_Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PESectionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PESectionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Section_Header is not None:
            self.Section_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='Section_Header', pretty_print=pretty_print)
        if self.Data_Hashes is not None:
            self.Data_Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Data_Hashes', pretty_print=pretty_print)
        if self.Entropy is not None:
            self.Entropy.export(lwrite, level, 'WinExecutableFileObj:', name_='Entropy', pretty_print=pretty_print)
        if self.Header_Hashes is not None:
            self.Header_Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Header_Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Section_Header':
            obj_ = PESectionHeaderStructType.factory()
            obj_.build(child_)
            self.set_Section_Header(obj_)
        elif nodeName_ == 'Data_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Data_Hashes(obj_)
        elif nodeName_ == 'Entropy':
            obj_ = EntropyType.factory()
            obj_.build(child_)
            self.set_Entropy(obj_)
        elif nodeName_ == 'Header_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Header_Hashes(obj_)
# end class PESectionType

class PEDataDirectoryStructType(GeneratedsSuper):
    """The PEDataDirectoryStruct type is intended as container for the
    properties relevant to a PE binary's data directory structure."""

    subclass = None
    superclass = None
    def __init__(self, Virtual_Address=None, Size=None):
        self.Virtual_Address = Virtual_Address
        self.Size = Size
    def factory(*args_, **kwargs_):
        if PEDataDirectoryStructType.subclass:
            return PEDataDirectoryStructType.subclass(*args_, **kwargs_)
        else:
            return PEDataDirectoryStructType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Virtual_Address(self): return self.Virtual_Address
    def set_Virtual_Address(self, Virtual_Address): self.Virtual_Address = Virtual_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Size(self): return self.Size
    def set_Size(self, Size): self.Size = Size
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Virtual_Address is not None or
            self.Size is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEDataDirectoryStructType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEDataDirectoryStructType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEDataDirectoryStructType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEDataDirectoryStructType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Virtual_Address is not None:
            self.Virtual_Address.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Address', pretty_print=pretty_print)
        if self.Size is not None:
            self.Size.export(lwrite, level, 'WinExecutableFileObj:', name_='Size', pretty_print=pretty_print)
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
        if nodeName_ == 'Virtual_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Address(obj_)
        elif nodeName_ == 'Size':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size(obj_)
# end class PEDataDirectoryStructType

class PESectionHeaderStructType(GeneratedsSuper):
    """The PESectionHeaderStruct type is intended as container for the
    properties relevant to a PE binary's section header structure."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Virtual_Size=None, Virtual_Address=None, Size_Of_Raw_Data=None, Pointer_To_Raw_Data=None, Pointer_To_Relocations=None, Pointer_To_Linenumbers=None, Number_Of_Relocations=None, Number_Of_Linenumbers=None, Characteristics=None):
        self.Name = Name
        self.Virtual_Size = Virtual_Size
        self.Virtual_Address = Virtual_Address
        self.Size_Of_Raw_Data = Size_Of_Raw_Data
        self.Pointer_To_Raw_Data = Pointer_To_Raw_Data
        self.Pointer_To_Relocations = Pointer_To_Relocations
        self.Pointer_To_Linenumbers = Pointer_To_Linenumbers
        self.Number_Of_Relocations = Number_Of_Relocations
        self.Number_Of_Linenumbers = Number_Of_Linenumbers
        self.Characteristics = Characteristics
    def factory(*args_, **kwargs_):
        if PESectionHeaderStructType.subclass:
            return PESectionHeaderStructType.subclass(*args_, **kwargs_)
        else:
            return PESectionHeaderStructType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Virtual_Size(self): return self.Virtual_Size
    def set_Virtual_Size(self, Virtual_Size): self.Virtual_Size = Virtual_Size
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Virtual_Address(self): return self.Virtual_Address
    def set_Virtual_Address(self, Virtual_Address): self.Virtual_Address = Virtual_Address
    def get_Size_Of_Raw_Data(self): return self.Size_Of_Raw_Data
    def set_Size_Of_Raw_Data(self, Size_Of_Raw_Data): self.Size_Of_Raw_Data = Size_Of_Raw_Data
    def get_Pointer_To_Raw_Data(self): return self.Pointer_To_Raw_Data
    def set_Pointer_To_Raw_Data(self, Pointer_To_Raw_Data): self.Pointer_To_Raw_Data = Pointer_To_Raw_Data
    def get_Pointer_To_Relocations(self): return self.Pointer_To_Relocations
    def set_Pointer_To_Relocations(self, Pointer_To_Relocations): self.Pointer_To_Relocations = Pointer_To_Relocations
    def get_Pointer_To_Linenumbers(self): return self.Pointer_To_Linenumbers
    def set_Pointer_To_Linenumbers(self, Pointer_To_Linenumbers): self.Pointer_To_Linenumbers = Pointer_To_Linenumbers
    def get_Number_Of_Relocations(self): return self.Number_Of_Relocations
    def set_Number_Of_Relocations(self, Number_Of_Relocations): self.Number_Of_Relocations = Number_Of_Relocations
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Linenumbers(self): return self.Number_Of_Linenumbers
    def set_Number_Of_Linenumbers(self, Number_Of_Linenumbers): self.Number_Of_Linenumbers = Number_Of_Linenumbers
    def get_Characteristics(self): return self.Characteristics
    def set_Characteristics(self, Characteristics): self.Characteristics = Characteristics
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Virtual_Size is not None or
            self.Virtual_Address is not None or
            self.Size_Of_Raw_Data is not None or
            self.Pointer_To_Raw_Data is not None or
            self.Pointer_To_Relocations is not None or
            self.Pointer_To_Linenumbers is not None or
            self.Number_Of_Relocations is not None or
            self.Number_Of_Linenumbers is not None or
            self.Characteristics is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionHeaderStructType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PESectionHeaderStructType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PESectionHeaderStructType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PESectionHeaderStructType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Name', pretty_print=pretty_print)
        if self.Virtual_Size is not None:
            self.Virtual_Size.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Size', pretty_print=pretty_print)
        if self.Virtual_Address is not None:
            self.Virtual_Address.export(lwrite, level, 'WinExecutableFileObj:', name_='Virtual_Address', pretty_print=pretty_print)
        if self.Size_Of_Raw_Data is not None:
            self.Size_Of_Raw_Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Raw_Data', pretty_print=pretty_print)
        if self.Pointer_To_Raw_Data is not None:
            self.Pointer_To_Raw_Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Pointer_To_Raw_Data', pretty_print=pretty_print)
        if self.Pointer_To_Relocations is not None:
            self.Pointer_To_Relocations.export(lwrite, level, 'WinExecutableFileObj:', name_='Pointer_To_Relocations', pretty_print=pretty_print)
        if self.Pointer_To_Linenumbers is not None:
            self.Pointer_To_Linenumbers.export(lwrite, level, 'WinExecutableFileObj:', name_='Pointer_To_Linenumbers', pretty_print=pretty_print)
        if self.Number_Of_Relocations is not None:
            self.Number_Of_Relocations.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Relocations', pretty_print=pretty_print)
        if self.Number_Of_Linenumbers is not None:
            self.Number_Of_Linenumbers.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Linenumbers', pretty_print=pretty_print)
        if self.Characteristics is not None:
            self.Characteristics.export(lwrite, level, 'WinExecutableFileObj:', name_='Characteristics', pretty_print=pretty_print)
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
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Virtual_Size':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Size(obj_)
        elif nodeName_ == 'Virtual_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Virtual_Address(obj_)
        elif nodeName_ == 'Size_Of_Raw_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Raw_Data(obj_)
        elif nodeName_ == 'Pointer_To_Raw_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer_To_Raw_Data(obj_)
        elif nodeName_ == 'Pointer_To_Relocations':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer_To_Relocations(obj_)
        elif nodeName_ == 'Pointer_To_Linenumbers':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer_To_Linenumbers(obj_)
        elif nodeName_ == 'Number_Of_Relocations':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Relocations(obj_)
        elif nodeName_ == 'Number_Of_Linenumbers':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Linenumbers(obj_)
        elif nodeName_ == 'Characteristics':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Characteristics(obj_)
# end class PESectionHeaderStructType

class DOSHeaderType(GeneratedsSuper):
    """The DOSHeaderType type is a container for the characteristics of the
    _IMAGE_DOS_HEADER structure, which can be found in Winnt.h and
    pe.h. See http://www.csn.ul.ie/~caolan/pub/winresdump/winresdump
    /doc/pefile.html for more information about the winnt.h file,
    and http://www.tavi.co.uk/phobos/exeformat.html for even more
    clarification."""

    subclass = None
    superclass = None
    def __init__(self, e_magic=None, e_cblp=None, e_cp=None, e_crlc=None, e_cparhdr=None, e_minalloc=None, e_maxalloc=None, e_ss=None, e_sp=None, e_csum=None, e_ip=None, e_cs=None, e_lfarlc=None, e_ovro=None, reserved1=None, e_oemid=None, e_oeminfo=None, reserved2=None, e_lfanew=None, Hashes=None):
        self.e_magic = e_magic
        self.e_cblp = e_cblp
        self.e_cp = e_cp
        self.e_crlc = e_crlc
        self.e_cparhdr = e_cparhdr
        self.e_minalloc = e_minalloc
        self.e_maxalloc = e_maxalloc
        self.e_ss = e_ss
        self.e_sp = e_sp
        self.e_csum = e_csum
        self.e_ip = e_ip
        self.e_cs = e_cs
        self.e_lfarlc = e_lfarlc
        self.e_ovro = e_ovro
        if reserved1 is None:
            self.reserved1 = []
        else:
            self.reserved1 = reserved1
        self.e_oemid = e_oemid
        self.e_oeminfo = e_oeminfo
        self.reserved2 = reserved2
        self.e_lfanew = e_lfanew
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if DOSHeaderType.subclass:
            return DOSHeaderType.subclass(*args_, **kwargs_)
        else:
            return DOSHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_e_magic(self): return self.e_magic
    def set_e_magic(self, e_magic): self.e_magic = e_magic
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_e_cblp(self): return self.e_cblp
    def set_e_cblp(self, e_cblp): self.e_cblp = e_cblp
    def get_e_cp(self): return self.e_cp
    def set_e_cp(self, e_cp): self.e_cp = e_cp
    def get_e_crlc(self): return self.e_crlc
    def set_e_crlc(self, e_crlc): self.e_crlc = e_crlc
    def get_e_cparhdr(self): return self.e_cparhdr
    def set_e_cparhdr(self, e_cparhdr): self.e_cparhdr = e_cparhdr
    def get_e_minalloc(self): return self.e_minalloc
    def set_e_minalloc(self, e_minalloc): self.e_minalloc = e_minalloc
    def get_e_maxalloc(self): return self.e_maxalloc
    def set_e_maxalloc(self, e_maxalloc): self.e_maxalloc = e_maxalloc
    def get_e_ss(self): return self.e_ss
    def set_e_ss(self, e_ss): self.e_ss = e_ss
    def get_e_sp(self): return self.e_sp
    def set_e_sp(self, e_sp): self.e_sp = e_sp
    def get_e_csum(self): return self.e_csum
    def set_e_csum(self, e_csum): self.e_csum = e_csum
    def get_e_ip(self): return self.e_ip
    def set_e_ip(self, e_ip): self.e_ip = e_ip
    def get_e_cs(self): return self.e_cs
    def set_e_cs(self, e_cs): self.e_cs = e_cs
    def get_e_lfarlc(self): return self.e_lfarlc
    def set_e_lfarlc(self, e_lfarlc): self.e_lfarlc = e_lfarlc
    def get_e_ovro(self): return self.e_ovro
    def set_e_ovro(self, e_ovro): self.e_ovro = e_ovro
    def get_reserved1(self): return self.reserved1
    def set_reserved1(self, reserved1): self.reserved1 = reserved1
    def add_reserved1(self, value): self.reserved1.append(value)
    def insert_reserved1(self, index, value): self.reserved1[index] = value
    def get_e_oemid(self): return self.e_oemid
    def set_e_oemid(self, e_oemid): self.e_oemid = e_oemid
    def get_e_oeminfo(self): return self.e_oeminfo
    def set_e_oeminfo(self, e_oeminfo): self.e_oeminfo = e_oeminfo
    def get_reserved2(self): return self.reserved2
    def set_reserved2(self, reserved2): self.reserved2 = reserved2
    def get_e_lfanew(self): return self.e_lfanew
    def set_e_lfanew(self, e_lfanew): self.e_lfanew = e_lfanew
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.e_magic is not None or
            self.e_cblp is not None or
            self.e_cp is not None or
            self.e_crlc is not None or
            self.e_cparhdr is not None or
            self.e_minalloc is not None or
            self.e_maxalloc is not None or
            self.e_ss is not None or
            self.e_sp is not None or
            self.e_csum is not None or
            self.e_ip is not None or
            self.e_cs is not None or
            self.e_lfarlc is not None or
            self.e_ovro is not None or
            self.reserved1 or
            self.e_oemid is not None or
            self.e_oeminfo is not None or
            self.reserved2 is not None or
            self.e_lfanew is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='DOSHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DOSHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='DOSHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='DOSHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.e_magic is not None:
            self.e_magic.export(lwrite, level, 'WinExecutableFileObj:', name_='e_magic', pretty_print=pretty_print)
        if self.e_cblp is not None:
            self.e_cblp.export(lwrite, level, 'WinExecutableFileObj:', name_='e_cblp', pretty_print=pretty_print)
        if self.e_cp is not None:
            self.e_cp.export(lwrite, level, 'WinExecutableFileObj:', name_='e_cp', pretty_print=pretty_print)
        if self.e_crlc is not None:
            self.e_crlc.export(lwrite, level, 'WinExecutableFileObj:', name_='e_crlc', pretty_print=pretty_print)
        if self.e_cparhdr is not None:
            self.e_cparhdr.export(lwrite, level, 'WinExecutableFileObj:', name_='e_cparhdr', pretty_print=pretty_print)
        if self.e_minalloc is not None:
            self.e_minalloc.export(lwrite, level, 'WinExecutableFileObj:', name_='e_minalloc', pretty_print=pretty_print)
        if self.e_maxalloc is not None:
            self.e_maxalloc.export(lwrite, level, 'WinExecutableFileObj:', name_='e_maxalloc', pretty_print=pretty_print)
        if self.e_ss is not None:
            self.e_ss.export(lwrite, level, 'WinExecutableFileObj:', name_='e_ss', pretty_print=pretty_print)
        if self.e_sp is not None:
            self.e_sp.export(lwrite, level, 'WinExecutableFileObj:', name_='e_sp', pretty_print=pretty_print)
        if self.e_csum is not None:
            self.e_csum.export(lwrite, level, 'WinExecutableFileObj:', name_='e_csum', pretty_print=pretty_print)
        if self.e_ip is not None:
            self.e_ip.export(lwrite, level, 'WinExecutableFileObj:', name_='e_ip', pretty_print=pretty_print)
        if self.e_cs is not None:
            self.e_cs.export(lwrite, level, 'WinExecutableFileObj:', name_='e_cs', pretty_print=pretty_print)
        if self.e_lfarlc is not None:
            self.e_lfarlc.export(lwrite, level, 'WinExecutableFileObj:', name_='e_lfarlc', pretty_print=pretty_print)
        if self.e_ovro is not None:
            self.e_ovro.export(lwrite, level, 'WinExecutableFileObj:', name_='e_ovro', pretty_print=pretty_print)
        for reserved1_ in self.reserved1:
            reserved1_.export(lwrite, level, 'WinExecutableFileObj:', name_='reserved1', pretty_print=pretty_print)
        if self.e_oemid is not None:
            self.e_oemid.export(lwrite, level, 'WinExecutableFileObj:', name_='e_oemid', pretty_print=pretty_print)
        if self.e_oeminfo is not None:
            self.e_oeminfo.export(lwrite, level, 'WinExecutableFileObj:', name_='e_oeminfo', pretty_print=pretty_print)
        if self.reserved2 is not None:
            self.reserved2.export(lwrite, level, 'WinExecutableFileObj:', name_='reserved2', pretty_print=pretty_print)
        if self.e_lfanew is not None:
            self.e_lfanew.export(lwrite, level, 'WinExecutableFileObj:', name_='e_lfanew', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'e_magic':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_magic(obj_)
        elif nodeName_ == 'e_cblp':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_cblp(obj_)
        elif nodeName_ == 'e_cp':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_cp(obj_)
        elif nodeName_ == 'e_crlc':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_crlc(obj_)
        elif nodeName_ == 'e_cparhdr':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_cparhdr(obj_)
        elif nodeName_ == 'e_minalloc':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_minalloc(obj_)
        elif nodeName_ == 'e_maxalloc':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_maxalloc(obj_)
        elif nodeName_ == 'e_ss':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_ss(obj_)
        elif nodeName_ == 'e_sp':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_sp(obj_)
        elif nodeName_ == 'e_csum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_csum(obj_)
        elif nodeName_ == 'e_ip':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_ip(obj_)
        elif nodeName_ == 'e_cs':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_cs(obj_)
        elif nodeName_ == 'e_lfarlc':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_lfarlc(obj_)
        elif nodeName_ == 'e_ovro':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_ovro(obj_)
        elif nodeName_ == 'reserved1':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.reserved1.append(obj_)
        elif nodeName_ == 'e_oemid':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_oemid(obj_)
        elif nodeName_ == 'e_oeminfo':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_oeminfo(obj_)
        elif nodeName_ == 'reserved2':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_reserved2(obj_)
        elif nodeName_ == 'e_lfanew':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_e_lfanew(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class DOSHeaderType

class PEHeadersType(GeneratedsSuper):
    """PEHeaderType specifies the headers found in PE and COFF files."""

    subclass = None
    superclass = None
    def __init__(self, DOS_Header=None, Signature=None, File_Header=None, Optional_Header=None, Entropy=None, Hashes=None):
        self.DOS_Header = DOS_Header
        self.Signature = Signature
        self.File_Header = File_Header
        self.Optional_Header = Optional_Header
        self.Entropy = Entropy
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PEHeadersType.subclass:
            return PEHeadersType.subclass(*args_, **kwargs_)
        else:
            return PEHeadersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_DOS_Header(self): return self.DOS_Header
    def set_DOS_Header(self, DOS_Header): self.DOS_Header = DOS_Header
    def get_Signature(self): return self.Signature
    def set_Signature(self, Signature): self.Signature = Signature
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_File_Header(self): return self.File_Header
    def set_File_Header(self, File_Header): self.File_Header = File_Header
    def get_Optional_Header(self): return self.Optional_Header
    def set_Optional_Header(self, Optional_Header): self.Optional_Header = Optional_Header
    def get_Entropy(self): return self.Entropy
    def set_Entropy(self, Entropy): self.Entropy = Entropy
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.DOS_Header is not None or
            self.Signature is not None or
            self.File_Header is not None or
            self.Optional_Header is not None or
            self.Entropy is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEHeadersType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEHeadersType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEHeadersType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEHeadersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DOS_Header is not None:
            self.DOS_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='DOS_Header', pretty_print=pretty_print)
        if self.Signature is not None:
            self.Signature.export(lwrite, level, 'WinExecutableFileObj:', name_='Signature', pretty_print=pretty_print)
        if self.File_Header is not None:
            self.File_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='File_Header', pretty_print=pretty_print)
        if self.Optional_Header is not None:
            self.Optional_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='Optional_Header', pretty_print=pretty_print)
        if self.Entropy is not None:
            self.Entropy.export(lwrite, level, 'WinExecutableFileObj:', name_='Entropy', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'DOS_Header':
            obj_ = DOSHeaderType.factory()
            obj_.build(child_)
            self.set_DOS_Header(obj_)
        elif nodeName_ == 'Signature':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature(obj_)
        elif nodeName_ == 'File_Header':
            obj_ = PEFileHeaderType.factory()
            obj_.build(child_)
            self.set_File_Header(obj_)
        elif nodeName_ == 'Optional_Header':
            obj_ = PEOptionalHeaderType.factory()
            obj_.build(child_)
            self.set_Optional_Header(obj_)
        elif nodeName_ == 'Entropy':
            obj_ = EntropyType.factory()
            obj_.build(child_)
            self.set_Entropy(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PEHeadersType

class PEFileHeaderType(GeneratedsSuper):
    """The PEFileHeaderType type refers to the PE file header (somtimes
    referred to as the COFF header) and its associated
    characteristics."""

    subclass = None
    superclass = None
    def __init__(self, Machine=None, Number_Of_Sections=None, Time_Date_Stamp=None, Pointer_To_Symbol_Table=None, Number_Of_Symbols=None, Size_Of_Optional_Header=None, Characteristics=None, Hashes=None):
        self.Machine = Machine
        self.Number_Of_Sections = Number_Of_Sections
        self.Time_Date_Stamp = Time_Date_Stamp
        self.Pointer_To_Symbol_Table = Pointer_To_Symbol_Table
        self.Number_Of_Symbols = Number_Of_Symbols
        self.Size_Of_Optional_Header = Size_Of_Optional_Header
        self.Characteristics = Characteristics
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PEFileHeaderType.subclass:
            return PEFileHeaderType.subclass(*args_, **kwargs_)
        else:
            return PEFileHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Machine(self): return self.Machine
    def set_Machine(self, Machine): self.Machine = Machine
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Sections(self): return self.Number_Of_Sections
    def set_Number_Of_Sections(self, Number_Of_Sections): self.Number_Of_Sections = Number_Of_Sections
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Time_Date_Stamp(self): return self.Time_Date_Stamp
    def set_Time_Date_Stamp(self, Time_Date_Stamp): self.Time_Date_Stamp = Time_Date_Stamp
    def get_Pointer_To_Symbol_Table(self): return self.Pointer_To_Symbol_Table
    def set_Pointer_To_Symbol_Table(self, Pointer_To_Symbol_Table): self.Pointer_To_Symbol_Table = Pointer_To_Symbol_Table
    def get_Number_Of_Symbols(self): return self.Number_Of_Symbols
    def set_Number_Of_Symbols(self, Number_Of_Symbols): self.Number_Of_Symbols = Number_Of_Symbols
    def get_Size_Of_Optional_Header(self): return self.Size_Of_Optional_Header
    def set_Size_Of_Optional_Header(self, Size_Of_Optional_Header): self.Size_Of_Optional_Header = Size_Of_Optional_Header
    def get_Characteristics(self): return self.Characteristics
    def set_Characteristics(self, Characteristics): self.Characteristics = Characteristics
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.Machine is not None or
            self.Number_Of_Sections is not None or
            self.Time_Date_Stamp is not None or
            self.Pointer_To_Symbol_Table is not None or
            self.Number_Of_Symbols is not None or
            self.Size_Of_Optional_Header is not None or
            self.Characteristics is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEFileHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEFileHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEFileHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEFileHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Machine is not None:
            self.Machine.export(lwrite, level, 'WinExecutableFileObj:', name_='Machine', pretty_print=pretty_print)
        if self.Number_Of_Sections is not None:
            self.Number_Of_Sections.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Sections', pretty_print=pretty_print)
        if self.Time_Date_Stamp is not None:
            self.Time_Date_Stamp.export(lwrite, level, 'WinExecutableFileObj:', name_='Time_Date_Stamp', pretty_print=pretty_print)
        if self.Pointer_To_Symbol_Table is not None:
            self.Pointer_To_Symbol_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Pointer_To_Symbol_Table', pretty_print=pretty_print)
        if self.Number_Of_Symbols is not None:
            self.Number_Of_Symbols.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Symbols', pretty_print=pretty_print)
        if self.Size_Of_Optional_Header is not None:
            self.Size_Of_Optional_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Optional_Header', pretty_print=pretty_print)
        if self.Characteristics is not None:
            self.Characteristics.export(lwrite, level, 'WinExecutableFileObj:', name_='Characteristics', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Machine':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Machine(obj_)
        elif nodeName_ == 'Number_Of_Sections':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Sections(obj_)
        elif nodeName_ == 'Time_Date_Stamp':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Time_Date_Stamp(obj_)
        elif nodeName_ == 'Pointer_To_Symbol_Table':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer_To_Symbol_Table(obj_)
        elif nodeName_ == 'Number_Of_Symbols':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Symbols(obj_)
        elif nodeName_ == 'Size_Of_Optional_Header':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Optional_Header(obj_)
        elif nodeName_ == 'Characteristics':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Characteristics(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PEFileHeaderType

class PEOptionalHeaderType(GeneratedsSuper):
    """The PEOptionalHeaderType type describes the PE Optional Header
    structure. Additional computed metadata, e.g., hashes of the
    header, are also included."""

    subclass = None
    superclass = None
    def __init__(self, Magic=None, Major_Linker_Version=None, Minor_Linker_Version=None, Size_Of_Code=None, Size_Of_Initialized_Data=None, Size_Of_Uninitialized_Data=None, Address_Of_Entry_Point=None, Base_Of_Code=None, Base_Of_Data=None, Image_Base=None, Section_Alignment=None, File_Alignment=None, Major_OS_Version=None, Minor_OS_Version=None, Major_Image_Version=None, Minor_Image_Version=None, Major_Subsystem_Version=None, Minor_Subsystem_Version=None, Win32_Version_Value=None, Size_Of_Image=None, Size_Of_Headers=None, Checksum=None, Subsystem=None, DLL_Characteristics=None, Size_Of_Stack_Reserve=None, Size_Of_Stack_Commit=None, Size_Of_Heap_Reserve=None, Size_Of_Heap_Commit=None, Loader_Flags=None, Number_Of_Rva_And_Sizes=None, Data_Directory=None, Hashes=None):
        self.Magic = Magic
        self.Major_Linker_Version = Major_Linker_Version
        self.Minor_Linker_Version = Minor_Linker_Version
        self.Size_Of_Code = Size_Of_Code
        self.Size_Of_Initialized_Data = Size_Of_Initialized_Data
        self.Size_Of_Uninitialized_Data = Size_Of_Uninitialized_Data
        self.Address_Of_Entry_Point = Address_Of_Entry_Point
        self.Base_Of_Code = Base_Of_Code
        self.Base_Of_Data = Base_Of_Data
        self.Image_Base = Image_Base
        self.Section_Alignment = Section_Alignment
        self.File_Alignment = File_Alignment
        self.Major_OS_Version = Major_OS_Version
        self.Minor_OS_Version = Minor_OS_Version
        self.Major_Image_Version = Major_Image_Version
        self.Minor_Image_Version = Minor_Image_Version
        self.Major_Subsystem_Version = Major_Subsystem_Version
        self.Minor_Subsystem_Version = Minor_Subsystem_Version
        self.Win32_Version_Value = Win32_Version_Value
        self.Size_Of_Image = Size_Of_Image
        self.Size_Of_Headers = Size_Of_Headers
        self.Checksum = Checksum
        self.Subsystem = Subsystem
        self.DLL_Characteristics = DLL_Characteristics
        self.Size_Of_Stack_Reserve = Size_Of_Stack_Reserve
        self.Size_Of_Stack_Commit = Size_Of_Stack_Commit
        self.Size_Of_Heap_Reserve = Size_Of_Heap_Reserve
        self.Size_Of_Heap_Commit = Size_Of_Heap_Commit
        self.Loader_Flags = Loader_Flags
        self.Number_Of_Rva_And_Sizes = Number_Of_Rva_And_Sizes
        self.Data_Directory = Data_Directory
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PEOptionalHeaderType.subclass:
            return PEOptionalHeaderType.subclass(*args_, **kwargs_)
        else:
            return PEOptionalHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Magic(self): return self.Magic
    def set_Magic(self, Magic): self.Magic = Magic
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Major_Linker_Version(self): return self.Major_Linker_Version
    def set_Major_Linker_Version(self, Major_Linker_Version): self.Major_Linker_Version = Major_Linker_Version
    def get_Minor_Linker_Version(self): return self.Minor_Linker_Version
    def set_Minor_Linker_Version(self, Minor_Linker_Version): self.Minor_Linker_Version = Minor_Linker_Version
    def get_Size_Of_Code(self): return self.Size_Of_Code
    def set_Size_Of_Code(self, Size_Of_Code): self.Size_Of_Code = Size_Of_Code
    def get_Size_Of_Initialized_Data(self): return self.Size_Of_Initialized_Data
    def set_Size_Of_Initialized_Data(self, Size_Of_Initialized_Data): self.Size_Of_Initialized_Data = Size_Of_Initialized_Data
    def get_Size_Of_Uninitialized_Data(self): return self.Size_Of_Uninitialized_Data
    def set_Size_Of_Uninitialized_Data(self, Size_Of_Uninitialized_Data): self.Size_Of_Uninitialized_Data = Size_Of_Uninitialized_Data
    def get_Address_Of_Entry_Point(self): return self.Address_Of_Entry_Point
    def set_Address_Of_Entry_Point(self, Address_Of_Entry_Point): self.Address_Of_Entry_Point = Address_Of_Entry_Point
    def get_Base_Of_Code(self): return self.Base_Of_Code
    def set_Base_Of_Code(self, Base_Of_Code): self.Base_Of_Code = Base_Of_Code
    def get_Base_Of_Data(self): return self.Base_Of_Data
    def set_Base_Of_Data(self, Base_Of_Data): self.Base_Of_Data = Base_Of_Data
    def get_Image_Base(self): return self.Image_Base
    def set_Image_Base(self, Image_Base): self.Image_Base = Image_Base
    def get_Section_Alignment(self): return self.Section_Alignment
    def set_Section_Alignment(self, Section_Alignment): self.Section_Alignment = Section_Alignment
    def get_File_Alignment(self): return self.File_Alignment
    def set_File_Alignment(self, File_Alignment): self.File_Alignment = File_Alignment
    def get_Major_OS_Version(self): return self.Major_OS_Version
    def set_Major_OS_Version(self, Major_OS_Version): self.Major_OS_Version = Major_OS_Version
    def get_Minor_OS_Version(self): return self.Minor_OS_Version
    def set_Minor_OS_Version(self, Minor_OS_Version): self.Minor_OS_Version = Minor_OS_Version
    def get_Major_Image_Version(self): return self.Major_Image_Version
    def set_Major_Image_Version(self, Major_Image_Version): self.Major_Image_Version = Major_Image_Version
    def get_Minor_Image_Version(self): return self.Minor_Image_Version
    def set_Minor_Image_Version(self, Minor_Image_Version): self.Minor_Image_Version = Minor_Image_Version
    def get_Major_Subsystem_Version(self): return self.Major_Subsystem_Version
    def set_Major_Subsystem_Version(self, Major_Subsystem_Version): self.Major_Subsystem_Version = Major_Subsystem_Version
    def get_Minor_Subsystem_Version(self): return self.Minor_Subsystem_Version
    def set_Minor_Subsystem_Version(self, Minor_Subsystem_Version): self.Minor_Subsystem_Version = Minor_Subsystem_Version
    def get_Win32_Version_Value(self): return self.Win32_Version_Value
    def set_Win32_Version_Value(self, Win32_Version_Value): self.Win32_Version_Value = Win32_Version_Value
    def get_Size_Of_Image(self): return self.Size_Of_Image
    def set_Size_Of_Image(self, Size_Of_Image): self.Size_Of_Image = Size_Of_Image
    def get_Size_Of_Headers(self): return self.Size_Of_Headers
    def set_Size_Of_Headers(self, Size_Of_Headers): self.Size_Of_Headers = Size_Of_Headers
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def get_Subsystem(self): return self.Subsystem
    def set_Subsystem(self, Subsystem): self.Subsystem = Subsystem
    def get_DLL_Characteristics(self): return self.DLL_Characteristics
    def set_DLL_Characteristics(self, DLL_Characteristics): self.DLL_Characteristics = DLL_Characteristics
    def get_Size_Of_Stack_Reserve(self): return self.Size_Of_Stack_Reserve
    def set_Size_Of_Stack_Reserve(self, Size_Of_Stack_Reserve): self.Size_Of_Stack_Reserve = Size_Of_Stack_Reserve
    def get_Size_Of_Stack_Commit(self): return self.Size_Of_Stack_Commit
    def set_Size_Of_Stack_Commit(self, Size_Of_Stack_Commit): self.Size_Of_Stack_Commit = Size_Of_Stack_Commit
    def get_Size_Of_Heap_Reserve(self): return self.Size_Of_Heap_Reserve
    def set_Size_Of_Heap_Reserve(self, Size_Of_Heap_Reserve): self.Size_Of_Heap_Reserve = Size_Of_Heap_Reserve
    def get_Size_Of_Heap_Commit(self): return self.Size_Of_Heap_Commit
    def set_Size_Of_Heap_Commit(self, Size_Of_Heap_Commit): self.Size_Of_Heap_Commit = Size_Of_Heap_Commit
    def get_Loader_Flags(self): return self.Loader_Flags
    def set_Loader_Flags(self, Loader_Flags): self.Loader_Flags = Loader_Flags
    def get_Number_Of_Rva_And_Sizes(self): return self.Number_Of_Rva_And_Sizes
    def set_Number_Of_Rva_And_Sizes(self, Number_Of_Rva_And_Sizes): self.Number_Of_Rva_And_Sizes = Number_Of_Rva_And_Sizes
    def get_Data_Directory(self): return self.Data_Directory
    def set_Data_Directory(self, Data_Directory): self.Data_Directory = Data_Directory
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.Magic is not None or
            self.Major_Linker_Version is not None or
            self.Minor_Linker_Version is not None or
            self.Size_Of_Code is not None or
            self.Size_Of_Initialized_Data is not None or
            self.Size_Of_Uninitialized_Data is not None or
            self.Address_Of_Entry_Point is not None or
            self.Base_Of_Code is not None or
            self.Base_Of_Data is not None or
            self.Image_Base is not None or
            self.Section_Alignment is not None or
            self.File_Alignment is not None or
            self.Major_OS_Version is not None or
            self.Minor_OS_Version is not None or
            self.Major_Image_Version is not None or
            self.Minor_Image_Version is not None or
            self.Major_Subsystem_Version is not None or
            self.Minor_Subsystem_Version is not None or
            self.Win32_Version_Value is not None or
            self.Size_Of_Image is not None or
            self.Size_Of_Headers is not None or
            self.Checksum is not None or
            self.Subsystem is not None or
            self.DLL_Characteristics is not None or
            self.Size_Of_Stack_Reserve is not None or
            self.Size_Of_Stack_Commit is not None or
            self.Size_Of_Heap_Reserve is not None or
            self.Size_Of_Heap_Commit is not None or
            self.Loader_Flags is not None or
            self.Number_Of_Rva_And_Sizes is not None or
            self.Data_Directory is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEOptionalHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEOptionalHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEOptionalHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEOptionalHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Magic is not None:
            self.Magic.export(lwrite, level, 'WinExecutableFileObj:', name_='Magic', pretty_print=pretty_print)
        if self.Major_Linker_Version is not None:
            self.Major_Linker_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Major_Linker_Version', pretty_print=pretty_print)
        if self.Minor_Linker_Version is not None:
            self.Minor_Linker_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Minor_Linker_Version', pretty_print=pretty_print)
        if self.Size_Of_Code is not None:
            self.Size_Of_Code.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Code', pretty_print=pretty_print)
        if self.Size_Of_Initialized_Data is not None:
            self.Size_Of_Initialized_Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Initialized_Data', pretty_print=pretty_print)
        if self.Size_Of_Uninitialized_Data is not None:
            self.Size_Of_Uninitialized_Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Uninitialized_Data', pretty_print=pretty_print)
        if self.Address_Of_Entry_Point is not None:
            self.Address_Of_Entry_Point.export(lwrite, level, 'WinExecutableFileObj:', name_='Address_Of_Entry_Point', pretty_print=pretty_print)
        if self.Base_Of_Code is not None:
            self.Base_Of_Code.export(lwrite, level, 'WinExecutableFileObj:', name_='Base_Of_Code', pretty_print=pretty_print)
        if self.Base_Of_Data is not None:
            self.Base_Of_Data.export(lwrite, level, 'WinExecutableFileObj:', name_='Base_Of_Data', pretty_print=pretty_print)
        if self.Image_Base is not None:
            self.Image_Base.export(lwrite, level, 'WinExecutableFileObj:', name_='Image_Base', pretty_print=pretty_print)
        if self.Section_Alignment is not None:
            self.Section_Alignment.export(lwrite, level, 'WinExecutableFileObj:', name_='Section_Alignment', pretty_print=pretty_print)
        if self.File_Alignment is not None:
            self.File_Alignment.export(lwrite, level, 'WinExecutableFileObj:', name_='File_Alignment', pretty_print=pretty_print)
        if self.Major_OS_Version is not None:
            self.Major_OS_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Major_OS_Version', pretty_print=pretty_print)
        if self.Minor_OS_Version is not None:
            self.Minor_OS_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Minor_OS_Version', pretty_print=pretty_print)
        if self.Major_Image_Version is not None:
            self.Major_Image_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Major_Image_Version', pretty_print=pretty_print)
        if self.Minor_Image_Version is not None:
            self.Minor_Image_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Minor_Image_Version', pretty_print=pretty_print)
        if self.Major_Subsystem_Version is not None:
            self.Major_Subsystem_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Major_Subsystem_Version', pretty_print=pretty_print)
        if self.Minor_Subsystem_Version is not None:
            self.Minor_Subsystem_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Minor_Subsystem_Version', pretty_print=pretty_print)
        if self.Win32_Version_Value is not None:
            self.Win32_Version_Value.export(lwrite, level, 'WinExecutableFileObj:', name_='Win32_Version_Value', pretty_print=pretty_print)
        if self.Size_Of_Image is not None:
            self.Size_Of_Image.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Image', pretty_print=pretty_print)
        if self.Size_Of_Headers is not None:
            self.Size_Of_Headers.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Headers', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'WinExecutableFileObj:', name_='Checksum', pretty_print=pretty_print)
        if self.Subsystem is not None:
            self.Subsystem.export(lwrite, level, 'WinExecutableFileObj:', name_='Subsystem', pretty_print=pretty_print)
        if self.DLL_Characteristics is not None:
            self.DLL_Characteristics.export(lwrite, level, 'WinExecutableFileObj:', name_='DLL_Characteristics', pretty_print=pretty_print)
        if self.Size_Of_Stack_Reserve is not None:
            self.Size_Of_Stack_Reserve.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Stack_Reserve', pretty_print=pretty_print)
        if self.Size_Of_Stack_Commit is not None:
            self.Size_Of_Stack_Commit.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Stack_Commit', pretty_print=pretty_print)
        if self.Size_Of_Heap_Reserve is not None:
            self.Size_Of_Heap_Reserve.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Heap_Reserve', pretty_print=pretty_print)
        if self.Size_Of_Heap_Commit is not None:
            self.Size_Of_Heap_Commit.export(lwrite, level, 'WinExecutableFileObj:', name_='Size_Of_Heap_Commit', pretty_print=pretty_print)
        if self.Loader_Flags is not None:
            self.Loader_Flags.export(lwrite, level, 'WinExecutableFileObj:', name_='Loader_Flags', pretty_print=pretty_print)
        if self.Number_Of_Rva_And_Sizes is not None:
            self.Number_Of_Rva_And_Sizes.export(lwrite, level, 'WinExecutableFileObj:', name_='Number_Of_Rva_And_Sizes', pretty_print=pretty_print)
        if self.Data_Directory is not None:
            self.Data_Directory.export(lwrite, level, 'WinExecutableFileObj:', name_='Data_Directory', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'WinExecutableFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Magic':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Magic(obj_)
        elif nodeName_ == 'Major_Linker_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Major_Linker_Version(obj_)
        elif nodeName_ == 'Minor_Linker_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Minor_Linker_Version(obj_)
        elif nodeName_ == 'Size_Of_Code':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Code(obj_)
        elif nodeName_ == 'Size_Of_Initialized_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Initialized_Data(obj_)
        elif nodeName_ == 'Size_Of_Uninitialized_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Uninitialized_Data(obj_)
        elif nodeName_ == 'Address_Of_Entry_Point':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address_Of_Entry_Point(obj_)
        elif nodeName_ == 'Base_Of_Code':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Base_Of_Code(obj_)
        elif nodeName_ == 'Base_Of_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Base_Of_Data(obj_)
        elif nodeName_ == 'Image_Base':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Image_Base(obj_)
        elif nodeName_ == 'Section_Alignment':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Section_Alignment(obj_)
        elif nodeName_ == 'File_Alignment':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Alignment(obj_)
        elif nodeName_ == 'Major_OS_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Major_OS_Version(obj_)
        elif nodeName_ == 'Minor_OS_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Minor_OS_Version(obj_)
        elif nodeName_ == 'Major_Image_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Major_Image_Version(obj_)
        elif nodeName_ == 'Minor_Image_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Minor_Image_Version(obj_)
        elif nodeName_ == 'Major_Subsystem_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Major_Subsystem_Version(obj_)
        elif nodeName_ == 'Minor_Subsystem_Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Minor_Subsystem_Version(obj_)
        elif nodeName_ == 'Win32_Version_Value':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Win32_Version_Value(obj_)
        elif nodeName_ == 'Size_Of_Image':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Image(obj_)
        elif nodeName_ == 'Size_Of_Headers':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Headers(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
        elif nodeName_ == 'Subsystem':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subsystem(obj_)
        elif nodeName_ == 'DLL_Characteristics':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_DLL_Characteristics(obj_)
        elif nodeName_ == 'Size_Of_Stack_Reserve':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Stack_Reserve(obj_)
        elif nodeName_ == 'Size_Of_Stack_Commit':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Stack_Commit(obj_)
        elif nodeName_ == 'Size_Of_Heap_Reserve':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Heap_Reserve(obj_)
        elif nodeName_ == 'Size_Of_Heap_Commit':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_Of_Heap_Commit(obj_)
        elif nodeName_ == 'Loader_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Loader_Flags(obj_)
        elif nodeName_ == 'Number_Of_Rva_And_Sizes':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Rva_And_Sizes(obj_)
        elif nodeName_ == 'Data_Directory':
            obj_ = DataDirectoryType.factory()
            obj_.build(child_)
            self.set_Data_Directory(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PEOptionalHeaderType

class DataDirectoryType(GeneratedsSuper):
    """The DataDirectoryType specifies the data directories that can appear
    in the PE file's optional header. The data directories, except
    the Certificate Table, are loaded into memory so they can be
    used at runtime."""

    subclass = None
    superclass = None
    def __init__(self, Export_Table=None, Import_Table=None, Resource_Table=None, Exception_Table=None, Certificate_Table=None, Base_Relocation_Table=None, Debug=None, Architecture=None, Global_Ptr=None, TLS_Table=None, Load_Config_Table=None, Bound_Import=None, Import_Address_Table=None, Delay_Import_Descriptor=None, CLR_Runtime_Header=None, Reserved=None):
        self.Export_Table = Export_Table
        self.Import_Table = Import_Table
        self.Resource_Table = Resource_Table
        self.Exception_Table = Exception_Table
        self.Certificate_Table = Certificate_Table
        self.Base_Relocation_Table = Base_Relocation_Table
        self.Debug = Debug
        self.Architecture = Architecture
        self.Global_Ptr = Global_Ptr
        self.TLS_Table = TLS_Table
        self.Load_Config_Table = Load_Config_Table
        self.Bound_Import = Bound_Import
        self.Import_Address_Table = Import_Address_Table
        self.Delay_Import_Descriptor = Delay_Import_Descriptor
        self.CLR_Runtime_Header = CLR_Runtime_Header
        self.Reserved = Reserved
    def factory(*args_, **kwargs_):
        if DataDirectoryType.subclass:
            return DataDirectoryType.subclass(*args_, **kwargs_)
        else:
            return DataDirectoryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Export_Table(self): return self.Export_Table
    def set_Export_Table(self, Export_Table): self.Export_Table = Export_Table
    def get_Import_Table(self): return self.Import_Table
    def set_Import_Table(self, Import_Table): self.Import_Table = Import_Table
    def get_Resource_Table(self): return self.Resource_Table
    def set_Resource_Table(self, Resource_Table): self.Resource_Table = Resource_Table
    def get_Exception_Table(self): return self.Exception_Table
    def set_Exception_Table(self, Exception_Table): self.Exception_Table = Exception_Table
    def get_Certificate_Table(self): return self.Certificate_Table
    def set_Certificate_Table(self, Certificate_Table): self.Certificate_Table = Certificate_Table
    def get_Base_Relocation_Table(self): return self.Base_Relocation_Table
    def set_Base_Relocation_Table(self, Base_Relocation_Table): self.Base_Relocation_Table = Base_Relocation_Table
    def get_Debug(self): return self.Debug
    def set_Debug(self, Debug): self.Debug = Debug
    def get_Architecture(self): return self.Architecture
    def set_Architecture(self, Architecture): self.Architecture = Architecture
    def get_Global_Ptr(self): return self.Global_Ptr
    def set_Global_Ptr(self, Global_Ptr): self.Global_Ptr = Global_Ptr
    def get_TLS_Table(self): return self.TLS_Table
    def set_TLS_Table(self, TLS_Table): self.TLS_Table = TLS_Table
    def get_Load_Config_Table(self): return self.Load_Config_Table
    def set_Load_Config_Table(self, Load_Config_Table): self.Load_Config_Table = Load_Config_Table
    def get_Bound_Import(self): return self.Bound_Import
    def set_Bound_Import(self, Bound_Import): self.Bound_Import = Bound_Import
    def get_Import_Address_Table(self): return self.Import_Address_Table
    def set_Import_Address_Table(self, Import_Address_Table): self.Import_Address_Table = Import_Address_Table
    def get_Delay_Import_Descriptor(self): return self.Delay_Import_Descriptor
    def set_Delay_Import_Descriptor(self, Delay_Import_Descriptor): self.Delay_Import_Descriptor = Delay_Import_Descriptor
    def get_CLR_Runtime_Header(self): return self.CLR_Runtime_Header
    def set_CLR_Runtime_Header(self, CLR_Runtime_Header): self.CLR_Runtime_Header = CLR_Runtime_Header
    def get_Reserved(self): return self.Reserved
    def set_Reserved(self, Reserved): self.Reserved = Reserved
    def hasContent_(self):
        if (
            self.Export_Table is not None or
            self.Import_Table is not None or
            self.Resource_Table is not None or
            self.Exception_Table is not None or
            self.Certificate_Table is not None or
            self.Base_Relocation_Table is not None or
            self.Debug is not None or
            self.Architecture is not None or
            self.Global_Ptr is not None or
            self.TLS_Table is not None or
            self.Load_Config_Table is not None or
            self.Bound_Import is not None or
            self.Import_Address_Table is not None or
            self.Delay_Import_Descriptor is not None or
            self.CLR_Runtime_Header is not None or
            self.Reserved is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='DataDirectoryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DataDirectoryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='DataDirectoryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='DataDirectoryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Export_Table is not None:
            self.Export_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Export_Table', pretty_print=pretty_print)
        if self.Import_Table is not None:
            self.Import_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Import_Table', pretty_print=pretty_print)
        if self.Resource_Table is not None:
            self.Resource_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Resource_Table', pretty_print=pretty_print)
        if self.Exception_Table is not None:
            self.Exception_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Exception_Table', pretty_print=pretty_print)
        if self.Certificate_Table is not None:
            self.Certificate_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Certificate_Table', pretty_print=pretty_print)
        if self.Base_Relocation_Table is not None:
            self.Base_Relocation_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Base_Relocation_Table', pretty_print=pretty_print)
        if self.Debug is not None:
            self.Debug.export(lwrite, level, 'WinExecutableFileObj:', name_='Debug', pretty_print=pretty_print)
        if self.Architecture is not None:
            self.Architecture.export(lwrite, level, 'WinExecutableFileObj:', name_='Architecture', pretty_print=pretty_print)
        if self.Global_Ptr is not None:
            self.Global_Ptr.export(lwrite, level, 'WinExecutableFileObj:', name_='Global_Ptr', pretty_print=pretty_print)
        if self.TLS_Table is not None:
            self.TLS_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='TLS_Table', pretty_print=pretty_print)
        if self.Load_Config_Table is not None:
            self.Load_Config_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Load_Config_Table', pretty_print=pretty_print)
        if self.Bound_Import is not None:
            self.Bound_Import.export(lwrite, level, 'WinExecutableFileObj:', name_='Bound_Import', pretty_print=pretty_print)
        if self.Import_Address_Table is not None:
            self.Import_Address_Table.export(lwrite, level, 'WinExecutableFileObj:', name_='Import_Address_Table', pretty_print=pretty_print)
        if self.Delay_Import_Descriptor is not None:
            self.Delay_Import_Descriptor.export(lwrite, level, 'WinExecutableFileObj:', name_='Delay_Import_Descriptor', pretty_print=pretty_print)
        if self.CLR_Runtime_Header is not None:
            self.CLR_Runtime_Header.export(lwrite, level, 'WinExecutableFileObj:', name_='CLR_Runtime_Header', pretty_print=pretty_print)
        if self.Reserved is not None:
            self.Reserved.export(lwrite, level, 'WinExecutableFileObj:', name_='Reserved', pretty_print=pretty_print)
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
        if nodeName_ == 'Export_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Export_Table(obj_)
        elif nodeName_ == 'Import_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Import_Table(obj_)
        elif nodeName_ == 'Resource_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Resource_Table(obj_)
        elif nodeName_ == 'Exception_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Exception_Table(obj_)
        elif nodeName_ == 'Certificate_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Certificate_Table(obj_)
        elif nodeName_ == 'Base_Relocation_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Base_Relocation_Table(obj_)
        elif nodeName_ == 'Debug':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Debug(obj_)
        elif nodeName_ == 'Architecture':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Architecture(obj_)
        elif nodeName_ == 'Global_Ptr':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Global_Ptr(obj_)
        elif nodeName_ == 'TLS_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_TLS_Table(obj_)
        elif nodeName_ == 'Load_Config_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Load_Config_Table(obj_)
        elif nodeName_ == 'Bound_Import':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Bound_Import(obj_)
        elif nodeName_ == 'Import_Address_Table':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Import_Address_Table(obj_)
        elif nodeName_ == 'Delay_Import_Descriptor':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Delay_Import_Descriptor(obj_)
        elif nodeName_ == 'CLR_Runtime_Header':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_CLR_Runtime_Header(obj_)
        elif nodeName_ == 'Reserved':
            obj_ = PEDataDirectoryStructType.factory()
            obj_.build(child_)
            self.set_Reserved(obj_)
# end class DataDirectoryType

class PEBuildInformationType(GeneratedsSuper):
    """The PEBuildInformationType captures information about the tools used
    to build the PE binary, including the compiler and linker."""

    subclass = None
    superclass = None
    def __init__(self, Linker_Name=None, Linker_Version=None, Compiler_Name=None, Compiler_Version=None):
        self.Linker_Name = Linker_Name
        self.Linker_Version = Linker_Version
        self.Compiler_Name = Compiler_Name
        self.Compiler_Version = Compiler_Version
    def factory(*args_, **kwargs_):
        if PEBuildInformationType.subclass:
            return PEBuildInformationType.subclass(*args_, **kwargs_)
        else:
            return PEBuildInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Linker_Name(self): return self.Linker_Name
    def set_Linker_Name(self, Linker_Name): self.Linker_Name = Linker_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Linker_Version(self): return self.Linker_Version
    def set_Linker_Version(self, Linker_Version): self.Linker_Version = Linker_Version
    def get_Compiler_Name(self): return self.Compiler_Name
    def set_Compiler_Name(self, Compiler_Name): self.Compiler_Name = Compiler_Name
    def get_Compiler_Version(self): return self.Compiler_Version
    def set_Compiler_Version(self, Compiler_Version): self.Compiler_Version = Compiler_Version
    def hasContent_(self):
        if (
            self.Linker_Name is not None or
            self.Linker_Version is not None or
            self.Compiler_Name is not None or
            self.Compiler_Version is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEBuildInformationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEBuildInformationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEBuildInformationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEBuildInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Linker_Name is not None:
            self.Linker_Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Linker_Name', pretty_print=pretty_print)
        if self.Linker_Version is not None:
            self.Linker_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Linker_Version', pretty_print=pretty_print)
        if self.Compiler_Name is not None:
            self.Compiler_Name.export(lwrite, level, 'WinExecutableFileObj:', name_='Compiler_Name', pretty_print=pretty_print)
        if self.Compiler_Version is not None:
            self.Compiler_Version.export(lwrite, level, 'WinExecutableFileObj:', name_='Compiler_Version', pretty_print=pretty_print)
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
        if nodeName_ == 'Linker_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Linker_Name(obj_)
        elif nodeName_ == 'Linker_Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Linker_Version(obj_)
        elif nodeName_ == 'Compiler_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Compiler_Name(obj_)
        elif nodeName_ == 'Compiler_Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Compiler_Version(obj_)
# end class PEBuildInformationType



class PEType(cybox_common.BaseObjectPropertyType):
    """PEType specifies PE file types via a union of the PETypeEnum type
    and the atomic xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(PEType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PEType.subclass:
            return PEType.subclass(*args_, **kwargs_)
        else:
            return PEType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PEType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PEType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='PEType'):
        super(PEType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PEType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='PEType', fromsubclass_=False, pretty_print=True):
        super(PEType, self).exportChildren(lwrite, level, 'WinExecutableFileObj:', name_, True, pretty_print=pretty_print)
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
        super(PEType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PEType

class SubsystemType(cybox_common.BaseObjectPropertyType):
    """SubsystemTypes specifies subsystem types via a union of the
    SubsystemTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SubsystemType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SubsystemType.subclass:
            return SubsystemType.subclass(*args_, **kwargs_)
        else:
            return SubsystemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SubsystemType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='SubsystemType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SubsystemType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='SubsystemType'):
        super(SubsystemType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SubsystemType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='SubsystemType', fromsubclass_=False, pretty_print=True):
        super(SubsystemType, self).exportChildren(lwrite, level, 'WinExecutableFileObj:', name_, True, pretty_print=pretty_print)
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
        super(SubsystemType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SubsystemType

class WindowsExecutableFileObjectType(win_file_object.WindowsFileObjectType):
    """The WindowsExecutableFileObjectType type is intended to characterize
    Windows PE (Portable Executable) files."""

    subclass = None
    superclass = win_file_object.WindowsFileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Filename_Accessed_Time=None, Filename_Created_Time=None, Filename_Modified_Time=None, Drive=None, Security_ID=None, Security_Type=None, Stream_List=None, Build_Information=None, Digital_Signature=None, Exports=None, Extraneous_Bytes=None, Headers=None, Imports=None, PE_Checksum=None, Resources=None, Sections=None, Type=None):
        super(WindowsExecutableFileObjectType, self).__init__(object_reference, Custom_Properties, is_packed, File_Name, File_Path, Device_Path, Full_Path, File_Extension, Size_In_Bytes, Magic_Number, File_Format, Hashes, Digital_Signatures, Modified_Time, Accessed_Time, Created_Time, File_Attributes_List, Permissions, User_Owner, Packer_List, Peak_Entropy, Sym_Links, Byte_Runs, Extracted_Features, Filename_Accessed_Time, Filename_Created_Time, Filename_Modified_Time, Drive, Security_ID, Security_Type, Stream_List, )
        self.Build_Information = Build_Information
        self.Digital_Signature = Digital_Signature
        self.Exports = Exports
        self.Extraneous_Bytes = Extraneous_Bytes
        self.Headers = Headers
        self.Imports = Imports
        self.PE_Checksum = PE_Checksum
        self.Resources = Resources
        self.Sections = Sections
        self.Type = Type
    def factory(*args_, **kwargs_):
        if WindowsExecutableFileObjectType.subclass:
            return WindowsExecutableFileObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsExecutableFileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Build_Information(self): return self.Build_Information
    def set_Build_Information(self, Build_Information): self.Build_Information = Build_Information
    def get_Digital_Signature(self): return self.Digital_Signature
    def set_Digital_Signature(self, Digital_Signature): self.Digital_Signature = Digital_Signature
    def get_Exports(self): return self.Exports
    def set_Exports(self, Exports): self.Exports = Exports
    def get_Extraneous_Bytes(self): return self.Extraneous_Bytes
    def set_Extraneous_Bytes(self, Extraneous_Bytes): self.Extraneous_Bytes = Extraneous_Bytes
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Headers(self): return self.Headers
    def set_Headers(self, Headers): self.Headers = Headers
    def get_Imports(self): return self.Imports
    def set_Imports(self, Imports): self.Imports = Imports
    def get_PE_Checksum(self): return self.PE_Checksum
    def set_PE_Checksum(self, PE_Checksum): self.PE_Checksum = PE_Checksum
    def get_Resources(self): return self.Resources
    def set_Resources(self, Resources): self.Resources = Resources
    def get_Sections(self): return self.Sections
    def set_Sections(self, Sections): self.Sections = Sections
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_PEType(self, value):
        # Validate type PEType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Build_Information is not None or
            self.Digital_Signature is not None or
            self.Exports is not None or
            self.Extraneous_Bytes is not None or
            self.Headers is not None or
            self.Imports is not None or
            self.PE_Checksum is not None or
            self.Resources is not None or
            self.Sections is not None or
            self.Type is not None or
            super(WindowsExecutableFileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='WindowsExecutableFileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsExecutableFileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinExecutableFileObj:', name_='WindowsExecutableFileObjectType'):
        super(WindowsExecutableFileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsExecutableFileObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinExecutableFileObj:', name_='WindowsExecutableFileObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsExecutableFileObjectType, self).exportChildren(lwrite, level, 'WinExecutableFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Build_Information is not None:
            self.Build_Information.export(lwrite, level, 'WinExecutableFileObj:', name_='Build_Information', pretty_print=pretty_print)
        if self.Digital_Signature is not None:
            self.Digital_Signature.export(lwrite, level, 'WinExecutableFileObj:', name_='Digital_Signature', pretty_print=pretty_print)
        if self.Exports is not None:
            self.Exports.export(lwrite, level, 'WinExecutableFileObj:', name_='Exports', pretty_print=pretty_print)
        if self.Extraneous_Bytes is not None:
            self.Extraneous_Bytes.export(lwrite, level, 'WinExecutableFileObj:', name_='Extraneous_Bytes', pretty_print=pretty_print)
        if self.Headers is not None:
            self.Headers.export(lwrite, level, 'WinExecutableFileObj:', name_='Headers', pretty_print=pretty_print)
        if self.Imports is not None:
            self.Imports.export(lwrite, level, 'WinExecutableFileObj:', name_='Imports', pretty_print=pretty_print)
        if self.PE_Checksum is not None:
            self.PE_Checksum.export(lwrite, level, 'WinExecutableFileObj:', name_='PE_Checksum', pretty_print=pretty_print)
        if self.Resources is not None:
            self.Resources.export(lwrite, level, 'WinExecutableFileObj:', name_='Resources', pretty_print=pretty_print)
        if self.Sections is not None:
            self.Sections.export(lwrite, level, 'WinExecutableFileObj:', name_='Sections', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinExecutableFileObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsExecutableFileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Build_Information':
            obj_ = PEBuildInformationType.factory()
            obj_.build(child_)
            self.set_Build_Information(obj_)
        elif nodeName_ == 'Digital_Signature':
            obj_ = cybox_common.DigitalSignatureInfoType.factory()
            obj_.build(child_)
            self.set_Digital_Signature(obj_)
        elif nodeName_ == 'Exports':
            obj_ = PEExportsType.factory()
            obj_.build(child_)
            self.set_Exports(obj_)
        elif nodeName_ == 'Extraneous_Bytes':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Extraneous_Bytes(obj_)
        elif nodeName_ == 'Headers':
            obj_ = PEHeadersType.factory()
            obj_.build(child_)
            self.set_Headers(obj_)
        elif nodeName_ == 'Imports':
            obj_ = PEImportListType.factory()
            obj_.build(child_)
            self.set_Imports(obj_)
        elif nodeName_ == 'PE_Checksum':
            obj_ = PEChecksumType.factory()
            obj_.build(child_)
            self.set_PE_Checksum(obj_)
        elif nodeName_ == 'Resources':
            obj_ = PEResourceListType.factory()
            obj_.build(child_)
            self.set_Resources(obj_)
        elif nodeName_ == 'Sections':
            obj_ = PESectionListType.factory()
            obj_.build(child_)
            self.set_Sections(obj_)
        elif nodeName_ == 'Type':
            obj_ = PEType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(WindowsExecutableFileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsExecutableFileObjectType

GDSClassesMapping = {
    'Extraneous_Bytes': cybox_common.IntegerObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Linker_Version': cybox_common.StringObjectPropertyType,
    'Errors': cybox_common.ErrorsType,
    'Major_Linker_Version': cybox_common.HexBinaryObjectPropertyType,
    'Size_Of_Stack_Commit': cybox_common.HexBinaryObjectPropertyType,
    'Filename_Accessed_Time': cybox_common.DateTimeObjectPropertyType,
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Comments': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'e_lfanew': cybox_common.HexBinaryObjectPropertyType,
    'Loader_Flags': cybox_common.HexBinaryObjectPropertyType,
    'Size_Of_Code': cybox_common.HexBinaryObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'e_cblp': cybox_common.HexBinaryObjectPropertyType,
    'Image_Base': cybox_common.HexBinaryObjectPropertyType,
    'Base_Of_Data': cybox_common.HexBinaryObjectPropertyType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'e_lfarlc': cybox_common.HexBinaryObjectPropertyType,
    'Pointer_To_Linenumbers': cybox_common.HexBinaryObjectPropertyType,
    'SpecialBuild': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Size_Of_Uninitialized_Data': cybox_common.HexBinaryObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Address_Of_Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Magic': cybox_common.HexBinaryObjectPropertyType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Checksum': cybox_common.HexBinaryObjectPropertyType,
    'e_csum': cybox_common.HexBinaryObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Number_Of_Rva_And_Sizes': cybox_common.HexBinaryObjectPropertyType,
    'e_oeminfo': cybox_common.HexBinaryObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Hint': cybox_common.HexBinaryObjectPropertyType,
    'Pointer_To_Symbol_Table': cybox_common.HexBinaryObjectPropertyType,
    'LegalCopyright': cybox_common.StringObjectPropertyType,
    'e_minalloc': cybox_common.HexBinaryObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Characteristics': cybox_common.HexBinaryObjectPropertyType,
    'PE_Computed_API': cybox_common.LongObjectPropertyType,
    'e_cp': cybox_common.HexBinaryObjectPropertyType,
    'e_cs': cybox_common.HexBinaryObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'File_Alignment': cybox_common.HexBinaryObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Full_Path': cybox_common.StringObjectPropertyType,
    'Attribute': win_file_object.WindowsFileAttributeType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Base_Of_Code': cybox_common.HexBinaryObjectPropertyType,
    'Number_Of_Linenumbers': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Filename_Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'Virtual_Address': cybox_common.HexBinaryObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Number_Of_Relocations': cybox_common.NonNegativeIntegerObjectPropertyType,
    'LangID': cybox_common.StringObjectPropertyType,
    'e_maxalloc': cybox_common.HexBinaryObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Size_Of_Raw_Data': cybox_common.HexBinaryObjectPropertyType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Ordinal': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Size_Of_Heap_Reserve': cybox_common.HexBinaryObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Size_Of_Initialized_Data': cybox_common.HexBinaryObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Size_Of_Stack_Reserve': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'Subsystem': cybox_common.HexBinaryObjectPropertyType,
    'Major_Image_Version': cybox_common.HexBinaryObjectPropertyType,
    'Size_Of_Optional_Header': cybox_common.HexBinaryObjectPropertyType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'Number_Of_Names': cybox_common.LongObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'Filename_Modified_Time': cybox_common.DateTimeObjectPropertyType,
    'InternalName': cybox_common.StringObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
    'Compiler_Name': cybox_common.StringObjectPropertyType,
    'Win32_Version_Value': cybox_common.HexBinaryObjectPropertyType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Time_Date_Stamp': cybox_common.HexBinaryObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Windows_File': win_file_object.WindowsFileObjectType,
    'Strings': cybox_common.ExtractedStringsType,
    'e_crlc': cybox_common.HexBinaryObjectPropertyType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Minor_OS_Version': cybox_common.HexBinaryObjectPropertyType,
    'Number_Of_Sections': cybox_common.NonNegativeIntegerObjectPropertyType,
    'LegalTrademarks': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'ProductName': cybox_common.StringObjectPropertyType,
    'DLL_Characteristics': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Size_Of_Headers': cybox_common.HexBinaryObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Data_Hashes': cybox_common.HashListType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'e_cparhdr': cybox_common.HexBinaryObjectPropertyType,
    'Security_Type': cybox_common.SIDType,
    'Instance': cybox_common.ObjectPropertiesType,
    'PE_File_API': cybox_common.LongObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Accessed_Time': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Compiler_Version': cybox_common.StringObjectPropertyType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Header_Hashes': cybox_common.HashListType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Size_Of_Image': cybox_common.HexBinaryObjectPropertyType,
    'PrivateBuild': cybox_common.StringObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Minor_Subsystem_Version': cybox_common.HexBinaryObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'e_ovro': cybox_common.HexBinaryObjectPropertyType,
    'Dependency': cybox_common.DependencyType,
    'PE_File_Raw': cybox_common.LongObjectPropertyType,
    'Build_Utility': cybox_common.BuildUtilityType,
    'Minor_Image_Version': cybox_common.HexBinaryObjectPropertyType,
    'Virtual_Size': cybox_common.HexBinaryObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Libraries': cybox_common.LibrariesType,
    'Stream': win_file_object.StreamObjectType,
    'CompanyName': cybox_common.StringObjectPropertyType,
    'Stream_List': win_file_object.StreamListType,
    'Imports': cybox_common.ImportsType,
    'Number_Of_Symbols': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Size_Of_Heap_Commit': cybox_common.HexBinaryObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Pointer_To_Relocations': cybox_common.HexBinaryObjectPropertyType,
    'Size': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Time': cybox_common.TimeType,
    'Min': cybox_common.FloatObjectPropertyType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Machine': cybox_common.HexBinaryObjectPropertyType,
    'Security_ID': cybox_common.StringObjectPropertyType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'reserved1': cybox_common.HexBinaryObjectPropertyType,
    'e_sp': cybox_common.HexBinaryObjectPropertyType,
    'e_ss': cybox_common.HexBinaryObjectPropertyType,
    'reserved2': cybox_common.HexBinaryObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
    'Linker_Name': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Compilers': cybox_common.CompilersType,
    'Segment': cybox_common.HashSegmentType,
    'Depth': cybox_common.IntegerObjectPropertyType,
    'Section_Alignment': cybox_common.HexBinaryObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'FileVersion': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Number_Of_Addresses': cybox_common.LongObjectPropertyType,
    'Drive': cybox_common.StringObjectPropertyType,
    'Hash': cybox_common.HashType,
    'Exports_Time_Stamp': cybox_common.DateTimeObjectPropertyType,
    'Minor_Linker_Version': cybox_common.HexBinaryObjectPropertyType,
    'Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'ProductVersion': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'FileDescription': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'OriginalFilename': cybox_common.StringObjectPropertyType,
    'e_ip': cybox_common.HexBinaryObjectPropertyType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
    'Major_Subsystem_Version': cybox_common.HexBinaryObjectPropertyType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Bound': cybox_common.HexBinaryObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'e_oemid': cybox_common.HexBinaryObjectPropertyType,
    'Pointer_To_Raw_Data': cybox_common.HexBinaryObjectPropertyType,
    'e_magic': cybox_common.HexBinaryObjectPropertyType,
    'Max': cybox_common.FloatObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Major_OS_Version': cybox_common.HexBinaryObjectPropertyType,
    'Function_Name': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Windows_Executable_File'
        rootClass = WindowsExecutableFileObjectType
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
        rootTag = 'Windows_Executable_File'
        rootClass = WindowsExecutableFileObjectType
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
        rootTag = 'Windows_Executable_File'
        rootClass = WindowsExecutableFileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Executable_File",
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
    "WindowsExecutableFileObjectType",
    "PEChecksumType",
    "PEExportsType",
    "PEExportedFunctionsType",
    "PESectionListType",
    "EntropyType",
    "PEImportType",
    "PEImportedFunctionsType",
    "PEResourceType",
    "PEVersionInfoResourceType",
    "PEExportedFunctionType",
    "PEResourceListType",
    "PEImportedFunctionType",
    "PEImportListType",
    "PESectionType",
    "PEDataDirectoryStructType",
    "PESectionHeaderStructType",
    "DOSHeaderType",
    "PEHeadersType",
    "PEFileHeaderType",
    "SubsystemType",
    "PEType",
    "PEOptionalHeaderType",
    "DataDirectoryType",
    "PEBuildInformationType"
    ]
