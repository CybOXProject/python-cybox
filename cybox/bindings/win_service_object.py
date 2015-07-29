# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_process_object


class ServiceDescriptionListType(GeneratedsSuper):
    """A collection of service descriptions."""

    subclass = None
    superclass = None
    def __init__(self, Description=None):
        if Description is None:
            self.Description = []
        else:
            self.Description = Description
    def factory(*args_, **kwargs_):
        if ServiceDescriptionListType.subclass:
            return ServiceDescriptionListType.subclass(*args_, **kwargs_)
        else:
            return ServiceDescriptionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def add_Description(self, value): self.Description.append(value)
    def insert_Description(self, index, value): self.Description[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Description
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceDescriptionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceDescriptionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinServiceObj:', name_='ServiceDescriptionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceDescriptionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Description_ in self.Description:
            Description_.export(lwrite, level, 'WinServiceObj:', name_='Description', pretty_print=pretty_print)
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
        if nodeName_ == 'Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Description.append(obj_)
# end class ServiceDescriptionListType

class ServiceType(cybox_common.BaseObjectPropertyType):
    """ServiceType specifies Windows service types via a union of the
    ServiceTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ServiceType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ServiceType.subclass:
            return ServiceType.subclass(*args_, **kwargs_)
        else:
            return ServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ServiceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinServiceObj:', name_='ServiceType'):
        super(ServiceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceType', fromsubclass_=False, pretty_print=True):
        super(ServiceType, self).exportChildren(lwrite, level, 'WinServiceObj:', name_, True, pretty_print=pretty_print)
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
        super(ServiceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ServiceType

class ServiceStatusType(cybox_common.BaseObjectPropertyType):
    """ServiceModeType specifies Windows service states via a union of the
    ServiceStatusEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ServiceStatusType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ServiceStatusType.subclass:
            return ServiceStatusType.subclass(*args_, **kwargs_)
        else:
            return ServiceStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ServiceStatusType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceStatusType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinServiceObj:', name_='ServiceStatusType'):
        super(ServiceStatusType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceStatusType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceStatusType', fromsubclass_=False, pretty_print=True):
        super(ServiceStatusType, self).exportChildren(lwrite, level, 'WinServiceObj:', name_, True, pretty_print=pretty_print)
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
        super(ServiceStatusType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ServiceStatusType

class ServiceModeType(cybox_common.BaseObjectPropertyType):
    """ServiceModeType specifies Windows service modes via a union of the
    ServiceModeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ServiceModeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ServiceModeType.subclass:
            return ServiceModeType.subclass(*args_, **kwargs_)
        else:
            return ServiceModeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ServiceModeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceModeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceModeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinServiceObj:', name_='ServiceModeType'):
        super(ServiceModeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ServiceModeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinServiceObj:', name_='ServiceModeType', fromsubclass_=False, pretty_print=True):
        super(ServiceModeType, self).exportChildren(lwrite, level, 'WinServiceObj:', name_, True, pretty_print=pretty_print)
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
        super(ServiceModeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ServiceModeType

class WindowsServiceObjectType(win_process_object.WindowsProcessObjectType):
    """The WindowsServiceObjectType type is intended to characterize
    Windows services.Indicates whether or not the DLL is
    signed.Indicates whether or not the DLL's signature was
    verified."""

    subclass = None
    superclass = win_process_object.WindowsProcessObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_hidden=None, PID=None, Name=None, Creation_Time=None, Parent_PID=None, Child_PID_List=None, Image_Info=None, Argument_List=None, Environment_Variable_List=None, Kernel_Time=None, Port_List=None, Network_Connection_List=None, Start_Time=None, Status=None, Username=None, User_Time=None, Extracted_Features=None, aslr_enabled=None, dep_enabled=None, Handle_List=None, Priority=None, Section_List=None, Security_ID=None, Startup_Info=None, Security_Type=None, Window_Title=None, service_dll_signature_verified=None, service_dll_signature_exists=None, Description_List=None, Display_Name=None, Group_Name=None, Service_Name=None, Service_DLL=None, Service_DLL_Certificate_Issuer=None, Service_DLL_Certificate_Subject=None, Service_DLL_Hashes=None, Service_DLL_Signature_Description=None, Startup_Command_Line=None, Startup_Type=None, Service_Status=None, Service_Type=None, Started_As=None):
        super(WindowsServiceObjectType, self).__init__(object_reference, Custom_Properties, is_hidden, PID, Name, Creation_Time, Parent_PID, Child_PID_List, Image_Info, Argument_List, Environment_Variable_List, Kernel_Time, Port_List, Network_Connection_List, Start_Time, Status, Username, User_Time, Extracted_Features, aslr_enabled, dep_enabled, Handle_List, Priority, Section_List, Security_ID, Startup_Info, Security_Type, Window_Title, )
        self.service_dll_signature_verified = _cast(bool, service_dll_signature_verified)
        self.service_dll_signature_exists = _cast(bool, service_dll_signature_exists)
        self.Description_List = Description_List
        self.Display_Name = Display_Name
        self.Group_Name = Group_Name
        self.Service_Name = Service_Name
        self.Service_DLL = Service_DLL
        self.Service_DLL_Certificate_Issuer = Service_DLL_Certificate_Issuer
        self.Service_DLL_Certificate_Subject = Service_DLL_Certificate_Subject
        self.Service_DLL_Hashes = Service_DLL_Hashes
        self.Service_DLL_Signature_Description = Service_DLL_Signature_Description
        self.Startup_Command_Line = Startup_Command_Line
        self.Startup_Type = Startup_Type
        self.Service_Status = Service_Status
        self.Service_Type = Service_Type
        self.Started_As = Started_As
    def factory(*args_, **kwargs_):
        if WindowsServiceObjectType.subclass:
            return WindowsServiceObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsServiceObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description_List(self): return self.Description_List
    def set_Description_List(self, Description_List): self.Description_List = Description_List
    def get_Display_Name(self): return self.Display_Name
    def set_Display_Name(self, Display_Name): self.Display_Name = Display_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Group_Name(self): return self.Group_Name
    def set_Group_Name(self, Group_Name): self.Group_Name = Group_Name
    def get_Service_Name(self): return self.Service_Name
    def set_Service_Name(self, Service_Name): self.Service_Name = Service_Name
    def get_Service_DLL(self): return self.Service_DLL
    def set_Service_DLL(self, Service_DLL): self.Service_DLL = Service_DLL
    def get_Service_DLL_Certificate_Issuer(self): return self.Service_DLL_Certificate_Issuer
    def set_Service_DLL_Certificate_Issuer(self, Service_DLL_Certificate_Issuer): self.Service_DLL_Certificate_Issuer = Service_DLL_Certificate_Issuer
    def get_Service_DLL_Certificate_Subject(self): return self.Service_DLL_Certificate_Subject
    def set_Service_DLL_Certificate_Subject(self, Service_DLL_Certificate_Subject): self.Service_DLL_Certificate_Subject = Service_DLL_Certificate_Subject
    def get_Service_DLL_Hashes(self): return self.Service_DLL_Hashes
    def set_Service_DLL_Hashes(self, Service_DLL_Hashes): self.Service_DLL_Hashes = Service_DLL_Hashes
    def get_Service_DLL_Signature_Description(self): return self.Service_DLL_Signature_Description
    def set_Service_DLL_Signature_Description(self, Service_DLL_Signature_Description): self.Service_DLL_Signature_Description = Service_DLL_Signature_Description
    def get_Startup_Command_Line(self): return self.Startup_Command_Line
    def set_Startup_Command_Line(self, Startup_Command_Line): self.Startup_Command_Line = Startup_Command_Line
    def get_Startup_Type(self): return self.Startup_Type
    def set_Startup_Type(self, Startup_Type): self.Startup_Type = Startup_Type
    def validate_ServiceModeType(self, value):
        # Validate type ServiceModeType, a restriction on None.
        pass
    def get_Service_Status(self): return self.Service_Status
    def set_Service_Status(self, Service_Status): self.Service_Status = Service_Status
    def validate_ServiceStatusType(self, value):
        # Validate type ServiceStatusType, a restriction on None.
        pass
    def get_Service_Type(self): return self.Service_Type
    def set_Service_Type(self, Service_Type): self.Service_Type = Service_Type
    def validate_ServiceType(self, value):
        # Validate type ServiceType, a restriction on None.
        pass
    def get_Started_As(self): return self.Started_As
    def set_Started_As(self, Started_As): self.Started_As = Started_As
    def get_service_dll_signature_verified(self): return self.service_dll_signature_verified
    def set_service_dll_signature_verified(self, service_dll_signature_verified): self.service_dll_signature_verified = service_dll_signature_verified
    def get_service_dll_signature_exists(self): return self.service_dll_signature_exists
    def set_service_dll_signature_exists(self, service_dll_signature_exists): self.service_dll_signature_exists = service_dll_signature_exists
    def hasContent_(self):
        if (
            self.Description_List is not None or
            self.Display_Name is not None or
            self.Group_Name is not None or
            self.Service_Name is not None or
            self.Service_DLL is not None or
            self.Service_DLL_Certificate_Issuer is not None or
            self.Service_DLL_Certificate_Subject is not None or
            self.Service_DLL_Hashes is not None or
            self.Service_DLL_Signature_Description is not None or
            self.Startup_Command_Line is not None or
            self.Startup_Type is not None or
            self.Service_Status is not None or
            self.Service_Type is not None or
            self.Started_As is not None or
            super(WindowsServiceObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinServiceObj:', name_='WindowsServiceObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsServiceObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinServiceObj:', name_='WindowsServiceObjectType'):
        super(WindowsServiceObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsServiceObjectType')
        if self.service_dll_signature_verified is not None:

            lwrite(' service_dll_signature_verified="%s"' % self.gds_format_boolean(self.service_dll_signature_verified, input_name='service_dll_signature_verified'))
        if self.service_dll_signature_exists is not None:

            lwrite(' service_dll_signature_exists="%s"' % self.gds_format_boolean(self.service_dll_signature_exists, input_name='service_dll_signature_exists'))
    def exportChildren(self, lwrite, level, namespace_='WinServiceObj:', name_='WindowsServiceObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsServiceObjectType, self).exportChildren(lwrite, level, 'WinServiceObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description_List is not None:
            self.Description_List.export(lwrite, level, 'WinServiceObj:', name_='Description_List', pretty_print=pretty_print)
        if self.Display_Name is not None:
            self.Display_Name.export(lwrite, level, 'WinServiceObj:', name_='Display_Name', pretty_print=pretty_print)
        if self.Group_Name is not None:
            self.Group_Name.export(lwrite, level, 'WinServiceObj:', name_='Group_Name', pretty_print=pretty_print)
        if self.Service_Name is not None:
            self.Service_Name.export(lwrite, level, 'WinServiceObj:', name_='Service_Name', pretty_print=pretty_print)
        if self.Service_DLL is not None:
            self.Service_DLL.export(lwrite, level, 'WinServiceObj:', name_='Service_DLL', pretty_print=pretty_print)
        if self.Service_DLL_Certificate_Issuer is not None:
            self.Service_DLL_Certificate_Issuer.export(lwrite, level, 'WinServiceObj:', name_='Service_DLL_Certificate_Issuer', pretty_print=pretty_print)
        if self.Service_DLL_Certificate_Subject is not None:
            self.Service_DLL_Certificate_Subject.export(lwrite, level, 'WinServiceObj:', name_='Service_DLL_Certificate_Subject', pretty_print=pretty_print)
        if self.Service_DLL_Hashes is not None:
            self.Service_DLL_Hashes.export(lwrite, level, 'WinServiceObj:', name_='Service_DLL_Hashes', pretty_print=pretty_print)
        if self.Service_DLL_Signature_Description is not None:
            self.Service_DLL_Signature_Description.export(lwrite, level, 'WinServiceObj:', name_='Service_DLL_Signature_Description', pretty_print=pretty_print)
        if self.Startup_Command_Line is not None:
            self.Startup_Command_Line.export(lwrite, level, 'WinServiceObj:', name_='Startup_Command_Line', pretty_print=pretty_print)
        if self.Startup_Type is not None:
            self.Startup_Type.export(lwrite, level, 'WinServiceObj:', name_='Startup_Type', pretty_print=pretty_print)
        if self.Service_Status is not None:
            self.Service_Status.export(lwrite, level, 'WinServiceObj:', name_='Service_Status', pretty_print=pretty_print)
        if self.Service_Type is not None:
            self.Service_Type.export(lwrite, level, 'WinServiceObj:', name_='Service_Type', pretty_print=pretty_print)
        if self.Started_As is not None:
            self.Started_As.export(lwrite, level, 'WinServiceObj:', name_='Started_As', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('service_dll_signature_verified', node)
        if value is not None:

            if value in ('true', '1'):
                self.service_dll_signature_verified = True
            elif value in ('false', '0'):
                self.service_dll_signature_verified = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('service_dll_signature_exists', node)
        if value is not None:

            if value in ('true', '1'):
                self.service_dll_signature_exists = True
            elif value in ('false', '0'):
                self.service_dll_signature_exists = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(WindowsServiceObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description_List':
            obj_ = ServiceDescriptionListType.factory()
            obj_.build(child_)
            self.set_Description_List(obj_)
        elif nodeName_ == 'Display_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Display_Name(obj_)
        elif nodeName_ == 'Group_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Group_Name(obj_)
        elif nodeName_ == 'Service_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_Name(obj_)
        elif nodeName_ == 'Service_DLL':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_DLL(obj_)
        elif nodeName_ == 'Service_DLL_Certificate_Issuer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_DLL_Certificate_Issuer(obj_)
        elif nodeName_ == 'Service_DLL_Certificate_Subject':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_DLL_Certificate_Subject(obj_)
        elif nodeName_ == 'Service_DLL_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Service_DLL_Hashes(obj_)
        elif nodeName_ == 'Service_DLL_Signature_Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Service_DLL_Signature_Description(obj_)
        elif nodeName_ == 'Startup_Command_Line':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Startup_Command_Line(obj_)
        elif nodeName_ == 'Startup_Type':
            obj_ = ServiceModeType.factory()
            obj_.build(child_)
            self.set_Startup_Type(obj_)
        elif nodeName_ == 'Service_Status':
            obj_ = ServiceStatusType.factory()
            obj_.build(child_)
            self.set_Service_Status(obj_)
        elif nodeName_ == 'Service_Type':
            obj_ = ServiceType.factory()
            obj_.build(child_)
            self.set_Service_Type(obj_)
        elif nodeName_ == 'Started_As':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Started_As(obj_)
        super(WindowsServiceObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsServiceObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Kernel_Time': cybox_common.DurationObjectPropertyType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Section_List': win_process_object.MemorySectionListType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'P3P': cybox_common.StringObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'lpDesktop': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Service_DLL_Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'Region_Start_Address': cybox_common.HexBinaryObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.PositiveIntegerObjectPropertyType,
    'Expect': cybox_common.StringObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'TE': cybox_common.StringObjectPropertyType,
    'Parent_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'dwXCountChars': cybox_common.PositiveIntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Warning': cybox_common.StringObjectPropertyType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Group_Name': cybox_common.StringObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'dwXSize': cybox_common.PositiveIntegerObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'lpTitle': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Link': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Path': cybox_common.StringObjectPropertyType,
    'Startup_Info': win_process_object.StartupInfoType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'dwFlags': cybox_common.IntegerObjectPropertyType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Via': cybox_common.StringObjectPropertyType,
    'X_Requested_For': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Security_Type': cybox_common.SIDType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Server': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Child_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'wShowWindow': cybox_common.IntegerObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'User_Time': cybox_common.DurationObjectPropertyType,
    'dwYSize': cybox_common.PositiveIntegerObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
    'dwFillAttribute': cybox_common.IntegerObjectPropertyType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Current_Directory': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'Startup_Command_Line': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Service_DLL': cybox_common.StringObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'dwY': cybox_common.IntegerObjectPropertyType,
    'Command_Line': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Connection': cybox_common.StringObjectPropertyType,
    'X_Requested_With': cybox_common.StringObjectPropertyType,
    'Window_Title': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'If_Unmodified_Since': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Priority': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'Service_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Argument': cybox_common.StringObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'Security_ID': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Windows_Process': win_process_object.WindowsProcessObjectType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Service_DLL_Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Service_DLL_Hashes': cybox_common.HashListType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Service_DLL_Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Started_As': cybox_common.StringObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'Display_Name': cybox_common.StringObjectPropertyType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Region_Size': cybox_common.UnsignedLongObjectPropertyType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'dwYCountChars': cybox_common.PositiveIntegerObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'ETag': cybox_common.StringObjectPropertyType,
    'Date_Ran': cybox_common.DateTimeObjectPropertyType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'If_Match': cybox_common.StringObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'dwX': cybox_common.IntegerObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
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
        rootTag = 'Windows_Service'
        rootClass = WindowsServiceObjectType
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
        rootTag = 'Windows_Service'
        rootClass = WindowsServiceObjectType
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
        rootTag = 'Windows_Service'
        rootClass = WindowsServiceObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Service",
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
    "WindowsServiceObjectType",
    "ServiceDescriptionListType",
    "ServiceModeType",
    "ServiceStatusType",
    "ServiceType"
    ]
