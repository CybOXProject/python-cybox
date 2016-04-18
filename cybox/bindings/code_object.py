# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class CodeSegmentXORType(cybox_common.StringObjectPropertyType):
    """Used to encapsulate a segment of code that has been XORed with a
    pattern in order to avoid tripping anti-virus detection.The
    xor_pattern field contains a 16-hexadecimal-character hex
    string, which represents the pattern that the Code_Segment_XOR
    field should be XORed with in order to recover the actual code.
    The default value is 55AA55AA55AA55BB, as specified by IETF RFC
    5901."""

    subclass = None
    superclass = cybox_common.StringObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, xor_pattern='55AA55AA55AA55BB', valueOf_=None):
        super(CodeSegmentXORType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.xor_pattern = _cast(None, xor_pattern)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CodeSegmentXORType.subclass:
            return CodeSegmentXORType.subclass(*args_, **kwargs_)
        else:
            return CodeSegmentXORType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_xor_pattern(self): return self.xor_pattern
    def set_xor_pattern(self, xor_pattern): self.xor_pattern = xor_pattern
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CodeSegmentXORType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='CodeSegmentXORType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeSegmentXORType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='CodeSegmentXORType'):
        super(CodeSegmentXORType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeSegmentXORType')
        if self.xor_pattern is not None:

            lwrite(' xor_pattern=%s' % (self.gds_format_string(quote_attrib(self.xor_pattern), input_name='xor_pattern'), ))
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='CodeSegmentXORType', fromsubclass_=False, pretty_print=True):
        super(CodeSegmentXORType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('xor_pattern', node)
        if value is not None:
            self.xor_pattern = value
        super(CodeSegmentXORType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CodeSegmentXORType

class TargetedPlatformsType(GeneratedsSuper):
    """A list of targeted platforms"""

    subclass = None
    superclass = None
    def __init__(self, Targeted_Platform=None):
        if Targeted_Platform is None:
            self.Targeted_Platform = []
        else:
            self.Targeted_Platform = Targeted_Platform
    def factory(*args_, **kwargs_):
        if TargetedPlatformsType.subclass:
            return TargetedPlatformsType.subclass(*args_, **kwargs_)
        else:
            return TargetedPlatformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Targeted_Platform(self): return self.Targeted_Platform
    def set_Targeted_Platform(self, Targeted_Platform): self.Targeted_Platform = Targeted_Platform
    def add_Targeted_Platform(self, value): self.Targeted_Platform.append(value)
    def insert_Targeted_Platform(self, index, value): self.Targeted_Platform[index] = value
    def hasContent_(self):
        if (
            self.Targeted_Platform
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='TargetedPlatformsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TargetedPlatformsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='TargetedPlatformsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='TargetedPlatformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Targeted_Platform_ in self.Targeted_Platform:
            Targeted_Platform_.export(lwrite, level, 'CodeObj:', name_='Targeted_Platform', pretty_print=pretty_print)
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
        if nodeName_ == 'Targeted_Platform':
            obj_ = cybox_common.PlatformSpecificationType.factory()
            obj_.build(child_)
            self.Targeted_Platform.append(obj_)
# end class TargetedPlatformsType

class ProcessorTypeType(cybox_common.BaseObjectPropertyType):
    """ProcessorTypeType specifies relevant processor families, via a union
    of the ProcessorTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ProcessorTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ProcessorTypeType.subclass:
            return ProcessorTypeType.subclass(*args_, **kwargs_)
        else:
            return ProcessorTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ProcessorTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='ProcessorTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessorTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='ProcessorTypeType'):
        super(ProcessorTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessorTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='ProcessorTypeType', fromsubclass_=False, pretty_print=True):
        super(ProcessorTypeType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
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
        super(ProcessorTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ProcessorTypeType

class CodeLanguageType(cybox_common.BaseObjectPropertyType):
    """CodeLanguageType specifies languages of code, via a union of the
    CodeLanguageEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    field is optional and specifies the expected type for the value
    of the specified field."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(CodeLanguageType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CodeLanguageType.subclass:
            return CodeLanguageType.subclass(*args_, **kwargs_)
        else:
            return CodeLanguageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CodeLanguageType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='CodeLanguageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeLanguageType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='CodeLanguageType'):
        super(CodeLanguageType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeLanguageType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='CodeLanguageType', fromsubclass_=False, pretty_print=True):
        super(CodeLanguageType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
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
        super(CodeLanguageType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CodeLanguageType

class CodePurposeType(cybox_common.BaseObjectPropertyType):
    """CodePurposeType specifies intended purposes of code, via a union of
    the CodePurposeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    field is optional and specifies the expected type for the value
    of the specified field."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(CodePurposeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CodePurposeType.subclass:
            return CodePurposeType.subclass(*args_, **kwargs_)
        else:
            return CodePurposeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CodePurposeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='CodePurposeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodePurposeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='CodePurposeType'):
        super(CodePurposeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CodePurposeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='CodePurposeType', fromsubclass_=False, pretty_print=True):
        super(CodePurposeType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
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
        super(CodePurposeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CodePurposeType

class CodeTypeType(cybox_common.BaseObjectPropertyType):
    """CodeTypeType specifies types of code, via a union of the
    CodeTypeEnum type and the atomic xs:string type. Its base type
    is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This field is
    optional and specifies the expected type for the value of the
    specified field."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(CodeTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CodeTypeType.subclass:
            return CodeTypeType.subclass(*args_, **kwargs_)
        else:
            return CodeTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(CodeTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='CodeTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='CodeTypeType'):
        super(CodeTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='CodeTypeType', fromsubclass_=False, pretty_print=True):
        super(CodeTypeType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
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
        super(CodeTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CodeTypeType

class CodeObjectType(cybox_common.ObjectPropertiesType):
    """The CodeObjectType type is intended to characterize a body of
    computer code."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Description=None, Type=None, Purpose=None, Code_Language=None, Targeted_Platforms=None, Processor_Family=None, Discovery_Method=None, Start_Address=None, Code_Segment=None, Code_Segment_XOR=None, Digital_Signatures=None, Extracted_Features=None):
        super(CodeObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Description = Description
        self.Type = Type
        self.Purpose = Purpose
        self.Code_Language = Code_Language
        self.Targeted_Platforms = Targeted_Platforms
        if Processor_Family is None:
            self.Processor_Family = []
        else:
            self.Processor_Family = Processor_Family
        self.Discovery_Method = Discovery_Method
        self.Start_Address = Start_Address
        self.Code_Segment = Code_Segment
        self.Code_Segment_XOR = Code_Segment_XOR
        self.Digital_Signatures = Digital_Signatures
        self.Extracted_Features = Extracted_Features
    def factory(*args_, **kwargs_):
        if CodeObjectType.subclass:
            return CodeObjectType.subclass(*args_, **kwargs_)
        else:
            return CodeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_CodeTypeType(self, value):
        # Validate type CodeTypeType, a restriction on None.
        pass
    def get_Purpose(self): return self.Purpose
    def set_Purpose(self, Purpose): self.Purpose = Purpose
    def validate_CodePurposeType(self, value):
        # Validate type CodePurposeType, a restriction on None.
        pass
    def get_Code_Language(self): return self.Code_Language
    def set_Code_Language(self, Code_Language): self.Code_Language = Code_Language
    def validate_CodeLanguageType(self, value):
        # Validate type CodeLanguageType, a restriction on None.
        pass
    def get_Targeted_Platforms(self): return self.Targeted_Platforms
    def set_Targeted_Platforms(self, Targeted_Platforms): self.Targeted_Platforms = Targeted_Platforms
    def get_Processor_Family(self): return self.Processor_Family
    def set_Processor_Family(self, Processor_Family): self.Processor_Family = Processor_Family
    def add_Processor_Family(self, value): self.Processor_Family.append(value)
    def validate_ProcessorTypeType(self, value):
        # Validate type ProcessorTypeType, a restriction on None.
        pass
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def get_Start_Address(self): return self.Start_Address
    def set_Start_Address(self, Start_Address): self.Start_Address = Start_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Code_Segment(self): return self.Code_Segment
    def set_Code_Segment(self, Code_Segment): self.Code_Segment = Code_Segment
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Code_Segment_XOR(self): return self.Code_Segment_XOR
    def set_Code_Segment_XOR(self, Code_Segment_XOR): self.Code_Segment_XOR = Code_Segment_XOR
    def get_Digital_Signatures(self): return self.Digital_Signatures
    def set_Digital_Signatures(self, Digital_Signatures): self.Digital_Signatures = Digital_Signatures
    def get_Extracted_Features(self): return self.Extracted_Features
    def set_Extracted_Features(self, Extracted_Features): self.Extracted_Features = Extracted_Features
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Type is not None or
            self.Purpose is not None or
            self.Code_Language is not None or
            self.Targeted_Platforms is not None or
            self.Processor_Family or
            self.Discovery_Method is not None or
            self.Start_Address is not None or
            self.Code_Segment is not None or
            self.Code_Segment_XOR is not None or
            self.Digital_Signatures is not None or
            self.Extracted_Features is not None or
            super(CodeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='CodeObj:', name_='CodeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='CodeObj:', name_='CodeObjectType'):
        super(CodeObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CodeObjectType')
    def exportChildren(self, lwrite, level, namespace_='CodeObj:', name_='CodeObjectType', fromsubclass_=False, pretty_print=True):
        super(CodeObjectType, self).exportChildren(lwrite, level, 'CodeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, 'CodeObj:', name_='Description', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'CodeObj:', name_='Type', pretty_print=pretty_print)
        if self.Purpose is not None:
            self.Purpose.export(lwrite, level, 'CodeObj:', name_='Purpose', pretty_print=pretty_print)
        if self.Code_Language is not None:
            self.Code_Language.export(lwrite, level, 'CodeObj:', name_='Code_Language', pretty_print=pretty_print)
        if self.Targeted_Platforms is not None:
            self.Targeted_Platforms.export(lwrite, level, 'CodeObj:', name_='Targeted_Platforms', pretty_print=pretty_print)
        for Processor_Family_ in self.Processor_Family:
            Processor_Family_.export(lwrite, level, 'CodeObj:', name_='Processor_Family', pretty_print=pretty_print)
        if self.Discovery_Method is not None:
            self.Discovery_Method.export(lwrite, level, 'CodeObj:', name_='Discovery_Method', pretty_print=pretty_print)
        if self.Start_Address is not None:
            self.Start_Address.export(lwrite, level, 'CodeObj:', name_='Start_Address', pretty_print=pretty_print)
        if self.Code_Segment is not None:
            self.Code_Segment.export(lwrite, level, 'CodeObj:', name_='Code_Segment', pretty_print=pretty_print)
        if self.Code_Segment_XOR is not None:
            self.Code_Segment_XOR.export(lwrite, level, 'CodeObj:', name_='Code_Segment_XOR', pretty_print=pretty_print)
        if self.Digital_Signatures is not None:
            self.Digital_Signatures.export(lwrite, level, 'CodeObj:', name_='Digital_Signatures', pretty_print=pretty_print)
        if self.Extracted_Features is not None:
            self.Extracted_Features.export(lwrite, level, 'CodeObj:', name_='Extracted_Features', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(CodeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Type':
            obj_ = CodeTypeType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Purpose':
            obj_ = CodePurposeType.factory()
            obj_.build(child_)
            self.set_Purpose(obj_)
        elif nodeName_ == 'Code_Language':
            obj_ = CodeLanguageType.factory()
            obj_.build(child_)
            self.set_Code_Language(obj_)
        elif nodeName_ == 'Targeted_Platforms':
            obj_ = TargetedPlatformsType.factory()
            obj_.build(child_)
            self.set_Targeted_Platforms(obj_)
        elif nodeName_ == 'Processor_Family':
            obj_ = ProcessorTypeType.factory()
            obj_.build(child_)
            self.Processor_Family.append(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Discovery_Method(obj_)
        elif nodeName_ == 'Start_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Start_Address(obj_)
        elif nodeName_ == 'Code_Segment':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Code_Segment(obj_)
        elif nodeName_ == 'Code_Segment_XOR':
            obj_ = CodeSegmentXORType.factory()
            obj_.build(child_)
            self.set_Code_Segment_XOR(obj_)
        elif nodeName_ == 'Digital_Signatures':
            obj_ = cybox_common.DigitalSignaturesType.factory()
            obj_.build(child_)
            self.set_Digital_Signatures(obj_)
        elif nodeName_ == 'Extracted_Features':
            obj_ = cybox_common.ExtractedFeaturesType.factory()
            obj_.build(child_)
            self.set_Extracted_Features(obj_)
        super(CodeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class CodeObjectType

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
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Code_Segment': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Targeted_Platform': cybox_common.PlatformSpecificationType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Byte_Run': cybox_common.ByteRunType,
    'Libraries': cybox_common.LibrariesType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Start_Address': cybox_common.HexBinaryObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Discovery_Method': cybox_common.MeasureSourceType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
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
        rootTag = 'Code_Object'
        rootClass = CodeObjectType
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
        rootTag = 'Code_Object'
        rootClass = CodeObjectType
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
        rootTag = 'Code_Object'
        rootClass = CodeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Code_Object",
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
    "CodeObjectType",
    "CodeTypeType",
    "CodeSegmentXORType",
    "CodePurposeType",
    "CodeLanguageType",
    "ProcessorTypeType",
    "TargetedPlatformsType"
    ]
