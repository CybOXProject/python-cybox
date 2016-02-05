# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *

#List delimiter value for lists captured in *ObjectPropertyTypes
__LIST_DELIMITER__ = "##comma##"


class DateWithPrecisionType(GeneratedsSuper):
    """This type is used as a replacement for the standard xs:date type but
    allows for the representation of the precision of the date. If
    the precision is given, consumers must ignore the portions of
    this field that is more precise than the given precision.
    Producers should zero-out (fill with zeros) digits in the date
    that are required by the xs:date datatype but are beyond the
    specified precision.In order to avoid ambiguity, it is strongly
    suggested that all dates include a specification of the timezone
    if it is known.The precision of the associated date. If omitted,
    the default is "day", meaning the full field value."""
    subclass = None
    superclass = None
    def __init__(self, precision='day', valueOf_=None):
        self.precision = _cast(None, precision)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DateWithPrecisionType.subclass:
            return DateWithPrecisionType.subclass(*args_, **kwargs_)
        else:
            return DateWithPrecisionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateWithPrecisionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateWithPrecisionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateWithPrecisionType'):
        if self.precision not in (None, 'second'):

            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateWithPrecisionType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('precision', node)
        if value is not None:

            self.precision = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateWithPrecisionType

class DateTimeWithPrecisionType(GeneratedsSuper):
    """This type is used as a replacement for the standard xs:dateTime type
    but allows for the representation of the precision of the
    dateTime. If the precision is given, consumers must ignore the
    portions of this field that is more precise than the given
    precision. Producers should zero-out (fill with zeros) digits in
    the dateTime that are required by the xs:dateTime datatype but
    are beyond the specified precision.In order to avoid ambiguity,
    it is strongly suggested that all dateTimes include a
    specification of the timezone if it is known.The precision of
    the associated dateTime. If omitted, the default is "second",
    meaning the full field value (including fractional seconds)."""
    subclass = None
    superclass = None
    def __init__(self, precision='second', valueOf_=None):
        self.precision = _cast(None, precision)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DateTimeWithPrecisionType.subclass:
            return DateTimeWithPrecisionType.subclass(*args_, **kwargs_)
        else:
            return DateTimeWithPrecisionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeWithPrecisionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeWithPrecisionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateTimeWithPrecisionType'):
        if self.precision not in (None, 'second'):

            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeWithPrecisionType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('precision', node)
        if value is not None:

            self.precision = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateTimeWithPrecisionType

class LocationType(GeneratedsSuper):
    """The LocationType is used to express geographic location
    information.This type is extended through the xsi:type
    mechanism. The default type is CIQAddress3.0InstanceType in the
    http://cybox.mitre.org/extensions/Address#CIQAddress3.0-1
    namespace. This type is defined in the
    extensions/location/ciq_address_3.0.xsd file or at the URL http:
    //cybox.mitre.org/XMLSchema/extensions/location/ciq_address_3.0/
    1.0/ciq_address_3.0.xsd.Those who wish to express a simple name
    may also do so by not specifying an xsi:type and using the Name
    field of this type.Specifies a unique ID for this
    Location.Specifies a reference to a unique ID defined elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Name=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Name = Name
    def factory(*args_, **kwargs_):
        if LocationType.subclass:
            return LocationType.subclass(*args_, **kwargs_)
        else:
            return LocationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Name is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='LocationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LocationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='LocationType'):
        if self.idref is not None:

            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None:

            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='LocationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            lwrite('<%sName>%s</%sName>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Name), input_name='Name'), 'cyboxCommon:', eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None:

            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None:

            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            Name_ = child_.text
            Name_ = self.gds_validate_string(Name_, node, 'Name')
            self.Name = Name_
# end class LocationType

class MeasureSourceType(GeneratedsSuper):
    """The MeasureSourceType is a type representing a description of a
    single cyber observation source.The class field is optional and
    enables identification of the high-level class of this cyber
    observation source.The source_type field is optional and enables
    identification of the broad type of this cyber observation
    source.The name field is optional and enables the assignment of
    a relevant name to a this Discovery Method."""
    subclass = None
    superclass = None
    def __init__(self, source_type=None, sighting_count=None, classxx=None, name=None, Information_Source_Type=None, Tool_Type=None, Description=None, Contributors=None, Time=None, Observation_Location=None, Tools=None, Platform=None, System=None, Instance=None, Observable_Location=None):
        self.source_type = _cast(None, source_type)
        self.sighting_count = _cast(int, sighting_count)
        self.classxx = _cast(None, classxx)
        self.name = _cast(None, name)
        self.Information_Source_Type = Information_Source_Type
        self.Tool_Type = Tool_Type
        self.Description = Description
        self.Contributors = Contributors
        self.Time = Time
        self.Observation_Location = Observation_Location
        self.Tools = Tools
        self.Platform = Platform
        self.System = System
        self.Instance = Instance
        self.Observable_Location = Observable_Location
    def factory(*args_, **kwargs_):
        if MeasureSourceType.subclass:
            return MeasureSourceType.subclass(*args_, **kwargs_)
        else:
            return MeasureSourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Information_Source_Type(self): return self.Information_Source_Type
    def set_Information_Source_Type(self, Information_Source_Type): self.Information_Source_Type = Information_Source_Type
    def get_Tool_Type(self): return self.Tool_Type
    def set_Tool_Type(self, Tool_Type): self.Tool_Type = Tool_Type
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Contributors(self): return self.Contributors
    def set_Contributors(self, Contributors): self.Contributors = Contributors
    def get_Time(self): return self.Time
    def set_Time(self, Time): self.Time = Time
    def get_Observation_Location(self): return self.Observation_Location
    def set_Observation_Location(self, Observation_Location): self.Observation_Location = Observation_Location
    def get_Tools(self): return self.Tools
    def set_Tools(self, Tools): self.Tools = Tools
    def get_Platform(self): return self.Platform
    def set_Platform(self, Platform): self.Platform = Platform
    def get_System(self): return self.System
    def set_System(self, System): self.System = System
    def get_Instance(self): return self.Instance
    def set_Instance(self, Instance): self.Instance = Instance
    def get_Observable_Location(self): return self.Observable_Location
    def set_Observable_Location(self, Observable_Location): self.Observable_Location = Observable_Location
    def get_source_type(self): return self.source_type
    def set_source_type(self, source_type): self.source_type = source_type
    def get_sighting_count(self): return self.sighting_count
    def set_sighting_count(self, sighting_count): self.sighting_count = sighting_count
    def get_class(self): return self.classxx
    def set_class(self, classxx): self.classxx = classxx
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def hasContent_(self):
        if (
            self.Information_Source_Type is not None or
            self.Tool_Type is not None or
            self.Description is not None or
            self.Contributors is not None or
            self.Time is not None or
            self.Observation_Location is not None or
            self.Tools is not None or
            self.Platform is not None or
            self.System is not None or
            self.Instance is not None or
            self.Observable_Location is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='MeasureSourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MeasureSourceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='MeasureSourceType'):
        if self.source_type is not None:

            lwrite(' source_type=%s' % (quote_attrib(self.source_type), ))
        if self.sighting_count is not None:

            lwrite(' sighting_count="%s"' % self.gds_format_integer(self.sighting_count, input_name='sighting_count'))
        if self.classxx is not None:

            lwrite(' class=%s' % (quote_attrib(self.classxx), ))
        if self.name is not None:

            lwrite(' name=%s' % (self.gds_format_string(quote_attrib(self.name), input_name='name'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='MeasureSourceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Information_Source_Type is not None:
            self.Information_Source_Type.export(lwrite, level, 'cyboxCommon:', name_='Information_Source_Type', pretty_print=pretty_print)
        if self.Tool_Type is not None:
            self.Tool_Type.export(lwrite, level, 'cyboxCommon:', name_='Tool_Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, 'cyboxCommon:', name_='Description', pretty_print=pretty_print)
        if self.Contributors is not None:
            self.Contributors.export(lwrite, level, 'cyboxCommon:', name_='Contributors', pretty_print=pretty_print)
        if self.Time is not None:
            self.Time.export(lwrite, level, 'cyboxCommon:', name_='Time', pretty_print=pretty_print)
        if self.Observation_Location is not None:
            self.Observation_Location.export(lwrite, level, 'cyboxCommon:', name_='Observation_Location', pretty_print=pretty_print)
        if self.Tools is not None:
            self.Tools.export(lwrite, level, 'cyboxCommon:', name_='Tools', pretty_print=pretty_print)
        if self.Platform is not None:
            self.Platform.export(lwrite, level, 'cyboxCommon:', name_='Platform', pretty_print=pretty_print)
        if self.System is not None:
            self.System.export(lwrite, level, 'cyboxCommon:', name_='System', pretty_print=pretty_print)
        if self.Instance is not None:
            self.Instance.export(lwrite, level, 'cyboxCommon:', name_='Instance', pretty_print=pretty_print)
        if self.Observable_Location is not None:
            self.Observable_Location.export(lwrite, level, 'cyboxCommon:', name_='Observable_Location', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('source_type', node)
        if value is not None:

            self.source_type = value
        value = find_attr_value_('sighting_count', node)
        if value is not None:

            try:
                self.sighting_count = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.sighting_count <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
        value = find_attr_value_('class', node)
        if value is not None:

            self.classxx = value
        value = find_attr_value_('name', node)
        if value is not None:

            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Information_Source_Type':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Information_Source_Type(obj_)
        elif nodeName_ == 'Tool_Type':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Tool_Type(obj_)
        elif nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Contributors':
            obj_ = PersonnelType.factory()
            obj_.build(child_)
            self.set_Contributors(obj_)
        elif nodeName_ == 'Time':
            obj_ = TimeType.factory()
            obj_.build(child_)
            self.set_Time(obj_)
        elif nodeName_ == 'Observation_Location':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CIQAddress3.0InstanceType":
                    import cybox.bindings.extensions.location.ciq_address_3_0 as ciq_address_binding
                    obj_ = ciq_address_binding.CIQAddress3_0InstanceType.factory()
            else:
                obj_ = LocationType.factory()

            obj_.build(child_)
            self.set_Observation_Location(obj_)
        elif nodeName_ == 'Tools':
            obj_ = ToolsInformationType.factory()
            obj_.build(child_)
            self.set_Tools(obj_)
        elif nodeName_ == 'Platform':
            obj_ = PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Platform(obj_)
        elif nodeName_ == 'System':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <System> element')
            self.set_System(obj_)
        elif nodeName_ == 'Instance':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Instance> element')
            self.set_Instance(obj_)
        elif nodeName_ == 'Observable_Location':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CIQAddress3.0InstanceType":
                    import cybox.bindings.extensions.location.ciq_address_3_0 as ciq_address_binding
                    obj_ = ciq_address_binding.CIQAddress3_0InstanceType.factory()
            else:
                obj_ = LocationType.factory()

            obj_.build(child_)
            self.set_Observable_Location(obj_)
# end class MeasureSourceType

class ContributorType(GeneratedsSuper):
    """The ContributorType represents a description of an individual who
    contributed as a source of cyber observation data."""

    subclass = None
    superclass = None
    def __init__(self, Role=None, Name=None, Email=None, Phone=None, Organization=None, Date=None, Contribution_Location=None):
        self.Role = Role
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.Organization = Organization
        self.Date = Date
        self.Contribution_Location = Contribution_Location
    def factory(*args_, **kwargs_):
        if ContributorType.subclass:
            return ContributorType.subclass(*args_, **kwargs_)
        else:
            return ContributorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Role(self): return self.Role
    def set_Role(self, Role): self.Role = Role
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Email(self): return self.Email
    def set_Email(self, Email): self.Email = Email
    def get_Phone(self): return self.Phone
    def set_Phone(self, Phone): self.Phone = Phone
    def get_Organization(self): return self.Organization
    def set_Organization(self, Organization): self.Organization = Organization
    def get_Date(self): return self.Date
    def set_Date(self, Date): self.Date = Date
    def get_Contribution_Location(self): return self.Contribution_Location
    def set_Contribution_Location(self, Contribution_Location): self.Contribution_Location = Contribution_Location
    def hasContent_(self):
        if (
            self.Role is not None or
            self.Name is not None or
            self.Email is not None or
            self.Phone is not None or
            self.Organization is not None or
            self.Date is not None or
            self.Contribution_Location is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ContributorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ContributorType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ContributorType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ContributorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Role is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRole>%s</%sRole>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Role), input_name='Role'), 'cyboxCommon:', eol_))
        if self.Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sName>%s</%sName>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Name), input_name='Name'), 'cyboxCommon:', eol_))
        if self.Email is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sEmail>%s</%sEmail>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Email), input_name='Email'), 'cyboxCommon:', eol_))
        if self.Phone is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sPhone>%s</%sPhone>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Phone), input_name='Phone'), 'cyboxCommon:', eol_))
        if self.Organization is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sOrganization>%s</%sOrganization>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Organization), input_name='Organization'), 'cyboxCommon:', eol_))
        if self.Date is not None:
            self.Date.export(lwrite, level, 'cyboxCommon:', name_='Date', pretty_print=pretty_print)
        if self.Contribution_Location is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sContribution_Location>%s</%sContribution_Location>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Contribution_Location), input_name='Contribution_Location'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Role':
            Role_ = child_.text
            Role_ = self.gds_validate_string(Role_, node, 'Role')
            self.Role = Role_
        elif nodeName_ == 'Name':
            Name_ = child_.text
            Name_ = self.gds_validate_string(Name_, node, 'Name')
            self.Name = Name_
        elif nodeName_ == 'Email':
            Email_ = child_.text
            Email_ = self.gds_validate_string(Email_, node, 'Email')
            self.Email = Email_
        elif nodeName_ == 'Phone':
            Phone_ = child_.text
            Phone_ = self.gds_validate_string(Phone_, node, 'Phone')
            self.Phone = Phone_
        elif nodeName_ == 'Organization':
            Organization_ = child_.text
            Organization_ = self.gds_validate_string(Organization_, node, 'Organization')
            self.Organization = Organization_
        elif nodeName_ == 'Date':
            obj_ = DateRangeType.factory()
            obj_.build(child_)
            self.set_Date(obj_)
        elif nodeName_ == 'Contribution_Location':
            Contribution_Location_ = child_.text
            Contribution_Location_ = self.gds_validate_string(Contribution_Location_, node, 'Contribution_Location')
            self.Contribution_Location = Contribution_Location_
# end class ContributorType

class DateRangeType(GeneratedsSuper):
    """The DateRangeType specifies a range of dates."""
    subclass = None
    superclass = None
    def __init__(self, Start_Date=None, End_Date=None):
        self.Start_Date = Start_Date
        self.End_Date = End_Date
    def factory(*args_, **kwargs_):
        if DateRangeType.subclass:
            return DateRangeType.subclass(*args_, **kwargs_)
        else:
            return DateRangeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Start_Date(self): return self.Start_Date
    def set_Start_Date(self, Start_Date): self.Start_Date = Start_Date
    def get_End_Date(self): return self.End_Date
    def set_End_Date(self, End_Date): self.End_Date = End_Date
    def hasContent_(self):
        if (
            self.Start_Date is not None or
            self.End_Date is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateRangeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateRangeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateRangeType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateRangeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Start_Date is not None:
            self.Start_Date.export(lwrite, level, 'cyboxCommon:', name_='Start_Date', pretty_print=pretty_print)
        if self.End_Date is not None:
            self.End_Date.export(lwrite, level, 'cyboxCommon:', name_='End_Date', pretty_print=pretty_print)
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
        if nodeName_ == 'Start_Date':
            obj_ = DateWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Start_Date(obj_)
        elif nodeName_ == 'End_Date':
            obj_ = DateWithPrecisionType.factory()
            obj_.build(child_)
            self.set_End_Date(obj_)
# end class DateRangeType

class PersonnelType(GeneratedsSuper):
    """The PersonnelType is an abstracted data type to standardize the
    description of sets of personnel."""

    subclass = None
    superclass = None
    def __init__(self, Contributor=None):
        if Contributor is None:
            self.Contributor = []
        else:
            self.Contributor = Contributor
    def factory(*args_, **kwargs_):
        if PersonnelType.subclass:
            return PersonnelType.subclass(*args_, **kwargs_)
        else:
            return PersonnelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Contributor(self): return self.Contributor
    def set_Contributor(self, Contributor): self.Contributor = Contributor
    def add_Contributor(self, value): self.Contributor.append(value)
    def insert_Contributor(self, index, value): self.Contributor[index] = value
    def hasContent_(self):
        if (
            self.Contributor
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PersonnelType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PersonnelType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PersonnelType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PersonnelType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Contributor_ in self.Contributor:
            Contributor_.export(lwrite, level, 'cyboxCommon:', name_='Contributor', pretty_print=pretty_print)
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
        if nodeName_ == 'Contributor':
            obj_ = ContributorType.factory()
            obj_.build(child_)
            self.Contributor.append(obj_)
# end class PersonnelType

class TimeType(GeneratedsSuper):
    """The TimeType specifies various time properties for this construct."""
    subclass = None
    superclass = None
    def __init__(self, Start_Time=None, End_Time=None, Produced_Time=None, Received_Time=None):
        self.Start_Time = Start_Time
        self.End_Time = End_Time
        self.Produced_Time = Produced_Time
        self.Received_Time = Received_Time
    def factory(*args_, **kwargs_):
        if TimeType.subclass:
            return TimeType.subclass(*args_, **kwargs_)
        else:
            return TimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Start_Time(self): return self.Start_Time
    def set_Start_Time(self, Start_Time): self.Start_Time = Start_Time
    def get_End_Time(self): return self.End_Time
    def set_End_Time(self, End_Time): self.End_Time = End_Time
    def get_Produced_Time(self): return self.Produced_Time
    def set_Produced_Time(self, Produced_Time): self.Produced_Time = Produced_Time
    def get_Received_Time(self): return self.Received_Time
    def set_Received_Time(self, Received_Time): self.Received_Time = Received_Time
    def hasContent_(self):
        if (
            self.Start_Time is not None or
            self.End_Time is not None or
            self.Produced_Time is not None or
            self.Received_Time is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='TimeType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Start_Time is not None:
            self.Start_Time.export(lwrite, level, 'cyboxCommon:', name_='Start_Time', pretty_print=pretty_print)
        if self.End_Time is not None:
            self.End_Time.export(lwrite, level, 'cyboxCommon:', name_='End_Time', pretty_print=pretty_print)
        if self.Produced_Time is not None:
            self.Produced_Time.export(lwrite, level, 'cyboxCommon:', name_='Produced_Time', pretty_print=pretty_print)
        if self.Received_Time is not None:
            self.Received_Time.export(lwrite, level, 'cyboxCommon:', name_='Received_Time', pretty_print=pretty_print)
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
        if nodeName_ == 'Start_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Start_Time(obj_)
        elif nodeName_ == 'End_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_End_Time(obj_)
        elif nodeName_ == 'Produced_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Produced_Time(obj_)
        elif nodeName_ == 'Received_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Received_Time(obj_)
# end class TimeType

class ToolSpecificDataType(GeneratedsSuper):
    """The ToolSpecificDataType is an Abstract type placeholder within the
    CybOX schema enabling the inclusion of metadata for a specific
    type of tool through the use of a custom type defined as an
    extension of this base Abstract type."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if ToolSpecificDataType.subclass:
            return ToolSpecificDataType.subclass(*args_, **kwargs_)
        else:
            return ToolSpecificDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolSpecificDataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolSpecificDataType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolSpecificDataType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolSpecificDataType', fromsubclass_=False, pretty_print=True):
        pass
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
        pass
# end class ToolSpecificDataType

