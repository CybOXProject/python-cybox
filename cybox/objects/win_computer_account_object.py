# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_computer_account_object as account_binding
from cybox.common import (DateTime, HexBinary, ObjectProperties, String,
                          UnsignedLong)
from cybox.objects.account_object import Account
from cybox.objects.port_object import Port


class FullyQualifiedName(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.FullyQualifiedNameType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    netbeui_name = cybox.TypedField("NetBEUI_Name", String)
    full_name = cybox.TypedField("Full_Name", String)


class KerberosService(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosServiceType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    computer = cybox.TypedField("Computer", String)
    name = cybox.TypedField("Name", String)
    port = cybox.TypedField("Port", Port)
    user = cybox.TypedField("User", String)


class KerberosDelegation(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosDelegationType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    bitmask = cybox.TypedField("Bitmask", HexBinary)
    service = cybox.TypedField("Service", KerberosService)


class Kerberos(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    delegation = cybox.TypedField("Delegation", KerberosDelegation)
    ticket = cybox.TypedField("Ticket", UnsignedLong)


class WinComputerAccount(Account):
    _binding = account_binding
    _binding_class = account_binding.WindowsComputerAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'
    _XSI_NS = "WinComputerAccountObj"
    _XSI_TYPE = "WindowsComputerAccountObjectType"

    fully_qualified_name = cybox.TypedField("Fully_Qualified_Name",
                                            FullyQualifiedName)
    kerberos = cybox.TypedField("Kerberos", Kerberos)
    security_id = cybox.TypedField("Security_ID", String)
    # TODO: implement common.SIDType
    # security_type = cybox.TypedField("Security_Type", SID)
    type_ = cybox.TypedField("Type", String)
