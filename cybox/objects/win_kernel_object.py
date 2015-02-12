# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_kernel_object as win_kernel_binding
from cybox.common import (DigitalSignature, ObjectProperties, String,
        HexBinary, NonNegativeInteger)


class IDTEntry(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.IDTEntryType

    type_attr = cybox.TypedField("Type_Attr", HexBinary)
    offset_high = cybox.TypedField("Offset_High", HexBinary)
    offset_low = cybox.TypedField("Offset_Low", HexBinary)
    offset_middle = cybox.TypedField("Offset_Middle", HexBinary)
    selector = cybox.TypedField("Selector", HexBinary)
    
class IDTEntryList(cybox.EntityList):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.IDTEntryListType
    _binding_var = "IDT_Entry"
    _contained_type = IDTEntry
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"

class SSDTEntry(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.SSDTEntryType

    hooked = cybox.TypedField("hooked")
    service_table_base = cybox.TypedField("Service_Table_Base", HexBinary)
    service_counter_table_base = cybox.TypedField("Service_Counter_Table_Base", HexBinary)
    number_of_services = cybox.TypedField("Number_Of_Services", NonNegativeInteger)
    argument_table_base = cybox.TypedField("Argument_Table_Base", HexBinary)
    
class SSDTEntryList(cybox.EntityList):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.SSDTEntryListType
    _binding_var = "SSDT_Entry"
    _contained_type = SSDTEntry
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"

class WinKernel(ObjectProperties):
    _binding = win_kernel_binding
    _binding_class = win_kernel_binding.WindowsKernelObjectType
    _namespace = "http://cybox.mitre.org/objects#WinKernelObject-2"
    _XSI_NS = "WinKernelObj"
    _XSI_TYPE = "WindowsKernelObjectType"

    idt = cybox.TypedField("IDT", IDTEntryList)
    ssdt = cybox.TypedField("SSDT", SSDTEntryList)