class ToolsInformationType(GeneratedsSuper):
    """The ToolsInformationType represents a description of a set of
    automated tools."""

    subclass = None
    superclass = None
    def __init__(self, Tool=None):
        if Tool is None:
            self.Tool = []
        else:
            self.Tool = Tool
    def factory(*args_, **kwargs_):
        if ToolsInformationType.subclass:
            return ToolsInformationType.subclass(*args_, **kwargs_)
        else:
            return ToolsInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Tool(self): return self.Tool
    def set_Tool(self, Tool): self.Tool = Tool
    def add_Tool(self, value): self.Tool.append(value)
    def insert_Tool(self, index, value): self.Tool[index] = value
    def hasContent_(self):
        if (
            self.Tool
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolsInformationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolsInformationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolsInformationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolsInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Tool_ in self.Tool:
            Tool_.export(lwrite, level, 'cyboxCommon:', name_='Tool', pretty_print=pretty_print)
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
        if nodeName_ == 'Tool':
            obj_ = ToolInformationType.factory()
            obj_.build(child_)
            self.Tool.append(obj_)
# end class ToolsInformationType

class ToolInformationType(GeneratedsSuper):
    """The ToolInformationType represens a description of a single
    automated tool.The id field specifies a unique ID for this
    Tool.The idref field specifies reference to a unique ID for this
    Tool."""

    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Name=None, Type=None, Description=None, References=None, Vendor=None, Version=None, Service_Pack=None, Tool_Specific_Data=None, Tool_Hashes=None, Tool_Configuration=None, Execution_Environment=None, Errors=None, Metadata=None, Compensation_Model=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Name = Name
        if Type is None:
            self.Type = []
        else:
            self.Type = Type
        self.Description = Description
        self.References = References
        self.Vendor = Vendor
        self.Version = Version
        self.Service_Pack = Service_Pack
        self.Tool_Specific_Data = Tool_Specific_Data
        self.Tool_Hashes = Tool_Hashes
        self.Tool_Configuration = Tool_Configuration
        self.Execution_Environment = Execution_Environment
        self.Errors = Errors
        if Metadata is None:
            self.Metadata = []
        else:
            self.Metadata = Metadata
        self.Compensation_Model = Compensation_Model
    def factory(*args_, **kwargs_):
        if ToolInformationType.subclass:
            return ToolInformationType.subclass(*args_, **kwargs_)
        else:
            return ToolInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def add_Type(self, value): self.Type.append(value)
    def insert_Type(self, index, value): self.Type[index] = value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_References(self): return self.References
    def set_References(self, References): self.References = References
    def get_Vendor(self): return self.Vendor
    def set_Vendor(self, Vendor): self.Vendor = Vendor
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def get_Service_Pack(self): return self.Service_Pack
    def set_Service_Pack(self, Service_Pack): self.Service_Pack = Service_Pack
    def get_Tool_Specific_Data(self): return self.Tool_Specific_Data
    def set_Tool_Specific_Data(self, Tool_Specific_Data): self.Tool_Specific_Data = Tool_Specific_Data
    def get_Tool_Hashes(self): return self.Tool_Hashes
    def set_Tool_Hashes(self, Tool_Hashes): self.Tool_Hashes = Tool_Hashes
    def get_Tool_Configuration(self): return self.Tool_Configuration
    def set_Tool_Configuration(self, Tool_Configuration): self.Tool_Configuration = Tool_Configuration
    def get_Execution_Environment(self): return self.Execution_Environment
    def set_Execution_Environment(self, Execution_Environment): self.Execution_Environment = Execution_Environment
    def get_Errors(self): return self.Errors
    def set_Errors(self, Errors): self.Errors = Errors
    def get_Metadata(self): return self.Metadata
    def set_Metadata(self, Metadata): self.Metadata = Metadata
    def add_Metadata(self, value): self.Metadata.append(value)
    def insert_Metadata(self, index, value): self.Metadata[index] = value
    def get_Compensation_Model(self): return self.Compensation_Model
    def set_Compensation_Model(self, Compensation_Model): self.Compensation_Model = Compensation_Model
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Type or
            self.Description is not None or
            self.References is not None or
            self.Vendor is not None or
            self.Version is not None or
            self.Service_Pack is not None or
            self.Tool_Specific_Data is not None or
            self.Tool_Hashes is not None or
            self.Tool_Configuration is not None or
            self.Execution_Environment is not None or
            self.Errors is not None or
            self.Metadata or
            self.Compensation_Model is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolInformationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolInformationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolInformationType'):
        if self.idref is not None:

            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None:

            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sName>%s</%sName>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Name), input_name='Name'), 'cyboxCommon:', eol_))
        for Type_ in self.Type:
            Type_.export(lwrite, level, 'cyboxCommon:', name_='Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, 'cyboxCommon:', name_='Description', pretty_print=pretty_print)
        if self.References is not None:
            self.References.export(lwrite, level, 'cyboxCommon:', name_='References', pretty_print=pretty_print)
        if self.Vendor is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sVendor>%s</%sVendor>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Vendor), input_name='Vendor'), 'cyboxCommon:', eol_))
        if self.Version is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sVersion>%s</%sVersion>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Version), input_name='Version'), 'cyboxCommon:', eol_))
        if self.Service_Pack is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sService_Pack>%s</%sService_Pack>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Service_Pack), input_name='Service_Pack'), 'cyboxCommon:', eol_))
        if self.Tool_Specific_Data is not None:
            self.Tool_Specific_Data.export(lwrite, level, 'cyboxCommon:', name_='Tool_Specific_Data', pretty_print=pretty_print)
        if self.Tool_Hashes is not None:
            self.Tool_Hashes.export(lwrite, level, 'cyboxCommon:', name_='Tool_Hashes', pretty_print=pretty_print)
        if self.Tool_Configuration is not None:
            self.Tool_Configuration.export(lwrite, level, 'cyboxCommon:', name_='Tool_Configuration', pretty_print=pretty_print)
        if self.Execution_Environment is not None:
            self.Execution_Environment.export(lwrite, level, 'cyboxCommon:', name_='Execution_Environment', pretty_print=pretty_print)
        if self.Errors is not None:
            self.Errors.export(lwrite, level, 'cyboxCommon:', name_='Errors', pretty_print=pretty_print)
        for Metadata_ in self.Metadata:
            Metadata_.export(lwrite, level, 'cyboxCommon:', name_='Metadata', pretty_print=pretty_print)
        if self.Compensation_Model is not None:
            self.Compensation_Model.export(lwrite, level, 'cyboxCommon:', name_='Compensation_Model', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None:

            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None:

            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            Name_ = child_.text
            Name_ = self.gds_validate_string(Name_, node, 'Name')
            self.Name = Name_
        elif nodeName_ == 'Type':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Type.append(obj_)
        elif nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'References':
            obj_ = ToolReferencesType.factory()
            obj_.build(child_)
            self.set_References(obj_)
        elif nodeName_ == 'Vendor':
            Vendor_ = child_.text
            Vendor_ = self.gds_validate_string(Vendor_, node, 'Vendor')
            self.Vendor = Vendor_
        elif nodeName_ == 'Version':
            Version_ = child_.text
            Version_ = self.gds_validate_string(Version_, node, 'Version')
            self.Version = Version_
        elif nodeName_ == 'Service_Pack':
            Service_Pack_ = child_.text
            Service_Pack_ = self.gds_validate_string(Service_Pack_, node, 'Service_Pack')
            self.Service_Pack = Service_Pack_
        elif nodeName_ == 'Tool_Specific_Data':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Tool_Specific_Data> element')
            self.set_Tool_Specific_Data(obj_)
        elif nodeName_ == 'Tool_Hashes':
            obj_ = HashListType.factory()
            obj_.build(child_)
            self.set_Tool_Hashes(obj_)
        elif nodeName_ == 'Tool_Configuration':
            obj_ = ToolConfigurationType.factory()
            obj_.build(child_)
            self.set_Tool_Configuration(obj_)
        elif nodeName_ == 'Execution_Environment':
            obj_ = ExecutionEnvironmentType.factory()
            obj_.build(child_)
            self.set_Execution_Environment(obj_)
        elif nodeName_ == 'Errors':
            obj_ = ErrorsType.factory()
            obj_.build(child_)
            self.set_Errors(obj_)
        elif nodeName_ == 'Metadata':
            obj_ = MetadataType.factory()
            obj_.build(child_)
            self.Metadata.append(obj_)
        elif nodeName_ == 'Compensation_Model':
            obj_ = CompensationModelType.factory()
            obj_.build(child_)
            self.set_Compensation_Model(obj_)
# end class ToolInformationType

class ToolReferencesType(GeneratedsSuper):
    """Used to indicate one or more references to tool instances and
    information"""

    subclass = None
    superclass = None
    def __init__(self, Reference=None):
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
    def factory(*args_, **kwargs_):
        if ToolReferencesType.subclass:
            return ToolReferencesType.subclass(*args_, **kwargs_)
        else:
            return ToolReferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Reference(self): return self.Reference
    def set_Reference(self, Reference): self.Reference = Reference
    def add_Reference(self, value): self.Reference.append(value)
    def insert_Reference(self, index, value): self.Reference[index] = value
    def hasContent_(self):
        if (
            self.Reference
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolReferencesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolReferencesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolReferencesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolReferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            Reference_.export(lwrite, level, 'cyboxCommon:', name_='Reference', pretty_print=pretty_print)
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
        if nodeName_ == 'Reference':
            obj_ = ToolReferenceType.factory()
            obj_.build(child_)
            self.Reference.append(obj_)
# end class ToolReferencesType

class ToolReferenceType(GeneratedsSuper):
    """Contains one reference to information or instances of a given
    toolIndicates the nature of the referenced material
    (documentation, source, executable, etc.)"""

    subclass = None
    superclass = None
    def __init__(self, reference_type=None, valueOf_=None):
        self.reference_type = _cast(None, reference_type)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ToolReferenceType.subclass:
            return ToolReferenceType.subclass(*args_, **kwargs_)
        else:
            return ToolReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_reference_type(self): return self.reference_type
    def set_reference_type(self, reference_type): self.reference_type = reference_type
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolReferenceType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolReferenceType'):
        if self.reference_type is not None:

            lwrite(' reference_type=%s' % (quote_attrib(self.reference_type), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolReferenceType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('reference_type', node)
        if value is not None:

            self.reference_type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ToolReferenceType

class ToolConfigurationType(GeneratedsSuper):
    """The ToolConfigurationType characterizes the configuration for a tool
    used as a cyber observation source."""
    subclass = None
    superclass = None
    def __init__(self, Configuration_Settings=None, Dependencies=None, Usage_Context_Assumptions=None, Internationalization_Settings=None, Build_Information=None):
        self.Configuration_Settings = Configuration_Settings
        self.Dependencies = Dependencies
        self.Usage_Context_Assumptions = Usage_Context_Assumptions
        self.Internationalization_Settings = Internationalization_Settings
        self.Build_Information = Build_Information
    def factory(*args_, **kwargs_):
        if ToolConfigurationType.subclass:
            return ToolConfigurationType.subclass(*args_, **kwargs_)
        else:
            return ToolConfigurationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Configuration_Settings(self): return self.Configuration_Settings
    def set_Configuration_Settings(self, Configuration_Settings): self.Configuration_Settings = Configuration_Settings
    def get_Dependencies(self): return self.Dependencies
    def set_Dependencies(self, Dependencies): self.Dependencies = Dependencies
    def get_Usage_Context_Assumptions(self): return self.Usage_Context_Assumptions
    def set_Usage_Context_Assumptions(self, Usage_Context_Assumptions): self.Usage_Context_Assumptions = Usage_Context_Assumptions
    def get_Internationalization_Settings(self): return self.Internationalization_Settings
    def set_Internationalization_Settings(self, Internationalization_Settings): self.Internationalization_Settings = Internationalization_Settings
    def get_Build_Information(self): return self.Build_Information
    def set_Build_Information(self, Build_Information): self.Build_Information = Build_Information
    def hasContent_(self):
        if (
            self.Configuration_Settings is not None or
            self.Dependencies is not None or
            self.Usage_Context_Assumptions is not None or
            self.Internationalization_Settings is not None or
            self.Build_Information is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolConfigurationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolConfigurationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ToolConfigurationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ToolConfigurationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Configuration_Settings is not None:
            self.Configuration_Settings.export(lwrite, level, 'cyboxCommon:', name_='Configuration_Settings', pretty_print=pretty_print)
        if self.Dependencies is not None:
            self.Dependencies.export(lwrite, level, 'cyboxCommon:', name_='Dependencies', pretty_print=pretty_print)
        if self.Usage_Context_Assumptions is not None:
            self.Usage_Context_Assumptions.export(lwrite, level, 'cyboxCommon:', name_='Usage_Context_Assumptions', pretty_print=pretty_print)
        if self.Internationalization_Settings is not None:
            self.Internationalization_Settings.export(lwrite, level, 'cyboxCommon:', name_='Internationalization_Settings', pretty_print=pretty_print)
        if self.Build_Information is not None:
            self.Build_Information.export(lwrite, level, 'cyboxCommon:', name_='Build_Information', pretty_print=pretty_print)
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
        if nodeName_ == 'Configuration_Settings':
            obj_ = ConfigurationSettingsType.factory()
            obj_.build(child_)
            self.set_Configuration_Settings(obj_)
        elif nodeName_ == 'Dependencies':
            obj_ = DependenciesType.factory()
            obj_.build(child_)
            self.set_Dependencies(obj_)
        elif nodeName_ == 'Usage_Context_Assumptions':
            obj_ = UsageContextAssumptionsType.factory()
            obj_.build(child_)
            self.set_Usage_Context_Assumptions(obj_)
        elif nodeName_ == 'Internationalization_Settings':
            obj_ = InternationalizationSettingsType.factory()
            obj_.build(child_)
            self.set_Internationalization_Settings(obj_)
        elif nodeName_ == 'Build_Information':
            obj_ = BuildInformationType.factory()
            obj_.build(child_)
            self.set_Build_Information(obj_)
# end class ToolConfigurationType

class ConfigurationSettingsType(GeneratedsSuper):
    """The ConfigurationSettingsType is a modularized data type used to
    provide a consistent approach to describing configuration
    settings for a tool, application or other cyber object"""

    subclass = None
    superclass = None
    def __init__(self, Configuration_Setting=None):
        if Configuration_Setting is None:
            self.Configuration_Setting = []
        else:
            self.Configuration_Setting = Configuration_Setting
    def factory(*args_, **kwargs_):
        if ConfigurationSettingsType.subclass:
            return ConfigurationSettingsType.subclass(*args_, **kwargs_)
        else:
            return ConfigurationSettingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Configuration_Setting(self): return self.Configuration_Setting
    def set_Configuration_Setting(self, Configuration_Setting): self.Configuration_Setting = Configuration_Setting
    def add_Configuration_Setting(self, value): self.Configuration_Setting.append(value)
    def insert_Configuration_Setting(self, index, value): self.Configuration_Setting[index] = value
    def hasContent_(self):
        if (
            self.Configuration_Setting
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ConfigurationSettingsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ConfigurationSettingsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ConfigurationSettingsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ConfigurationSettingsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Configuration_Setting_ in self.Configuration_Setting:
            Configuration_Setting_.export(lwrite, level, 'cyboxCommon:', name_='Configuration_Setting', pretty_print=pretty_print)
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
        if nodeName_ == 'Configuration_Setting':
            obj_ = ConfigurationSettingType.factory()
            obj_.build(child_)
            self.Configuration_Setting.append(obj_)
# end class ConfigurationSettingsType

class ConfigurationSettingType(GeneratedsSuper):
    """The ConfigurationSettingType is a modularized data type used to
    provide a consistent approach to describing a particular
    configuration setting for a tool, application or other cyber
    object"""

    subclass = None
    superclass = None
    def __init__(self, Item_Name=None, Item_Value=None, Item_Type=None, Item_Description=None):
        self.Item_Name = Item_Name
        self.Item_Value = Item_Value
        self.Item_Type = Item_Type
        self.Item_Description = Item_Description
    def factory(*args_, **kwargs_):
        if ConfigurationSettingType.subclass:
            return ConfigurationSettingType.subclass(*args_, **kwargs_)
        else:
            return ConfigurationSettingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Item_Name(self): return self.Item_Name
    def set_Item_Name(self, Item_Name): self.Item_Name = Item_Name
    def get_Item_Value(self): return self.Item_Value
    def set_Item_Value(self, Item_Value): self.Item_Value = Item_Value
    def get_Item_Type(self): return self.Item_Type
    def set_Item_Type(self, Item_Type): self.Item_Type = Item_Type
    def get_Item_Description(self): return self.Item_Description
    def set_Item_Description(self, Item_Description): self.Item_Description = Item_Description
    def hasContent_(self):
        if (
            self.Item_Name is not None or
            self.Item_Value is not None or
            self.Item_Type is not None or
            self.Item_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ConfigurationSettingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ConfigurationSettingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ConfigurationSettingType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ConfigurationSettingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Item_Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sItem_Name>%s</%sItem_Name>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Item_Name), input_name='Item_Name'), 'cyboxCommon:', eol_))
        if self.Item_Value is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sItem_Value>%s</%sItem_Value>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Item_Value), input_name='Item_Value'), 'cyboxCommon:', eol_))
        if self.Item_Type is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sItem_Type>%s</%sItem_Type>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Item_Type), input_name='Item_Type'), 'cyboxCommon:', eol_))
        if self.Item_Description is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sItem_Description>%s</%sItem_Description>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Item_Description), input_name='Item_Description'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Item_Name':
            Item_Name_ = child_.text
            Item_Name_ = self.gds_validate_string(Item_Name_, node, 'Item_Name')
            self.Item_Name = Item_Name_
        elif nodeName_ == 'Item_Value':
            Item_Value_ = child_.text
            Item_Value_ = self.gds_validate_string(Item_Value_, node, 'Item_Value')
            self.Item_Value = Item_Value_
        elif nodeName_ == 'Item_Type':
            Item_Type_ = child_.text
            Item_Type_ = self.gds_validate_string(Item_Type_, node, 'Item_Type')
            self.Item_Type = Item_Type_
        elif nodeName_ == 'Item_Description':
            Item_Description_ = child_.text
            Item_Description_ = self.gds_validate_string(Item_Description_, node, 'Item_Description')
            self.Item_Description = Item_Description_
# end class ConfigurationSettingType

class DependenciesType(GeneratedsSuper):
    """The DependenciesType contains information describing a set of
    dependencies for this tool."""

    subclass = None
    superclass = None
    def __init__(self, Dependency=None):
        if Dependency is None:
            self.Dependency = []
        else:
            self.Dependency = Dependency
    def factory(*args_, **kwargs_):
        if DependenciesType.subclass:
            return DependenciesType.subclass(*args_, **kwargs_)
        else:
            return DependenciesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Dependency(self): return self.Dependency
    def set_Dependency(self, Dependency): self.Dependency = Dependency
    def add_Dependency(self, value): self.Dependency.append(value)
    def insert_Dependency(self, index, value): self.Dependency[index] = value
    def hasContent_(self):
        if (
            self.Dependency
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DependenciesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DependenciesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DependenciesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DependenciesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Dependency_ in self.Dependency:
            Dependency_.export(lwrite, level, 'cyboxCommon:', name_='Dependency', pretty_print=pretty_print)
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
        if nodeName_ == 'Dependency':
            obj_ = DependencyType.factory()
            obj_.build(child_)
            self.Dependency.append(obj_)
# end class DependenciesType

class DependencyType(GeneratedsSuper):
    """The DependencyType contains information describing a single
    dependency for this tool."""

    subclass = None
    superclass = None
    def __init__(self, Dependency_Type=None, Dependency_Description=None):
        self.Dependency_Type = Dependency_Type
        self.Dependency_Description = Dependency_Description
    def factory(*args_, **kwargs_):
        if DependencyType.subclass:
            return DependencyType.subclass(*args_, **kwargs_)
        else:
            return DependencyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Dependency_Type(self): return self.Dependency_Type
    def set_Dependency_Type(self, Dependency_Type): self.Dependency_Type = Dependency_Type
    def get_Dependency_Description(self): return self.Dependency_Description
    def set_Dependency_Description(self, Dependency_Description): self.Dependency_Description = Dependency_Description
    def hasContent_(self):
        if (
            self.Dependency_Type is not None or
            self.Dependency_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DependencyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DependencyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DependencyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DependencyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Dependency_Type is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDependency_Type>%s</%sDependency_Type>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Dependency_Type), input_name='Dependency_Type'), 'cyboxCommon:', eol_))
        if self.Dependency_Description is not None:
            self.Dependency_Description.export(lwrite, level, 'cyboxCommon:', name_='Dependency_Description', pretty_print=pretty_print)
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
        if nodeName_ == 'Dependency_Type':
            Dependency_Type_ = child_.text
            Dependency_Type_ = self.gds_validate_string(Dependency_Type_, node, 'Dependency_Type')
            self.Dependency_Type = Dependency_Type_
        elif nodeName_ == 'Dependency_Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Dependency_Description(obj_)
