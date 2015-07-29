# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import file_object


class PDFXRefTableListType(GeneratedsSuper):
    """The PDFXrefTableListType captures a list of PDF cross-reference
    tables."""

    subclass = None
    superclass = None
    def __init__(self, Cross_Reference_Table=None):
        if Cross_Reference_Table is None:
            self.Cross_Reference_Table = []
        else:
            self.Cross_Reference_Table = Cross_Reference_Table
    def factory(*args_, **kwargs_):
        if PDFXRefTableListType.subclass:
            return PDFXRefTableListType.subclass(*args_, **kwargs_)
        else:
            return PDFXRefTableListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Cross_Reference_Table(self): return self.Cross_Reference_Table
    def set_Cross_Reference_Table(self, Cross_Reference_Table): self.Cross_Reference_Table = Cross_Reference_Table
    def add_Cross_Reference_Table(self, value): self.Cross_Reference_Table.append(value)
    def insert_Cross_Reference_Table(self, index, value): self.Cross_Reference_Table[index] = value
    def hasContent_(self):
        if (
            self.Cross_Reference_Table
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXRefTableListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXRefTableListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXRefTableListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXRefTableListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Cross_Reference_Table_ in self.Cross_Reference_Table:
            Cross_Reference_Table_.export(lwrite, level, 'PDFFileObj:', name_='Cross_Reference_Table', pretty_print=pretty_print)
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
        if nodeName_ == 'Cross_Reference_Table':
            obj_ = PDFXRefTableType.factory()
            obj_.build(child_)
            self.Cross_Reference_Table.append(obj_)
# end class PDFXRefTableListType

class PDFXRefTableType(GeneratedsSuper):
    """The PDFXRefTableType captures the details of a PDF cross-reference
    table, which provides a capability for the random access of
    indirect objects contained in the file."""

    subclass = None
    superclass = None
    def __init__(self, Subsections=None, Offset=None, Hashes=None):
        self.Subsections = Subsections
        self.Offset = Offset
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PDFXRefTableType.subclass:
            return PDFXRefTableType.subclass(*args_, **kwargs_)
        else:
            return PDFXRefTableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Subsections(self): return self.Subsections
    def set_Subsections(self, Subsections): self.Subsections = Subsections
    def get_Offset(self): return self.Offset
    def set_Offset(self, Offset): self.Offset = Offset
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.Subsections is not None or
            self.Offset is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXRefTableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXRefTableType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXRefTableType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXRefTableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Subsections is not None:
            self.Subsections.export(lwrite, level, 'PDFFileObj:', name_='Subsections', pretty_print=pretty_print)
        if self.Offset is not None:
            self.Offset.export(lwrite, level, 'PDFFileObj:', name_='Offset', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'PDFFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Subsections':
            obj_ = PDFXrefTableSubsectionListType.factory()
            obj_.build(child_)
            self.set_Subsections(obj_)
        elif nodeName_ == 'Offset':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PDFXRefTableType

class PDFXrefTableSubsectionListType(GeneratedsSuper):
    """The PDFXrefTableSubsectionListType captures a list of cross-
    reference table subsections."""

    subclass = None
    superclass = None
    def __init__(self, Subsection=None):
        if Subsection is None:
            self.Subsection = []
        else:
            self.Subsection = Subsection
    def factory(*args_, **kwargs_):
        if PDFXrefTableSubsectionListType.subclass:
            return PDFXrefTableSubsectionListType.subclass(*args_, **kwargs_)
        else:
            return PDFXrefTableSubsectionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Subsection(self): return self.Subsection
    def set_Subsection(self, Subsection): self.Subsection = Subsection
    def add_Subsection(self, value): self.Subsection.append(value)
    def insert_Subsection(self, index, value): self.Subsection[index] = value
    def hasContent_(self):
        if (
            self.Subsection
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXrefTableSubsectionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Subsection_ in self.Subsection:
            Subsection_.export(lwrite, level, 'PDFFileObj:', name_='Subsection', pretty_print=pretty_print)
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
        if nodeName_ == 'Subsection':
            obj_ = PDFXrefTableSubsectionType.factory()
            obj_.build(child_)
            self.Subsection.append(obj_)
# end class PDFXrefTableSubsectionListType

class PDFXrefTableSubsectionType(GeneratedsSuper):
    """The PDFXrefTableSubsectionType captures details of subsections
    contained within a PDF cross-reference table."""

    subclass = None
    superclass = None
    def __init__(self, First_Object_Number=None, Number_Of_Objects=None, Cross_Reference_Entries=None):
        self.First_Object_Number = First_Object_Number
        self.Number_Of_Objects = Number_Of_Objects
        self.Cross_Reference_Entries = Cross_Reference_Entries
    def factory(*args_, **kwargs_):
        if PDFXrefTableSubsectionType.subclass:
            return PDFXrefTableSubsectionType.subclass(*args_, **kwargs_)
        else:
            return PDFXrefTableSubsectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_First_Object_Number(self): return self.First_Object_Number
    def set_First_Object_Number(self, First_Object_Number): self.First_Object_Number = First_Object_Number
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Objects(self): return self.Number_Of_Objects
    def set_Number_Of_Objects(self, Number_Of_Objects): self.Number_Of_Objects = Number_Of_Objects
    def get_Cross_Reference_Entries(self): return self.Cross_Reference_Entries
    def set_Cross_Reference_Entries(self, Cross_Reference_Entries): self.Cross_Reference_Entries = Cross_Reference_Entries
    def hasContent_(self):
        if (
            self.First_Object_Number is not None or
            self.Number_Of_Objects is not None or
            self.Cross_Reference_Entries is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXrefTableSubsectionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefTableSubsectionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.First_Object_Number is not None:
            self.First_Object_Number.export(lwrite, level, 'PDFFileObj:', name_='First_Object_Number', pretty_print=pretty_print)
        if self.Number_Of_Objects is not None:
            self.Number_Of_Objects.export(lwrite, level, 'PDFFileObj:', name_='Number_Of_Objects', pretty_print=pretty_print)
        if self.Cross_Reference_Entries is not None:
            self.Cross_Reference_Entries.export(lwrite, level, 'PDFFileObj:', name_='Cross_Reference_Entries', pretty_print=pretty_print)
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
        if nodeName_ == 'First_Object_Number':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_First_Object_Number(obj_)
        elif nodeName_ == 'Number_Of_Objects':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Objects(obj_)
        elif nodeName_ == 'Cross_Reference_Entries':
            obj_ = PDFXrefEntryListType.factory()
            obj_.build(child_)
            self.set_Cross_Reference_Entries(obj_)
# end class PDFXrefTableSubsectionType

class PDFTrailerListType(GeneratedsSuper):
    """The PDFTrailerListType captures a list of PDF trailers."""

    subclass = None
    superclass = None
    def __init__(self, Trailer=None):
        if Trailer is None:
            self.Trailer = []
        else:
            self.Trailer = Trailer
    def factory(*args_, **kwargs_):
        if PDFTrailerListType.subclass:
            return PDFTrailerListType.subclass(*args_, **kwargs_)
        else:
            return PDFTrailerListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Trailer(self): return self.Trailer
    def set_Trailer(self, Trailer): self.Trailer = Trailer
    def add_Trailer(self, value): self.Trailer.append(value)
    def insert_Trailer(self, index, value): self.Trailer[index] = value
    def hasContent_(self):
        if (
            self.Trailer
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFTrailerListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFTrailerListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFTrailerListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFTrailerListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Trailer_ in self.Trailer:
            Trailer_.export(lwrite, level, 'PDFFileObj:', name_='Trailer', pretty_print=pretty_print)
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
        if nodeName_ == 'Trailer':
            obj_ = PDFTrailerType.factory()
            obj_.build(child_)
            self.Trailer.append(obj_)
# end class PDFTrailerListType

class PDFTrailerType(GeneratedsSuper):
    """The PDFTrailerType captures the details of a PDF trailer."""

    subclass = None
    superclass = None
    def __init__(self, Size=None, Prev=None, Root=None, Encrypt=None, Info=None, ID=None, Last_Cross_Reference_Offset=None, Offset=None, Hashes=None):
        self.Size = Size
        self.Prev = Prev
        self.Root = Root
        self.Encrypt = Encrypt
        self.Info = Info
        self.ID = ID
        self.Last_Cross_Reference_Offset = Last_Cross_Reference_Offset
        self.Offset = Offset
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PDFTrailerType.subclass:
            return PDFTrailerType.subclass(*args_, **kwargs_)
        else:
            return PDFTrailerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Size(self): return self.Size
    def set_Size(self, Size): self.Size = Size
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Prev(self): return self.Prev
    def set_Prev(self, Prev): self.Prev = Prev
    def get_Root(self): return self.Root
    def set_Root(self, Root): self.Root = Root
    def get_Encrypt(self): return self.Encrypt
    def set_Encrypt(self, Encrypt): self.Encrypt = Encrypt
    def get_Info(self): return self.Info
    def set_Info(self, Info): self.Info = Info
    def get_ID(self): return self.ID
    def set_ID(self, ID): self.ID = ID
    def get_Last_Cross_Reference_Offset(self): return self.Last_Cross_Reference_Offset
    def set_Last_Cross_Reference_Offset(self, Last_Cross_Reference_Offset): self.Last_Cross_Reference_Offset = Last_Cross_Reference_Offset
    def get_Offset(self): return self.Offset
    def set_Offset(self, Offset): self.Offset = Offset
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def hasContent_(self):
        if (
            self.Size is not None or
            self.Prev is not None or
            self.Root is not None or
            self.Encrypt is not None or
            self.Info is not None or
            self.ID is not None or
            self.Last_Cross_Reference_Offset is not None or
            self.Offset is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFTrailerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFTrailerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFTrailerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFTrailerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Size is not None:
            self.Size.export(lwrite, level, 'PDFFileObj:', name_='Size', pretty_print=pretty_print)
        if self.Prev is not None:
            self.Prev.export(lwrite, level, 'PDFFileObj:', name_='Prev', pretty_print=pretty_print)
        if self.Root is not None:
            self.Root.export(lwrite, level, 'PDFFileObj:', name_='Root', pretty_print=pretty_print)
        if self.Encrypt is not None:
            self.Encrypt.export(lwrite, level, 'PDFFileObj:', name_='Encrypt', pretty_print=pretty_print)
        if self.Info is not None:
            self.Info.export(lwrite, level, 'PDFFileObj:', name_='Info', pretty_print=pretty_print)
        if self.ID is not None:
            self.ID.export(lwrite, level, 'PDFFileObj:', name_='ID', pretty_print=pretty_print)
        if self.Last_Cross_Reference_Offset is not None:
            self.Last_Cross_Reference_Offset.export(lwrite, level, 'PDFFileObj:', name_='Last_Cross_Reference_Offset', pretty_print=pretty_print)
        if self.Offset is not None:
            self.Offset.export(lwrite, level, 'PDFFileObj:', name_='Offset', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'PDFFileObj:', name_='Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Size':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size(obj_)
        elif nodeName_ == 'Prev':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Prev(obj_)
        elif nodeName_ == 'Root':
            obj_ = PDFIndirectObjectIDType.factory()
            obj_.build(child_)
            self.set_Root(obj_)
        elif nodeName_ == 'Encrypt':
            obj_ = PDFDictionaryType.factory()
            obj_.build(child_)
            self.set_Encrypt(obj_)
        elif nodeName_ == 'Info':
            obj_ = PDFIndirectObjectIDType.factory()
            obj_.build(child_)
            self.set_Info(obj_)
        elif nodeName_ == 'ID':
            obj_ = PDFFileIDType.factory()
            obj_.build(child_)
            self.set_ID(obj_)
        elif nodeName_ == 'Last_Cross_Reference_Offset':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Cross_Reference_Offset(obj_)
        elif nodeName_ == 'Offset':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PDFTrailerType

class PDFFileIDType(GeneratedsSuper):
    """The PDFTrailerIDType captures the details of a PDF ID value stored
    in a trailer."""

    subclass = None
    superclass = None
    def __init__(self, ID_String=None):
        if ID_String is None:
            self.ID_String = []
        else:
            self.ID_String = ID_String
    def factory(*args_, **kwargs_):
        if PDFFileIDType.subclass:
            return PDFFileIDType.subclass(*args_, **kwargs_)
        else:
            return PDFFileIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ID_String(self): return self.ID_String
    def set_ID_String(self, ID_String): self.ID_String = ID_String
    def add_ID_String(self, value): self.ID_String.append(value)
    def insert_ID_String(self, index, value): self.ID_String[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.ID_String
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFFileIDType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFFileIDType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileIDType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ID_String_ in self.ID_String:
            ID_String_.export(lwrite, level, 'PDFFileObj:', name_='ID_String', pretty_print=pretty_print)
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
        if nodeName_ == 'ID_String':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.ID_String.append(obj_)
# end class PDFFileIDType

class PDFIndirectObjectListType(GeneratedsSuper):
    """The PDFIndirectObjectListType captures a list of PDF indirect
    objects."""

    subclass = None
    superclass = None
    def __init__(self, Indirect_Object=None):
        if Indirect_Object is None:
            self.Indirect_Object = []
        else:
            self.Indirect_Object = Indirect_Object
    def factory(*args_, **kwargs_):
        if PDFIndirectObjectListType.subclass:
            return PDFIndirectObjectListType.subclass(*args_, **kwargs_)
        else:
            return PDFIndirectObjectListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Indirect_Object(self): return self.Indirect_Object
    def set_Indirect_Object(self, Indirect_Object): self.Indirect_Object = Indirect_Object
    def add_Indirect_Object(self, value): self.Indirect_Object.append(value)
    def insert_Indirect_Object(self, index, value): self.Indirect_Object[index] = value
    def hasContent_(self):
        if (
            self.Indirect_Object
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFIndirectObjectListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFIndirectObjectListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Indirect_Object_ in self.Indirect_Object:
            Indirect_Object_.export(lwrite, level, 'PDFFileObj:', name_='Indirect_Object', pretty_print=pretty_print)
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
        if nodeName_ == 'Indirect_Object':
            obj_ = PDFIndirectObjectType.factory()
            obj_.build(child_)
            self.Indirect_Object.append(obj_)
# end class PDFIndirectObjectListType

class PDFIndirectObjectType(GeneratedsSuper):
    """The PDFObjectType captures the details of a PDF document indirect
    object, used in constructing and storing data associated with
    the PDF document.The type field specifies the basic type of the
    PDF indirect object."""

    subclass = None
    superclass = None
    def __init__(self, type_=None, ID=None, Contents=None, Offset=None, Hashes=None):
        self.type_ = _cast(None, type_)
        self.ID = ID
        self.Contents = Contents
        self.Offset = Offset
        self.Hashes = Hashes
    def factory(*args_, **kwargs_):
        if PDFIndirectObjectType.subclass:
            return PDFIndirectObjectType.subclass(*args_, **kwargs_)
        else:
            return PDFIndirectObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ID(self): return self.ID
    def set_ID(self, ID): self.ID = ID
    def get_Contents(self): return self.Contents
    def set_Contents(self, Contents): self.Contents = Contents
    def get_Offset(self): return self.Offset
    def set_Offset(self, Offset): self.Offset = Offset
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def hasContent_(self):
        if (
            self.ID is not None or
            self.Contents is not None or
            self.Offset is not None or
            self.Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFIndirectObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFIndirectObjectType'):
        if self.type_ is not None:

            lwrite(' type=%s' % (quote_attrib(self.type_), ))
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ID is not None:
            self.ID.export(lwrite, level, 'PDFFileObj:', name_='ID', pretty_print=pretty_print)
        if self.Contents is not None:
            self.Contents.export(lwrite, level, 'PDFFileObj:', name_='Contents', pretty_print=pretty_print)
        if self.Offset is not None:
            self.Offset.export(lwrite, level, 'PDFFileObj:', name_='Offset', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'PDFFileObj:', name_='Hashes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None:

            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ID':
            obj_ = PDFFileIDType.factory()
            obj_.build(child_)
            self.set_ID(obj_)
        elif nodeName_ == 'Contents':
            obj_ = PDFIndirectObjectContentsType.factory()
            obj_.build(child_)
            self.set_Contents(obj_)
        elif nodeName_ == 'Offset':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
# end class PDFIndirectObjectType

class PDFIndirectObjectIDType(GeneratedsSuper):
    """The PDFIndirectObjectIDType captures the details of PDF indirect
    object IDs."""

    subclass = None
    superclass = None
    def __init__(self, Object_Number=None, Generation_Number=None):
        self.Object_Number = Object_Number
        self.Generation_Number = Generation_Number
    def factory(*args_, **kwargs_):
        if PDFIndirectObjectIDType.subclass:
            return PDFIndirectObjectIDType.subclass(*args_, **kwargs_)
        else:
            return PDFIndirectObjectIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Object_Number(self): return self.Object_Number
    def set_Object_Number(self, Object_Number): self.Object_Number = Object_Number
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Generation_Number(self): return self.Generation_Number
    def set_Generation_Number(self, Generation_Number): self.Generation_Number = Generation_Number
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Object_Number is not None or
            self.Generation_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFIndirectObjectIDType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFIndirectObjectIDType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectIDType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Object_Number is not None:
            self.Object_Number.export(lwrite, level, 'PDFFileObj:', name_='Object_Number', pretty_print=pretty_print)
        if self.Generation_Number is not None:
            self.Generation_Number.export(lwrite, level, 'PDFFileObj:', name_='Generation_Number', pretty_print=pretty_print)
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
        if nodeName_ == 'Object_Number':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Object_Number(obj_)
        elif nodeName_ == 'Generation_Number':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Generation_Number(obj_)
# end class PDFIndirectObjectIDType

class PDFIndirectObjectContentsType(GeneratedsSuper):
    """The PDFIndirectObjectContentsType captures the contents of a PDF
    indirect object, including both stream and non-stream portions."""

    subclass = None
    superclass = None
    def __init__(self, Non_Stream_Contents=None, Stream_Contents=None):
        self.Non_Stream_Contents = Non_Stream_Contents
        self.Stream_Contents = Stream_Contents
    def factory(*args_, **kwargs_):
        if PDFIndirectObjectContentsType.subclass:
            return PDFIndirectObjectContentsType.subclass(*args_, **kwargs_)
        else:
            return PDFIndirectObjectContentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Non_Stream_Contents(self): return self.Non_Stream_Contents
    def set_Non_Stream_Contents(self, Non_Stream_Contents): self.Non_Stream_Contents = Non_Stream_Contents
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Stream_Contents(self): return self.Stream_Contents
    def set_Stream_Contents(self, Stream_Contents): self.Stream_Contents = Stream_Contents
    def hasContent_(self):
        if (
            self.Non_Stream_Contents is not None or
            self.Stream_Contents is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectContentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFIndirectObjectContentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFIndirectObjectContentsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFIndirectObjectContentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Non_Stream_Contents is not None:
            if self.Non_Stream_Contents.get_valueOf_() is not None:
                value = self.Non_Stream_Contents.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Non_Stream_Contents.set_valueOf_(value)
            self.Non_Stream_Contents.export(lwrite, level, 'PDFFileObj:', name_='Non_Stream_Contents', pretty_print=pretty_print)
        if self.Stream_Contents is not None:
            self.Stream_Contents.export(lwrite, level, 'PDFFileObj:', name_='Stream_Contents', pretty_print=pretty_print)
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
        if nodeName_ == 'Non_Stream_Contents':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Non_Stream_Contents(obj_)
        elif nodeName_ == 'Stream_Contents':
            obj_ = PDFStreamType.factory()
            obj_.build(child_)
            self.set_Stream_Contents(obj_)
# end class PDFIndirectObjectContentsType

class PDFStreamType(GeneratedsSuper):
    """The PDFStreamType element captures details of PDF document stream
    objects, which represent arbitrary sequences of bytes."""

    subclass = None
    superclass = None
    def __init__(self, Raw_Stream=None, Raw_Stream_Hashes=None, Decoded_Stream=None, Decoded_Stream_Hashes=None):
        self.Raw_Stream = Raw_Stream
        self.Raw_Stream_Hashes = Raw_Stream_Hashes
        self.Decoded_Stream = Decoded_Stream
        self.Decoded_Stream_Hashes = Decoded_Stream_Hashes
    def factory(*args_, **kwargs_):
        if PDFStreamType.subclass:
            return PDFStreamType.subclass(*args_, **kwargs_)
        else:
            return PDFStreamType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Raw_Stream(self): return self.Raw_Stream
    def set_Raw_Stream(self, Raw_Stream): self.Raw_Stream = Raw_Stream
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Raw_Stream_Hashes(self): return self.Raw_Stream_Hashes
    def set_Raw_Stream_Hashes(self, Raw_Stream_Hashes): self.Raw_Stream_Hashes = Raw_Stream_Hashes
    def get_Decoded_Stream(self): return self.Decoded_Stream
    def set_Decoded_Stream(self, Decoded_Stream): self.Decoded_Stream = Decoded_Stream
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Decoded_Stream_Hashes(self): return self.Decoded_Stream_Hashes
    def set_Decoded_Stream_Hashes(self, Decoded_Stream_Hashes): self.Decoded_Stream_Hashes = Decoded_Stream_Hashes
    def hasContent_(self):
        if (
            self.Raw_Stream is not None or
            self.Raw_Stream_Hashes is not None or
            self.Decoded_Stream is not None or
            self.Decoded_Stream_Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFStreamType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFStreamType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFStreamType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFStreamType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Raw_Stream is not None:
            self.Raw_Stream.export(lwrite, level, 'PDFFileObj:', name_='Raw_Stream', pretty_print=pretty_print)
        if self.Raw_Stream_Hashes is not None:
            self.Raw_Stream_Hashes.export(lwrite, level, 'PDFFileObj:', name_='Raw_Stream_Hashes', pretty_print=pretty_print)
        if self.Decoded_Stream is not None:
            self.Decoded_Stream.export(lwrite, level, 'PDFFileObj:', name_='Decoded_Stream', pretty_print=pretty_print)
        if self.Decoded_Stream_Hashes is not None:
            self.Decoded_Stream_Hashes.export(lwrite, level, 'PDFFileObj:', name_='Decoded_Stream_Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Raw_Stream':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Stream(obj_)
        elif nodeName_ == 'Raw_Stream_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Raw_Stream_Hashes(obj_)
        elif nodeName_ == 'Decoded_Stream':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Decoded_Stream(obj_)
        elif nodeName_ == 'Decoded_Stream_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Decoded_Stream_Hashes(obj_)
# end class PDFStreamType

class PDFDocumentInformationDictionaryType(GeneratedsSuper):
    """The PDFDocumentInformationDictionaryType captures details of the PDF
    Document Information Dictionary, used for storing metadata
    associated with the PDF document."""

    subclass = None
    superclass = None
    def __init__(self, Title=None, Author=None, Subject=None, Keywords=None, Creator=None, Producer=None, CreationDate=None, ModDate=None, Trapped=None):
        self.Title = Title
        self.Author = Author
        self.Subject = Subject
        self.Keywords = Keywords
        self.Creator = Creator
        self.Producer = Producer
        self.CreationDate = CreationDate
        self.ModDate = ModDate
        self.Trapped = Trapped
    def factory(*args_, **kwargs_):
        if PDFDocumentInformationDictionaryType.subclass:
            return PDFDocumentInformationDictionaryType.subclass(*args_, **kwargs_)
        else:
            return PDFDocumentInformationDictionaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Author(self): return self.Author
    def set_Author(self, Author): self.Author = Author
    def get_Subject(self): return self.Subject
    def set_Subject(self, Subject): self.Subject = Subject
    def get_Keywords(self): return self.Keywords
    def set_Keywords(self, Keywords): self.Keywords = Keywords
    def get_Creator(self): return self.Creator
    def set_Creator(self, Creator): self.Creator = Creator
    def get_Producer(self): return self.Producer
    def set_Producer(self, Producer): self.Producer = Producer
    def get_CreationDate(self): return self.CreationDate
    def set_CreationDate(self, CreationDate): self.CreationDate = CreationDate
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_ModDate(self): return self.ModDate
    def set_ModDate(self, ModDate): self.ModDate = ModDate
    def get_Trapped(self): return self.Trapped
    def set_Trapped(self, Trapped): self.Trapped = Trapped
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Author is not None or
            self.Subject is not None or
            self.Keywords is not None or
            self.Creator is not None or
            self.Producer is not None or
            self.CreationDate is not None or
            self.ModDate is not None or
            self.Trapped is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFDocumentInformationDictionaryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFDocumentInformationDictionaryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFDocumentInformationDictionaryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFDocumentInformationDictionaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            self.Title.export(lwrite, level, 'PDFFileObj:', name_='Title', pretty_print=pretty_print)
        if self.Author is not None:
            self.Author.export(lwrite, level, 'PDFFileObj:', name_='Author', pretty_print=pretty_print)
        if self.Subject is not None:
            self.Subject.export(lwrite, level, 'PDFFileObj:', name_='Subject', pretty_print=pretty_print)
        if self.Keywords is not None:
            self.Keywords.export(lwrite, level, 'PDFFileObj:', name_='Keywords', pretty_print=pretty_print)
        if self.Creator is not None:
            self.Creator.export(lwrite, level, 'PDFFileObj:', name_='Creator', pretty_print=pretty_print)
        if self.Producer is not None:
            self.Producer.export(lwrite, level, 'PDFFileObj:', name_='Producer', pretty_print=pretty_print)
        if self.CreationDate is not None:
            self.CreationDate.export(lwrite, level, 'PDFFileObj:', name_='CreationDate', pretty_print=pretty_print)
        if self.ModDate is not None:
            self.ModDate.export(lwrite, level, 'PDFFileObj:', name_='ModDate', pretty_print=pretty_print)
        if self.Trapped is not None:
            self.Trapped.export(lwrite, level, 'PDFFileObj:', name_='Trapped', pretty_print=pretty_print)
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
        if nodeName_ == 'Title':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Title(obj_)
        elif nodeName_ == 'Author':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Author(obj_)
        elif nodeName_ == 'Subject':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject(obj_)
        elif nodeName_ == 'Keywords':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Keywords(obj_)
        elif nodeName_ == 'Creator':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creator(obj_)
        elif nodeName_ == 'Producer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Producer(obj_)
        elif nodeName_ == 'CreationDate':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_CreationDate(obj_)
        elif nodeName_ == 'ModDate':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ModDate(obj_)
        elif nodeName_ == 'Trapped':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trapped(obj_)
# end class PDFDocumentInformationDictionaryType

class PDFXrefEntryListType(GeneratedsSuper):
    """The PDFXrefEntryListType captures a list of cross-reference table
    subsection entries."""

    subclass = None
    superclass = None
    def __init__(self, Cross_Reference_Entry=None):
        if Cross_Reference_Entry is None:
            self.Cross_Reference_Entry = []
        else:
            self.Cross_Reference_Entry = Cross_Reference_Entry
    def factory(*args_, **kwargs_):
        if PDFXrefEntryListType.subclass:
            return PDFXrefEntryListType.subclass(*args_, **kwargs_)
        else:
            return PDFXrefEntryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Cross_Reference_Entry(self): return self.Cross_Reference_Entry
    def set_Cross_Reference_Entry(self, Cross_Reference_Entry): self.Cross_Reference_Entry = Cross_Reference_Entry
    def add_Cross_Reference_Entry(self, value): self.Cross_Reference_Entry.append(value)
    def insert_Cross_Reference_Entry(self, index, value): self.Cross_Reference_Entry[index] = value
    def hasContent_(self):
        if (
            self.Cross_Reference_Entry
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefEntryListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXrefEntryListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXrefEntryListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefEntryListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Cross_Reference_Entry_ in self.Cross_Reference_Entry:
            Cross_Reference_Entry_.export(lwrite, level, 'PDFFileObj:', name_='Cross_Reference_Entry', pretty_print=pretty_print)
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
        if nodeName_ == 'Cross_Reference_Entry':
            obj_ = PDFXrefEntryType.factory()
            obj_.build(child_)
            self.Cross_Reference_Entry.append(obj_)
# end class PDFXrefEntryListType

class PDFXrefEntryType(GeneratedsSuper):
    """The PDFXrefEntryType captures details of a cross-reference table
    subsection entry.The type field specifies the type of the cross-
    reference entry."""

    subclass = None
    superclass = None
    def __init__(self, type_=None, Byte_Offset=None, Object_Number=None, Generation_Number=None):
        self.type_ = _cast(None, type_)
        self.Byte_Offset = Byte_Offset
        self.Object_Number = Object_Number
        self.Generation_Number = Generation_Number
    def factory(*args_, **kwargs_):
        if PDFXrefEntryType.subclass:
            return PDFXrefEntryType.subclass(*args_, **kwargs_)
        else:
            return PDFXrefEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Byte_Offset(self): return self.Byte_Offset
    def set_Byte_Offset(self, Byte_Offset): self.Byte_Offset = Byte_Offset
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Object_Number(self): return self.Object_Number
    def set_Object_Number(self, Object_Number): self.Object_Number = Object_Number
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Generation_Number(self): return self.Generation_Number
    def set_Generation_Number(self, Generation_Number): self.Generation_Number = Generation_Number
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def hasContent_(self):
        if (
            self.Byte_Offset is not None or
            self.Object_Number is not None or
            self.Generation_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFXrefEntryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFXrefEntryType'):
        if self.type_ is not None:

            lwrite(' type=%s' % (quote_attrib(self.type_), ))
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFXrefEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Byte_Offset is not None:
            self.Byte_Offset.export(lwrite, level, 'PDFFileObj:', name_='Byte_Offset', pretty_print=pretty_print)
        if self.Object_Number is not None:
            self.Object_Number.export(lwrite, level, 'PDFFileObj:', name_='Object_Number', pretty_print=pretty_print)
        if self.Generation_Number is not None:
            self.Generation_Number.export(lwrite, level, 'PDFFileObj:', name_='Generation_Number', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None:

            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Byte_Offset':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Byte_Offset(obj_)
        elif nodeName_ == 'Object_Number':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Object_Number(obj_)
        elif nodeName_ == 'Generation_Number':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Generation_Number(obj_)
# end class PDFXrefEntryType

class PDFDictionaryType(GeneratedsSuper):
    """The PDFDictionaryType captures a PDF dictionary as a set of key
    value pairs, or as a reference to an indirect object that
    contains."""

    subclass = None
    superclass = None
    def __init__(self, Object_Reference=None, Raw_Contents=None):
        self.Object_Reference = Object_Reference
        self.Raw_Contents = Raw_Contents
    def factory(*args_, **kwargs_):
        if PDFDictionaryType.subclass:
            return PDFDictionaryType.subclass(*args_, **kwargs_)
        else:
            return PDFDictionaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Object_Reference(self): return self.Object_Reference
    def set_Object_Reference(self, Object_Reference): self.Object_Reference = Object_Reference
    def get_Raw_Contents(self): return self.Raw_Contents
    def set_Raw_Contents(self, Raw_Contents): self.Raw_Contents = Raw_Contents
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Object_Reference is not None or
            self.Raw_Contents is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFDictionaryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFDictionaryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFDictionaryType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFDictionaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Object_Reference is not None:
            self.Object_Reference.export(lwrite, level, 'PDFFileObj:', name_='Object_Reference', pretty_print=pretty_print)
        if self.Raw_Contents is not None:
            if self.Raw_Contents.get_valueOf_() is not None:
                value = self.Raw_Contents.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Contents.set_valueOf_(value)
            self.Raw_Contents.export(lwrite, level, 'PDFFileObj:', name_='Raw_Contents', pretty_print=pretty_print)
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
        if nodeName_ == 'Object_Reference':
            obj_ = PDFIndirectObjectIDType.factory()
            obj_.build(child_)
            self.set_Object_Reference(obj_)
        elif nodeName_ == 'Raw_Contents':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Contents(obj_)
# end class PDFDictionaryType

class PDFFileMetadataType(GeneratedsSuper):
    """The PDFFileMetadaType captures some metadata regarding the PDF file
    object.The encrypted field specifies whether the PDF file is
    encrypted.The optimized field specifies whether the PDF file has
    been optimized."""

    subclass = None
    superclass = None
    def __init__(self, encrypted=None, optimized=None, Document_Information_Dictionary=None, Number_Of_Indirect_Objects=None, Number_Of_Trailers=None, Number_Of_Cross_Reference_Tables=None, Keyword_Counts=None):
        self.encrypted = _cast(bool, encrypted)
        self.optimized = _cast(bool, optimized)
        self.Document_Information_Dictionary = Document_Information_Dictionary
        self.Number_Of_Indirect_Objects = Number_Of_Indirect_Objects
        self.Number_Of_Trailers = Number_Of_Trailers
        self.Number_Of_Cross_Reference_Tables = Number_Of_Cross_Reference_Tables
        self.Keyword_Counts = Keyword_Counts
    def factory(*args_, **kwargs_):
        if PDFFileMetadataType.subclass:
            return PDFFileMetadataType.subclass(*args_, **kwargs_)
        else:
            return PDFFileMetadataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Document_Information_Dictionary(self): return self.Document_Information_Dictionary
    def set_Document_Information_Dictionary(self, Document_Information_Dictionary): self.Document_Information_Dictionary = Document_Information_Dictionary
    def get_Number_Of_Indirect_Objects(self): return self.Number_Of_Indirect_Objects
    def set_Number_Of_Indirect_Objects(self, Number_Of_Indirect_Objects): self.Number_Of_Indirect_Objects = Number_Of_Indirect_Objects
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Number_Of_Trailers(self): return self.Number_Of_Trailers
    def set_Number_Of_Trailers(self, Number_Of_Trailers): self.Number_Of_Trailers = Number_Of_Trailers
    def get_Number_Of_Cross_Reference_Tables(self): return self.Number_Of_Cross_Reference_Tables
    def set_Number_Of_Cross_Reference_Tables(self, Number_Of_Cross_Reference_Tables): self.Number_Of_Cross_Reference_Tables = Number_Of_Cross_Reference_Tables
    def get_Keyword_Counts(self): return self.Keyword_Counts
    def set_Keyword_Counts(self, Keyword_Counts): self.Keyword_Counts = Keyword_Counts
    def get_encrypted(self): return self.encrypted
    def set_encrypted(self, encrypted): self.encrypted = encrypted
    def get_optimized(self): return self.optimized
    def set_optimized(self, optimized): self.optimized = optimized
    def hasContent_(self):
        if (
            self.Document_Information_Dictionary is not None or
            self.Number_Of_Indirect_Objects is not None or
            self.Number_Of_Trailers is not None or
            self.Number_Of_Cross_Reference_Tables is not None or
            self.Keyword_Counts is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileMetadataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFFileMetadataType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFFileMetadataType'):
        if self.encrypted is not None:

            lwrite(' encrypted="%s"' % self.gds_format_boolean(self.encrypted, input_name='encrypted'))
        if self.optimized is not None:

            lwrite(' optimized="%s"' % self.gds_format_boolean(self.optimized, input_name='optimized'))
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileMetadataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Document_Information_Dictionary is not None:
            self.Document_Information_Dictionary.export(lwrite, level, 'PDFFileObj:', name_='Document_Information_Dictionary', pretty_print=pretty_print)
        if self.Number_Of_Indirect_Objects is not None:
            self.Number_Of_Indirect_Objects.export(lwrite, level, 'PDFFileObj:', name_='Number_Of_Indirect_Objects', pretty_print=pretty_print)
        if self.Number_Of_Trailers is not None:
            self.Number_Of_Trailers.export(lwrite, level, 'PDFFileObj:', name_='Number_Of_Trailers', pretty_print=pretty_print)
        if self.Number_Of_Cross_Reference_Tables is not None:
            self.Number_Of_Cross_Reference_Tables.export(lwrite, level, 'PDFFileObj:', name_='Number_Of_Cross_Reference_Tables', pretty_print=pretty_print)
        if self.Keyword_Counts is not None:
            self.Keyword_Counts.export(lwrite, level, 'PDFFileObj:', name_='Keyword_Counts', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('encrypted', node)
        if value is not None:

            if value in ('true', '1'):
                self.encrypted = True
            elif value in ('false', '0'):
                self.encrypted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('optimized', node)
        if value is not None:

            if value in ('true', '1'):
                self.optimized = True
            elif value in ('false', '0'):
                self.optimized = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Document_Information_Dictionary':
            obj_ = PDFDocumentInformationDictionaryType.factory()
            obj_.build(child_)
            self.set_Document_Information_Dictionary(obj_)
        elif nodeName_ == 'Number_Of_Indirect_Objects':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Indirect_Objects(obj_)
        elif nodeName_ == 'Number_Of_Trailers':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Trailers(obj_)
        elif nodeName_ == 'Number_Of_Cross_Reference_Tables':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number_Of_Cross_Reference_Tables(obj_)
        elif nodeName_ == 'Keyword_Counts':
            obj_ = PDFKeywordCountsType.factory()
            obj_.build(child_)
            self.set_Keyword_Counts(obj_)
# end class PDFFileMetadataType

class PDFKeywordCountsType(GeneratedsSuper):
    """The PDFKeywordCountsType captures the occurrences of various
    keywords in a PDF file."""

    subclass = None
    superclass = None
    def __init__(self, Page_Count=None, Encrypt_Count=None, ObjStm_Count=None, JS_Count=None, JavaScript_Count=None, AA_Count=None, OpenAction_Count=None, ASCIIHexDecode_Count=None, ASCII85Decode_Count=None, LZWDecode_Count=None, FlateDecode_Count=None, RunLengthDecode_Count=None, JBIG2Decode_Count=None, DCTDecode_Count=None, RichMedia_Count=None, CCITTFaxDecode_Count=None, Launch_Count=None, XFA_Count=None):
        self.Page_Count = Page_Count
        self.Encrypt_Count = Encrypt_Count
        self.ObjStm_Count = ObjStm_Count
        self.JS_Count = JS_Count
        self.JavaScript_Count = JavaScript_Count
        self.AA_Count = AA_Count
        self.OpenAction_Count = OpenAction_Count
        self.ASCIIHexDecode_Count = ASCIIHexDecode_Count
        self.ASCII85Decode_Count = ASCII85Decode_Count
        self.LZWDecode_Count = LZWDecode_Count
        self.FlateDecode_Count = FlateDecode_Count
        self.RunLengthDecode_Count = RunLengthDecode_Count
        self.JBIG2Decode_Count = JBIG2Decode_Count
        self.DCTDecode_Count = DCTDecode_Count
        self.RichMedia_Count = RichMedia_Count
        self.CCITTFaxDecode_Count = CCITTFaxDecode_Count
        self.Launch_Count = Launch_Count
        self.XFA_Count = XFA_Count
    def factory(*args_, **kwargs_):
        if PDFKeywordCountsType.subclass:
            return PDFKeywordCountsType.subclass(*args_, **kwargs_)
        else:
            return PDFKeywordCountsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Page_Count(self): return self.Page_Count
    def set_Page_Count(self, Page_Count): self.Page_Count = Page_Count
    def get_Encrypt_Count(self): return self.Encrypt_Count
    def set_Encrypt_Count(self, Encrypt_Count): self.Encrypt_Count = Encrypt_Count
    def get_ObjStm_Count(self): return self.ObjStm_Count
    def set_ObjStm_Count(self, ObjStm_Count): self.ObjStm_Count = ObjStm_Count
    def get_JS_Count(self): return self.JS_Count
    def set_JS_Count(self, JS_Count): self.JS_Count = JS_Count
    def get_JavaScript_Count(self): return self.JavaScript_Count
    def set_JavaScript_Count(self, JavaScript_Count): self.JavaScript_Count = JavaScript_Count
    def get_AA_Count(self): return self.AA_Count
    def set_AA_Count(self, AA_Count): self.AA_Count = AA_Count
    def get_OpenAction_Count(self): return self.OpenAction_Count
    def set_OpenAction_Count(self, OpenAction_Count): self.OpenAction_Count = OpenAction_Count
    def get_ASCIIHexDecode_Count(self): return self.ASCIIHexDecode_Count
    def set_ASCIIHexDecode_Count(self, ASCIIHexDecode_Count): self.ASCIIHexDecode_Count = ASCIIHexDecode_Count
    def get_ASCII85Decode_Count(self): return self.ASCII85Decode_Count
    def set_ASCII85Decode_Count(self, ASCII85Decode_Count): self.ASCII85Decode_Count = ASCII85Decode_Count
    def get_LZWDecode_Count(self): return self.LZWDecode_Count
    def set_LZWDecode_Count(self, LZWDecode_Count): self.LZWDecode_Count = LZWDecode_Count
    def get_FlateDecode_Count(self): return self.FlateDecode_Count
    def set_FlateDecode_Count(self, FlateDecode_Count): self.FlateDecode_Count = FlateDecode_Count
    def get_RunLengthDecode_Count(self): return self.RunLengthDecode_Count
    def set_RunLengthDecode_Count(self, RunLengthDecode_Count): self.RunLengthDecode_Count = RunLengthDecode_Count
    def get_JBIG2Decode_Count(self): return self.JBIG2Decode_Count
    def set_JBIG2Decode_Count(self, JBIG2Decode_Count): self.JBIG2Decode_Count = JBIG2Decode_Count
    def get_DCTDecode_Count(self): return self.DCTDecode_Count
    def set_DCTDecode_Count(self, DCTDecode_Count): self.DCTDecode_Count = DCTDecode_Count
    def get_RichMedia_Count(self): return self.RichMedia_Count
    def set_RichMedia_Count(self, RichMedia_Count): self.RichMedia_Count = RichMedia_Count
    def get_CCITTFaxDecode_Count(self): return self.CCITTFaxDecode_Count
    def set_CCITTFaxDecode_Count(self, CCITTFaxDecode_Count): self.CCITTFaxDecode_Count = CCITTFaxDecode_Count
    def get_Launch_Count(self): return self.Launch_Count
    def set_Launch_Count(self, Launch_Count): self.Launch_Count = Launch_Count
    def get_XFA_Count(self): return self.XFA_Count
    def set_XFA_Count(self, XFA_Count): self.XFA_Count = XFA_Count
    def hasContent_(self):
        if (
            self.Page_Count is not None or
            self.Encrypt_Count is not None or
            self.ObjStm_Count is not None or
            self.JS_Count is not None or
            self.JavaScript_Count is not None or
            self.AA_Count is not None or
            self.OpenAction_Count is not None or
            self.ASCIIHexDecode_Count is not None or
            self.ASCII85Decode_Count is not None or
            self.LZWDecode_Count is not None or
            self.FlateDecode_Count is not None or
            self.RunLengthDecode_Count is not None or
            self.JBIG2Decode_Count is not None or
            self.DCTDecode_Count is not None or
            self.RichMedia_Count is not None or
            self.CCITTFaxDecode_Count is not None or
            self.Launch_Count is not None or
            self.XFA_Count is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFKeywordCountsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFKeywordCountsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFKeywordCountsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFKeywordCountsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Page_Count is not None:
            self.Page_Count.export(lwrite, level, 'PDFFileObj:', name_='Page_Count', pretty_print=pretty_print)
        if self.Encrypt_Count is not None:
            self.Encrypt_Count.export(lwrite, level, 'PDFFileObj:', name_='Encrypt_Count', pretty_print=pretty_print)
        if self.ObjStm_Count is not None:
            self.ObjStm_Count.export(lwrite, level, 'PDFFileObj:', name_='ObjStm_Count', pretty_print=pretty_print)
        if self.JS_Count is not None:
            self.JS_Count.export(lwrite, level, 'PDFFileObj:', name_='JS_Count', pretty_print=pretty_print)
        if self.JavaScript_Count is not None:
            self.JavaScript_Count.export(lwrite, level, 'PDFFileObj:', name_='JavaScript_Count', pretty_print=pretty_print)
        if self.AA_Count is not None:
            self.AA_Count.export(lwrite, level, 'PDFFileObj:', name_='AA_Count', pretty_print=pretty_print)
        if self.OpenAction_Count is not None:
            self.OpenAction_Count.export(lwrite, level, 'PDFFileObj:', name_='OpenAction_Count', pretty_print=pretty_print)
        if self.ASCIIHexDecode_Count is not None:
            self.ASCIIHexDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='ASCIIHexDecode_Count', pretty_print=pretty_print)
        if self.ASCII85Decode_Count is not None:
            self.ASCII85Decode_Count.export(lwrite, level, 'PDFFileObj:', name_='ASCII85Decode_Count', pretty_print=pretty_print)
        if self.LZWDecode_Count is not None:
            self.LZWDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='LZWDecode_Count', pretty_print=pretty_print)
        if self.FlateDecode_Count is not None:
            self.FlateDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='FlateDecode_Count', pretty_print=pretty_print)
        if self.RunLengthDecode_Count is not None:
            self.RunLengthDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='RunLengthDecode_Count', pretty_print=pretty_print)
        if self.JBIG2Decode_Count is not None:
            self.JBIG2Decode_Count.export(lwrite, level, 'PDFFileObj:', name_='JBIG2Decode_Count', pretty_print=pretty_print)
        if self.DCTDecode_Count is not None:
            self.DCTDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='DCTDecode_Count', pretty_print=pretty_print)
        if self.RichMedia_Count is not None:
            self.RichMedia_Count.export(lwrite, level, 'PDFFileObj:', name_='RichMedia_Count', pretty_print=pretty_print)
        if self.CCITTFaxDecode_Count is not None:
            self.CCITTFaxDecode_Count.export(lwrite, level, 'PDFFileObj:', name_='CCITTFaxDecode_Count', pretty_print=pretty_print)
        if self.Launch_Count is not None:
            self.Launch_Count.export(lwrite, level, 'PDFFileObj:', name_='Launch_Count', pretty_print=pretty_print)
        if self.XFA_Count is not None:
            self.XFA_Count.export(lwrite, level, 'PDFFileObj:', name_='XFA_Count', pretty_print=pretty_print)
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
        if nodeName_ == 'Page_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_Page_Count(obj_)
        elif nodeName_ == 'Encrypt_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_Encrypt_Count(obj_)
        elif nodeName_ == 'ObjStm_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_ObjStm_Count(obj_)
        elif nodeName_ == 'JS_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_JS_Count(obj_)
        elif nodeName_ == 'JavaScript_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_JavaScript_Count(obj_)
        elif nodeName_ == 'AA_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_AA_Count(obj_)
        elif nodeName_ == 'OpenAction_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_OpenAction_Count(obj_)
        elif nodeName_ == 'ASCIIHexDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_ASCIIHexDecode_Count(obj_)
        elif nodeName_ == 'ASCII85Decode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_ASCII85Decode_Count(obj_)
        elif nodeName_ == 'LZWDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_LZWDecode_Count(obj_)
        elif nodeName_ == 'FlateDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_FlateDecode_Count(obj_)
        elif nodeName_ == 'RunLengthDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_RunLengthDecode_Count(obj_)
        elif nodeName_ == 'JBIG2Decode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_JBIG2Decode_Count(obj_)
        elif nodeName_ == 'DCTDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_DCTDecode_Count(obj_)
        elif nodeName_ == 'RichMedia_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_RichMedia_Count(obj_)
        elif nodeName_ == 'CCITTFaxDecode_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_CCITTFaxDecode_Count(obj_)
        elif nodeName_ == 'Launch_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_Launch_Count(obj_)
        elif nodeName_ == 'XFA_Count':
            obj_ = PDFKeywordCountType.factory()
            obj_.build(child_)
            self.set_XFA_Count(obj_)
# end class PDFKeywordCountsType

class PDFKeywordCountType(GeneratedsSuper):
    """The PDFKeywordCountType captures the obfuscated and non-obfuscated
    occurrences of a keyword."""

    subclass = None
    superclass = None
    def __init__(self, Non_Obfuscated_Count=None, Obfuscated_Count=None):
        self.Non_Obfuscated_Count = Non_Obfuscated_Count
        self.Obfuscated_Count = Obfuscated_Count
    def factory(*args_, **kwargs_):
        if PDFKeywordCountType.subclass:
            return PDFKeywordCountType.subclass(*args_, **kwargs_)
        else:
            return PDFKeywordCountType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Non_Obfuscated_Count(self): return self.Non_Obfuscated_Count
    def set_Non_Obfuscated_Count(self, Non_Obfuscated_Count): self.Non_Obfuscated_Count = Non_Obfuscated_Count
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Obfuscated_Count(self): return self.Obfuscated_Count
    def set_Obfuscated_Count(self, Obfuscated_Count): self.Obfuscated_Count = Obfuscated_Count
    def hasContent_(self):
        if (
            self.Non_Obfuscated_Count is not None or
            self.Obfuscated_Count is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFKeywordCountType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFKeywordCountType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFKeywordCountType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFKeywordCountType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Non_Obfuscated_Count is not None:
            self.Non_Obfuscated_Count.export(lwrite, level, 'PDFFileObj:', name_='Non_Obfuscated_Count', pretty_print=pretty_print)
        if self.Obfuscated_Count is not None:
            self.Obfuscated_Count.export(lwrite, level, 'PDFFileObj:', name_='Obfuscated_Count', pretty_print=pretty_print)
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
        if nodeName_ == 'Non_Obfuscated_Count':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Non_Obfuscated_Count(obj_)
        elif nodeName_ == 'Obfuscated_Count':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Obfuscated_Count(obj_)
# end class PDFKeywordCountType

class PDFFileObjectType(file_object.FileObjectType):
    """The PDFFileObjectType type is intended to characterize the
    structural makeup of PDF files."""

    subclass = None
    superclass = file_object.FileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Metadata=None, Version=None, Indirect_Objects=None, Cross_Reference_Tables=None, Trailers=None):
        super(PDFFileObjectType, self).__init__(object_reference, Custom_Properties, is_packed, File_Name, File_Path, Device_Path, Full_Path, File_Extension, Size_In_Bytes, Magic_Number, File_Format, Hashes, Digital_Signatures, Modified_Time, Accessed_Time, Created_Time, File_Attributes_List, Permissions, User_Owner, Packer_List, Peak_Entropy, Sym_Links, Byte_Runs, Extracted_Features, )
        self.Metadata = Metadata
        self.Version = Version
        self.Indirect_Objects = Indirect_Objects
        self.Cross_Reference_Tables = Cross_Reference_Tables
        self.Trailers = Trailers
    def factory(*args_, **kwargs_):
        if PDFFileObjectType.subclass:
            return PDFFileObjectType.subclass(*args_, **kwargs_)
        else:
            return PDFFileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Metadata(self): return self.Metadata
    def set_Metadata(self, Metadata): self.Metadata = Metadata
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_DoubleObjectPropertyType(self, value):
        # Validate type cybox_common.DoubleObjectPropertyType, a restriction on None.
        pass
    def get_Indirect_Objects(self): return self.Indirect_Objects
    def set_Indirect_Objects(self, Indirect_Objects): self.Indirect_Objects = Indirect_Objects
    def get_Cross_Reference_Tables(self): return self.Cross_Reference_Tables
    def set_Cross_Reference_Tables(self, Cross_Reference_Tables): self.Cross_Reference_Tables = Cross_Reference_Tables
    def get_Trailers(self): return self.Trailers
    def set_Trailers(self, Trailers): self.Trailers = Trailers
    def hasContent_(self):
        if (
            self.Metadata is not None or
            self.Version is not None or
            self.Indirect_Objects is not None or
            self.Cross_Reference_Tables is not None or
            self.Trailers is not None or
            super(PDFFileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFFileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PDFFileObj:', name_='PDFFileObjectType'):
        super(PDFFileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PDFFileObjectType')
    def exportChildren(self, lwrite, level, namespace_='PDFFileObj:', name_='PDFFileObjectType', fromsubclass_=False, pretty_print=True):
        super(PDFFileObjectType, self).exportChildren(lwrite, level, 'PDFFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Metadata is not None:
            self.Metadata.export(lwrite, level, 'PDFFileObj:', name_='Metadata', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(lwrite, level, 'PDFFileObj:', name_='Version', pretty_print=pretty_print)
        if self.Indirect_Objects is not None:
            self.Indirect_Objects.export(lwrite, level, 'PDFFileObj:', name_='Indirect_Objects', pretty_print=pretty_print)
        if self.Cross_Reference_Tables is not None:
            self.Cross_Reference_Tables.export(lwrite, level, 'PDFFileObj:', name_='Cross_Reference_Tables', pretty_print=pretty_print)
        if self.Trailers is not None:
            self.Trailers.export(lwrite, level, 'PDFFileObj:', name_='Trailers', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PDFFileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Metadata':
            obj_ = PDFFileMetadataType.factory()
            obj_.build(child_)
            self.set_Metadata(obj_)
        elif nodeName_ == 'Version':
            obj_ = cybox_common.DoubleObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Indirect_Objects':
            obj_ = PDFIndirectObjectListType.factory()
            obj_.build(child_)
            self.set_Indirect_Objects(obj_)
        elif nodeName_ == 'Cross_Reference_Tables':
            obj_ = PDFXRefTableListType.factory()
            obj_.build(child_)
            self.set_Cross_Reference_Tables(obj_)
        elif nodeName_ == 'Trailers':
            obj_ = PDFTrailerListType.factory()
            obj_.build(child_)
            self.set_Trailers(obj_)
        super(PDFFileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class PDFFileObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Title': cybox_common.StringObjectPropertyType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Number_Of_Trailers': cybox_common.PositiveIntegerObjectPropertyType,
    'Trapped': cybox_common.StringObjectPropertyType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'Author': cybox_common.StringObjectPropertyType,
    'Generation_Number': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Dependencies': cybox_common.DependenciesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Raw_Contents': cybox_common.StringObjectPropertyType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'Producer': cybox_common.StringObjectPropertyType,
    'Raw_Stream_Hashes': cybox_common.HashListType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Last_Cross_Reference_Offset': cybox_common.PositiveIntegerObjectPropertyType,
    'Subject': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'Byte_Offset': cybox_common.IntegerObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Type': file_object.PackerClassType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Non_Stream_Contents': cybox_common.StringObjectPropertyType,
    'Detected_Entrypoint_Signatures': file_object.EntryPointSignatureListType,
    'Tool_Hashes': cybox_common.HashListType,
    'File_Path': file_object.FilePathType,
    'Entry_Point_Signature': file_object.EntryPointSignatureType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Packer': file_object.PackerType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Number_Of_Indirect_Objects': cybox_common.PositiveIntegerObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'File_Attributes_List': file_object.FileAttributeType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Number_Of_Objects': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Size': cybox_common.PositiveIntegerObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Sym_Links': file_object.SymLinksListType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Number_Of_Cross_Reference_Tables': cybox_common.PositiveIntegerObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Obfuscated_Count': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Accessed_Time': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Decoded_Stream': cybox_common.HexBinaryObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Raw_Stream': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Permissions': file_object.FilePermissionsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Packer_List': file_object.PackerListType,
    'Time': cybox_common.TimeType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Creator': cybox_common.StringObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Object_Number': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'References': cybox_common.ToolReferencesType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Keywords': cybox_common.StringObjectPropertyType,
    'Non_Obfuscated_Count': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Libraries': cybox_common.LibrariesType,
    'Decoded_Stream_Hashes': cybox_common.HashListType,
    'Prev': cybox_common.PositiveIntegerObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
    'ModDate': cybox_common.DateTimeObjectPropertyType,
    'ID_String': cybox_common.StringObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Depth': cybox_common.IntegerObjectPropertyType,
    'Full_Path': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'First_Object_Number': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'EP_Jump_Codes': file_object.EPJumpCodeType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'File': file_object.FileObjectType,
    'Contributor': cybox_common.ContributorType,
    'CreationDate': cybox_common.DateTimeObjectPropertyType,
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
        rootTag = 'PDF_File'
        rootClass = PDFFileObjectType
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
        rootTag = 'PDF_File'
        rootClass = PDFFileObjectType
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
        rootTag = 'PDF_File'
        rootClass = PDFFileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="PDF_File",
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
    "PDFFileObjectType",
    "PDFXRefTableListType",
    "PDFXRefTableType",
    "PDFXrefTableSubsectionListType",
    "PDFXrefTableSubsectionType",
    "PDFTrailerListType",
    "PDFTrailerType",
    "PDFFileIDType",
    "PDFIndirectObjectListType",
    "PDFIndirectObjectType",
    "PDFIndirectObjectIDType",
    "PDFIndirectObjectContentsType",
    "PDFStreamType",
    "PDFDocumentInformationDictionaryType",
    "PDFXrefEntryListType",
    "PDFXrefEntryType",
    "PDFDictionaryType",
    "PDFFileMetadataType",
    "PDFKeywordCountsType",
    "PDFKeywordCountType"
    ]
