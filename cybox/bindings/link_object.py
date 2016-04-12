# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import uri_object


class URLLabelType(cybox_common.StringObjectPropertyType):

    subclass = None
    superclass = None
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(URLLabelType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
        pass
    def factory(*args_, **kwargs_):
        if URLLabelType.subclass:
            return URLLabelType.subclass(*args_, **kwargs_)
        else:
            return URLLabelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            super(URLLabelType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='LinkObj:', name_='URL_Label', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='URLLabelType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='LinkObj:', name_='URLLabelType'):
        super(URLLabelType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='URLLabelType')
    def exportChildren(self, lwrite, level, namespace_='LinkObj:', name_='URLLabelType', fromsubclass_=False, pretty_print=True):
        super(URLLabelType, self).exportChildren(lwrite, level, 'LinkObj:', name_, True, pretty_print=pretty_print)
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
        super(URLLabelType, self).buildAttributes(node, attrs, already_processed)
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(URLLabelType, self).buildChildren(child_, node, nodeName_, True)
        pass
# End URLLabelType

class LinkObjectType(uri_object.URIObjectType):
    """The Link Object is intended to characterize links, such as those on
        a webpage or in an e-mail message."""
    subclass = None
    superclass = uri_object.URIObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, type_=None, Value=None, URL_Label=None):
        super(LinkObjectType, self).__init__(object_reference, Custom_Properties, type_, Value, )
        self.URL_Label = URL_Label
    def factory(*args_, **kwargs_):
        if LinkObjectType.subclass:
            return LinkObjectType.subclass(*args_, **kwargs_)
        else:
            return LinkObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_URL_Label(self): return self.URL_Label
    def set_URL_Label(self, URL_Label): self.URL_Label = URL_Label
    def validate_StringObjectPropertyType(self, value):
        # Validate type StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.URL_Label is not None or
            super(LinkObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='LinkObj:', name_='LinkObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, 'LinkObj:', name_='LinkObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, 'LinkObj:', name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='LinkObj:', name_='LinkObjectType'):
        super(LinkObjectType, self).exportAttributes(lwrite, level, already_processed, 'LinkObj:', name_='LinkObjectType')
    def exportChildren(self, lwrite, level, namespace_='LinkObj:', name_='LinkObjectType', fromsubclass_=False, pretty_print=True):
        super(LinkObjectType, self).exportChildren(lwrite, level, 'LinkObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.URL_Label is not None:
            self.URL_Label.export(lwrite, level, 'LinkObj:', name_='URL_Label', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(LinkObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'URL_Label':
            obj_ = URLLabelType.factory()
            obj_.build(child_)
            self.set_URL_Label(obj_)
        super(LinkObjectType, self).buildChildren(child_, node, nodeName_, True)

# end class LinkObjectType

GDSClassesMapping = {
    'URI': uri_object.URIObjectType,
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
        rootTag = 'Link'
        rootClass = LinkObjectType
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
        rootTag = 'Link'
        rootClass = LinkObjectType
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
        rootTag = 'Link'
        rootClass = LinkObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Link",
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
    "LinkObjectType"
    ]