# end class DependencyType

class UsageContextAssumptionsType(GeneratedsSuper):
    """The UsageContextAssumptionsType contains descriptions of the various
    relevant usage context assumptions for this tool"""

    subclass = None
    superclass = None
    def __init__(self, Usage_Context_Assumption=None):
        if Usage_Context_Assumption is None:
            self.Usage_Context_Assumption = []
        else:
            self.Usage_Context_Assumption = Usage_Context_Assumption
    def factory(*args_, **kwargs_):
        if UsageContextAssumptionsType.subclass:
            return UsageContextAssumptionsType.subclass(*args_, **kwargs_)
        else:
            return UsageContextAssumptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Usage_Context_Assumption(self): return self.Usage_Context_Assumption
    def set_Usage_Context_Assumption(self, Usage_Context_Assumption): self.Usage_Context_Assumption = Usage_Context_Assumption
    def add_Usage_Context_Assumption(self, value): self.Usage_Context_Assumption.append(value)
    def insert_Usage_Context_Assumption(self, index, value): self.Usage_Context_Assumption[index] = value
    def hasContent_(self):
        if (
            self.Usage_Context_Assumption
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='UsageContextAssumptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UsageContextAssumptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='UsageContextAssumptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='UsageContextAssumptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Usage_Context_Assumption_ in self.Usage_Context_Assumption:
            Usage_Context_Assumption_.export(lwrite, level, 'cyboxCommon:', name_='Usage_Context_Assumption', pretty_print=pretty_print)
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
        if nodeName_ == 'Usage_Context_Assumption':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.Usage_Context_Assumption.append(obj_)
# end class UsageContextAssumptionsType

class InternationalizationSettingsType(GeneratedsSuper):
    """The InternationalizationSettingsType contains information describing
    relevant internationalization setting for this tool"""

    subclass = None
    superclass = None
    def __init__(self, Internal_Strings=None):
        if Internal_Strings is None:
            self.Internal_Strings = []
        else:
            self.Internal_Strings = Internal_Strings
    def factory(*args_, **kwargs_):
        if InternationalizationSettingsType.subclass:
            return InternationalizationSettingsType.subclass(*args_, **kwargs_)
        else:
            return InternationalizationSettingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Internal_Strings(self): return self.Internal_Strings
    def set_Internal_Strings(self, Internal_Strings): self.Internal_Strings = Internal_Strings
    def add_Internal_Strings(self, value): self.Internal_Strings.append(value)
    def insert_Internal_Strings(self, index, value): self.Internal_Strings[index] = value
    def hasContent_(self):
        if (
            self.Internal_Strings
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='InternationalizationSettingsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='InternationalizationSettingsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='InternationalizationSettingsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='InternationalizationSettingsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Internal_Strings_ in self.Internal_Strings:
            Internal_Strings_.export(lwrite, level, 'cyboxCommon:', name_='Internal_Strings', pretty_print=pretty_print)
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
        if nodeName_ == 'Internal_Strings':
            obj_ = InternalStringsType.factory()
            obj_.build(child_)
            self.Internal_Strings.append(obj_)
# end class InternationalizationSettingsType

class InternalStringsType(GeneratedsSuper):
    """The InternalStringsType contains a single internal string instance
    for this internationalization setting instance."""

    subclass = None
    superclass = None
    def __init__(self, Key=None, Content=None):
        self.Key = Key
        self.Content = Content
    def factory(*args_, **kwargs_):
        if InternalStringsType.subclass:
            return InternalStringsType.subclass(*args_, **kwargs_)
        else:
            return InternalStringsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Key(self): return self.Key
    def set_Key(self, Key): self.Key = Key
    def get_Content(self): return self.Content
    def set_Content(self, Content): self.Content = Content
    def hasContent_(self):
        if (
            self.Key is not None or
            self.Content is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='InternalStringsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='InternalStringsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='InternalStringsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='InternalStringsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Key is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sKey>%s</%sKey>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Key), input_name='Key'), 'cyboxCommon:', eol_))
        if self.Content is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sContent>%s</%sContent>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Content), input_name='Content'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Key':
            Key_ = child_.text
            Key_ = self.gds_validate_string(Key_, node, 'Key')
            self.Key = Key_
        elif nodeName_ == 'Content':
            Content_ = child_.text
            Content_ = self.gds_validate_string(Content_, node, 'Content')
            self.Content = Content_
# end class InternalStringsType

class BuildInformationType(GeneratedsSuper):
    """The BuildInformationType contains information describing how this
    tool was built."""
    subclass = None
    superclass = None
    def __init__(self, Build_ID=None, Build_Project=None, Build_Utility=None, Build_Version=None, Build_Label=None, Compilers=None, Compilation_Date=None, Build_Configuration=None, Build_Script=None, Libraries=None, Build_Output_Log=None):
        self.Build_ID = Build_ID
        self.Build_Project = Build_Project
        self.Build_Utility = Build_Utility
        self.Build_Version = Build_Version
        self.Build_Label = Build_Label
        self.Compilers = Compilers
        self.Compilation_Date = Compilation_Date
        self.Build_Configuration = Build_Configuration
        self.Build_Script = Build_Script
        self.Libraries = Libraries
        self.Build_Output_Log = Build_Output_Log
    def factory(*args_, **kwargs_):
        if BuildInformationType.subclass:
            return BuildInformationType.subclass(*args_, **kwargs_)
        else:
            return BuildInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Build_ID(self): return self.Build_ID
    def set_Build_ID(self, Build_ID): self.Build_ID = Build_ID
    def get_Build_Project(self): return self.Build_Project
    def set_Build_Project(self, Build_Project): self.Build_Project = Build_Project
    def get_Build_Utility(self): return self.Build_Utility
    def set_Build_Utility(self, Build_Utility): self.Build_Utility = Build_Utility
    def get_Build_Version(self): return self.Build_Version
    def set_Build_Version(self, Build_Version): self.Build_Version = Build_Version
    def get_Build_Label(self): return self.Build_Label
    def set_Build_Label(self, Build_Label): self.Build_Label = Build_Label
    def get_Compilers(self): return self.Compilers
    def set_Compilers(self, Compilers): self.Compilers = Compilers
    def get_Compilation_Date(self): return self.Compilation_Date
    def set_Compilation_Date(self, Compilation_Date): self.Compilation_Date = Compilation_Date
    def get_Build_Configuration(self): return self.Build_Configuration
    def set_Build_Configuration(self, Build_Configuration): self.Build_Configuration = Build_Configuration
    def get_Build_Script(self): return self.Build_Script
    def set_Build_Script(self, Build_Script): self.Build_Script = Build_Script
    def get_Libraries(self): return self.Libraries
    def set_Libraries(self, Libraries): self.Libraries = Libraries
    def get_Build_Output_Log(self): return self.Build_Output_Log
    def set_Build_Output_Log(self, Build_Output_Log): self.Build_Output_Log = Build_Output_Log
    def hasContent_(self):
        if (
            self.Build_ID is not None or
            self.Build_Project is not None or
            self.Build_Utility is not None or
            self.Build_Version is not None or
            self.Build_Label is not None or
            self.Compilers is not None or
            self.Compilation_Date is not None or
            self.Build_Configuration is not None or
            self.Build_Script is not None or
            self.Libraries is not None or
            self.Build_Output_Log is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildInformationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BuildInformationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='BuildInformationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Build_ID is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_ID>%s</%sBuild_ID>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_ID), input_name='Build_ID'), 'cyboxCommon:', eol_))
        if self.Build_Project is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Project>%s</%sBuild_Project>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Project), input_name='Build_Project'), 'cyboxCommon:', eol_))
        if self.Build_Utility is not None:
            self.Build_Utility.export(lwrite, level, 'cyboxCommon:', name_='Build_Utility', pretty_print=pretty_print)
        if self.Build_Version is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Version>%s</%sBuild_Version>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Version), input_name='Build_Version'), 'cyboxCommon:', eol_))
        if self.Build_Label is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Label>%s</%sBuild_Label>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Label), input_name='Build_Label'), 'cyboxCommon:', eol_))
        if self.Compilers is not None:
            self.Compilers.export(lwrite, level, 'cyboxCommon:', name_='Compilers', pretty_print=pretty_print)
        if self.Compilation_Date is not None:
            self.Compilation_Date.export(lwrite, level, 'cyboxCommon:', name_='Compilation_Date', pretty_print=pretty_print)
        if self.Build_Configuration is not None:
            self.Build_Configuration.export(lwrite, level, 'cyboxCommon:', name_='Build_Configuration', pretty_print=pretty_print)
        if self.Build_Script is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Script>%s</%sBuild_Script>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Script), input_name='Build_Script'), 'cyboxCommon:', eol_))
        if self.Libraries is not None:
            self.Libraries.export(lwrite, level, 'cyboxCommon:', name_='Libraries', pretty_print=pretty_print)
        if self.Build_Output_Log is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Output_Log>%s</%sBuild_Output_Log>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Output_Log), input_name='Build_Output_Log'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Build_ID':
            Build_ID_ = child_.text
            Build_ID_ = self.gds_validate_string(Build_ID_, node, 'Build_ID')
            self.Build_ID = Build_ID_
        elif nodeName_ == 'Build_Project':
            Build_Project_ = child_.text
            Build_Project_ = self.gds_validate_string(Build_Project_, node, 'Build_Project')
            self.Build_Project = Build_Project_
        elif nodeName_ == 'Build_Utility':
            obj_ = BuildUtilityType.factory()
            obj_.build(child_)
            self.set_Build_Utility(obj_)
        elif nodeName_ == 'Build_Version':
            Build_Version_ = child_.text
            Build_Version_ = self.gds_validate_string(Build_Version_, node, 'Build_Version')
            self.Build_Version = Build_Version_
        elif nodeName_ == 'Build_Label':
            Build_Label_ = child_.text
            Build_Label_ = self.gds_validate_string(Build_Label_, node, 'Build_Label')
            self.Build_Label = Build_Label_
        elif nodeName_ == 'Compilers':
            obj_ = CompilersType.factory()
            obj_.build(child_)
            self.set_Compilers(obj_)
        elif nodeName_ == 'Compilation_Date':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Compilation_Date(obj_)
        elif nodeName_ == 'Build_Configuration':
            obj_ = BuildConfigurationType.factory()
            obj_.build(child_)
            self.set_Build_Configuration(obj_)
        elif nodeName_ == 'Build_Script':
            Build_Script_ = child_.text
            Build_Script_ = self.gds_validate_string(Build_Script_, node, 'Build_Script')
            self.Build_Script = Build_Script_
        elif nodeName_ == 'Libraries':
            obj_ = LibrariesType.factory()
            obj_.build(child_)
            self.set_Libraries(obj_)
        elif nodeName_ == 'Build_Output_Log':
            Build_Output_Log_ = child_.text
            Build_Output_Log_ = self.gds_validate_string(Build_Output_Log_, node, 'Build_Output_Log')
            self.Build_Output_Log = Build_Output_Log_
# end class BuildInformationType

class BuildUtilityType(GeneratedsSuper):
    """The BuildUtilityType contains information identifying the utility
    used to build this application."""

    subclass = None
    superclass = None
    def __init__(self, Build_Utility_Name=None, Build_Utility_Platform_Specification=None):
        self.Build_Utility_Name = Build_Utility_Name
        self.Build_Utility_Platform_Specification = Build_Utility_Platform_Specification
    def factory(*args_, **kwargs_):
        if BuildUtilityType.subclass:
            return BuildUtilityType.subclass(*args_, **kwargs_)
        else:
            return BuildUtilityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Build_Utility_Name(self): return self.Build_Utility_Name
    def set_Build_Utility_Name(self, Build_Utility_Name): self.Build_Utility_Name = Build_Utility_Name
    def get_Build_Utility_Platform_Specification(self): return self.Build_Utility_Platform_Specification
    def set_Build_Utility_Platform_Specification(self, Build_Utility_Platform_Specification): self.Build_Utility_Platform_Specification = Build_Utility_Platform_Specification
    def hasContent_(self):
        if (
            self.Build_Utility_Name is not None or
            self.Build_Utility_Platform_Specification is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildUtilityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BuildUtilityType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='BuildUtilityType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildUtilityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Build_Utility_Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBuild_Utility_Name>%s</%sBuild_Utility_Name>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Build_Utility_Name), input_name='Build_Utility_Name'), 'cyboxCommon:', eol_))
        if self.Build_Utility_Platform_Specification is not None:
            self.Build_Utility_Platform_Specification.export(lwrite, level, 'cyboxCommon:', name_='Build_Utility_Platform_Specification', pretty_print=pretty_print)
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
        if nodeName_ == 'Build_Utility_Name':
            Build_Utility_Name_ = child_.text
            Build_Utility_Name_ = self.gds_validate_string(Build_Utility_Name_, node, 'Build_Utility_Name')
            self.Build_Utility_Name = Build_Utility_Name_
        elif nodeName_ == 'Build_Utility_Platform_Specification':
            obj_ = PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Build_Utility_Platform_Specification(obj_)
# end class BuildUtilityType

class CompilersType(GeneratedsSuper):
    """The CompilersType describes the compilers utilized during this build
    of this application."""

    subclass = None
    superclass = None
    def __init__(self, Compiler=None):
        if Compiler is None:
            self.Compiler = []
        else:
            self.Compiler = Compiler
    def factory(*args_, **kwargs_):
        if CompilersType.subclass:
            return CompilersType.subclass(*args_, **kwargs_)
        else:
            return CompilersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Compiler(self): return self.Compiler
    def set_Compiler(self, Compiler): self.Compiler = Compiler
    def add_Compiler(self, value): self.Compiler.append(value)
    def insert_Compiler(self, index, value): self.Compiler[index] = value
    def hasContent_(self):
        if (
            self.Compiler
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilersType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompilersType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CompilersType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Compiler_ in self.Compiler:
            Compiler_.export(lwrite, level, 'cyboxCommon:', name_='Compiler', pretty_print=pretty_print)
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
        if nodeName_ == 'Compiler':
            obj_ = CompilerType.factory()
            obj_.build(child_)
            self.Compiler.append(obj_)
# end class CompilersType

class CompilerType(GeneratedsSuper):
    """The CompilerType describes a single compiler utilized during this
    build of this application."""

    subclass = None
    superclass = None
    def __init__(self, Compiler_Informal_Description=None, Compiler_Platform_Specification=None):
        self.Compiler_Informal_Description = Compiler_Informal_Description
        self.Compiler_Platform_Specification = Compiler_Platform_Specification
    def factory(*args_, **kwargs_):
        if CompilerType.subclass:
            return CompilerType.subclass(*args_, **kwargs_)
        else:
            return CompilerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Compiler_Informal_Description(self): return self.Compiler_Informal_Description
    def set_Compiler_Informal_Description(self, Compiler_Informal_Description): self.Compiler_Informal_Description = Compiler_Informal_Description
    def get_Compiler_Platform_Specification(self): return self.Compiler_Platform_Specification
    def set_Compiler_Platform_Specification(self, Compiler_Platform_Specification): self.Compiler_Platform_Specification = Compiler_Platform_Specification
    def hasContent_(self):
        if (
            self.Compiler_Informal_Description is not None or
            self.Compiler_Platform_Specification is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompilerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CompilerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Compiler_Informal_Description is not None:
            self.Compiler_Informal_Description.export(lwrite, level, 'cyboxCommon:', name_='Compiler_Informal_Description', pretty_print=pretty_print)
        if self.Compiler_Platform_Specification is not None:
            self.Compiler_Platform_Specification.export(lwrite, level, 'cyboxCommon:', name_='Compiler_Platform_Specification', pretty_print=pretty_print)
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
        if nodeName_ == 'Compiler_Informal_Description':
            obj_ = CompilerInformalDescriptionType.factory()
            obj_.build(child_)
            self.set_Compiler_Informal_Description(obj_)
        elif nodeName_ == 'Compiler_Platform_Specification':
            obj_ = PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Compiler_Platform_Specification(obj_)
# end class CompilerType

class CompilerInformalDescriptionType(GeneratedsSuper):
    """The CompilerInformalDescriptionType contains the informal
    description of this compiler instance."""

    subclass = None
    superclass = None
    def __init__(self, Compiler_Name=None, Compiler_Version=None):
        self.Compiler_Name = Compiler_Name
        self.Compiler_Version = Compiler_Version
    def factory(*args_, **kwargs_):
        if CompilerInformalDescriptionType.subclass:
            return CompilerInformalDescriptionType.subclass(*args_, **kwargs_)
        else:
            return CompilerInformalDescriptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Compiler_Name(self): return self.Compiler_Name
    def set_Compiler_Name(self, Compiler_Name): self.Compiler_Name = Compiler_Name
    def get_Compiler_Version(self): return self.Compiler_Version
    def set_Compiler_Version(self, Compiler_Version): self.Compiler_Version = Compiler_Version
    def hasContent_(self):
        if (
            self.Compiler_Name is not None or
            self.Compiler_Version is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilerInformalDescriptionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompilerInformalDescriptionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CompilerInformalDescriptionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CompilerInformalDescriptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Compiler_Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sCompiler_Name>%s</%sCompiler_Name>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Compiler_Name), input_name='Compiler_Name'), 'cyboxCommon:', eol_))
        if self.Compiler_Version is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sCompiler_Version>%s</%sCompiler_Version>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Compiler_Version), input_name='Compiler_Version'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Compiler_Name':
            Compiler_Name_ = child_.text
            Compiler_Name_ = self.gds_validate_string(Compiler_Name_, node, 'Compiler_Name')
            self.Compiler_Name = Compiler_Name_
        elif nodeName_ == 'Compiler_Version':
            Compiler_Version_ = child_.text
            Compiler_Version_ = self.gds_validate_string(Compiler_Version_, node, 'Compiler_Version')
            self.Compiler_Version = Compiler_Version_
# end class CompilerInformalDescriptionType

class BuildConfigurationType(GeneratedsSuper):
    """The BuildConfigurationType describes how the build utility was
    configured for this build of this application."""

    subclass = None
    superclass = None
    def __init__(self, Configuration_Setting_Description=None, Configuration_Settings=None):
        self.Configuration_Setting_Description = Configuration_Setting_Description
        self.Configuration_Settings = Configuration_Settings
    def factory(*args_, **kwargs_):
        if BuildConfigurationType.subclass:
            return BuildConfigurationType.subclass(*args_, **kwargs_)
        else:
            return BuildConfigurationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Configuration_Setting_Description(self): return self.Configuration_Setting_Description
    def set_Configuration_Setting_Description(self, Configuration_Setting_Description): self.Configuration_Setting_Description = Configuration_Setting_Description
    def get_Configuration_Settings(self): return self.Configuration_Settings
    def set_Configuration_Settings(self, Configuration_Settings): self.Configuration_Settings = Configuration_Settings
    def hasContent_(self):
        if (
            self.Configuration_Setting_Description is not None or
            self.Configuration_Settings is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildConfigurationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BuildConfigurationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='BuildConfigurationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='BuildConfigurationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Configuration_Setting_Description is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sConfiguration_Setting_Description>%s</%sConfiguration_Setting_Description>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Configuration_Setting_Description), input_name='Configuration_Setting_Description'), 'cyboxCommon:', eol_))
        if self.Configuration_Settings is not None:
            self.Configuration_Settings.export(lwrite, level, 'cyboxCommon:', name_='Configuration_Settings', pretty_print=pretty_print)
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
        if nodeName_ == 'Configuration_Setting_Description':
            Configuration_Setting_Description_ = child_.text
            Configuration_Setting_Description_ = self.gds_validate_string(Configuration_Setting_Description_, node, 'Configuration_Setting_Description')
            self.Configuration_Setting_Description = Configuration_Setting_Description_
        elif nodeName_ == 'Configuration_Settings':
            obj_ = ConfigurationSettingsType.factory()
            obj_.build(child_)
            self.set_Configuration_Settings(obj_)
# end class BuildConfigurationType

