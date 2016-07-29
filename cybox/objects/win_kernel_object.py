# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_kernel_object as win_kernel_binding
from cybox.common import ObjectProperties, HexBinary, NonNegativeInteger


class IDTEntry(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.IDTEntryType

    type_attr = fields.TypedField("Type_Attr", HexBinary)
    offset_high = fields.TypedField("Offset_High", HexBinary)
    offset_low = fields.TypedField("Offset_Low", HexBinary)
    offset_middle = fields.TypedField("Offset_Middle", HexBinary)
    selector = fields.TypedField("Selector", HexBinary)


class IDTEntryList(entities.EntityList):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.IDTEntryListType
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    idt_entry = fields.TypedField("IDT_Entry", IDTEntry, multiple=True)


class SSDTEntry(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.SSDTEntryType

    hooked = fields.TypedField("hooked")
    service_table_base = fields.TypedField("Service_Table_Base", HexBinary)
    service_counter_table_base = fields.TypedField("Service_Counter_Table_Base", HexBinary)
    number_of_services = fields.TypedField("Number_Of_Services", NonNegativeInteger)
    argument_table_base = fields.TypedField("Argument_Table_Base", HexBinary)


class SSDTEntryList(entities.EntityList):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.SSDTEntryListType
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    ssdt_entry = fields.TypedField("SSDT_Entry", SSDTEntry, multiple=True)


class WinKernel(ObjectProperties):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.WindowsKernelObjectType
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _XSI_NS = "WinKernelObj"
    _XSI_TYPE = "WindowsKernelObjectType"

    idt = fields.TypedField("IDT", IDTEntryList)
    ssdt = fields.TypedField("SSDT", SSDTEntryList)
