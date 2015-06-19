# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_computer_account_object as account_binding
from cybox.common import HexBinary, String, UnsignedLong
from cybox.objects.account_object import Account
from cybox.objects.port_object import Port


class FullyQualifiedName(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.FullyQualifiedNameType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    netbeui_name = fields.TypedField("NetBEUI_Name", String)
    full_name = fields.TypedField("Full_Name", String)


class KerberosService(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosServiceType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    computer = fields.TypedField("Computer", String)
    name = fields.TypedField("Name", String)
    port = fields.TypedField("Port", Port)
    user = fields.TypedField("User", String)


class KerberosDelegation(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosDelegationType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    bitmask = fields.TypedField("Bitmask", HexBinary)
    service = fields.TypedField("Service", KerberosService)


class Kerberos(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.KerberosType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'

    delegation = fields.TypedField("Delegation", KerberosDelegation)
    ticket = fields.TypedField("Ticket", UnsignedLong)


class WinComputerAccount(Account):
    _binding = account_binding
    _binding_class = account_binding.WindowsComputerAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinComputerAccountObject-2'
    _XSI_NS = "WinComputerAccountObj"
    _XSI_TYPE = "WindowsComputerAccountObjectType"

    fully_qualified_name = fields.TypedField("Fully_Qualified_Name",
                                            FullyQualifiedName)
    kerberos = fields.TypedField("Kerberos", Kerberos)
    security_id = fields.TypedField("Security_ID", String)
    # TODO: implement common.SIDType
    # security_type = fields.TypedField("Security_Type", SID)
    type_ = fields.TypedField("Type", String)