class LibrariesType(GeneratedsSuper):
    """The LibrariesType identifies the libraries incorporated into the
    build of the tool."""

    subclass = None
    superclass = None
    def __init__(self, Library=None):
        self.Library = Library
    def factory(*args_, **kwargs_):
        if LibrariesType.subclass:
            return LibrariesType.subclass(*args_, **kwargs_)
        else:
            return LibrariesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Library(self): return self.Library
    def set_Library(self, Library): self.Library = Library
    def hasContent_(self):
        if (
            self.Library is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='LibrariesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LibrariesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='LibrariesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='LibrariesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Library is not None:
            self.Library.export(lwrite, level, 'cyboxCommon:', name_='Library', pretty_print=pretty_print)
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
        if nodeName_ == 'Library':
            obj_ = LibraryType.factory()
            obj_.build(child_)
            self.set_Library(obj_)
# end class LibrariesType

class LibraryType(GeneratedsSuper):
    """The LibraryType identifies a single library incorporated into the
    build of the tool.This field identifies the name of the
    library.This field identifies the version of the library."""

    subclass = None
    superclass = None
    def __init__(self, version=None, name=None):
        self.version = _cast(None, version)
        self.name = _cast(None, name)
        pass
    def factory(*args_, **kwargs_):
        if LibraryType.subclass:
            return LibraryType.subclass(*args_, **kwargs_)
        else:
            return LibraryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='LibraryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LibraryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='LibraryType'):
        if self.version is not None:

            lwrite(' version=%s' % (self.gds_format_string(quote_attrib(self.version), input_name='version'), ))
        if self.name is not None:

            lwrite(' name=%s' % (self.gds_format_string(quote_attrib(self.name), input_name='name'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='LibraryType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None:

            self.version = value
        value = find_attr_value_('name', node)
        if value is not None:

            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class LibraryType

class ExecutionEnvironmentType(GeneratedsSuper):
    """The ExecutionEnvironmentType contains information describing the
    execution environment of the tool."""
    subclass = None
    superclass = None
    def __init__(self, System=None, User_Account_Info=None, Command_Line=None, Start_Time=None):
        self.System = System
        self.User_Account_Info = User_Account_Info
        self.Command_Line = Command_Line
        self.Start_Time = Start_Time
    def factory(*args_, **kwargs_):
        if ExecutionEnvironmentType.subclass:
            return ExecutionEnvironmentType.subclass(*args_, **kwargs_)
        else:
            return ExecutionEnvironmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_System(self): return self.System
    def set_System(self, System): self.System = System
    def get_User_Account_Info(self): return self.User_Account_Info
    def set_User_Account_Info(self, User_Account_Info): self.User_Account_Info = User_Account_Info
    def get_Command_Line(self): return self.Command_Line
    def set_Command_Line(self, Command_Line): self.Command_Line = Command_Line
    def get_Start_Time(self): return self.Start_Time
    def set_Start_Time(self, Start_Time): self.Start_Time = Start_Time
    def hasContent_(self):
        if (
            self.System is not None or
            self.User_Account_Info is not None or
            self.Command_Line is not None or
            self.Start_Time is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ExecutionEnvironmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExecutionEnvironmentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ExecutionEnvironmentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ExecutionEnvironmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.System is not None:
            self.System.export(lwrite, level, 'cyboxCommon:', name_='System', pretty_print=pretty_print)
        if self.User_Account_Info is not None:
            self.User_Account_Info.export(lwrite, level, 'cyboxCommon:', name_='User_Account_Info', pretty_print=pretty_print)
        if self.Command_Line is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sCommand_Line>%s</%sCommand_Line>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Command_Line), input_name='Command_Line'), 'cyboxCommon:', eol_))
        if self.Start_Time is not None:
            self.Start_Time.export(lwrite, level, 'cyboxCommon:', name_='Start_Time', pretty_print=pretty_print)
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
        if nodeName_ == 'System':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <System> element')
            self.set_System(obj_)
        elif nodeName_ == 'User_Account_Info':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <User_Account_Info> element')
            self.set_User_Account_Info(obj_)
        elif nodeName_ == 'Command_Line':
            Command_Line_ = child_.text
            Command_Line_ = self.gds_validate_string(Command_Line_, node, 'Command_Line')
            self.Command_Line = Command_Line_
        elif nodeName_ == 'Start_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Start_Time(obj_)
# end class ExecutionEnvironmentType

class ErrorsType(GeneratedsSuper):
    """The ErrorsType captures any errors generated during the run of the
    tool."""

    subclass = None
    superclass = None
    def __init__(self, Error=None):
        if Error is None:
            self.Error = []
        else:
            self.Error = Error
    def factory(*args_, **kwargs_):
        if ErrorsType.subclass:
            return ErrorsType.subclass(*args_, **kwargs_)
        else:
            return ErrorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Error(self): return self.Error
    def set_Error(self, Error): self.Error = Error
    def add_Error(self, value): self.Error.append(value)
    def insert_Error(self, index, value): self.Error[index] = value
    def hasContent_(self):
        if (
            self.Error
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ErrorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ErrorsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Error_ in self.Error:
            Error_.export(lwrite, level, 'cyboxCommon:', name_='Error', pretty_print=pretty_print)
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
        if nodeName_ == 'Error':
            obj_ = ErrorType.factory()
            obj_.build(child_)
            self.Error.append(obj_)
# end class ErrorsType

class ErrorType(GeneratedsSuper):
    """The ErrorType captures a single error generated during the run of
    the tool."""

    subclass = None
    superclass = None
    def __init__(self, Error_Type=None, Error_Count=None, Error_Instances=None):
        self.Error_Type = Error_Type
        self.Error_Count = Error_Count
        self.Error_Instances = Error_Instances
    def factory(*args_, **kwargs_):
        if ErrorType.subclass:
            return ErrorType.subclass(*args_, **kwargs_)
        else:
            return ErrorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Error_Type(self): return self.Error_Type
    def set_Error_Type(self, Error_Type): self.Error_Type = Error_Type
    def get_Error_Count(self): return self.Error_Count
    def set_Error_Count(self, Error_Count): self.Error_Count = Error_Count
    def get_Error_Instances(self): return self.Error_Instances
    def set_Error_Instances(self, Error_Instances): self.Error_Instances = Error_Instances
    def hasContent_(self):
        if (
            self.Error_Type is not None or
            self.Error_Count is not None or
            self.Error_Instances is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ErrorType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ErrorType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Error_Type is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sError_Type>%s</%sError_Type>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Error_Type), input_name='Error_Type'), 'cyboxCommon:', eol_))
        if self.Error_Count is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sError_Count>%s</%sError_Count>%s' % ('cyboxCommon:', self.gds_format_integer(self.Error_Count, input_name='Error_Count'), 'cyboxCommon:', eol_))
        if self.Error_Instances is not None:
            self.Error_Instances.export(lwrite, level, 'cyboxCommon:', name_='Error_Instances', pretty_print=pretty_print)
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
        if nodeName_ == 'Error_Type':
            Error_Type_ = child_.text
            Error_Type_ = self.gds_validate_string(Error_Type_, node, 'Error_Type')
            self.Error_Type = Error_Type_
        elif nodeName_ == 'Error_Count':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError) as exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'Error_Count')
            self.Error_Count = ival_
        elif nodeName_ == 'Error_Instances':
            obj_ = ErrorInstancesType.factory()
            obj_.build(child_)
            self.set_Error_Instances(obj_)
# end class ErrorType

class ErrorInstancesType(GeneratedsSuper):
    """The ErrorInstancesType captures the actual error output for each
    instance of this type of error."""

    subclass = None
    superclass = None
    def __init__(self, Error_Instance=None):
        if Error_Instance is None:
            self.Error_Instance = []
        else:
            self.Error_Instance = Error_Instance
    def factory(*args_, **kwargs_):
        if ErrorInstancesType.subclass:
            return ErrorInstancesType.subclass(*args_, **kwargs_)
        else:
            return ErrorInstancesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Error_Instance(self): return self.Error_Instance
    def set_Error_Instance(self, Error_Instance): self.Error_Instance = Error_Instance
    def add_Error_Instance(self, value): self.Error_Instance.append(value)
    def insert_Error_Instance(self, index, value): self.Error_Instance[index] = value
    def hasContent_(self):
        if (
            self.Error_Instance
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorInstancesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ErrorInstancesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ErrorInstancesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ErrorInstancesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Error_Instance_ in self.Error_Instance:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sError_Instance>%s</%sError_Instance>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(Error_Instance_), input_name='Error_Instance'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Error_Instance':
            Error_Instance_ = child_.text
            Error_Instance_ = self.gds_validate_string(Error_Instance_, node, 'Error_Instance')
            self.Error_Instance.append(Error_Instance_)
# end class ErrorInstancesType

class ObjectPropertiesType(GeneratedsSuper):
    """The ObjectPropertiesType is an Abstract type placeholder within the
    CybOX schema enabling the inclusion of contextually varying
    object properties descriptions. This Abstract type is leveraged
    as the extension base for all predefined CybOX object properties
    schemas. Through this extension mechanism any object instance
    data based on an object properties schema extended from
    ObjectPropertiesType (e.g. File_Object, Address_Object, etc.)
    can be directly integrated into any instance document where a
    field is defined as ObjectPropertiesType. For flexibility and
    extensibility purposes any user of CybOX can specify their own
    externally defined object properties schemas (outside of or
    derived from the set of predefined objects) extended from
    ObjectPropertiesType and utilize them as part of their CybOX
    content.The object_reference field specifies a unique ID
    reference to an Object defined elsewhere. This construct allows
    for the re-use of the defined Properties of one Object within
    another, without the need to embed the full Object in the
    location from which it is being referenced. Thus, this ID
    reference is intended to resolve to the Properties of the Object
    that it points to."""

    subclass = None
    superclass = None
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None):
        self.object_reference = _cast(None, object_reference)
        self.Custom_Properties = Custom_Properties
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if ObjectPropertiesType.subclass:
            return ObjectPropertiesType.subclass(*args_, **kwargs_)
        else:
            return ObjectPropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Custom_Properties(self): return self.Custom_Properties
    def set_Custom_Properties(self, Custom_Properties): self.Custom_Properties = Custom_Properties
    def get_object_reference(self): return self.object_reference
    def set_object_reference(self, object_reference): self.object_reference = object_reference
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (
            self.Custom_Properties is not None or
            self.object_reference is not None or
            self.xsi_type is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ObjectPropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ObjectPropertiesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ObjectPropertiesType'):
        if self.object_reference is not None:

            lwrite(' object_reference=%s' % (quote_attrib(self.object_reference), ))
        if self.xsi_type is not None:

            lwrite(' xsi:type="%s"' % self.xsi_type)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ObjectPropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Custom_Properties is not None:
            self.Custom_Properties.export(lwrite, level, 'cyboxCommon:', name_='Custom_Properties', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('object_reference', node)
        if value is not None:

            self.object_reference = value
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.xsi_type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Custom_Properties':
            obj_ = CustomPropertiesType.factory()
            obj_.build(child_)
            self.set_Custom_Properties(obj_)
# end class ObjectPropertiesType

class CustomPropertiesType(GeneratedsSuper):
    """The CustomPropertiesType enables the specification of a set of
    custom Object Properties that may not be defined in existing
    Properties schemas."""

    subclass = None
    superclass = None
    def __init__(self, Property=None):
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
    def factory(*args_, **kwargs_):
        if CustomPropertiesType.subclass:
            return CustomPropertiesType.subclass(*args_, **kwargs_)
        else:
            return CustomPropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Property(self): return self.Property
    def set_Property(self, Property): self.Property = Property
    def add_Property(self, value): self.Property.append(value)
    def insert_Property(self, index, value): self.Property[index] = value
    def hasContent_(self):
        if (
            self.Property
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CustomPropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CustomPropertiesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CustomPropertiesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CustomPropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            Property_.export(lwrite, level, 'cyboxCommon:', name_='Property', pretty_print=pretty_print)
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
        if nodeName_ == 'Property':
            obj_ = PropertyType.factory()
            obj_.build(child_)
            self.Property.append(obj_)
# end class CustomPropertiesType

class BaseObjectPropertyType(GeneratedsSuper):
    """The BaseObjectPropertyType is a type representing a common typing
    foundation for the specification of a single Object
    Property.Properties that use this type can express multiple
    values by providing them using a delimiter-separated list. The
    default delimiter is '##comma##' (no quotes) but can be
    overridden through use of the delimiter field. Note that
    whitespace is preserved and so, when specifying a list of
    values, do not include a space following the delimiter in a list
    unless the first character of the next list item should, in
    fact, be a space."""
    subclass = None
    superclass = None
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        self.obfuscation_algorithm_ref = _cast(None, obfuscation_algorithm_ref)
        self.refanging_transform_type = _cast(None, refanging_transform_type)
        self.has_changed = _cast(bool, has_changed)
        self.delimiter = _cast(None, delimiter)
        self.pattern_type = _cast(None, pattern_type)
        self.datatype = _cast(None, datatype)
        self.refanging_transform = _cast(None, refanging_transform)
        self.is_case_sensitive = _cast(bool, is_case_sensitive)
        self.bit_mask = _cast(None, bit_mask)
        self.appears_random = _cast(bool, appears_random)
        self.observed_encoding = _cast(None, observed_encoding)
        self.defanging_algorithm_ref = _cast(None, defanging_algorithm_ref)
        self.is_obfuscated = _cast(bool, is_obfuscated)
        self.regex_syntax = _cast(None, regex_syntax)
        self.apply_condition = _cast(None, apply_condition)
        self.trend = _cast(bool, trend)
        self.idref = _cast(None, idref)
        self.is_defanged = _cast(bool, is_defanged)
        self.id = _cast(None, id)
        self.condition = _cast(None, condition)
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if BaseObjectPropertyType.subclass:
            return BaseObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return BaseObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_obfuscation_algorithm_ref(self): return self.obfuscation_algorithm_ref
    def set_obfuscation_algorithm_ref(self, obfuscation_algorithm_ref): self.obfuscation_algorithm_ref = obfuscation_algorithm_ref
    def get_refanging_transform_type(self): return self.refanging_transform_type
    def set_refanging_transform_type(self, refanging_transform_type): self.refanging_transform_type = refanging_transform_type
    def get_has_changed(self): return self.has_changed
    def set_has_changed(self, has_changed): self.has_changed = has_changed
    def get_delimiter(self): return self.delimiter
    def set_delimiter(self, delimiter): self.delimiter = delimiter
    def get_pattern_type(self): return self.pattern_type
    def set_pattern_type(self, pattern_type): self.pattern_type = pattern_type
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_refanging_transform(self): return self.refanging_transform
    def set_refanging_transform(self, refanging_transform): self.refanging_transform = refanging_transform
    def get_is_case_sensitive(self): return self.is_case_sensitive
    def set_is_case_sensitive(self, is_case_sensitive): self.is_case_sensitive = is_case_sensitive
    def get_bit_mask(self): return self.bit_mask
    def set_bit_mask(self, bit_mask): self.bit_mask = bit_mask
    def get_appears_random(self): return self.appears_random
    def set_appears_random(self, appears_random): self.appears_random = appears_random
    def get_observed_encoding(self): return self.observed_encoding
    def set_observed_encoding(self, observed_encoding): self.observed_encoding = observed_encoding
    def get_defanging_algorithm_ref(self): return self.defanging_algorithm_ref
    def set_defanging_algorithm_ref(self, defanging_algorithm_ref): self.defanging_algorithm_ref = defanging_algorithm_ref
    def get_is_obfuscated(self): return self.is_obfuscated
    def set_is_obfuscated(self, is_obfuscated): self.is_obfuscated = is_obfuscated
    def get_regex_syntax(self): return self.regex_syntax
    def set_regex_syntax(self, regex_syntax): self.regex_syntax = regex_syntax
    def get_apply_condition(self): return self.apply_condition
    def set_apply_condition(self, apply_condition): self.apply_condition = apply_condition
    def get_trend(self): return self.trend
    def set_trend(self, trend): self.trend = trend
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_is_defanged(self): return self.is_defanged
    def set_is_defanged(self, is_defanged): self.is_defanged = is_defanged
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_condition(self): return self.condition
    def set_condition(self, condition): self.condition = condition
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='BaseObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BaseObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='BaseObjectPropertyType'):
        if self.obfuscation_algorithm_ref is not None:

            lwrite(' obfuscation_algorithm_ref=%s' % (self.gds_format_string(quote_attrib(self.obfuscation_algorithm_ref), input_name='obfuscation_algorithm_ref'), ))
        if self.refanging_transform_type is not None:

            lwrite(' refanging_transform_type=%s' % (self.gds_format_string(quote_attrib(self.refanging_transform_type), input_name='refanging_transform_type'), ))
        if self.has_changed is not None:

            lwrite(' has_changed="%s"' % self.gds_format_boolean(self.has_changed, input_name='has_changed'))
        if self.delimiter not in (None, "##comma##"):

            lwrite(' delimiter=%s' % (self.gds_format_string(quote_attrib(self.delimiter), input_name='delimiter'), ))
        if self.pattern_type is not None:

            lwrite(' pattern_type=%s' % (quote_attrib(self.pattern_type), ))
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
        if self.refanging_transform is not None:

            lwrite(' refanging_transform=%s' % (self.gds_format_string(quote_attrib(self.refanging_transform), input_name='refanging_transform'), ))
        if self.is_case_sensitive not in (None, True):

            lwrite(' is_case_sensitive="%s"' % self.gds_format_boolean(self.is_case_sensitive, input_name='is_case_sensitive'))
        if self.bit_mask is not None:

            lwrite(' bit_mask=%s' % (self.gds_format_string(quote_attrib(self.bit_mask), input_name='bit_mask'), ))
        if self.appears_random is not None:

            lwrite(' appears_random="%s"' % self.gds_format_boolean(self.appears_random, input_name='appears_random'))
        if self.observed_encoding is not None:

            lwrite(' observed_encoding=%s' % (self.gds_format_string(quote_attrib(self.observed_encoding), input_name='observed_encoding'), ))
        if self.defanging_algorithm_ref is not None:

            lwrite(' defanging_algorithm_ref=%s' % (self.gds_format_string(quote_attrib(self.defanging_algorithm_ref), input_name='defanging_algorithm_ref'), ))
        if self.is_obfuscated is not None:

            lwrite(' is_obfuscated="%s"' % self.gds_format_boolean(self.is_obfuscated, input_name='is_obfuscated'))
        if self.regex_syntax is not None:

            lwrite(' regex_syntax=%s' % (self.gds_format_string(quote_attrib(self.regex_syntax), input_name='regex_syntax'), ))
        if self.trend is not None:

            lwrite(' trend="%s"' % self.gds_format_boolean(self.trend, input_name='trend'))
        if self.idref is not None:

            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.is_defanged is not None:

            lwrite(' is_defanged="%s"' % self.gds_format_boolean(self.is_defanged, input_name='is_defanged'))
        if self.id is not None:

            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.condition is not None:

            lwrite(' condition=%s' % (quote_attrib(self.condition), ))
            if self.apply_condition is not None and (self.delimiter is not None and self.delimiter in self.valueOf_):

                lwrite(' apply_condition=%s' % (quote_attrib(self.apply_condition), ))
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='BaseObjectPropertyType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('obfuscation_algorithm_ref', node)
        if value is not None:

            self.obfuscation_algorithm_ref = value
        value = find_attr_value_('refanging_transform_type', node)
        if value is not None:

            self.refanging_transform_type = value
        value = find_attr_value_('has_changed', node)
        if value is not None:

            if value in ('true', '1'):
                self.has_changed = True
            elif value in ('false', '0'):
                self.has_changed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('delimiter', node)
        if value is not None:

            self.delimiter = value
        value = find_attr_value_('pattern_type', node)
        if value is not None:

            self.pattern_type = value
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        value = find_attr_value_('refanging_transform', node)
        if value is not None:

            self.refanging_transform = value
        value = find_attr_value_('is_case_sensitive', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_case_sensitive = True
            elif value in ('false', '0'):
                self.is_case_sensitive = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('bit_mask', node)
        if value is not None:

            self.bit_mask = value
        value = find_attr_value_('appears_random', node)
        if value is not None:

            if value in ('true', '1'):
                self.appears_random = True
            elif value in ('false', '0'):
                self.appears_random = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('observed_encoding', node)
        if value is not None:

            self.observed_encoding = value
        value = find_attr_value_('defanging_algorithm_ref', node)
        if value is not None:

            self.defanging_algorithm_ref = value
        value = find_attr_value_('is_obfuscated', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_obfuscated = True
            elif value in ('false', '0'):
                self.is_obfuscated = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('regex_syntax', node)
        if value is not None:

            self.regex_syntax = value
        value = find_attr_value_('apply_condition', node)
        if value is not None:

            self.apply_condition = value
        value = find_attr_value_('trend', node)
        if value is not None:

            if value in ('true', '1'):
                self.trend = True
            elif value in ('false', '0'):
                self.trend = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('idref', node)
        if value is not None:

            self.idref = value
        value = find_attr_value_('is_defanged', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_defanged = True
            elif value in ('false', '0'):
                self.is_defanged = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('id', node)
        if value is not None:

            self.id = value
        value = find_attr_value_('condition', node)
        if value is not None:

            self.condition = value
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BaseObjectPropertyType

class DateObjectPropertyRestrictionType(BaseObjectPropertyType):
    """This type is an intermediate type to allow for the addition of the
    precision attribute to DateObjectPropertyType. It should not be
    used directly.This attribute is optional and specifies the type
    of the value of the specified property. If a type different than
    the default is used, it MUST be specified here."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='date', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DateObjectPropertyRestrictionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if DateObjectPropertyRestrictionType.subclass:
            return DateObjectPropertyRestrictionType.subclass(*args_, **kwargs_)
        else:
            return DateObjectPropertyRestrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DateObjectPropertyRestrictionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateObjectPropertyRestrictionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateObjectPropertyRestrictionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateObjectPropertyRestrictionType'):
        super(DateObjectPropertyRestrictionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DateObjectPropertyRestrictionType')
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateObjectPropertyRestrictionType', fromsubclass_=False, pretty_print=True):
        super(DateObjectPropertyRestrictionType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
        super(DateObjectPropertyRestrictionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateObjectPropertyRestrictionType

class DateObjectPropertyType(DateObjectPropertyRestrictionType):
    """The DateObjectPropertyType is a type (extended from
    BaseObjectPropertyType) representing the specification of a
    single Object property whose core value is of type Date. This
    type will be assigned to any property of a CybOX object that
    should contain content of type Date and enables the use of
    relevant metadata for the property. In order to avoid ambiguity,
    it is strongly suggested that any date representation in this
    field include a timezone if it is known. As with the rest of the
    field, this should be formatted per the xs:date
    specification.Properties that use this type can express multiple
    values by providing them using a delimiter-separated list. The
    default delimiter is '##comma##' (no quotes) but can be
    overridden through use of the delimiter field. Note that
    whitespace is preserved and so, when specifying a list of
    values, do not include a space following the delimiter in a list
    unless the first character of the next list item should, in
    fact, be a space.For fields of this type using CybOX patterning,
    it is strongly suggested that the condition (pattern type) is
    limited to one of Equals, DoesNotEqual, GreaterThan, LessThan,
    GreaterThanOrEqual, LessThanOrEqual, ExclusiveBetween, or
    InclusiveBetween. The use of other conditions may lead to
    ambiguity or unexpected results. When evaluating data against a
    pattern, the evaluator should take into account the precision of
    the field (as given by the precision attribute) and any timezone
    information that is available to perform a data-aware
    comparison. The usage of simple string comparisons is
    discouraged due to ambiguities in how precision and timezone
    information is processed.The precision of the associated time.
    If omitted, the default is "day", meaning the full field value.
    Digits in the date that are required by the xs:date datatype but
    are beyond the specified precision should be zeroed out.When
    used in conjunction with CybOX patterning, the pattern should
    only be evaluated against the target up to the given precision."""
    subclass = None
    superclass = DateObjectPropertyRestrictionType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='date', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, precision='day'):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DateObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.precision = _cast(None, precision)
    def factory(*args_, **kwargs_):
        if DateObjectPropertyType.subclass:
            return DateObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return DateObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DateObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateObjectPropertyType'):
        super(DateObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DateObjectPropertyType')
        if self.precision not in (None, 'second'):

            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(DateObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('precision', node)
        if value is not None:

            self.precision = value
        super(DateObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateObjectPropertyType

class DateTimeObjectPropertyRestrictionType(BaseObjectPropertyType):
    """This type is an intermediate type to allow for the addition of the
    precision attribute to DateTimeObjectPropertyType. It should not
    be used directly.This attribute is optional and specifies the
    type of the value of the specified property. If a type different
    than the default is used, it MUST be specified here."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='dateTime', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DateTimeObjectPropertyRestrictionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if DateTimeObjectPropertyRestrictionType.subclass:
            return DateTimeObjectPropertyRestrictionType.subclass(*args_, **kwargs_)
        else:
            return DateTimeObjectPropertyRestrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DateTimeObjectPropertyRestrictionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyRestrictionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeObjectPropertyRestrictionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyRestrictionType'):
        super(DateTimeObjectPropertyRestrictionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeObjectPropertyRestrictionType')
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyRestrictionType', fromsubclass_=False, pretty_print=True):
        super(DateTimeObjectPropertyRestrictionType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
        super(DateTimeObjectPropertyRestrictionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateTimeObjectPropertyRestrictionType

class DateTimeObjectPropertyType(DateTimeObjectPropertyRestrictionType):
    """The DateTimeObjectPropertyType is a type (extended from
    BaseObjectPropertyType) representing the specification of a
    single Object property whose core value is of type DateTime.
    This type will be assigned to any property of a CybOX object
    that should contain content of type DateTime and enables the use
    of relevant metadata for the property. In order to avoid
    ambiguity, it is strongly suggested that any dateTime
    representation in this field include a timezone. As with the
    rest of the field, this should be formatted per the xs:dateTime
    specification.Properties that use this type can express multiple
    values by providing them using a delimiter-separated list. The
    default delimiter is '##comma##' (no quotes) but can be
    overridden through use of the delimiter field. Note that
    whitespace is preserved and so, when specifying a list of
    values, do not include a space following the delimiter in a list
    unless the first character of the next list item should, in
    fact, be a space.For fields of this type using CybOX patterning,
    it is strongly suggested that the condition (pattern type) is
    limited to one of Equals, DoesNotEqual, GreaterThan, LessThan,
    GreaterThanOrEqual, LessThanOrEqual, ExclusiveBetween, or
    InclusiveBetween. The use of other conditions may lead to
    ambiguity or unexpected results. When evaluating data against a
    pattern, the evaluator should take into account the precision of
    the field (as given by the precision attribute) and any timezone
    information that is available to perform a data-aware
    comparison. The usage of simple string comparisons is
    discouraged due to ambiguities in how precision and timezone
    information is processed.The precision of the associated time.
    If omitted, the default is "second", meaning the full field
    value (including fractional seconds). Digits in the dateTime
    that are required by the xs:dateTime datatype but are beyond the
    specified precision should be zeroed out.When used in
    conjunction with CybOX patterning, the pattern should only be
    evaluated against the target up to the given precision."""
    subclass = None
    superclass = DateTimeObjectPropertyRestrictionType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='dateTime', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, precision='second'):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DateTimeObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.precision = _cast(None, precision)
    def factory(*args_, **kwargs_):
        if DateTimeObjectPropertyType.subclass:
            return DateTimeObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return DateTimeObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DateTimeObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyType'):
        super(DateTimeObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeObjectPropertyType')
        if self.precision not in (None, 'second'):

            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DateTimeObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(DateTimeObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('precision', node)
        if value is not None:

            self.precision = value
        super(DateTimeObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateTimeObjectPropertyType

class IntegerObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='int', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(IntegerObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if IntegerObjectPropertyType.subclass:
            return IntegerObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return IntegerObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IntegerObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='IntegerObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IntegerObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='IntegerObjectPropertyType'):
        super(IntegerObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IntegerObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='IntegerObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(IntegerObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(IntegerObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IntegerObjectPropertyType

class StringObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(StringObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if StringObjectPropertyType.subclass:
            return StringObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return StringObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(StringObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='StringObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
            #lwrite('    ' * level)
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StringObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='StringObjectPropertyType'):
        super(StringObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='StringObjectPropertyType')
        if self.extensiontype_ is not None:
            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='StringObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(StringObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None:
            self.extensiontype_ = value
        super(StringObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class StringObjectPropertyType

class NameObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='name', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(NameObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if NameObjectPropertyType.subclass:
            return NameObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return NameObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NameObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='NameObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NameObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='NameObjectPropertyType'):
        super(NameObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NameObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='NameObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(NameObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(NameObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NameObjectPropertyType



class FloatObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='float', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(FloatObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if FloatObjectPropertyType.subclass:
            return FloatObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return FloatObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            str(self.valueOf_) == '0' or
            str(self.valueOf_) == '0.0' or
            self.valueOf_ or
            super(FloatObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='FloatObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FloatObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='FloatObjectPropertyType'):
        super(FloatObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='FloatObjectPropertyType')

    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='FloatObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(FloatObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(FloatObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class FloatObjectPropertyType

class DoubleObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='double', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DoubleObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if DoubleObjectPropertyType.subclass:
            return DoubleObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return DoubleObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            str(self.valueOf_) == '0' or
            str(self.valueOf_) == '0.0' or
            self.valueOf_ or
            super(DoubleObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DoubleObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DoubleObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DoubleObjectPropertyType'):
        super(DoubleObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DoubleObjectPropertyType')

    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DoubleObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(DoubleObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(DoubleObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DoubleObjectPropertyType

class UnsignedLongObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='unsignedLong', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(UnsignedLongObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if UnsignedLongObjectPropertyType.subclass:
            return UnsignedLongObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return UnsignedLongObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(UnsignedLongObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='UnsignedLongObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnsignedLongObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='UnsignedLongObjectPropertyType'):
        super(UnsignedLongObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnsignedLongObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='UnsignedLongObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(UnsignedLongObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(UnsignedLongObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class UnsignedLongObjectPropertyType

class UnsignedIntegerObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='unsignedInt', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(UnsignedIntegerObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if UnsignedIntegerObjectPropertyType.subclass:
            return UnsignedIntegerObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return UnsignedIntegerObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(UnsignedIntegerObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='UnsignedIntegerObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnsignedIntegerObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='UnsignedIntegerObjectPropertyType'):
        super(UnsignedIntegerObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnsignedIntegerObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='UnsignedIntegerObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(UnsignedIntegerObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(UnsignedIntegerObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class UnsignedIntegerObjectPropertyType

class PositiveIntegerObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='positiveInteger', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(PositiveIntegerObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if PositiveIntegerObjectPropertyType.subclass:
            return PositiveIntegerObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return PositiveIntegerObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PositiveIntegerObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PositiveIntegerObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PositiveIntegerObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PositiveIntegerObjectPropertyType'):
        super(PositiveIntegerObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PositiveIntegerObjectPropertyType')

    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PositiveIntegerObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(PositiveIntegerObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(PositiveIntegerObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PositiveIntegerObjectPropertyType

class HexBinaryObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='hexBinary', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(HexBinaryObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if HexBinaryObjectPropertyType.subclass:
            return HexBinaryObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return HexBinaryObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(HexBinaryObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HexBinaryObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HexBinaryObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HexBinaryObjectPropertyType'):
        super(HexBinaryObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='HexBinaryObjectPropertyType')

        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HexBinaryObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(HexBinaryObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
        super(HexBinaryObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class HexBinaryObjectPropertyType

class LongObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='long', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(LongObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if LongObjectPropertyType.subclass:
            return LongObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return LongObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(LongObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='LongObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LongObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='LongObjectPropertyType'):
        super(LongObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='LongObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='LongObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(LongObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(LongObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class LongObjectPropertyType

class NonNegativeIntegerObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='nonNegativeInteger', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(NonNegativeIntegerObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if NonNegativeIntegerObjectPropertyType.subclass:
            return NonNegativeIntegerObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return NonNegativeIntegerObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NonNegativeIntegerObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='NonNegativeIntegerObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NonNegativeIntegerObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='NonNegativeIntegerObjectPropertyType'):
        super(NonNegativeIntegerObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NonNegativeIntegerObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='NonNegativeIntegerObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(NonNegativeIntegerObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(NonNegativeIntegerObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NonNegativeIntegerObjectPropertyType

class AnyURIObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='anyURI', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(AnyURIObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if AnyURIObjectPropertyType.subclass:
            return AnyURIObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return AnyURIObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(AnyURIObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='AnyURIObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AnyURIObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='AnyURIObjectPropertyType'):
        super(AnyURIObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AnyURIObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='AnyURIObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(AnyURIObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(AnyURIObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AnyURIObjectPropertyType

class DurationObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='duration', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DurationObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if DurationObjectPropertyType.subclass:
            return DurationObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return DurationObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DurationObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DurationObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DurationObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DurationObjectPropertyType'):
        super(DurationObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DurationObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DurationObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(DurationObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(DurationObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DurationObjectPropertyType

class TimeObjectPropertyRestrictionType(BaseObjectPropertyType):
    """This type is an intermediate type to allow for the addition of the
    precision attribute to TimeObjectPropertyType. It should not be
    used directly.This attribute is optional and specifies the type
    of the value of the specified property. If a type different than
    the default is used, it MUST be specified here."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='time', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(TimeObjectPropertyRestrictionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if TimeObjectPropertyRestrictionType.subclass:
            return TimeObjectPropertyRestrictionType.subclass(*args_, **kwargs_)
        else:
            return TimeObjectPropertyRestrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TimeObjectPropertyRestrictionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeObjectPropertyRestrictionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeObjectPropertyRestrictionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='TimeObjectPropertyRestrictionType'):
        super(TimeObjectPropertyRestrictionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeObjectPropertyRestrictionType')
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeObjectPropertyRestrictionType', fromsubclass_=False, pretty_print=True):
        super(TimeObjectPropertyRestrictionType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
        super(TimeObjectPropertyRestrictionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TimeObjectPropertyRestrictionType

class TimeObjectPropertyType(TimeObjectPropertyRestrictionType):
    """The TimeObjectPropertyType is a type (extended from
    BaseObjectPropertyType) representing the specification of a
    single Object property whose core value is of type time. This
    type will be assigned to any property of a CybOX object that
    should contain content of type Time and enables the use of
    relevant metadata for the property. In order to avoid ambiguity,
    it is strongly suggested that any time representation in this
    field include a specification of the timezone if it is known. As
    with the rest of the field, this should be formatted per the
    xs:time specification.Properties that use this type can express
    multiple values by providing them using a delimiter-separated
    list. The default delimiter is '##comma##' (no quotes) but can
    be overridden through use of the delimiter field. Note that
    whitespace is preserved and so, when specifying a list of
    values, do not include a space following the delimiter in a list
    unless the first character of the next list item should, in
    fact, be a space.For fields of this type using CybOX patterning,
    it is strongly suggested that the condition (pattern type) is
    limited to one of Equals, DoesNotEqual, GreaterThan, LessThan,
    GreaterThanOrEqual, LessThanOrEqual, ExclusiveBetween, or
    InclusiveBetween. The use of other conditions may lead to
    ambiguity or unexpected results. When evaluating data against a
    pattern, the evaluator should take into account the precision of
    the field (as given by the precision attribute) and any timezone
    information that is available to perform a data-aware
    comparison. The usage of simple string comparisons is
    discouraged due to ambiguities in how precision and timezone
    information is processed.The precision of the associated time.
    If omitted, the default is "second", meaning the full field
    value (including fractional seconds). Digits in the time that
    are required by the xs:time datatype but are beyond the
    specified precision should be zeroed out.When used in
    conjunction with CybOX patterning, the pattern should only be
    evaluated against the target up to the given precision."""
    subclass = None
    superclass = TimeObjectPropertyRestrictionType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='time', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, precision='second'):
        # PROP: This is a BaseObjectPropertyType subclass
        super(TimeObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.precision = _cast(None, precision)
    def factory(*args_, **kwargs_):
        if TimeObjectPropertyType.subclass:
            return TimeObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return TimeObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TimeObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='TimeObjectPropertyType'):
        super(TimeObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeObjectPropertyType')
        if self.precision not in (None, 'second'):

            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='TimeObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(TimeObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('precision', node)
        if value is not None:

            self.precision = value
        super(TimeObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TimeObjectPropertyType

class Base64BinaryObjectPropertyType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='base64Binary', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(Base64BinaryObjectPropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if Base64BinaryObjectPropertyType.subclass:
            return Base64BinaryObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return Base64BinaryObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(Base64BinaryObjectPropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='Base64BinaryObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Base64BinaryObjectPropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='Base64BinaryObjectPropertyType'):
        super(Base64BinaryObjectPropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Base64BinaryObjectPropertyType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='Base64BinaryObjectPropertyType', fromsubclass_=False, pretty_print=True):
        super(Base64BinaryObjectPropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(Base64BinaryObjectPropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class Base64BinaryObjectPropertyType

class Layer4ProtocolType(BaseObjectPropertyType):
    """Layer4ProtocolType specifies Layer 4 protocol types, via a union of
    the Layer4ProtocolEnum type and the atomic xs:string type. Its
    base type is the CybOX Core BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(Layer4ProtocolType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if Layer4ProtocolType.subclass:
            return Layer4ProtocolType.subclass(*args_, **kwargs_)
        else:
            return Layer4ProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(Layer4ProtocolType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='Layer4ProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer4ProtocolType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='Layer4ProtocolType'):
        super(Layer4ProtocolType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer4ProtocolType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='Layer4ProtocolType', fromsubclass_=False, pretty_print=True):
        super(Layer4ProtocolType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(Layer4ProtocolType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class Layer4ProtocolType

class EndiannessType(BaseObjectPropertyType):
    """The EndiannessType specifies names for byte ordering methods.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(EndiannessType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if EndiannessType.subclass:
            return EndiannessType.subclass(*args_, **kwargs_)
        else:
            return EndiannessType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(EndiannessType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='EndiannessType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EndiannessType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='EndiannessType'):
        super(EndiannessType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='EndiannessType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='EndiannessType', fromsubclass_=False, pretty_print=True):
        super(EndiannessType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(EndiannessType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class EndiannessType

class CipherType(BaseObjectPropertyType):
    """CipherType specifies encryption algorithms, via a union of the
    CipherEnum type and the atomic xs:string type. Its base type is
    the CybOX Core BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(CipherType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if CipherType.subclass:
            return CipherType.subclass(*args_, **kwargs_)
        else:
            return CipherType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CipherType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CipherType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CipherType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CipherType'):
        super(CipherType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CipherType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CipherType', fromsubclass_=False, pretty_print=True):
        super(CipherType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(CipherType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CipherType

class RegionalRegistryType(BaseObjectPropertyType):
    """The RegionalRegistryType specifies a Regional Internet Registry
    (RIR) for a given WHOIS entry. RIRs defined by the
    RegionalRegistryTypeEnum may be used, as well as those specified
    by a free form text string."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(RegionalRegistryType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if RegionalRegistryType.subclass:
            return RegionalRegistryType.subclass(*args_, **kwargs_)
        else:
            return RegionalRegistryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(RegionalRegistryType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='RegionalRegistryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegionalRegistryType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='RegionalRegistryType'):
        super(RegionalRegistryType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RegionalRegistryType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='RegionalRegistryType', fromsubclass_=False, pretty_print=True):
        super(RegionalRegistryType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(RegionalRegistryType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class RegionalRegistryType

class ExtractedFeaturesType(GeneratedsSuper):
    """The ExtractedFeaturesType is a type representing a description of
    features extracted from an object such as a file."""
    subclass = None
    superclass = None
    def __init__(self, Strings=None, Imports=None, Functions=None, Code_Snippets=None):
        self.Strings = Strings
        self.Imports = Imports
        self.Functions = Functions
        self.Code_Snippets = Code_Snippets
    def factory(*args_, **kwargs_):
        if ExtractedFeaturesType.subclass:
            return ExtractedFeaturesType.subclass(*args_, **kwargs_)
        else:
            return ExtractedFeaturesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Strings(self): return self.Strings
    def set_Strings(self, Strings): self.Strings = Strings
    def get_Imports(self): return self.Imports
    def set_Imports(self, Imports): self.Imports = Imports
    def get_Functions(self): return self.Functions
    def set_Functions(self, Functions): self.Functions = Functions
    def get_Code_Snippets(self): return self.Code_Snippets
    def set_Code_Snippets(self, Code_Snippets): self.Code_Snippets = Code_Snippets
    def hasContent_(self):
        if (
            self.Strings is not None or
            self.Imports is not None or
            self.Functions is not None or
            self.Code_Snippets is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedFeaturesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExtractedFeaturesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ExtractedFeaturesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedFeaturesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Strings is not None:
            self.Strings.export(lwrite, level, 'cyboxCommon:', name_='Strings', pretty_print=pretty_print)
        if self.Imports is not None:
            self.Imports.export(lwrite, level, 'cyboxCommon:', name_='Imports', pretty_print=pretty_print)
        if self.Functions is not None:
            self.Functions.export(lwrite, level, 'cyboxCommon:', name_='Functions', pretty_print=pretty_print)
        if self.Code_Snippets is not None:
            self.Code_Snippets.export(lwrite, level, 'cyboxCommon:', name_='Code_Snippets', pretty_print=pretty_print)
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
        if nodeName_ == 'Strings':
            obj_ = ExtractedStringsType.factory()
            obj_.build(child_)
            self.set_Strings(obj_)
        elif nodeName_ == 'Imports':
            obj_ = ImportsType.factory()
            obj_.build(child_)
            self.set_Imports(obj_)
        elif nodeName_ == 'Functions':
            obj_ = FunctionsType.factory()
            obj_.build(child_)
            self.set_Functions(obj_)
        elif nodeName_ == 'Code_Snippets':
            obj_ = CodeSnippetsType.factory()
            obj_.build(child_)
            self.set_Code_Snippets(obj_)
# end class ExtractedFeaturesType

class ExtractedStringsType(GeneratedsSuper):
    """The ExtractedStringsType type is intended as container for strings
    extracted from CybOX objects."""

    subclass = None
    superclass = None
    def __init__(self, String=None):
        if String is None:
            self.String = []
        else:
            self.String = String
    def factory(*args_, **kwargs_):
        if ExtractedStringsType.subclass:
            return ExtractedStringsType.subclass(*args_, **kwargs_)
        else:
            return ExtractedStringsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_String(self): return self.String
    def set_String(self, String): self.String = String
    def add_String(self, value): self.String.append(value)
    def insert_String(self, index, value): self.String[index] = value
    def hasContent_(self):
        if (
            self.String
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedStringsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExtractedStringsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ExtractedStringsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedStringsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for String_ in self.String:
            String_.export(lwrite, level, 'cyboxCommon:', name_='String', pretty_print=pretty_print)
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
        if nodeName_ == 'String':
            obj_ = ExtractedStringType.factory()
            obj_.build(child_)
            self.String.append(obj_)
# end class ExtractedStringsType

class ExtractedStringType(GeneratedsSuper):
    """The ExtractedStringType type is intended as container a single
    string extracted from a CybOX object."""

    subclass = None
    superclass = None
    def __init__(self, Encoding=None, String_Value=None, Byte_String_Value=None, Hashes=None, Address=None, Length=None, Language=None, English_Translation=None):
        self.Encoding = Encoding
        self.String_Value = String_Value
        self.Byte_String_Value = Byte_String_Value
        self.Hashes = Hashes
        self.Address = Address
        self.Length = Length
        self.Language = Language
        self.English_Translation = English_Translation
    def factory(*args_, **kwargs_):
        if ExtractedStringType.subclass:
            return ExtractedStringType.subclass(*args_, **kwargs_)
        else:
            return ExtractedStringType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Encoding(self): return self.Encoding
    def set_Encoding(self, Encoding): self.Encoding = Encoding
    def get_String_Value(self): return self.String_Value
    def set_String_Value(self, String_Value): self.String_Value = String_Value
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def get_Byte_String_Value(self): return self.Byte_String_Value
    def set_Byte_String_Value(self, Byte_String_Value): self.Byte_String_Value = Byte_String_Value
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Address(self): return self.Address
    def set_Address(self, Address): self.Address = Address
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Language(self): return self.Language
    def set_Language(self, Language): self.Language = Language
    def get_English_Translation(self): return self.English_Translation
    def set_English_Translation(self, English_Translation): self.English_Translation = English_Translation
    def hasContent_(self):
        if (
            self.Encoding is not None or
            self.String_Value is not None or
            self.Byte_String_Value is not None or
            self.Hashes is not None or
            self.Address is not None or
            self.Length is not None or
            self.Language is not None or
            self.English_Translation is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedStringType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExtractedStringType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ExtractedStringType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ExtractedStringType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Encoding is not None:
            self.Encoding.export(lwrite, level, 'cyboxCommon:', name_='Encoding', pretty_print=pretty_print)
        if self.String_Value is not None:
            self.String_Value.export(lwrite, level, 'cyboxCommon:', name_='String_Value', pretty_print=pretty_print)
        if self.Byte_String_Value is not None:
            self.Byte_String_Value.export(lwrite, level, 'cyboxCommon:', name_='Byte_String_Value', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'cyboxCommon:', name_='Hashes', pretty_print=pretty_print)
        if self.Address is not None:
            self.Address.export(lwrite, level, 'cyboxCommon:', name_='Address', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'cyboxCommon:', name_='Length', pretty_print=pretty_print)
        if self.Language is not None:
            self.Language.export(lwrite, level, 'cyboxCommon:', name_='Language', pretty_print=pretty_print)
        if self.English_Translation is not None:
            self.English_Translation.export(lwrite, level, 'cyboxCommon:', name_='English_Translation', pretty_print=pretty_print)
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
        if nodeName_ == 'Encoding':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Encoding(obj_)
        elif nodeName_ == 'String_Value':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_String_Value(obj_)
        elif nodeName_ == 'Byte_String_Value':
            obj_ = HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Byte_String_Value(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Address':
            obj_ = HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address(obj_)
        elif nodeName_ == 'Length':
            obj_ = PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Language':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Language(obj_)
        elif nodeName_ == 'English_Translation':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_English_Translation(obj_)
# end class ExtractedStringType

class ImportsType(GeneratedsSuper):
    """The ImportsType is intended to represent an extracted list of
    imports specified within a CybOX object."""

    subclass = None
    superclass = None
    def __init__(self, Import=None):
        if Import is None:
            self.Import = []
        else:
            self.Import = Import
    def factory(*args_, **kwargs_):
        if ImportsType.subclass:
            return ImportsType.subclass(*args_, **kwargs_)
        else:
            return ImportsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Import(self): return self.Import
    def set_Import(self, Import): self.Import = Import
    def add_Import(self, value): self.Import.append(value)
    def insert_Import(self, index, value): self.Import[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Import
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ImportsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ImportsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ImportsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ImportsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Import_ in self.Import:
            Import_.export(lwrite, level, 'cyboxCommon:', name_='Import', pretty_print=pretty_print)
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
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Import.append(obj_)
# end class ImportsType

class FunctionsType(GeneratedsSuper):
    """The FunctionsType is intended to represent an extracted list of
    functions leveraged within a CybOX object."""

    subclass = None
    superclass = None
    def __init__(self, Function=None):
        if Function is None:
            self.Function = []
        else:
            self.Function = Function
    def factory(*args_, **kwargs_):
        if FunctionsType.subclass:
            return FunctionsType.subclass(*args_, **kwargs_)
        else:
            return FunctionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Function(self): return self.Function
    def set_Function(self, Function): self.Function = Function
    def add_Function(self, value): self.Function.append(value)
    def insert_Function(self, index, value): self.Function[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Function
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='FunctionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FunctionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='FunctionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='FunctionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Function_ in self.Function:
            Function_.export(lwrite, level, 'cyboxCommon:', name_='Function', pretty_print=pretty_print)
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
        if nodeName_ == 'Function':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Function.append(obj_)
# end class FunctionsType

class CodeSnippetsType(GeneratedsSuper):
    """The CodeSnippetsType is intended to represent an set of code
    snippets extracted from within a CybOX object."""

    subclass = None
    superclass = None
    def __init__(self, Code_Snippet=None):
        if Code_Snippet is None:
            self.Code_Snippet = []
        else:
            self.Code_Snippet = Code_Snippet
    def factory(*args_, **kwargs_):
        if CodeSnippetsType.subclass:
            return CodeSnippetsType.subclass(*args_, **kwargs_)
        else:
            return CodeSnippetsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Code_Snippet(self): return self.Code_Snippet
    def set_Code_Snippet(self, Code_Snippet): self.Code_Snippet = Code_Snippet
    def add_Code_Snippet(self, value): self.Code_Snippet.append(value)
    def insert_Code_Snippet(self, index, value): self.Code_Snippet[index] = value
    def hasContent_(self):
        if (
            self.Code_Snippet
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CodeSnippetsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeSnippetsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CodeSnippetsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CodeSnippetsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Code_Snippet_ in self.get_Code_Snippet():
            Code_Snippet_.export(lwrite, level, 'cyboxCommon:', name_='Code_Snippet', pretty_print=pretty_print)
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
        if nodeName_ == 'Code_Snippet':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Code_Snippet> element')
            self.Code_Snippet.append(obj_)
# end class CodeSnippetsType

class ByteRunsType(GeneratedsSuper):
    """The ByteRunsType is used for representing a list of byte runs from
    within a raw object."""

    subclass = None
    superclass = None
    def __init__(self, Byte_Run=None):
        if Byte_Run is None:
            self.Byte_Run = []
        else:
            self.Byte_Run = Byte_Run
    def factory(*args_, **kwargs_):
        if ByteRunsType.subclass:
            return ByteRunsType.subclass(*args_, **kwargs_)
        else:
            return ByteRunsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Byte_Run(self): return self.Byte_Run
    def set_Byte_Run(self, Byte_Run): self.Byte_Run = Byte_Run
    def add_Byte_Run(self, value): self.Byte_Run.append(value)
    def insert_Byte_Run(self, index, value): self.Byte_Run[index] = value
    def hasContent_(self):
        if (
            self.Byte_Run
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ByteRunsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ByteRunsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ByteRunsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ByteRunsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Byte_Run_ in self.Byte_Run:
            Byte_Run_.export(lwrite, level, 'cyboxCommon:', name_='Byte_Run', pretty_print=pretty_print)
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
        if nodeName_ == 'Byte_Run':
            obj_ = ByteRunType.factory()
            obj_.build(child_)
            self.Byte_Run.append(obj_)
# end class ByteRunsType

class ByteRunType(GeneratedsSuper):
    """The ByteRunType is used for representing a single byte run from
    within a raw object."""
    subclass = None
    superclass = None
    def __init__(self, Offset=None, Byte_Order=None, File_System_Offset=None, Image_Offset=None, Length=None, Hashes=None, Byte_Run_Data=None):
        self.Offset = Offset
        self.Byte_Order = Byte_Order
        self.File_System_Offset = File_System_Offset
        self.Image_Offset = Image_Offset
        self.Length = Length
        self.Hashes = Hashes
        self.Byte_Run_Data = Byte_Run_Data
    def factory(*args_, **kwargs_):
        if ByteRunType.subclass:
            return ByteRunType.subclass(*args_, **kwargs_)
        else:
            return ByteRunType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Offset(self): return self.Offset
    def set_Offset(self, Offset): self.Offset = Offset
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Byte_Order(self): return self.Byte_Order
    def set_Byte_Order(self, Byte_Order): self.Byte_Order = Byte_Order
    def validate_EndiannessType(self, value):
        # Validate type EndiannessType, a restriction on None.
        pass
    def get_File_System_Offset(self): return self.File_System_Offset
    def set_File_System_Offset(self, File_System_Offset): self.File_System_Offset = File_System_Offset
    def get_Image_Offset(self): return self.Image_Offset
    def set_Image_Offset(self, Image_Offset): self.Image_Offset = Image_Offset
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Byte_Run_Data(self): return self.Byte_Run_Data
    def set_Byte_Run_Data(self, Byte_Run_Data): self.Byte_Run_Data = Byte_Run_Data
    def hasContent_(self):
        if (
            self.Offset is not None or
            self.Byte_Order is not None or
            self.File_System_Offset is not None or
            self.Image_Offset is not None or
            self.Length is not None or
            self.Hashes is not None or
            self.Byte_Run_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ByteRunType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ByteRunType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ByteRunType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ByteRunType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Offset is not None:
            self.Offset.export(lwrite, level, 'cyboxCommon:', name_='Offset', pretty_print=pretty_print)
        if self.Byte_Order is not None:
            self.Byte_Order.export(lwrite, level, 'cyboxCommon:', name_='Byte_Order', pretty_print=pretty_print)
        if self.File_System_Offset is not None:
            self.File_System_Offset.export(lwrite, level, 'cyboxCommon:', name_='File_System_Offset', pretty_print=pretty_print)
        if self.Image_Offset is not None:
            self.Image_Offset.export(lwrite, level, 'cyboxCommon:', name_='Image_Offset', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'cyboxCommon:', name_='Length', pretty_print=pretty_print)
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'cyboxCommon:', name_='Hashes', pretty_print=pretty_print)
        if self.Byte_Run_Data is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sByte_Run_Data>%s</%sByte_Run_Data>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Byte_Run_Data), input_name='Byte_Run_Data'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Offset':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset(obj_)
        elif nodeName_ == 'Byte_Order':
            obj_ = EndiannessType.factory()
            obj_.build(child_)
            self.set_Byte_Order(obj_)
        elif nodeName_ == 'File_System_Offset':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_System_Offset(obj_)
        elif nodeName_ == 'Image_Offset':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Image_Offset(obj_)
        elif nodeName_ == 'Length':
            obj_ = PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Hashes':
            obj_ = HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Byte_Run_Data':
            Byte_Run_Data_ = child_.text
            Byte_Run_Data_ = self.gds_validate_string(Byte_Run_Data_, node, 'Byte_Run_Data')
            self.Byte_Run_Data = Byte_Run_Data_
# end class ByteRunType

class HashListType(GeneratedsSuper):
    """The HashListType type is used for representing a list of hash
    values."""

    subclass = None
    superclass = None
    def __init__(self, Hash=None):
        if Hash is None:
            self.Hash = []
        else:
            self.Hash = Hash
    def factory(*args_, **kwargs_):
        if HashListType.subclass:
            return HashListType.subclass(*args_, **kwargs_)
        else:
            return HashListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hash(self): return self.Hash
    def set_Hash(self, Hash): self.Hash = Hash
    def add_Hash(self, value): self.Hash.append(value)
    def insert_Hash(self, index, value): self.Hash[index] = value
    def hasContent_(self):
        if (
            self.Hash
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HashListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HashListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HashListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HashListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Hash_ in self.Hash:
            Hash_.export(lwrite, level, 'cyboxCommon:', name_='Hash', pretty_print=pretty_print)
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
        if nodeName_ == 'Hash':
            obj_ = HashType.factory()
            obj_.build(child_)
            self.Hash.append(obj_)
# end class HashListType

class HashValueType(GeneratedsSuper):
    """The HashValueType is used for specifying the resulting value from a
    hash calculation."""

    subclass = None
    superclass = None
    def __init__(self, Simple_Hash_Value=None, Fuzzy_Hash_Value=None):
        self.Simple_Hash_Value = Simple_Hash_Value
        self.Fuzzy_Hash_Value = Fuzzy_Hash_Value
    def factory(*args_, **kwargs_):
        if HashValueType.subclass:
            return HashValueType.subclass(*args_, **kwargs_)
        else:
            return HashValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Simple_Hash_Value(self): return self.Simple_Hash_Value
    def set_Simple_Hash_Value(self, Simple_Hash_Value): self.Simple_Hash_Value = Simple_Hash_Value
    def get_Fuzzy_Hash_Value(self): return self.Fuzzy_Hash_Value
    def set_Fuzzy_Hash_Value(self, Fuzzy_Hash_Value): self.Fuzzy_Hash_Value = Fuzzy_Hash_Value
    def hasContent_(self):
        if (
            self.Simple_Hash_Value is not None or
            self.Fuzzy_Hash_Value is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HashValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HashValueType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HashValueType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HashValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Simple_Hash_Value is not None:
            self.Simple_Hash_Value.export(lwrite, level, 'cyboxCommon:', name_='Simple_Hash_Value', pretty_print=pretty_print)
        if self.Fuzzy_Hash_Value is not None:
            self.Fuzzy_Hash_Value.export(lwrite, level, 'cyboxCommon:', name_='Fuzzy_Hash_Value', pretty_print=pretty_print)
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
        if nodeName_ == 'Simple_Hash_Value':
            obj_ = HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Simple_Hash_Value(obj_)
        elif nodeName_ == 'Fuzzy_Hash_Value':
            obj_ = FuzzyHashValueType.factory()
            obj_.build(child_)
            self.set_Fuzzy_Hash_Value(obj_)
# end class HashValueType

class SimpleHashValueType(HexBinaryObjectPropertyType):
    """The SimpleHashValueType is used for characterizing the output of
    basic cryptograhic hash functions outputing a single hexbinary
    hash value."""

    subclass = None
    superclass = HexBinaryObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='hexBinary', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(SimpleHashValueType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if SimpleHashValueType.subclass:
            return SimpleHashValueType.subclass(*args_, **kwargs_)
        else:
            return SimpleHashValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            super(SimpleHashValueType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='SimpleHashValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SimpleHashValueType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='SimpleHashValueType'):
        super(SimpleHashValueType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SimpleHashValueType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='SimpleHashValueType', fromsubclass_=False, pretty_print=True):
        super(SimpleHashValueType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(SimpleHashValueType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SimpleHashValueType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SimpleHashValueType

class FuzzyHashValueType(StringObjectPropertyType):
    """The FuzzyHashValueType is used for characterizing the output of
    cryptograhic fuzzy hash functions outputing a single complex
    string based hash value."""

    subclass = None
    superclass = StringObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(FuzzyHashValueType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if FuzzyHashValueType.subclass:
            return FuzzyHashValueType.subclass(*args_, **kwargs_)
        else:
            return FuzzyHashValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            super(FuzzyHashValueType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FuzzyHashValueType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='FuzzyHashValueType'):
        super(FuzzyHashValueType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='FuzzyHashValueType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashValueType', fromsubclass_=False, pretty_print=True):
        super(FuzzyHashValueType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(FuzzyHashValueType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(FuzzyHashValueType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class FuzzyHashValueType

class FuzzyHashStructureType(GeneratedsSuper):
    """The FuzzyHashStructureType is used for characterizing the internal
    components of a cryptograhic fuzzy hash algorithmic calculation."""

    subclass = None
    superclass = None
    def __init__(self, Block_Size=None, Block_Hash=None):
        self.Block_Size = Block_Size
        self.Block_Hash = Block_Hash
    def factory(*args_, **kwargs_):
        if FuzzyHashStructureType.subclass:
            return FuzzyHashStructureType.subclass(*args_, **kwargs_)
        else:
            return FuzzyHashStructureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Block_Size(self): return self.Block_Size
    def set_Block_Size(self, Block_Size): self.Block_Size = Block_Size
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Block_Hash(self): return self.Block_Hash
    def set_Block_Hash(self, Block_Hash): self.Block_Hash = Block_Hash
    def hasContent_(self):
        if (
            self.Block_Size is not None or
            self.Block_Hash is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashStructureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FuzzyHashStructureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='FuzzyHashStructureType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashStructureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Block_Size is not None:
            self.Block_Size.export(lwrite, level, 'cyboxCommon:', name_='Block_Size', pretty_print=pretty_print)
        if self.Block_Hash is not None:
            self.Block_Hash.export(lwrite, level, 'cyboxCommon:', name_='Block_Hash', pretty_print=pretty_print)
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
        if nodeName_ == 'Block_Size':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Block_Size(obj_)
        elif nodeName_ == 'Block_Hash':
            obj_ = FuzzyHashBlockType.factory()
            obj_.build(child_)
            self.set_Block_Hash(obj_)
# end class FuzzyHashStructureType

class FuzzyHashBlockType(GeneratedsSuper):
    """The FuzzyHashBlockType is used for characterizing the internal
    components of a single block in a cryptograhic fuzzy hash
    algorithmic calculation."""

    subclass = None
    superclass = None
    def __init__(self, Block_Hash_Value=None, Segment_Count=None, Segments=None):
        self.Block_Hash_Value = Block_Hash_Value
        self.Segment_Count = Segment_Count
        self.Segments = Segments
    def factory(*args_, **kwargs_):
        if FuzzyHashBlockType.subclass:
            return FuzzyHashBlockType.subclass(*args_, **kwargs_)
        else:
            return FuzzyHashBlockType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Block_Hash_Value(self): return self.Block_Hash_Value
    def set_Block_Hash_Value(self, Block_Hash_Value): self.Block_Hash_Value = Block_Hash_Value
    def get_Segment_Count(self): return self.Segment_Count
    def set_Segment_Count(self, Segment_Count): self.Segment_Count = Segment_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Segments(self): return self.Segments
    def set_Segments(self, Segments): self.Segments = Segments
    def hasContent_(self):
        if (
            self.Block_Hash_Value is not None or
            self.Segment_Count is not None or
            self.Segments is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashBlockType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FuzzyHashBlockType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='FuzzyHashBlockType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='FuzzyHashBlockType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Block_Hash_Value is not None:
            self.Block_Hash_Value.export(lwrite, level, 'cyboxCommon:', name_='Block_Hash_Value', pretty_print=pretty_print)
        if self.Segment_Count is not None:
            self.Segment_Count.export(lwrite, level, 'cyboxCommon:', name_='Segment_Count', pretty_print=pretty_print)
        if self.Segments is not None:
            self.Segments.export(lwrite, level, 'cyboxCommon:', name_='Segments', pretty_print=pretty_print)
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
        if nodeName_ == 'Block_Hash_Value':
            obj_ = HashValueType.factory()
            obj_.build(child_)
            self.set_Block_Hash_Value(obj_)
        elif nodeName_ == 'Segment_Count':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Segment_Count(obj_)
        elif nodeName_ == 'Segments':
            obj_ = HashSegmentsType.factory()
            obj_.build(child_)
            self.set_Segments(obj_)
# end class FuzzyHashBlockType

class HashSegmentsType(GeneratedsSuper):
    """The HashSegmentsType is used for characterizing the internal
    components of a set of trigger point-delimited segments in a
    cryptograhic fuzzy hash algorithmic calculation."""

    subclass = None
    superclass = None
    def __init__(self, Segment=None):
        if Segment is None:
            self.Segment = []
        else:
            self.Segment = Segment
    def factory(*args_, **kwargs_):
        if HashSegmentsType.subclass:
            return HashSegmentsType.subclass(*args_, **kwargs_)
        else:
            return HashSegmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Segment(self): return self.Segment
    def set_Segment(self, Segment): self.Segment = Segment
    def add_Segment(self, value): self.Segment.append(value)
    def insert_Segment(self, index, value): self.Segment[index] = value
    def hasContent_(self):
        if (
            self.Segment
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HashSegmentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HashSegmentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HashSegmentsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HashSegmentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Segment_ in self.Segment:
            Segment_.export(lwrite, level, 'cyboxCommon:', name_='Segment', pretty_print=pretty_print)
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
        if nodeName_ == 'Segment':
            obj_ = HashSegmentType.factory()
            obj_.build(child_)
            self.Segment.append(obj_)
# end class HashSegmentsType

class HashSegmentType(GeneratedsSuper):
    """The HashSegmentType is used for characterizing the internal
    components of a single trigger point-delimited segment in a
    cryptograhic fuzzy hash algorithmic calculation."""

    subclass = None
    superclass = None
    def __init__(self, Trigger_Point=None, Segment_Hash=None, Raw_Segment_Content=None):
        self.Trigger_Point = Trigger_Point
        self.Segment_Hash = Segment_Hash
        self.Raw_Segment_Content = Raw_Segment_Content
    def factory(*args_, **kwargs_):
        if HashSegmentType.subclass:
            return HashSegmentType.subclass(*args_, **kwargs_)
        else:
            return HashSegmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Trigger_Point(self): return self.Trigger_Point
    def set_Trigger_Point(self, Trigger_Point): self.Trigger_Point = Trigger_Point
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Segment_Hash(self): return self.Segment_Hash
    def set_Segment_Hash(self, Segment_Hash): self.Segment_Hash = Segment_Hash
    def get_Raw_Segment_Content(self): return self.Raw_Segment_Content
    def set_Raw_Segment_Content(self, Raw_Segment_Content): self.Raw_Segment_Content = Raw_Segment_Content
    def hasContent_(self):
        if (
            self.Trigger_Point is not None or
            self.Segment_Hash is not None or
            self.Raw_Segment_Content is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HashSegmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HashSegmentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HashSegmentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HashSegmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Trigger_Point is not None:
            self.Trigger_Point.export(lwrite, level, 'cyboxCommon:', name_='Trigger_Point', pretty_print=pretty_print)
        if self.Segment_Hash is not None:
            self.Segment_Hash.export(lwrite, level, 'cyboxCommon:', name_='Segment_Hash', pretty_print=pretty_print)
        if self.Raw_Segment_Content is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRaw_Segment_Content>%s</%sRaw_Segment_Content>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Raw_Segment_Content), input_name='Raw_Segment_Content'), 'cyboxCommon:', eol_))
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
        if nodeName_ == 'Trigger_Point':
            obj_ = HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Point(obj_)
        elif nodeName_ == 'Segment_Hash':
            obj_ = HashValueType.factory()
            obj_.build(child_)
            self.set_Segment_Hash(obj_)
        elif nodeName_ == 'Raw_Segment_Content':
            Raw_Segment_Content_ = child_.text
            Raw_Segment_Content_ = self.gds_validate_string(Raw_Segment_Content_, node, 'Raw_Segment_Content')
            self.Raw_Segment_Content = Raw_Segment_Content_
# end class HashSegmentType

class HashType(GeneratedsSuper):
    """The HashType type is intended to characterize hash values."""

    subclass = None
    superclass = None
    def __init__(self, Type=None, Simple_Hash_Value=None, Fuzzy_Hash_Value=None, Fuzzy_Hash_Structure=None):
        self.Type = Type
        self.Simple_Hash_Value = Simple_Hash_Value
        self.Fuzzy_Hash_Value = Fuzzy_Hash_Value
        if Fuzzy_Hash_Structure is None:
            self.Fuzzy_Hash_Structure = []
        else:
            self.Fuzzy_Hash_Structure = Fuzzy_Hash_Structure
    def factory(*args_, **kwargs_):
        if HashType.subclass:
            return HashType.subclass(*args_, **kwargs_)
        else:
            return HashType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Simple_Hash_Value(self): return self.Simple_Hash_Value
    def set_Simple_Hash_Value(self, Simple_Hash_Value): self.Simple_Hash_Value = Simple_Hash_Value
    def get_Fuzzy_Hash_Value(self): return self.Fuzzy_Hash_Value
    def set_Fuzzy_Hash_Value(self, Fuzzy_Hash_Value): self.Fuzzy_Hash_Value = Fuzzy_Hash_Value
    def get_Fuzzy_Hash_Structure(self): return self.Fuzzy_Hash_Structure
    def set_Fuzzy_Hash_Structure(self, Fuzzy_Hash_Structure): self.Fuzzy_Hash_Structure = Fuzzy_Hash_Structure
    def add_Fuzzy_Hash_Structure(self, value): self.Fuzzy_Hash_Structure.append(value)
    def insert_Fuzzy_Hash_Structure(self, index, value): self.Fuzzy_Hash_Structure[index] = value
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Simple_Hash_Value is not None or
            self.Fuzzy_Hash_Value is not None or
            self.Fuzzy_Hash_Structure
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='HashType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HashType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='HashType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='HashType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'cyboxCommon:', name_='Type', pretty_print=pretty_print)
        if self.Simple_Hash_Value is not None:
            self.Simple_Hash_Value.export(lwrite, level, 'cyboxCommon:', name_='Simple_Hash_Value', pretty_print=pretty_print)
        if self.Fuzzy_Hash_Value is not None:
            self.Fuzzy_Hash_Value.export(lwrite, level, 'cyboxCommon:', name_='Fuzzy_Hash_Value', pretty_print=pretty_print)
        for Fuzzy_Hash_Structure_ in self.Fuzzy_Hash_Structure:
            Fuzzy_Hash_Structure_.export(lwrite, level, 'cyboxCommon:', name_='Fuzzy_Hash_Structure', pretty_print=pretty_print)
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
        if nodeName_ == 'Type':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Simple_Hash_Value':
            obj_ = HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Simple_Hash_Value(obj_)
        elif nodeName_ == 'Fuzzy_Hash_Value':
            obj_ = FuzzyHashValueType.factory()
            obj_.build(child_)
            self.set_Fuzzy_Hash_Value(obj_)
        elif nodeName_ == 'Fuzzy_Hash_Structure':
            obj_ = FuzzyHashStructureType.factory()
            obj_.build(child_)
            self.Fuzzy_Hash_Structure.append(obj_)
# end class HashType

class StructuredTextType(GeneratedsSuper):
    """The StructuredTextType is a type representing a generalized
    structure for capturing structured or unstructured textual
    information such as descriptions of things.Used to indicate a
    particular structuring format (e.g., HTML5) used within an
    instance of StructuredTextType. Note that if the markup tags
    used by this format would be interpreted as XML information
    (such as the bracket-based tags of HTML) the text area should be
    enclosed in a CDATA section to prevent the markup from
    interferring with XML validation of the CybOX document. If this
    attribute is absent, the implication is that no markup is being
    used."""

    subclass = None
    superclass = None
    def __init__(self, structuring_format=None, valueOf_=None):
        self.structuring_format = _cast(None, structuring_format)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if StructuredTextType.subclass:
            return StructuredTextType.subclass(*args_, **kwargs_)
        else:
            return StructuredTextType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_structuring_format(self): return self.structuring_format
    def set_structuring_format(self, structuring_format): self.structuring_format = structuring_format
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='StructuredTextType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StructuredTextType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='StructuredTextType'):
        if self.structuring_format is not None:

            lwrite(' structuring_format=%s' % (self.gds_format_string(quote_attrib(self.structuring_format), input_name='structuring_format'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='StructuredTextType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('structuring_format', node)
        if value is not None:

            self.structuring_format = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class StructuredTextType


class DataSegmentType(GeneratedsSuper):
    """The DataSegmentType is intended to provide a relatively abstract way
    of characterizing data segments that may be
    written/read/transmitted or otherwise utilized in actions or
    behaviors.The id field specifies a unique id for this data
    segment."""
    subclass = None
    superclass = None
    def __init__(self, id=None, Data_Format=None, Data_Size=None, Byte_Order=None, Data_Segment=None, Offset=None, Search_Distance=None, Search_Within=None):
        self.id = _cast(None, id)
        self.Data_Format = Data_Format
        self.Data_Size = Data_Size
        self.Byte_Order = Byte_Order
        self.Data_Segment = Data_Segment
        self.Offset = Offset
        self.Search_Distance = Search_Distance
        self.Search_Within = Search_Within
    def factory(*args_, **kwargs_):
        if DataSegmentType.subclass:
            return DataSegmentType.subclass(*args_, **kwargs_)
        else:
            return DataSegmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data_Format(self): return self.Data_Format
    def set_Data_Format(self, Data_Format): self.Data_Format = Data_Format
    def validate_DataFormatEnum(self, value):
        # Validate type DataFormatEnum, a restriction on xs:string.
        pass
    def get_Data_Size(self): return self.Data_Size
    def set_Data_Size(self, Data_Size): self.Data_Size = Data_Size
    def get_Byte_Order(self): return self.Byte_Order
    def set_Byte_Order(self, Byte_Order): self.Byte_Order = Byte_Order
    def validate_EndiannessType(self, value):
        # Validate type EndiannessType, a restriction on None.
        pass
    def get_Data_Segment(self): return self.Data_Segment
    def set_Data_Segment(self, Data_Segment): self.Data_Segment = Data_Segment
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def get_Offset(self): return self.Offset
    def set_Offset(self, Offset): self.Offset = Offset
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Search_Distance(self): return self.Search_Distance
    def set_Search_Distance(self, Search_Distance): self.Search_Distance = Search_Distance
    def get_Search_Within(self): return self.Search_Within
    def set_Search_Within(self, Search_Within): self.Search_Within = Search_Within
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Data_Format is not None or
            self.Data_Size is not None or
            self.Byte_Order is not None or
            self.Data_Segment is not None or
            self.Offset is not None or
            self.Search_Distance is not None or
            self.Search_Within is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DataSegmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DataSegmentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DataSegmentType'):
        if self.id is not None:

            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DataSegmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data_Format is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sData_Format>%s</%sData_Format>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Data_Format), input_name='Data_Format'), 'cyboxCommon:', eol_))
        if self.Data_Size is not None:
            self.Data_Size.export(lwrite, level, 'cyboxCommon:', name_='Data_Size', pretty_print=pretty_print)
        if self.Byte_Order is not None:
            self.Byte_Order.export(lwrite, level, 'cyboxCommon:', name_='Byte_Order', pretty_print=pretty_print)
        if self.Data_Segment is not None:
            self.Data_Segment.export(lwrite, level, 'cyboxCommon:', name_='Data_Segment', pretty_print=pretty_print)
        if self.Offset is not None:
            self.Offset.export(lwrite, level, 'cyboxCommon:', name_='Offset', pretty_print=pretty_print)
        if self.Search_Distance is not None:
            self.Search_Distance.export(lwrite, level, 'cyboxCommon:', name_='Search_Distance', pretty_print=pretty_print)
        if self.Search_Within is not None:
            self.Search_Within.export(lwrite, level, 'cyboxCommon:', name_='Search_Within', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None:

            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data_Format':
            Data_Format = child_.text
            Data_Format = self.gds_validate_string(Data_Format, node, 'Data_Format')
            self.Data_Format = Data_Format
        elif nodeName_ == 'Data_Size':
            obj_ = DataSizeType.factory()
            obj_.build(child_)
            self.set_Data_Size(obj_)
        elif nodeName_ == 'Byte_Order':
            obj_ = EndiannessType.factory()
            obj_.build(child_)
            self.set_Byte_Order(obj_)
        elif nodeName_ == 'Data_Segment':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data_Segment(obj_)
        elif nodeName_ == 'Offset':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Offset(obj_)
        elif nodeName_ == 'Search_Distance':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Search_Distance(obj_)
        elif nodeName_ == 'Search_Within':
            obj_ = IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Search_Within(obj_)
# end class DataSegmentType

class DataSizeType(StringObjectPropertyType):
    """The DataSizeType specifies the size of the data segment.This field
    represents the Units used in the object size element. Possible
    values are: Bytes, Kilobytes, Megabytes."""

    subclass = None
    superclass = StringObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, units=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DataSizeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.units = _cast(None, units)
    def factory(*args_, **kwargs_):
        if DataSizeType.subclass:
            return DataSizeType.subclass(*args_, **kwargs_)
        else:
            return DataSizeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DataSizeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DataSizeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DataSizeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DataSizeType'):
        super(DataSizeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DataSizeType')
        if self.units is not None:
            lwrite(' units=%s' % (quote_attrib(self.units), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DataSizeType', fromsubclass_=False, pretty_print=True):
        super(DataSizeType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('units', node)
        if value is not None:
            self.units = value
        super(DataSizeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DataSizeType

class PlatformSpecificationType(GeneratedsSuper):
    """PlatformSpecificationType is a modularized data type intended for
    providing a consistent approach to uniquely specifying the
    identity of a specific platform.In addition to capturing basic
    information, this type is intended to be extended to enable the
    structured description of a platform instance using the XML
    Schema extension feature. The CybOX default extension uses the
    Common Platform Enumeration (CPE) Applicability Language schema
    to do so. The extension that defines this is captured in the
    CPE23PlatformSpecificationType in the
    http://cybox.mitre.org/extensions/platform#CPE2.3-1 namespace.
    This type is defined in the extensions/platform/cpe2.3.xsd file."""

    subclass = None
    superclass = None
    def __init__(self, Description=None, Identifier=None):
        self.Description = Description
        if Identifier is None:
            self.Identifier = []
        else:
            self.Identifier = Identifier
    def factory(*args_, **kwargs_):
        if PlatformSpecificationType.subclass:
            return PlatformSpecificationType.subclass(*args_, **kwargs_)
        else:
            return PlatformSpecificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Identifier(self): return self.Identifier
    def set_Identifier(self, Identifier): self.Identifier = Identifier
    def add_Identifier(self, value): self.Identifier.append(value)
    def insert_Identifier(self, index, value): self.Identifier[index] = value
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Identifier
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PlatformSpecificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PlatformSpecificationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PlatformSpecificationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PlatformSpecificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'cyboxCommon:', name_='Description', pretty_print=pretty_print)
        for Identifier_ in self.Identifier:
            Identifier_.export(lwrite, level, 'cyboxCommon:', name_='Identifier', pretty_print=pretty_print)
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
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Identifier':
            obj_ = PlatformIdentifierType.factory()
            obj_.build(child_)
            self.Identifier.append(obj_)
# end class PlatformSpecificationType

class PlatformIdentifierType(StringObjectPropertyType):
    """Used to specify a name for a platform using a particular naming
    system and also allowing a reference pointing to more
    information about that naming scheme. For example, one could
    provide a CPE (Common Platform Enumeration) name using the CPE
    naming format. In this case, the system value could be "CPE"
    while the system_ref value could be
    "http://scap.nist.gov/specifications/cpe/".Indicates the naming
    system from which the indicated name was drawn.A reference to
    information about the naming system from which the indicated
    name was drawn."""

    subclass = None
    superclass = StringObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, system_ref=None, system=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(PlatformIdentifierType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.system_ref = _cast(None, system_ref)
        self.system = _cast(None, system)
    def factory(*args_, **kwargs_):
        if PlatformIdentifierType.subclass:
            return PlatformIdentifierType.subclass(*args_, **kwargs_)
        else:
            return PlatformIdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system_ref(self): return self.system_ref
    def set_system_ref(self, system_ref): self.system_ref = system_ref
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PlatformIdentifierType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PlatformIdentifierType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PlatformIdentifierType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PlatformIdentifierType'):
        super(PlatformIdentifierType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PlatformIdentifierType')
        if self.system_ref is not None:

            lwrite(' system-ref=%s' % (self.gds_format_string(quote_attrib(self.system_ref), input_name='system-ref'), ))
        if self.system is not None:

            lwrite(' system=%s' % (self.gds_format_string(quote_attrib(self.system), input_name='system'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PlatformIdentifierType', fromsubclass_=False, pretty_print=True):
        super(PlatformIdentifierType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('system-ref', node)
        if value is not None:

            self.system_ref = value
        value = find_attr_value_('system', node)
        if value is not None:

            self.system = value
        super(PlatformIdentifierType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PlatformIdentifierType

class MetadataType(GeneratedsSuper):
    """The MetadataType is intended as mechanism to capture any non-
    context-specific metadataThis field specifies the type of name
    of a single metadata field."""

    subclass = None
    superclass = None
    def __init__(self, type_=None, Value=None, SubDatum=None):
        self.type_ = _cast(None, type_)
        self.Value = Value
        if SubDatum is None:
            self.SubDatum = []
        else:
            self.SubDatum = SubDatum
    def factory(*args_, **kwargs_):
        if MetadataType.subclass:
            return MetadataType.subclass(*args_, **kwargs_)
        else:
            return MetadataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def get_SubDatum(self): return self.SubDatum
    def set_SubDatum(self, SubDatum): self.SubDatum = SubDatum
    def add_SubDatum(self, value): self.SubDatum.append(value)
    def insert_SubDatum(self, index, value): self.SubDatum[index] = value
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def hasContent_(self):
        if (
            self.Value is not None or
            self.SubDatum
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='MetadataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MetadataType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='MetadataType'):
        if self.type_ is not None:

            lwrite(' type=%s' % (self.gds_format_string(quote_attrib(self.type_), input_name='type'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='MetadataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            lwrite('<%sValue>%s</%sValue>%s' % ('cyboxCommon:', self.gds_format_string(quote_xml(self.Value), input_name='Value'), 'cyboxCommon:', eol_))
        for SubDatum_ in self.SubDatum:
            SubDatum_.export(lwrite, level, 'cyboxCommon:', name_='SubDatum', pretty_print=pretty_print)
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
        if nodeName_ == 'Value':
            Value_ = child_.text
            Value_ = self.gds_validate_string(Value_, node, 'Value')
            self.Value = Value_
        elif nodeName_ == 'SubDatum':
            obj_ = MetadataType.factory()
            obj_.build(child_)
            self.SubDatum.append(obj_)
# end class MetadataType

class EnvironmentVariableListType(GeneratedsSuper):
    """The EnvironmentVariableListType type is used for representing a list
    of environment variables."""

    subclass = None
    superclass = None
    def __init__(self, Environment_Variable=None):
        if Environment_Variable is None:
            self.Environment_Variable = []
        else:
            self.Environment_Variable = Environment_Variable
    def factory(*args_, **kwargs_):
        if EnvironmentVariableListType.subclass:
            return EnvironmentVariableListType.subclass(*args_, **kwargs_)
        else:
            return EnvironmentVariableListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Environment_Variable(self): return self.Environment_Variable
    def set_Environment_Variable(self, Environment_Variable): self.Environment_Variable = Environment_Variable
    def add_Environment_Variable(self, value): self.Environment_Variable.append(value)
    def insert_Environment_Variable(self, index, value): self.Environment_Variable[index] = value
    def hasContent_(self):
        if (
            self.Environment_Variable
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='EnvironmentVariableListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EnvironmentVariableListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='EnvironmentVariableListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='EnvironmentVariableListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Environment_Variable_ in self.Environment_Variable:
            Environment_Variable_.export(lwrite, level, 'cyboxCommon:', name_='Environment_Variable', pretty_print=pretty_print)
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
        if nodeName_ == 'Environment_Variable':
            obj_ = EnvironmentVariableType.factory()
            obj_.build(child_)
            self.Environment_Variable.append(obj_)
# end class EnvironmentVariableListType

class EnvironmentVariableType(GeneratedsSuper):
    """The EnvironmentVariableType type is used for representing
    environment variables using a name/value pair."""

    subclass = None
    superclass = None
    def __init__(self, Name=None, Value=None):
        self.Name = Name
        self.Value = Value
    def factory(*args_, **kwargs_):
        if EnvironmentVariableType.subclass:
            return EnvironmentVariableType.subclass(*args_, **kwargs_)
        else:
            return EnvironmentVariableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Value is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='EnvironmentVariableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EnvironmentVariableType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='EnvironmentVariableType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='EnvironmentVariableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'cyboxCommon:', name_='Name', pretty_print=pretty_print)
        if self.Value is not None:
            self.Value.export(lwrite, level, 'cyboxCommon:', name_='Value', pretty_print=pretty_print)
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
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Value':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Value(obj_)
# end class EnvironmentVariableType

class DigitalSignaturesType(GeneratedsSuper):
    """The DigitalSignaturesType is used for representing a list of digital
    signatures."""

    subclass = None
    superclass = None
    def __init__(self, Digital_Signature=None):
        if Digital_Signature is None:
            self.Digital_Signature = []
        else:
            self.Digital_Signature = Digital_Signature
    def factory(*args_, **kwargs_):
        if DigitalSignaturesType.subclass:
            return DigitalSignaturesType.subclass(*args_, **kwargs_)
        else:
            return DigitalSignaturesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Digital_Signature(self): return self.Digital_Signature
    def set_Digital_Signature(self, Digital_Signature): self.Digital_Signature = Digital_Signature
    def add_Digital_Signature(self, value): self.Digital_Signature.append(value)
    def insert_Digital_Signature(self, index, value): self.Digital_Signature[index] = value
    def hasContent_(self):
        if (
            self.Digital_Signature
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DigitalSignaturesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DigitalSignaturesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DigitalSignaturesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DigitalSignaturesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Digital_Signature_ in self.Digital_Signature:
            Digital_Signature_.export(lwrite, level, 'cyboxCommon:', name_='Digital_Signature', pretty_print=pretty_print)
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
        if nodeName_ == 'Digital_Signature':
            obj_ = DigitalSignatureInfoType.factory()
            obj_.build(child_)
            self.Digital_Signature.append(obj_)
# end class DigitalSignaturesType

class DigitalSignatureInfoType(GeneratedsSuper):
    """The DigitalSignatureInfoType type is used as a way to represent some
    of the basic information about a digital signature.Specifies
    whether the digital signature exists.Specifies if the digital
    signature is verified."""

    subclass = None
    superclass = None
    def __init__(self, signature_verified=None, signature_exists=None, Certificate_Issuer=None, Certificate_Subject=None, Signature_Description=None):
        self.signature_verified = _cast(bool, signature_verified)
        self.signature_exists = _cast(bool, signature_exists)
        self.Certificate_Issuer = Certificate_Issuer
        self.Certificate_Subject = Certificate_Subject
        self.Signature_Description = Signature_Description
    def factory(*args_, **kwargs_):
        if DigitalSignatureInfoType.subclass:
            return DigitalSignatureInfoType.subclass(*args_, **kwargs_)
        else:
            return DigitalSignatureInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Certificate_Issuer(self): return self.Certificate_Issuer
    def set_Certificate_Issuer(self, Certificate_Issuer): self.Certificate_Issuer = Certificate_Issuer
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def get_Certificate_Subject(self): return self.Certificate_Subject
    def set_Certificate_Subject(self, Certificate_Subject): self.Certificate_Subject = Certificate_Subject
    def get_Signature_Description(self): return self.Signature_Description
    def set_Signature_Description(self, Signature_Description): self.Signature_Description = Signature_Description
    def get_signature_verified(self): return self.signature_verified
    def set_signature_verified(self, signature_verified): self.signature_verified = signature_verified
    def get_signature_exists(self): return self.signature_exists
    def set_signature_exists(self, signature_exists): self.signature_exists = signature_exists
    def hasContent_(self):
        if (
            self.Certificate_Issuer is not None or
            self.Certificate_Subject is not None or
            self.Signature_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='DigitalSignatureInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DigitalSignatureInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='DigitalSignatureInfoType'):
        if self.signature_verified is not None:

            lwrite(' signature_verified="%s"' % self.gds_format_boolean(self.signature_verified, input_name='signature_verified'))
        if self.signature_exists is not None:

            lwrite(' signature_exists="%s"' % self.gds_format_boolean(self.signature_exists, input_name='signature_exists'))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='DigitalSignatureInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Certificate_Issuer is not None:
            self.Certificate_Issuer.export(lwrite, level, 'cyboxCommon:', name_='Certificate_Issuer', pretty_print=pretty_print)
        if self.Certificate_Subject is not None:
            self.Certificate_Subject.export(lwrite, level, 'cyboxCommon:', name_='Certificate_Subject', pretty_print=pretty_print)
        if self.Signature_Description is not None:
            self.Signature_Description.export(lwrite, level, 'cyboxCommon:', name_='Signature_Description', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('signature_verified', node)
        if value is not None:

            if value in ('true', '1'):
                self.signature_verified = True
            elif value in ('false', '0'):
                self.signature_verified = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('signature_exists', node)
        if value is not None:

            if value in ('true', '1'):
                self.signature_exists = True
            elif value in ('false', '0'):
                self.signature_exists = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Certificate_Issuer':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Certificate_Issuer(obj_)
        elif nodeName_ == 'Certificate_Subject':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Certificate_Subject(obj_)
        elif nodeName_ == 'Signature_Description':
            obj_ = StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature_Description(obj_)
# end class DigitalSignatureInfoType

class PatternableFieldType(GeneratedsSuper):
    """The PatternableFieldType is a grouping of attributes applicable to
    defining patterns on a specific field."""

    subclass = None
    superclass = None
    def __init__(self, pattern_type=None, has_changed=None, trend=None, apply_condition='ANY', bit_mask=None, regex_syntax=None, condition=None, is_case_sensitive=True, delimiter='##comma##', valueOf_=None, extensiontype_=None):
        self.pattern_type = _cast(None, pattern_type)
        self.has_changed = _cast(bool, has_changed)
        self.trend = _cast(bool, trend)
        self.apply_condition = _cast(None, apply_condition)
        self.bit_mask = _cast(None, bit_mask)
        self.regex_syntax = _cast(None, regex_syntax)
        self.condition = _cast(None, condition)
        self.is_case_sensitive = _cast(bool, is_case_sensitive)
        self.delimiter = _cast(None, delimiter)
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if PatternableFieldType.subclass:
            return PatternableFieldType.subclass(*args_, **kwargs_)
        else:
            return PatternableFieldType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_pattern_type(self): return self.pattern_type
    def set_pattern_type(self, pattern_type): self.pattern_type = pattern_type
    def get_has_changed(self): return self.has_changed
    def set_has_changed(self, has_changed): self.has_changed = has_changed
    def get_trend(self): return self.trend
    def set_trend(self, trend): self.trend = trend
    def get_apply_condition(self): return self.apply_condition
    def set_apply_condition(self, apply_condition): self.apply_condition = apply_condition
    def get_bit_mask(self): return self.bit_mask
    def set_bit_mask(self, bit_mask): self.bit_mask = bit_mask
    def get_regex_syntax(self): return self.regex_syntax
    def set_regex_syntax(self, regex_syntax): self.regex_syntax = regex_syntax
    def get_condition(self): return self.condition
    def set_condition(self, condition): self.condition = condition
    def get_is_case_sensitive(self): return self.is_case_sensitive
    def set_is_case_sensitive(self, is_case_sensitive): self.is_case_sensitive = is_case_sensitive
    def get_delimiter(self): return self.delimiter
    def set_delimiter(self, delimiter): self.delimiter = delimiter
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PatternableFieldType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PatternableFieldType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PatternableFieldType'):
        if self.pattern_type is not None:

            lwrite(' pattern_type=%s' % (quote_attrib(self.pattern_type), ))
        if self.has_changed is not None:

            lwrite(' has_changed="%s"' % self.gds_format_boolean(self.has_changed, input_name='has_changed'))
        if self.trend is not None:

            lwrite(' trend="%s"' % self.gds_format_boolean(self.trend, input_name='trend'))
            # Only add 'apply_condition' if 'condition' is set, and the value
            # appears to be a list (by presence of a comma)
            if (self.apply_condition is not None and self.valueOf_ is not None and ',' in self.valueOf_
                    and 'apply_condition' not in already_processed):

                lwrite(' apply_condition=%s' % (quote_attrib(self.apply_condition), ))
        if self.bit_mask is not None:

            lwrite(' bit_mask=%s' % (self.gds_format_string(quote_attrib(self.bit_mask), input_name='bit_mask'), ))
        if self.regex_syntax is not None:

            lwrite(' regex_syntax=%s' % (self.gds_format_string(quote_attrib(self.regex_syntax), input_name='regex_syntax'), ))
        if self.condition is not None:

            lwrite(' condition=%s' % (quote_attrib(self.condition), ))
        if self.is_case_sensitive not in (None, True):

            lwrite(' is_case_sensitive="%s"' % self.gds_format_boolean(self.is_case_sensitive, input_name='is_case_sensitive'))
        if self.delimiter not in (None, "##comma##"):

            lwrite(' delimiter=%s' % (self.gds_format_string(quote_attrib(self.delimiter), input_name='delimiter'), ))
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PatternableFieldType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('pattern_type', node)
        if value is not None:

            self.pattern_type = value
        value = find_attr_value_('has_changed', node)
        if value is not None:

            if value in ('true', '1'):
                self.has_changed = True
            elif value in ('false', '0'):
                self.has_changed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('trend', node)
        if value is not None:

            if value in ('true', '1'):
                self.trend = True
            elif value in ('false', '0'):
                self.trend = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('apply_condition', node)
        if value is not None:

            self.apply_condition = value
        value = find_attr_value_('bit_mask', node)
        if value is not None:

            self.bit_mask = value
        value = find_attr_value_('regex_syntax', node)
        if value is not None:

            self.regex_syntax = value
        value = find_attr_value_('condition', node)
        if value is not None:

            self.condition = value
        value = find_attr_value_('is_case_sensitive', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_case_sensitive = True
            elif value in ('false', '0'):
                self.is_case_sensitive = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('delimiter', node)
        if value is not None:

            self.delimiter = value
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PatternableFieldType

class ControlledVocabularyStringType(PatternableFieldType):
    """The ControlledVocabularyStringType is used as the basis for defining
    controlled vocabularies.The vocab_name field specifies the name
    of the controlled vocabulary.The vocab_reference field specifies
    the URI to the location of where the controlled vocabulary is
    defined, e.g., in an externally located XML schema file."""

    subclass = None
    superclass = PatternableFieldType
    def __init__(self, pattern_type=None, has_changed=None, trend=None, apply_condition='ANY', bit_mask=None, regex_syntax=None, condition=None, is_case_sensitive=True, delimiter='##comma##', vocab_reference=None, vocab_name=None, valueOf_=None, xsi_type=None):
        super(ControlledVocabularyStringType, self).__init__(pattern_type, has_changed, trend, apply_condition, bit_mask, regex_syntax, condition, is_case_sensitive, delimiter, valueOf_, )
        self.vocab_reference = _cast(None, vocab_reference)
        self.vocab_name = _cast(None, vocab_name)
        self.valueOf_ = valueOf_
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if ControlledVocabularyStringType.subclass:
            return ControlledVocabularyStringType.subclass(*args_, **kwargs_)
        else:
            return ControlledVocabularyStringType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_vocab_reference(self): return self.vocab_reference
    def set_vocab_reference(self, vocab_reference): self.vocab_reference = vocab_reference
    def get_vocab_name(self): return self.vocab_name
    def set_vocab_name(self, vocab_name): self.vocab_name = vocab_name
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (
            self.valueOf_ or
            self.xsi_type is not None or
            super(ControlledVocabularyStringType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='ControlledVocabularyStringType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ControlledVocabularyStringType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='ControlledVocabularyStringType'):
        super(ControlledVocabularyStringType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ControlledVocabularyStringType')
        if self.vocab_reference is not None:

            lwrite(' vocab_reference=%s' % (self.gds_format_string(quote_attrib(self.vocab_reference), input_name='vocab_reference'), ))
        if self.vocab_name is not None:

            lwrite(' vocab_name=%s' % (self.gds_format_string(quote_attrib(self.vocab_name), input_name='vocab_name'), ))
        if self.xsi_type is not None:

            lwrite(' xsi:type=%s' % (self.gds_format_string(quote_attrib(self.xsi_type), input_name='xsi:type'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='ControlledVocabularyStringType', fromsubclass_=False, pretty_print=True):
        super(ControlledVocabularyStringType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('vocab_reference', node)
        if value is not None:
            self.vocab_reference = value
        value = find_attr_value_('vocab_name', node)
        if value is not None:
            self.vocab_name = value
        value = find_attr_value_('xsi:type', node)
        if value is not None:
            self.xsi_type = value
        super(ControlledVocabularyStringType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ControlledVocabularyStringType

class SIDType(BaseObjectPropertyType):
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(SIDType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if SIDType.subclass:
            return SIDType.subclass(*args_, **kwargs_)
        else:
            return SIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SIDType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='SIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SIDType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='SIDType'):
        super(SIDType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SIDType')
#        if self.datatype is not None:
#
#            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='SIDType', fromsubclass_=False, pretty_print=True):
        super(SIDType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(SIDType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SIDType

class PropertyType(BaseObjectPropertyType):
    """The PropertyType is a type representing the specification of a
    single Object Property.The name field specifies a name for this
    property.A description of what this property represents."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None, name=None, description=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(PropertyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        self.name = _cast(None, name)
        self.description = _cast(None, description)
    def factory(*args_, **kwargs_):
        if PropertyType.subclass:
            return PropertyType.subclass(*args_, **kwargs_)
        else:
            return PropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PropertyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='PropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PropertyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='PropertyType'):
        super(PropertyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PropertyType')
        if self.name is not None:

            lwrite(' name=%s' % (self.gds_format_string(quote_attrib(self.name), input_name='name'), ))
        if self.description is not None:

            lwrite(' description=%s' % (self.gds_format_string(quote_attrib(self.description), input_name='description'), ))
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='PropertyType', fromsubclass_=False, pretty_print=True):
        super(PropertyType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('name', node)
        if value is not None:

            self.name = value
        value = find_attr_value_('description', node)
        if value is not None:

            self.description = value
        super(PropertyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PropertyType

class CompensationModelType(BaseObjectPropertyType):
    """The CompensationModelType characterizes the compensation model for a
    tool.This attribute is optional and specifies the expected type
    for the value of the specified property."""
    subclass = None
    superclass = BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(CompensationModelType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if CompensationModelType.subclass:
            return CompensationModelType.subclass(*args_, **kwargs_)
        else:
            return CompensationModelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CompensationModelType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='cyboxCommon:', name_='CompensationModelType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompensationModelType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='cyboxCommon:', name_='CompensationModelType'):
        super(CompensationModelType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CompensationModelType')
    def exportChildren(self, lwrite, level, namespace_='cyboxCommon:', name_='CompensationModelType', fromsubclass_=False, pretty_print=True):
        super(CompensationModelType, self).exportChildren(lwrite, level, 'cyboxCommon:', name_, True, pretty_print=pretty_print)
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
        super(CompensationModelType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CompensationModelType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MeasureSourceType'
        rootClass = MeasureSourceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj


def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MeasureSourceType'
        rootClass = MeasureSourceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="MeasureSourceType",
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
    "MeasureSourceType",
    "ContributorType",
    "DateRangeType",
    "PersonnelType",
    "TimeType",
    "ToolSpecificDataType",
    "ToolsInformationType",
    "ToolInformationType",
    "CompensationModelType",
    "ToolReferencesType",
    "ToolReferenceType",
    "ToolConfigurationType",
    "ConfigurationSettingsType",
    "ConfigurationSettingType",
    "DependenciesType",
    "DependencyType",
    "UsageContextAssumptionsType",
    "InternationalizationSettingsType",
    "InternalStringsType",
    "BuildInformationType",
    "BuildUtilityType",
    "CompilersType",
    "CompilerType",
    "CompilerInformalDescriptionType",
    "BuildConfigurationType",
    "LibrariesType",
    "LibraryType",
    "ExecutionEnvironmentType",
    "ErrorsType",
    "ErrorType",
    "ErrorInstancesType",
    "ObjectPropertiesType",
    "CustomPropertiesType",
    "PropertyType",
    "BaseObjectPropertyType",
    "IntegerObjectPropertyType",
    "StringObjectPropertyType",
    "NameObjectPropertyType",
    "DateObjectPropertyRestrictionType",
    "DateObjectPropertyType",
    "DateTimeObjectPropertyRestrictionType",
    "DateTimeObjectPropertyType",
    "FloatObjectPropertyType",
    "DoubleObjectPropertyType",
    "UnsignedLongObjectPropertyType",
    "UnsignedIntegerObjectPropertyType",
    "PositiveIntegerObjectPropertyType",
    "HexBinaryObjectPropertyType",
    "LongObjectPropertyType",
    "NonNegativeIntegerObjectPropertyType",
    "AnyURIObjectPropertyType",
    "DurationObjectPropertyType",
    "TimeObjectPropertyRestrictionType",
    "TimeObjectPropertyType",
    "Base64BinaryObjectPropertyType",
    "LocationType",
    "ExtractedFeaturesType",
    "ExtractedStringsType",
    "ExtractedStringType",
    "ImportsType",
    "FunctionsType",
    "CodeSnippetsType",
    "ByteRunsType",
    "ByteRunType",
    "HashListType",
    "HashValueType",
    "SimpleHashValueType",
    "FuzzyHashValueType",
    "FuzzyHashStructureType",
    "FuzzyHashBlockType",
    "HashSegmentsType",
    "HashSegmentType",
    "HashType",
    "StructuredTextType",
    "DataSegmentType",
    "DataSizeType",
    "PlatformSpecificationType",
    "PlatformIdentifierType",
    "MetadataType",
    "EnvironmentVariableListType",
    "EnvironmentVariableType",
    "DigitalSignaturesType",
    "DigitalSignatureInfoType",
    "PatternableFieldType",
    "ControlledVocabularyStringType",
    "DateWithPrecisionType",
    "DateTimeWithPrecisionType",
    "SIDType",
    "Layer4ProtocolType",
    "EndiannessType",
    "CipherType",
    "RegionalRegistryType"
    ]
