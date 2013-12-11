#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#
# Generated Mon Apr 08 15:04:49 2013 by generateDS.py version 2.9a.
#

import sys
import getopt
import re as re_

import cybox_common
import base64
from datetime import datetime, tzinfo, timedelta
from cybox.bindings.cybox_common import ControlledVocabularyStringType
#Object Imports
try:
    from cybox.bindings.win_kernel_object import WindowsKernelObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_user_account_object import WindowsUserAccountObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_file_object import WindowsFileObjectType
except ImportError:
    pass
try:
    from cybox.bindings.port_object import PortObjectType
except ImportError:
    pass
try:
    from cybox.bindings.process_object import ProcessObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_user_account_object import UnixUserAccountObjectType
except ImportError:
    pass
try:
    from cybox.bindings.linux_package_object import LinuxPackageObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_packet_object import NetworkPacketType
except ImportError:
    pass
try:
    from cybox.bindings.disk_partition_object import DiskPartitionObjectType
except ImportError:
    pass
try:
    from cybox.bindings.pipe_object import PipeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.device_object import DeviceObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_volume_object import UnixVolumeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.dns_cache_object import DNSCacheEntryType
except ImportError:
    pass
try:
    from cybox.bindings.win_kernel_hook_object import WindowsKernelHookObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_process_object import UnixProcessObjectType
except ImportError:
    pass
try:
    from cybox.bindings.artifact_object import ArtifactObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_task_object import WindowsTaskObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_registry_key_object import WindowsRegistryKeyObjectType
except ImportError:
    pass
try:
    from cybox.bindings.uri_object import URIObjectType
except ImportError:
    pass
try:
    from cybox.bindings.memory_object import MemoryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.file_object import FileObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_pipe_object import WindowsPipeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_socket_object import NetworkSocketObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_thread_object import WindowsThreadObjectType
except ImportError:
    pass
try:
    from cybox.bindings.x509_certificate_object import X509CertificateObjectType
except ImportError:
    pass
try:
    from cybox.bindings.library_object import LibraryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_process_object import WindowsProcessObjectType
except ImportError:
    pass
try:
    from cybox.bindings.link_object import LinkObjectType
except ImportError:
    pass
try:
    from cybox.bindings.account_object import AccountObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_route_object import NetRouteObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_driver_object import WindowsDriverObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_event_object import WindowsEventObjectType
except ImportError:
    pass
try:
    from cybox.bindings.socket_address_object import SocketAddressObjectType
except ImportError:
    pass
try:
    from cybox.bindings.address_object import AddressObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_network_route_entry_object import WindowsNetworkRouteEntryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.http_session_object import HTTPSessionObjectType
except ImportError:
    pass
try:
    from cybox.bindings.whois_object import WhoisObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_file_object import UnixFileObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_event_log_object import WindowsEventLogObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_flow_object import NetworkFlowObjectType
except ImportError:
    pass
try:
    from cybox.bindings.mutex_object import MutexObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_connection_object import NetworkConnectionObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_semaphore_object import WindowsSemaphoreObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_system_restore_object import WindowsSystemRestoreObjectType
except ImportError:
    pass
try:
    from cybox.bindings.custom_object import CustomObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_service_object import WindowsServiceObjectType
except ImportError:
    pass
try:
    from cybox.bindings.semaphore_object import SemaphoreObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_computer_account_object import WinComputerAccountObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_waitable_timer_object import WindowsWaitableTimerObjectType
except ImportError:
    pass
try:
    from cybox.bindings.gui_object import GUIObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_volume_object import WindowsVolumeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_network_share_object import WindowsNetworkShareObjectType
except ImportError:
    pass
try:
    from cybox.bindings.user_account_object import UserAccountObjectType
except ImportError:
    pass
try:
    from cybox.bindings.gui_dialogbox_object import GUIDialogboxObjectType
except ImportError:
    pass
try:
    from cybox.bindings.dns_record_object import DNSRecordObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_system_object import WindowsSystemObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_memory_page_region_object import WindowsMemoryPageRegionObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_prefetch_object import WindowsPrefetchObjectType
except ImportError:
    pass
try:
    from cybox.bindings.volume_object import VolumeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_network_route_entry_object import UnixNetworkRouteEntryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.api_object import APIObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_route_entry_object import NetworkRouteEntryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.system_object import SystemObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_critical_section_object import WinCriticalSectionObjectType
except ImportError:
    pass
try:
    from cybox.bindings.pdf_file_object import PDFFileObjectType
except ImportError:
    pass
try:
    from cybox.bindings.unix_pipe_object import UnixPipeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_executable_file_object import WindowsExecutableFileObjectType
except ImportError:
    pass
try:
    from cybox.bindings.code_object import CodeObjectType
except ImportError:
    pass
try:
    from cybox.bindings.disk_object import DiskObjectType
except ImportError:
    pass
try:
    from cybox.bindings.gui_window_object import GUIWindowObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_mutex_object import WindowsMutexObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_mailslot_object import WindowsMailslotObjectType
except ImportError:
    pass
try:
    from cybox.bindings.email_message_object import EmailMessageObjectType
except ImportError:
    pass
try:
    from cybox.bindings.network_subnet_object import NetworkSubnetObjectType
except ImportError:
    pass
try:
    from cybox.bindings.dns_query_object import DNSQueryObjectType
except ImportError:
    pass
try:
    from cybox.bindings.win_handle_object import WindowsHandleObjectType
except ImportError:
    pass

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser(huge_tree=True)
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(tzinfo):
            def __init__(self, offset, name):
                self.__offset = timedelta(minutes = offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node,
                        'Requires sequence of booleans '
                        '("true", "1", "false", "0")')
            return input_data
        def gds_validate_datetime(self, input_data, node, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if isinstance(input_data, basestring):
                return input_data
            if input_data.microsecond == 0:
                _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S')
            else:
                _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S.%f')
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_parse_datetime(self, input_data, node, input_name=''):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime.strptime(
                        input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime.strptime(
                        input_data, '%Y-%m-%dT%H:%M:%S')
            return dt.replace(tzinfo = tz)

        def gds_validate_date(self, input_data, node, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            if isinstance(input_data, basestring):
                return input_data
            _svalue = input_data.strftime('%Y-%m-%d')
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_parse_date(self, input_data, node, input_name=''):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            return datetime.strptime(input_data,
                '%Y-%m-%d').replace(tzinfo = tz)
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return unicode(s1).encode(ExternalEncoding)

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return unicode(s1).encode(ExternalEncoding)

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (
            msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' %
                (self.name, base64.b64encode(self.value), self.name))
    def to_etree(self, element):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class ObservablesType(GeneratedsSuper):
    """The ObservablesType is a type representing a collection of cyber
    observables.The cybox_major_version field specifies the major
    version of the CybOX language utilized for this set of
    Observables.The cybox_minor_version field specifies the minor
    version of the CybOX language utilized for this set of
    Observables.The cybox_update_version field specifies the update
    version of the CybOX language utilized for this set of
    Observables. This field MUST be used when using an update
    version of CybOX."""
    subclass = None
    superclass = None
    def __init__(self, cybox_major_version="2", cybox_minor_version="0", cybox_update_version="1", Observable_Package_Source=None, Observable=None, Pools=None):
        self.cybox_minor_version = _cast(None, cybox_minor_version)
        self.cybox_update_version = _cast(None, cybox_update_version)
        self.cybox_major_version = _cast(None, cybox_major_version)
        self.Observable_Package_Source = Observable_Package_Source
        if Observable is None:
            self.Observable = []
        else:
            self.Observable = Observable
        self.Pools = Pools
    def factory(*args_, **kwargs_):
        if ObservablesType.subclass:
            return ObservablesType.subclass(*args_, **kwargs_)
        else:
            return ObservablesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observable_Package_Source(self): return self.Observable_Package_Source
    def set_Observable_Package_Source(self, Observable_Package_Source): self.Observable_Package_Source = Observable_Package_Source
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def add_Observable(self, value): self.Observable.append(value)
    def insert_Observable(self, index, value): self.Observable[index] = value
    def get_Pools(self): return self.Pools
    def set_Pools(self, Pools): self.Pools = Pools
    def get_cybox_minor_version(self): return self.cybox_minor_version
    def set_cybox_minor_version(self, cybox_minor_version): self.cybox_minor_version = cybox_minor_version
    def get_cybox_update_version(self): return self.cybox_update_version
    def set_cybox_update_version(self, cybox_update_version): self.cybox_update_version = cybox_update_version
    def get_cybox_major_version(self): return self.cybox_major_version
    def set_cybox_major_version(self, cybox_major_version): self.cybox_major_version = cybox_major_version
    def hasContent_(self):
        if (
            self.Observable_Package_Source is not None or
            self.Observable or
            self.Pools is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='Observables', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Observables')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='Observables'):
        if self.cybox_major_version is not None and 'cybox_major_version' not in already_processed:
            already_processed.add('cybox_major_version')
            outfile.write(' cybox_major_version=%s' % (self.gds_format_string(quote_attrib(self.cybox_major_version).encode(ExternalEncoding), input_name='cybox_major_version'), ))
        if self.cybox_minor_version is not None and 'cybox_minor_version' not in already_processed:
            already_processed.add('cybox_minor_version')
            outfile.write(' cybox_minor_version=%s' % (self.gds_format_string(quote_attrib(self.cybox_minor_version).encode(ExternalEncoding), input_name='cybox_minor_version'), ))
        if self.cybox_update_version is not None and 'cybox_update_version' not in already_processed:
            already_processed.add('cybox_update_version')
            outfile.write(' cybox_update_version=%s' % (self.gds_format_string(quote_attrib(self.cybox_update_version).encode(ExternalEncoding), input_name='cybox_update_version'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='Observables', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Observable_Package_Source is not None:
            self.Observable_Package_Source.export(outfile, level, "cybox:", name_='Observable_Package_Source', pretty_print=pretty_print)
        for Observable_ in self.Observable:
            Observable_.export(outfile, level, "cybox:", name_='Observable', pretty_print=pretty_print)
        if self.Pools is not None:
            self.Pools.export(outfile, level, "cybox:", name_='Pools', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Observables'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.cybox_minor_version is not None and 'cybox_minor_version' not in already_processed:
            already_processed.add('cybox_minor_version')
            showIndent(outfile, level)
            outfile.write('cybox_minor_version = "%s",\n' % (self.cybox_minor_version,))
        if self.cybox_update_version is not None and 'cybox_update_version' not in already_processed:
            already_processed.add('cybox_update_version')
            showIndent(outfile, level)
            outfile.write('cybox_update_version = "%s",\n' % (self.cybox_update_version,))
        if self.cybox_major_version is not None and 'cybox_major_version' not in already_processed:
            already_processed.add('cybox_major_version')
            showIndent(outfile, level)
            outfile.write('cybox_major_version = "%s",\n' % (self.cybox_major_version,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Observable_Package_Source is not None:
            showIndent(outfile, level)
            outfile.write('Observable_Package_Source=model_.MeasureSourceType(\n')
            self.Observable_Package_Source.exportLiteral(outfile, level, name_='Observable_Package_Source')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Observable=[\n')
        level += 1
        for Observable_ in self.Observable:
            showIndent(outfile, level)
            outfile.write('model_.Observable(\n')
            Observable_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Pools is not None:
            showIndent(outfile, level)
            outfile.write('Pools=model_.PoolsType(\n')
            self.Pools.exportLiteral(outfile, level, name_='Pools')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('cybox_minor_version', node)
        if value is not None and 'cybox_minor_version' not in already_processed:
            already_processed.add('cybox_minor_version')
            self.cybox_minor_version = value
        value = find_attr_value_('cybox_update_version', node)
        if value is not None and 'cybox_update_version' not in already_processed:
            already_processed.add('cybox_update_version')
            self.cybox_update_version = value
        value = find_attr_value_('cybox_major_version', node)
        if value is not None and 'cybox_major_version' not in already_processed:
            already_processed.add('cybox_major_version')
            self.cybox_major_version = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observable_Package_Source':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Observable_Package_Source(obj_)
        elif nodeName_ == 'Observable':
            obj_ = ObservableType.factory()
            obj_.build(child_)
            self.Observable.append(obj_)
        elif nodeName_ == 'Pools':
            obj_ = PoolsType.factory()
            obj_.build(child_)
            self.set_Pools(obj_)
# end class ObservablesType

class ObservableType(GeneratedsSuper):
    """The ObservableType is a type representing a description of a single
    cyber observable.The id field specifies a unique id for this
    Observable.The idref field specifies a unique id reference to an
    Observable defined elsewhere.The negate field, when set to true,
    indicates the absence (rather than the presence) of the given
    Observable in a CybOX pattern."""
    member_data_items_ = {
        'negate': MemberSpec_('negate', 'xs:boolean', 0),
        'idref': MemberSpec_('idref', 'xs:QName', 0),
        'id': MemberSpec_('id', 'xs:QName', 0),
        'Title': MemberSpec_('Title', 'xs:string', 0),
        'Description': MemberSpec_('Description', 'cybox_common.StructuredTextType', 0),
        'Keywords': MemberSpec_('Keywords', 'KeywordsType', 0),
        'Observable_Source': MemberSpec_('Observable_Source', 'cybox_common.MeasureSourceType', 0),
        'Object': MemberSpec_('Object', 'ObjectType', 0),
        'Event': MemberSpec_('Event', 'EventType', 0),
        'Observable_Composition': MemberSpec_('Observable_Composition', 'ObservableCompositionType', 0),
        'Pattern_Fidelity': MemberSpec_('Pattern_Fidelity', 'PatternFidelityType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, negate=False, idref=None, id=None, Title=None, Description=None, Keywords=None, Observable_Source=None, Object=None, Event=None, Observable_Composition=None, Pattern_Fidelity=None):
        self.negate = _cast(bool, negate)
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Title = Title
        self.Description = Description
        self.Keywords = Keywords
        self.Observable_Source = Observable_Source
        self.Object = Object
        self.Event = Event
        self.Observable_Composition = Observable_Composition
        self.Pattern_Fidelity = Pattern_Fidelity
    def factory(*args_, **kwargs_):
        if ObservableType.subclass:
            return ObservableType.subclass(*args_, **kwargs_)
        else:
            return ObservableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Keywords(self): return self.Keywords
    def set_Keywords(self, Keywords): self.Keywords = Keywords
    def get_Observable_Source(self): return self.Observable_Source
    def set_Observable_Source(self, Observable_Source): self.Observable_Source = Observable_Source
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def get_Observable_Composition(self): return self.Observable_Composition
    def set_Observable_Composition(self, Observable_Composition): self.Observable_Composition = Observable_Composition
    def get_Pattern_Fidelity(self): return self.Pattern_Fidelity
    def set_Pattern_Fidelity(self, Pattern_Fidelity): self.Pattern_Fidelity = Pattern_Fidelity
    def get_negate(self): return self.negate
    def set_negate(self, negate): self.negate = negate
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Keywords is not None or
            self.Observable_Source is not None or
            self.Object is not None or
            self.Event is not None or
            self.Observable_Composition is not None or
            self.Pattern_Fidelity is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObservableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservableType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObservableType'):
        # Only add "negate" attribute if it is True.
        if self.negate not in (None, False) and 'negate' not in already_processed:
            already_processed.add('negate')
            outfile.write(' negate="%s"' % self.gds_format_boolean(self.negate, input_name='negate'))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObservableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTitle>%s</%sTitle>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Title).encode(ExternalEncoding), input_name='Title'), 'cybox:', eol_))
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Keywords is not None:
            self.Keywords.export(outfile, level, 'cybox:', name_='Keywords', pretty_print=pretty_print)
        if self.Observable_Source is not None:
            self.Observable_Source.export(outfile, level, 'cybox:', name_='Observable_Source', pretty_print=pretty_print)
        if self.Object is not None:
            self.Object.export(outfile, level, 'cybox:', name_='Object', pretty_print=pretty_print)
        if self.Event is not None:
            self.Event.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
        if self.Observable_Composition is not None:
            self.Observable_Composition.export(outfile, level, 'cybox:', name_='Observable_Composition', pretty_print=pretty_print)
        if self.Pattern_Fidelity is not None:
            self.Pattern_Fidelity.export(outfile, level, 'cybox:', name_='Pattern_Fidelity', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObservableType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.negate is not None and 'negate' not in already_processed:
            already_processed.add('negate')
            showIndent(outfile, level)
            outfile.write('negate = %s,\n' % (self.negate,))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Title is not None:
            showIndent(outfile, level)
            outfile.write('Title=%s,\n' % quote_python(self.Title).encode(ExternalEncoding))
        if self.Description is not None:
            outfile.write('Description=model_.cybox_common.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.Keywords is not None:
            outfile.write('Keywords=model_.KeywordsType(\n')
            self.Keywords.exportLiteral(outfile, level, name_='Keywords')
            outfile.write('),\n')
        if self.Observable_Source is not None:
            outfile.write('Observable_Source=model_.cybox_common.MeasureSourceType(\n')
            self.Observable_Source.exportLiteral(outfile, level, name_='Observable_Source')
            outfile.write('),\n')
        if self.Object is not None:
            outfile.write('Object=model_.Object(\n')
            self.Object.exportLiteral(outfile, level)
            outfile.write('),\n')
        if self.Event is not None:
            outfile.write('Event=model_.Event(\n')
            self.Event.exportLiteral(outfile, level)
            outfile.write('),\n')
        if self.Observable_Composition is not None:
            outfile.write('Observable_Composition=model_.ObservableCompositionType(\n')
            self.Observable_Composition.exportLiteral(outfile, level, name_='Observable_Composition')
            outfile.write('),\n')
        if self.Pattern_Fidelity is not None:
            outfile.write('Pattern_Fidelity=model_.PatternFidelityType(\n')
            self.Pattern_Fidelity.exportLiteral(outfile, level, name_='Pattern_Fidelity')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('negate', node)
        if value is not None and 'negate' not in already_processed:
            already_processed.add('negate')
            if value in ('true', '1'):
                self.negate = True
            elif value in ('false', '0'):
                self.negate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Keywords':
            obj_ = KeywordsType.factory()
            obj_.build(child_)
            self.set_Keywords(obj_)
        elif nodeName_ == 'Observable_Source':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Observable_Source(obj_)
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_Object(obj_)
        elif nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.set_Event(obj_)
        elif nodeName_ == 'Observable_Composition':
            obj_ = ObservableCompositionType.factory()
            obj_.build(child_)
            self.set_Observable_Composition(obj_)
        elif nodeName_ == 'Pattern_Fidelity':
            obj_ = PatternFidelityType.factory()
            obj_.build(child_)
            self.set_Pattern_Fidelity(obj_)
# end class ObservableType

class EventType(GeneratedsSuper):
    """The EventType is a complex type representing a cyber observable
    event that is dynamic in nature with specific action(s) taken
    against specific cyber relevant objects (e.g. a file is deleted,
    a registry key is created or an HTTP Get Request is
    received).The id field specifies a unique id for this Event.The
    idref field specifies a unique id reference to an Event defined
    elsewhere."""
    member_data_items_ = {
        'idref': MemberSpec_('idref', 'xs:QName', 0),
        'id': MemberSpec_('id', 'xs:QName', 0),
        'Type': MemberSpec_('Type', 'cybox_common.ControlledVocabularyStringType', 0),
        'Description': MemberSpec_('Description', 'cybox_common.StructuredTextType', 0),
        'Observation_Method': MemberSpec_('Observation_Method', 'cybox_common.MeasureSourceType', 0),
        'Actions': MemberSpec_('Actions', 'ActionsType', 0),
        'Frequency': MemberSpec_('Frequency', 'FrequencyType', 0),
        'Event': MemberSpec_('Event', 'EventType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Type=None, Description=None, Observation_Method=None, Actions=None, Frequency=None, Event=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Type = Type
        self.Description = Description
        self.Observation_Method = Observation_Method
        self.Actions = Actions
        self.Frequency = Frequency
        if Event is None:
            self.Event = []
        else:
            self.Event = Event
    def factory(*args_, **kwargs_):
        if EventType.subclass:
            return EventType.subclass(*args_, **kwargs_)
        else:
            return EventType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Observation_Method(self): return self.Observation_Method
    def set_Observation_Method(self, Observation_Method): self.Observation_Method = Observation_Method
    def get_Actions(self): return self.Actions
    def set_Actions(self, Actions): self.Actions = Actions
    def get_Frequency(self): return self.Frequency
    def set_Frequency(self, Frequency): self.Frequency = Frequency
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def add_Event(self, value): self.Event.append(value)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Description is not None or
            self.Observation_Method is not None or
            self.Actions is not None or
            self.Frequency is not None or
            self.Event
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='EventType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EventType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='EventType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='EventType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(outfile, level, 'cybox:', name_='Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Observation_Method is not None:
            self.Observation_Method.export(outfile, level, 'cybox:', name_='Observation_Method', pretty_print=pretty_print)
        if self.Actions is not None:
            self.Actions.export(outfile, level, 'cybox:', name_='Actions', pretty_print=pretty_print)
        if self.Frequency is not None:
            self.Frequency.export(outfile, level, 'cybox:', name_='Frequency', pretty_print=pretty_print)
        for Event_ in self.Event:
            Event_.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='EventType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Type is not None:
            outfile.write('Type=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            outfile.write('),\n')
        if self.Description is not None:
            outfile.write('Description=model_.cybox_common.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.Observation_Method is not None:
            outfile.write('Observation_Method=model_.cybox_common.MeasureSourceType(\n')
            self.Observation_Method.exportLiteral(outfile, level, name_='Observation_Method')
            outfile.write('),\n')
        if self.Actions is not None:
            outfile.write('Actions=model_.ActionsType(\n')
            self.Actions.exportLiteral(outfile, level, name_='Actions')
            outfile.write('),\n')
        if self.Frequency is not None:
            outfile.write('Frequency=model_.FrequencyType(\n')
            self.Frequency.exportLiteral(outfile, level, name_='Frequency')
            outfile.write('),\n')
        for Event_ in self.Event:
            outfile.write('Event=model_.EventType(\n')
            Event_.exportLiteral(outfile, level, name_='Event')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Observation_Method':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Observation_Method(obj_)
        elif nodeName_ == 'Actions':
            obj_ = ActionsType.factory()
            obj_.build(child_)
            self.set_Actions(obj_)
        elif nodeName_ == 'Frequency':
            obj_ = FrequencyType.factory()
            obj_.build(child_)
            self.set_Frequency(obj_)
        elif nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.Event.append(obj_)
# end class EventType

class FrequencyType(GeneratedsSuper):
    """The FrequencyType is a type representing the specification of a
    frequency for a given action or event.This field specifies the
    rate for this defined frequency.This field specifies the units
    for this defined frequency.This field specifies the time scale
    for this defined frequency.This field is optional and conveys a
    targeted observation pattern of the nature of any trend in the
    frequency of the associated event or action. This field would be
    leveraged within an event or action pattern observable
    triggering on the matching of a specified trend in the frequency
    of an event or action."""
    member_data_items_ = {
        'units': MemberSpec_('units', 'xs:string', 0),
        'trend': MemberSpec_('trend', 'cybox:TrendEnum', 0),
        'rate': MemberSpec_('rate', 'xs:float', 0),
        'scale': MemberSpec_('scale', 'xs:string', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, units=None, trend=None, rate=None, scale=None):
        self.units = _cast(None, units)
        self.trend = _cast(None, trend)
        self.rate = _cast(float, rate)
        self.scale = _cast(None, scale)
        pass
    def factory(*args_, **kwargs_):
        if FrequencyType.subclass:
            return FrequencyType.subclass(*args_, **kwargs_)
        else:
            return FrequencyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_trend(self): return self.trend
    def set_trend(self, trend): self.trend = trend
    def get_rate(self): return self.rate
    def set_rate(self, rate): self.rate = rate
    def get_scale(self): return self.scale
    def set_scale(self, scale): self.scale = scale
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='FrequencyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FrequencyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='FrequencyType'):
        if self.units is not None and 'units' not in already_processed:
            already_processed.add('units')
            outfile.write(' units=%s' % (self.gds_format_string(quote_attrib(self.units).encode(ExternalEncoding), input_name='units'), ))
        if self.trend is not None and 'trend' not in already_processed:
            already_processed.add('trend')
            outfile.write(' trend=%s' % (quote_attrib(self.trend), ))
        if self.rate is not None and 'rate' not in already_processed:
            already_processed.add('rate')
            outfile.write(' rate="%s"' % self.gds_format_float(self.rate, input_name='rate'))
        if self.scale is not None and 'scale' not in already_processed:
            already_processed.add('scale')
            outfile.write(' scale=%s' % (self.gds_format_string(quote_attrib(self.scale).encode(ExternalEncoding), input_name='scale'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='FrequencyType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='FrequencyType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.units is not None and 'units' not in already_processed:
            already_processed.add('units')
            showIndent(outfile, level)
            outfile.write('units = "%s",\n' % (self.units,))
        if self.trend is not None and 'trend' not in already_processed:
            already_processed.add('trend')
            showIndent(outfile, level)
            outfile.write('trend = %s,\n' % (self.trend,))
        if self.rate is not None and 'rate' not in already_processed:
            already_processed.add('rate')
            showIndent(outfile, level)
            outfile.write('rate = %f,\n' % (self.rate,))
        if self.scale is not None and 'scale' not in already_processed:
            already_processed.add('scale')
            showIndent(outfile, level)
            outfile.write('scale = "%s",\n' % (self.scale,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('units', node)
        if value is not None and 'units' not in already_processed:
            already_processed.add('units')
            self.units = value
        value = find_attr_value_('trend', node)
        if value is not None and 'trend' not in already_processed:
            already_processed.add('trend')
            self.trend = value
        value = find_attr_value_('rate', node)
        if value is not None and 'rate' not in already_processed:
            already_processed.add('rate')
            try:
                self.rate = float(value)
            except ValueError, exp:
                raise ValueError('Bad float/double attribute (rate): %s' % exp)
        value = find_attr_value_('scale', node)
        if value is not None and 'scale' not in already_processed:
            already_processed.add('scale')
            self.scale = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class FrequencyType

class ActionsType(GeneratedsSuper):
    """The ActionsType is a complex type representing a set of cyber
    observable actions."""
    member_data_items_ = {
        'Action': MemberSpec_('Action', 'ActionType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Action=None):
        if Action is None:
            self.Action = []
        else:
            self.Action = Action
    def factory(*args_, **kwargs_):
        if ActionsType.subclass:
            return ActionsType.subclass(*args_, **kwargs_)
        else:
            return ActionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action(self): return self.Action
    def set_Action(self, Action): self.Action = Action
    def add_Action(self, value): self.Action.append(value)
    def insert_Action(self, index, value): self.Action[index] = value
    def hasContent_(self):
        if (
            self.Action
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_ in self.Action:
            Action_.export(outfile, level, 'cybox:', name_='Action', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action=[\n')
        level += 1
        for Action_ in self.Action:
            outfile.write('model_.Action(\n')
            Action_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action':
            obj_ = ActionType.factory()
            obj_.build(child_)
            self.Action.append(obj_)
# end class ActionsType

class ActionType(GeneratedsSuper):
    """The ActionType is a complex type representing a single cyber
    observable action.The id field specifies a unique id for this
    Action.The idref field specifies a unique id reference to an
    Action defined elsewhere.The ordinal_position field is intended
    to reference the ordinal position of the action with within a
    series of actions.The action_status field enables description of
    the status of the action being described.The context field is
    optional and enables simple characterization of the broad
    operational context in which the Action is relevantThe timestamp
    field represents the local or relative time at which the action
    occurred or was observed."""
    member_data_items_ = {
        'timestamp': MemberSpec_('timestamp', 'xs:dateTime', 0),
        'action_status': MemberSpec_('action_status', 'cybox:ActionStatusTypeEnum', 0),
        'ordinal_position': MemberSpec_('ordinal_position', 'xs:positiveInteger', 0),
        'context': MemberSpec_('context', 'cybox:ActionContextTypeEnum', 0),
        'idref': MemberSpec_('idref', 'xs:QName', 0),
        'id': MemberSpec_('id', 'xs:QName', 0),
        'Type': MemberSpec_('Type', 'cybox_common.ControlledVocabularyStringType', 0),
        'Name': MemberSpec_('Name', 'cybox_common.ControlledVocabularyStringType', 0),
        'Description': MemberSpec_('Description', 'cybox_common.StructuredTextType', 0),
        'Action_Aliases': MemberSpec_('Action_Aliases', 'ActionAliasesType', 0),
        'Action_Arguments': MemberSpec_('Action_Arguments', 'ActionArgumentsType', 0),
        'Discovery_Method': MemberSpec_('Discovery_Method', 'cybox_common.MeasureSourceType', 0),
        'Associated_Objects': MemberSpec_('Associated_Objects', 'AssociatedObjectsType', 0),
        'Relationships': MemberSpec_('Relationships', 'RelationshipsType', 0),
        'Frequency': MemberSpec_('Frequency', 'FrequencyType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, timestamp=None, action_status=None, ordinal_position=None, context=None, idref=None, id=None, Type=None, Name=None, Description=None, Action_Aliases=None, Action_Arguments=None, Discovery_Method=None, Associated_Objects=None, Relationships=None, Frequency=None):
        self.timestamp = _cast(None, timestamp)
        self.action_status = _cast(None, action_status)
        self.ordinal_position = _cast(int, ordinal_position)
        self.context = _cast(None, context)
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Type = Type
        self.Name = Name
        self.Description = Description
        self.Action_Aliases = Action_Aliases
        self.Action_Arguments = Action_Arguments
        self.Discovery_Method = Discovery_Method
        self.Associated_Objects = Associated_Objects
        self.Relationships = Relationships
        self.Frequency = Frequency
    def factory(*args_, **kwargs_):
        if ActionType.subclass:
            return ActionType.subclass(*args_, **kwargs_)
        else:
            return ActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Action_Aliases(self): return self.Action_Aliases
    def set_Action_Aliases(self, Action_Aliases): self.Action_Aliases = Action_Aliases
    def get_Action_Arguments(self): return self.Action_Arguments
    def set_Action_Arguments(self, Action_Arguments): self.Action_Arguments = Action_Arguments
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def get_Associated_Objects(self): return self.Associated_Objects
    def set_Associated_Objects(self, Associated_Objects): self.Associated_Objects = Associated_Objects
    def get_Relationships(self): return self.Relationships
    def set_Relationships(self, Relationships): self.Relationships = Relationships
    def get_Frequency(self): return self.Frequency
    def set_Frequency(self, Frequency): self.Frequency = Frequency
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_action_status(self): return self.action_status
    def set_action_status(self, action_status): self.action_status = action_status
    def get_ordinal_position(self): return self.ordinal_position
    def set_ordinal_position(self, ordinal_position): self.ordinal_position = ordinal_position
    def get_context(self): return self.context
    def set_context(self, context): self.context = context
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Name is not None or
            self.Description is not None or
            self.Action_Aliases is not None or
            self.Action_Arguments is not None or
            self.Discovery_Method is not None or
            self.Associated_Objects is not None or
            self.Relationships is not None or
            self.Frequency is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionType'):
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            outfile.write(' timestamp="%s"' % self.gds_format_datetime(self.timestamp))
        if self.action_status is not None and 'action_status' not in already_processed:
            already_processed.add('action_status')
            outfile.write(' action_status=%s' % (quote_attrib(self.action_status), ))
        if self.ordinal_position is not None and 'ordinal_position' not in already_processed:
            already_processed.add('ordinal_position')
            outfile.write(' ordinal_position="%s"' % self.gds_format_integer(self.ordinal_position, input_name='ordinal_position'))
        if self.context is not None and 'context' not in already_processed:
            already_processed.add('context')
            outfile.write(' context=%s' % (quote_attrib(self.context), ))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(outfile, level, 'cybox:', name_='Type', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(outfile, level, 'cybox:', name_='Name', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Action_Aliases is not None:
            self.Action_Aliases.export(outfile, level, 'cybox:', name_='Action_Aliases', pretty_print=pretty_print)
        if self.Action_Arguments is not None:
            self.Action_Arguments.export(outfile, level, 'cybox:', name_='Action_Arguments', pretty_print=pretty_print)
        if self.Discovery_Method is not None:
            self.Discovery_Method.export(outfile, level, 'cybox:', name_='Discovery_Method', pretty_print=pretty_print)
        if self.Associated_Objects is not None:
            self.Associated_Objects.export(outfile, level, 'cybox:', name_='Associated_Objects', pretty_print=pretty_print)
        if self.Relationships is not None:
            self.Relationships.export(outfile, level, 'cybox:', name_='Relationships', pretty_print=pretty_print)
        if self.Frequency is not None:
            self.Frequency.export(outfile, level, 'cybox:', name_='Frequency', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            showIndent(outfile, level)
            outfile.write('timestamp = "%s",\n' % (self.timestamp,))
        if self.action_status is not None and 'action_status' not in already_processed:
            already_processed.add('action_status')
            showIndent(outfile, level)
            outfile.write('action_status = %s,\n' % (self.action_status,))
        if self.ordinal_position is not None and 'ordinal_position' not in already_processed:
            already_processed.add('ordinal_position')
            showIndent(outfile, level)
            outfile.write('ordinal_position = %d,\n' % (self.ordinal_position,))
        if self.context is not None and 'context' not in already_processed:
            already_processed.add('context')
            showIndent(outfile, level)
            outfile.write('context = %s,\n' % (self.context,))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Type is not None:
            outfile.write('Type=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            outfile.write('),\n')
        if self.Name is not None:
            outfile.write('Name=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Name.exportLiteral(outfile, level, name_='Name')
            outfile.write('),\n')
        if self.Description is not None:
            outfile.write('Description=model_.cybox_common.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.Action_Aliases is not None:
            outfile.write('Action_Aliases=model_.ActionAliasesType(\n')
            self.Action_Aliases.exportLiteral(outfile, level, name_='Action_Aliases')
            outfile.write('),\n')
        if self.Action_Arguments is not None:
            outfile.write('Action_Arguments=model_.ActionArgumentsType(\n')
            self.Action_Arguments.exportLiteral(outfile, level, name_='Action_Arguments')
            outfile.write('),\n')
        if self.Discovery_Method is not None:
            outfile.write('Discovery_Method=model_.cybox_common.MeasureSourceType(\n')
            self.Discovery_Method.exportLiteral(outfile, level, name_='Discovery_Method')
            outfile.write('),\n')
        if self.Associated_Objects is not None:
            outfile.write('Associated_Objects=model_.AssociatedObjectsType(\n')
            self.Associated_Objects.exportLiteral(outfile, level, name_='Associated_Objects')
            outfile.write('),\n')
        if self.Relationships is not None:
            outfile.write('Relationships=model_.RelationshipsType(\n')
            self.Relationships.exportLiteral(outfile, level, name_='Relationships')
            outfile.write('),\n')
        if self.Frequency is not None:
            outfile.write('Frequency=model_.FrequencyType(\n')
            self.Frequency.exportLiteral(outfile, level, name_='Frequency')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
        value = find_attr_value_('action_status', node)
        if value is not None and 'action_status' not in already_processed:
            already_processed.add('action_status')
            self.action_status = value
        value = find_attr_value_('ordinal_position', node)
        if value is not None and 'ordinal_position' not in already_processed:
            already_processed.add('ordinal_position')
            try:
                self.ordinal_position = int(value)
            except ValueError, exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.ordinal_position <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
        value = find_attr_value_('context', node)
        if value is not None and 'context' not in already_processed:
            already_processed.add('context')
            self.context = value
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Action_Aliases':
            obj_ = ActionAliasesType.factory()
            obj_.build(child_)
            self.set_Action_Aliases(obj_)
        elif nodeName_ == 'Action_Arguments':
            obj_ = ActionArgumentsType.factory()
            obj_.build(child_)
            self.set_Action_Arguments(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Discovery_Method(obj_)
        elif nodeName_ == 'Associated_Objects':
            obj_ = AssociatedObjectsType.factory()
            obj_.build(child_)
            self.set_Associated_Objects(obj_)
        elif nodeName_ == 'Relationships':
            obj_ = RelationshipsType.factory()
            obj_.build(child_)
            self.set_Relationships(obj_)
        elif nodeName_ == 'Frequency':
            obj_ = FrequencyType.factory()
            obj_.build(child_)
            self.set_Frequency(obj_)
# end class ActionType

class ActionAliasesType(GeneratedsSuper):
    """The ActionAliasesType enables identification of other potentially
    used names for this Action."""
    member_data_items_ = {
        'Action_Alias': MemberSpec_('Action_Alias', 'xs:string', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Action_Alias=None):
        if Action_Alias is None:
            self.Action_Alias = []
        else:
            self.Action_Alias = Action_Alias
    def factory(*args_, **kwargs_):
        if ActionAliasesType.subclass:
            return ActionAliasesType.subclass(*args_, **kwargs_)
        else:
            return ActionAliasesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Alias(self): return self.Action_Alias
    def set_Action_Alias(self, Action_Alias): self.Action_Alias = Action_Alias
    def add_Action_Alias(self, value): self.Action_Alias.append(value)
    def insert_Action_Alias(self, index, value): self.Action_Alias[index] = value
    def hasContent_(self):
        if (
            self.Action_Alias
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionAliasesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionAliasesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionAliasesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionAliasesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_Alias_ in self.Action_Alias:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAction_Alias>%s</%sAction_Alias>%s' % ('cybox:', self.gds_format_string(quote_xml(Action_Alias_).encode(ExternalEncoding), input_name='Action_Alias'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='ActionAliasesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action_Alias=[\n')
        level += 1
        for Action_Alias_ in self.Action_Alias:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Action_Alias_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Alias':
            Action_Alias_ = child_.text
            Action_Alias_ = self.gds_validate_string(Action_Alias_, node, 'Action_Alias')
            self.Action_Alias.append(Action_Alias_)
# end class ActionAliasesType

class ActionArgumentsType(GeneratedsSuper):
    """The ActionArgumentsType enables the specification of relevant
    arguments/parameters for this Action."""
    member_data_items_ = {
        'Action_Argument': MemberSpec_('Action_Argument', 'ActionArgumentType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Action_Argument=None):
        if Action_Argument is None:
            self.Action_Argument = []
        else:
            self.Action_Argument = Action_Argument
    def factory(*args_, **kwargs_):
        if ActionArgumentsType.subclass:
            return ActionArgumentsType.subclass(*args_, **kwargs_)
        else:
            return ActionArgumentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Argument(self): return self.Action_Argument
    def set_Action_Argument(self, Action_Argument): self.Action_Argument = Action_Argument
    def add_Action_Argument(self, value): self.Action_Argument.append(value)
    def insert_Action_Argument(self, index, value): self.Action_Argument[index] = value
    def hasContent_(self):
        if (
            self.Action_Argument
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionArgumentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionArgumentsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionArgumentsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionArgumentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_Argument_ in self.Action_Argument:
            Action_Argument_.export(outfile, level, 'cybox:', name_='Action_Argument', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionArgumentsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action_Argument=[\n')
        level += 1
        for Action_Argument_ in self.Action_Argument:
            outfile.write('model_.ActionArgumentType(\n')
            Action_Argument_.exportLiteral(outfile, level, name_='ActionArgumentType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Argument':
            obj_ = ActionArgumentType.factory()
            obj_.build(child_)
            self.Action_Argument.append(obj_)
# end class ActionArgumentsType

class ActionArgumentType(GeneratedsSuper):
    """The ActionArgumentType enables the specification of a single
    relevant argument/parameter for this Action."""
    member_data_items_ = {
        'Argument_Name': MemberSpec_('Argument_Name', 'cybox_common.ControlledVocabularyStringType', 0),
        'Argument_Value': MemberSpec_('Argument_Value', 'xs:string', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, Argument_Name=None, Argument_Value=None):
        self.Argument_Name = Argument_Name
        self.Argument_Value = Argument_Value
    def factory(*args_, **kwargs_):
        if ActionArgumentType.subclass:
            return ActionArgumentType.subclass(*args_, **kwargs_)
        else:
            return ActionArgumentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Argument_Name(self): return self.Argument_Name
    def set_Argument_Name(self, Argument_Name): self.Argument_Name = Argument_Name
    def get_Argument_Value(self): return self.Argument_Value
    def set_Argument_Value(self, Argument_Value): self.Argument_Value = Argument_Value
    def hasContent_(self):
        if (
            self.Argument_Name is not None or
            self.Argument_Value is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionArgumentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionArgumentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionArgumentType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionArgumentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Argument_Name is not None:
            self.Argument_Name.export(outfile, level, 'cybox:', name_='Argument_Name', pretty_print=pretty_print)
        if self.Argument_Value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sArgument_Value>%s</%sArgument_Value>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Argument_Value).encode(ExternalEncoding), input_name='Argument_Value'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='ActionArgumentType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Argument_Name is not None:
            outfile.write('Argument_Name=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Argument_Name.exportLiteral(outfile, level, name_='Argument_Name')
            outfile.write('),\n')
        if self.Argument_Value is not None:
            showIndent(outfile, level)
            outfile.write('Argument_Value=%s,\n' % quote_python(self.Argument_Value).encode(ExternalEncoding))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Argument_Name':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Argument_Name(obj_)
        elif nodeName_ == 'Argument_Value':
            Argument_Value_ = child_.text
            Argument_Value_ = self.gds_validate_string(Argument_Value_, node, 'Argument_Value')
            self.Argument_Value = Argument_Value_
# end class ActionArgumentType

class AssociatedObjectsType(GeneratedsSuper):
    """The AssociatedObjectsType enables the description/specification of
    cyber Objects relevant to an Action."""
    member_data_items_ = {
        'Associated_Object': MemberSpec_('Associated_Object', 'AssociatedObjectType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Associated_Object=None):
        if Associated_Object is None:
            self.Associated_Object = []
        else:
            self.Associated_Object = Associated_Object
    def factory(*args_, **kwargs_):
        if AssociatedObjectsType.subclass:
            return AssociatedObjectsType.subclass(*args_, **kwargs_)
        else:
            return AssociatedObjectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Associated_Object(self): return self.Associated_Object
    def set_Associated_Object(self, Associated_Object): self.Associated_Object = Associated_Object
    def add_Associated_Object(self, value): self.Associated_Object.append(value)
    def insert_Associated_Object(self, index, value): self.Associated_Object[index] = value
    def hasContent_(self):
        if (
            self.Associated_Object
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AssociatedObjectsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Associated_Object_ in self.Associated_Object:
            Associated_Object_.export(outfile, level, 'cybox:', name_='Associated_Object', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='AssociatedObjectsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Associated_Object=[\n')
        level += 1
        for Associated_Object_ in self.Associated_Object:
            outfile.write('model_.AssociatedObjectType(\n')
            Associated_Object_.exportLiteral(outfile, level, name_='AssociatedObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Associated_Object':
            obj_ = AssociatedObjectType.factory()
            obj_.build(child_)
            self.Associated_Object.append(obj_)
# end class AssociatedObjectsType

class ActionPertinentObjectPropertiesType(GeneratedsSuper):
    """The ActionPertinentObjectPropertiesType identifies which of the
    Properties of this Object are specifically pertinent to this
    Action."""
    member_data_items_ = {
        'Property': MemberSpec_('Property', 'cybox_common.PropertyType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Property=None):
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
    def factory(*args_, **kwargs_):
        if ActionPertinentObjectPropertiesType.subclass:
            return ActionPertinentObjectPropertiesType.subclass(*args_, **kwargs_)
        else:
            return ActionPertinentObjectPropertiesType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectPropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPertinentObjectPropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPertinentObjectPropertiesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectPropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            Property_.export(outfile, level, 'cybox:', name_='Property', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionPertinentObjectPropertiesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Property=[\n')
        level += 1
        for Property_ in self.Property:
            outfile.write('model_.ActionPertinentObjectPropertyType(\n')
            Property_.exportLiteral(outfile, level, name_='ActionPertinentObjectPropertyType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            obj_ = ActionPertinentObjectPropertyType.factory()
            obj_.build(child_)
            self.Property.append(obj_)
# end class ActionPertinentObjectPropertiesType

class ActionPertinentObjectPropertyType(GeneratedsSuper):
    """The ActionPertinentObjectPropertyType identifies one of the
    Properties of an Object that specifically pertinent to an
    Action.The name field specifies the field name for the pertinent
    Object Property.The xpath field specifies the XPath 1.0
    expression identifying the pertinent property within the
    Properties schema for this object type."""
    member_data_items_ = {
        'xpath': MemberSpec_('xpath', 'xs:string', 0),
        'name': MemberSpec_('name', 'xs:string', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, xpath=None, name=None):
        self.xpath = _cast(None, xpath)
        self.name = _cast(None, name)
        pass
    def factory(*args_, **kwargs_):
        if ActionPertinentObjectPropertyType.subclass:
            return ActionPertinentObjectPropertyType.subclass(*args_, **kwargs_)
        else:
            return ActionPertinentObjectPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_xpath(self): return self.xpath
    def set_xpath(self, xpath): self.xpath = xpath
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectPropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPertinentObjectPropertyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPertinentObjectPropertyType'):
        if self.xpath is not None and 'xpath' not in already_processed:
            already_processed.add('xpath')
            outfile.write(' xpath=%s' % (self.gds_format_string(quote_attrib(self.xpath).encode(ExternalEncoding), input_name='xpath'), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectPropertyType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='ActionPertinentObjectPropertyType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.xpath is not None and 'xpath' not in already_processed:
            already_processed.add('xpath')
            showIndent(outfile, level)
            outfile.write('xpath = "%s",\n' % (self.xpath,))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            showIndent(outfile, level)
            outfile.write('name = "%s",\n' % (self.name,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xpath', node)
        if value is not None and 'xpath' not in already_processed:
            already_processed.add('xpath')
            self.xpath = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ActionPertinentObjectPropertyType

class RelationshipsType(GeneratedsSuper):
    """The RelationshipsType enables description of other cyber observable
    actions that are related to this Action."""
    member_data_items_ = {
        'Relationship': MemberSpec_('Relationship', 'ActionRelationshipType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Relationship=None):
        if Relationship is None:
            self.Relationship = []
        else:
            self.Relationship = Relationship
    def factory(*args_, **kwargs_):
        if RelationshipsType.subclass:
            return RelationshipsType.subclass(*args_, **kwargs_)
        else:
            return RelationshipsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Relationship(self): return self.Relationship
    def set_Relationship(self, Relationship): self.Relationship = Relationship
    def add_Relationship(self, value): self.Relationship.append(value)
    def insert_Relationship(self, index, value): self.Relationship[index] = value
    def hasContent_(self):
        if (
            self.Relationship
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='RelationshipsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelationshipsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelationshipsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelationshipsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Relationship_ in self.Relationship:
            Relationship_.export(outfile, level, 'cybox:', name_='Relationship', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RelationshipsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Relationship=[\n')
        level += 1
        for Relationship_ in self.Relationship:
            outfile.write('model_.ActionRelationshipType(\n')
            Relationship_.exportLiteral(outfile, level, name_='ActionRelationshipType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Relationship':
            obj_ = ActionRelationshipType.factory()
            obj_.build(child_)
            self.Relationship.append(obj_)
# end class RelationshipsType

class ActionRelationshipType(GeneratedsSuper):
    """The ActionRelationshipType characterizes a relationship between a
    specified cyber observable action and another cyber observable
    action."""
    member_data_items_ = {
        'Type': MemberSpec_('Type', 'cybox_common.ControlledVocabularyStringType', 0),
        'Action_Reference': MemberSpec_('Action_Reference', 'ActionReferenceType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Type=None, Action_Reference=None):
        self.Type = Type
        if Action_Reference is None:
            self.Action_Reference = []
        else:
            self.Action_Reference = Action_Reference
    def factory(*args_, **kwargs_):
        if ActionRelationshipType.subclass:
            return ActionRelationshipType.subclass(*args_, **kwargs_)
        else:
            return ActionRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Action_Reference(self): return self.Action_Reference
    def set_Action_Reference(self, Action_Reference): self.Action_Reference = Action_Reference
    def add_Action_Reference(self, value): self.Action_Reference.append(value)
    def insert_Action_Reference(self, index, value): self.Action_Reference[index] = value
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Action_Reference
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionRelationshipType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionRelationshipType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(outfile, level, 'cybox:', name_='Type', pretty_print=pretty_print)
        for Action_Reference_ in self.Action_Reference:
            Action_Reference_.export(outfile, level, 'cybox:', name_='Action_Reference', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionRelationshipType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Type is not None:
            outfile.write('Type=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Action_Reference=[\n')
        level += 1
        for Action_Reference_ in self.Action_Reference:
            outfile.write('model_.ActionReferenceType(\n')
            Action_Reference_.exportLiteral(outfile, level, name_='ActionReferenceType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Action_Reference':
            obj_ = ActionReferenceType.factory()
            obj_.build(child_)
            self.Action_Reference.append(obj_)
# end class ActionRelationshipType

class ActionReferenceType(GeneratedsSuper):
    """ActionReferenceType is intended to serve as a method for linking to
    actions.The action_id field refers to the id of the action being
    referenced."""
    member_data_items_ = {
        'action_id': MemberSpec_('action_id', 'xs:QName', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, action_id=None):
        self.action_id = _cast(None, action_id)
        pass
    def factory(*args_, **kwargs_):
        if ActionReferenceType.subclass:
            return ActionReferenceType.subclass(*args_, **kwargs_)
        else:
            return ActionReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_action_id(self): return self.action_id
    def set_action_id(self, action_id): self.action_id = action_id
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionReferenceType'):
        if self.action_id is not None and 'action_id' not in already_processed:
            already_processed.add('action_id')
            outfile.write(' action_id=%s' % (quote_attrib(self.action_id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionReferenceType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='ActionReferenceType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.action_id is not None and 'action_id' not in already_processed:
            already_processed.add('action_id')
            showIndent(outfile, level)
            outfile.write('action_id = %s,\n' % (self.action_id,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('action_id', node)
        if value is not None and 'action_id' not in already_processed:
            already_processed.add('action_id')
            self.action_id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ActionReferenceType

class ObjectType(GeneratedsSuper):
    """The ObjectType is a complex type representing the characteristics of
    a specific cyber-relevant object (e.g. a file, a registry key or
    a process). The id field specifies a unique id for this
    Object.The idref field specifies a unique id reference to an
    Object defined elsewhere.The has_changed field is optional and
    conveys a targeted observation pattern of whether the associated
    object specified has changed. This field would be leveraged
    within a pattern observable triggering on whether the value of
    an object specification has changed."""
    member_data_items_ = {
        'has_changed': MemberSpec_('has_changed', 'xs:boolean', 0),
        'idref': MemberSpec_('idref', 'xs:QName', 0),
        'id': MemberSpec_('id', 'xs:QName', 0),
        'State': MemberSpec_('State', 'cybox_common.ControlledVocabularyStringType', 0),
        'Description': MemberSpec_('Description', 'cybox_common.StructuredTextType', 0),
        'Properties': MemberSpec_('Properties', 'cybox_common.ObjectPropertiesType', 0),
        'Domain_Specific_Object_Properties': MemberSpec_('Domain_Specific_Object_Properties', 'DomainSpecificObjectPropertiesType', 0),
        'Related_Objects': MemberSpec_('Related_Objects', 'RelatedObjectsType', 0),
        'Defined_Effect': MemberSpec_('Defined_Effect', 'DefinedEffectType', 0),
        'Discovery_Method': MemberSpec_('Discovery_Method', 'cybox_common.MeasureSourceType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, has_changed=None, idref=None, id=None, State=None, Description=None, Properties=None, Domain_Specific_Object_Properties=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, extensiontype_=None):
        self.has_changed = _cast(bool, has_changed)
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.State = State
        self.Description = Description
        self.Properties = Properties
        self.Domain_Specific_Object_Properties = Domain_Specific_Object_Properties
        self.Related_Objects = Related_Objects
        self.Defined_Effect = Defined_Effect
        self.Discovery_Method = Discovery_Method
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_State(self): return self.State
    def set_State(self, State): self.State = State
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Properties(self): return self.Properties
    def set_Properties(self, Properties): self.Properties = Properties
    def get_Domain_Specific_Object_Properties(self): return self.Domain_Specific_Object_Properties
    def set_Domain_Specific_Object_Properties(self, Domain_Specific_Object_Properties): self.Domain_Specific_Object_Properties = Domain_Specific_Object_Properties
    def get_Related_Objects(self): return self.Related_Objects
    def set_Related_Objects(self, Related_Objects): self.Related_Objects = Related_Objects
    def get_Defined_Effect(self): return self.Defined_Effect
    def set_Defined_Effect(self, Defined_Effect): self.Defined_Effect = Defined_Effect
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def get_has_changed(self): return self.has_changed
    def set_has_changed(self, has_changed): self.has_changed = has_changed
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.State is not None or
            self.Description is not None or
            self.Properties is not None or
            self.Domain_Specific_Object_Properties is not None or
            self.Related_Objects is not None or
            self.Defined_Effect is not None or
            self.Discovery_Method is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObjectType'):
        if self.has_changed is not None and 'has_changed' not in already_processed:
            already_processed.add('has_changed')
            outfile.write(' has_changed="%s"' % self.gds_format_boolean(self.has_changed, input_name='has_changed'))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.State is not None:
            self.State.export(outfile, level, 'cybox:', name_='State', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Properties is not None:
            self.Properties.export(outfile, level, 'cybox:', name_='Properties', pretty_print=pretty_print)
        if self.Domain_Specific_Object_Properties is not None:
            self.Domain_Specific_Object_Properties.export(outfile, level, 'cybox:', name_='Domain_Specific_Object_Properties', pretty_print=pretty_print)
        if self.Related_Objects is not None:
            self.Related_Objects.export(outfile, level, 'cybox:', name_='Related_Objects', pretty_print=pretty_print)
        if self.Defined_Effect is not None:
            self.Defined_Effect.export(outfile, level, 'cybox:', name_='Defined_Effect', pretty_print=pretty_print)
        if self.Discovery_Method is not None:
            self.Discovery_Method.export(outfile, level, 'cybox:', name_='Discovery_Method', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObjectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.has_changed is not None and 'has_changed' not in already_processed:
            already_processed.add('has_changed')
            showIndent(outfile, level)
            outfile.write('has_changed = %s,\n' % (self.has_changed,))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.State is not None:
            outfile.write('State=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.State.exportLiteral(outfile, level, name_='State')
            outfile.write('),\n')
        if self.Description is not None:
            outfile.write('Description=model_.cybox_common.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.cybox_common.ObjectPropertiesType is not None:
            showIndent(outfile, level)
            outfile.write('cybox_common.ObjectPropertiesType=model_.cybox_common.ObjectPropertiesType(\n')
            self.cybox_common.ObjectPropertiesType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.DomainSpecificObjectPropertiesType is not None:
            showIndent(outfile, level)
            outfile.write('DomainSpecificObjectPropertiesType=model_.DomainSpecificObjectPropertiesType(\n')
            self.DomainSpecificObjectPropertiesType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Related_Objects is not None:
            outfile.write('Related_Objects=model_.RelatedObjectsType(\n')
            self.Related_Objects.exportLiteral(outfile, level, name_='Related_Objects')
            outfile.write('),\n')
        if self.DefinedEffectType is not None:
            showIndent(outfile, level)
            outfile.write('DefinedEffectType=model_.DefinedEffectType(\n')
            self.DefinedEffectType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Discovery_Method is not None:
            outfile.write('Discovery_Method=model_.cybox_common.MeasureSourceType(\n')
            self.Discovery_Method.exportLiteral(outfile, level, name_='Discovery_Method')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('has_changed', node)
        if value is not None and 'has_changed' not in already_processed:
            already_processed.add('has_changed')
            if value in ('true', '1'):
                self.has_changed = True
            elif value in ('false', '0'):
                self.has_changed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'State':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_State(obj_)
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Properties':
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
                    'Class not implemented for <Properties> element')
            self.set_Properties(obj_)
        elif nodeName_ == 'Domain_Specific_Object_Properties':
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
                    'Class not implemented for <Domain_Specific_Object_Properties> element')
            self.set_Domain_Specific_Object_Properties(obj_)
        elif nodeName_ == 'Related_Objects':
            obj_ = RelatedObjectsType.factory()
            obj_.build(child_)
            self.set_Related_Objects(obj_)
        elif nodeName_ == 'Defined_Effect':
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
                    'Class not implemented for <Defined_Effect> element')
            self.set_Defined_Effect(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = cybox_common.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Discovery_Method(obj_)
# end class ObjectType

class DomainSpecificObjectPropertiesType(GeneratedsSuper):
    """The DomainSpecificObjectPropertiesType is an abstract type
    placeholder within the CybOX schema enabling the inclusion of
    domain-specific metadata for an object through the use of a
    custom type defined as an extension of this base Abstract type.
    This enables domains utilizing CybOX such as malware analysis or
    forensics to incorporate non-generalized object metadata from
    their domains into CybOX objects."""
    member_data_items_ = {
        }
    subclass = None
    superclass = None
    def __init__(self, xsi_type = None):
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if DomainSpecificObjectPropertiesType.subclass:
            return DomainSpecificObjectPropertiesType.subclass(*args_, **kwargs_)
        else:
            return DomainSpecificObjectPropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (
            self.xsi_type is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DomainSpecificObjectPropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DomainSpecificObjectPropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DomainSpecificObjectPropertiesType'):
        if self.xsi_type is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xsi:type="%s"' % self.xsi_type)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DomainSpecificObjectPropertiesType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='DomainSpecificObjectPropertiesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.xsi_type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DomainSpecificObjectPropertiesType

class RelatedObjectsType(GeneratedsSuper):
    """The RelatedObjectsType enables the identification and/or
    specification of Objects with relevant relationships with this
    Object."""
    member_data_items_ = {
        'Related_Object': MemberSpec_('Related_Object', 'RelatedObjectType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Related_Object=None):
        if Related_Object is None:
            self.Related_Object = []
        else:
            self.Related_Object = Related_Object
    def factory(*args_, **kwargs_):
        if RelatedObjectsType.subclass:
            return RelatedObjectsType.subclass(*args_, **kwargs_)
        else:
            return RelatedObjectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Object(self): return self.Related_Object
    def set_Related_Object(self, Related_Object): self.Related_Object = Related_Object
    def add_Related_Object(self, value): self.Related_Object.append(value)
    def insert_Related_Object(self, index, value): self.Related_Object[index] = value
    def hasContent_(self):
        if (
            self.Related_Object
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='RelatedObjectsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelatedObjectsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelatedObjectsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Object_ in self.Related_Object:
            Related_Object_.export(outfile, level, 'cybox:', name_='Related_Object', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RelatedObjectsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Related_Object=[\n')
        level += 1
        for Related_Object_ in self.Related_Object:
            outfile.write('model_.RelatedObjectType(\n')
            Related_Object_.exportLiteral(outfile, level, name_='RelatedObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Object':
            obj_ = RelatedObjectType.factory()
            obj_.build(child_)
            self.Related_Object.append(obj_)
# end class RelatedObjectsType

class RelatedObjectType(ObjectType):
    """The RelatedObjectType enables the identification and/or
    specification of an Object with a relevant relationship with
    this Object."""
    member_data_items_ = {
        'Relationship': MemberSpec_('Relationship', 'cybox_common.ControlledVocabularyStringType', 0),
        }
    subclass = None
    superclass = ObjectType
    def __init__(self, has_changed=None, idref=None, id=None, State=None, Description=None, Properties=None, Domain_Specific_Object_Properties=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, Relationship=None):
        super(RelatedObjectType, self).__init__(has_changed, idref, id, State, Description, Properties, Domain_Specific_Object_Properties, Related_Objects, Defined_Effect, Discovery_Method, )
        self.Relationship = Relationship
    def factory(*args_, **kwargs_):
        if RelatedObjectType.subclass:
            return RelatedObjectType.subclass(*args_, **kwargs_)
        else:
            return RelatedObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Relationship(self): return self.Relationship
    def set_Relationship(self, Relationship): self.Relationship = Relationship
    def hasContent_(self):
        if (
            self.Relationship is not None or
            super(RelatedObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='RelatedObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelatedObjectType'):
        super(RelatedObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelatedObjectType', fromsubclass_=False, pretty_print=True):
        super(RelatedObjectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Relationship is not None:
            self.Relationship.export(outfile, level, 'cybox:', name_='Relationship', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RelatedObjectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(RelatedObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(RelatedObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Relationship is not None:
            outfile.write('Relationship=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Relationship.exportLiteral(outfile, level, name_='Relationship')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Relationship':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Relationship(obj_)
        super(RelatedObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedObjectType

class DefinedEffectType(GeneratedsSuper):
    """The DefinedEffectType is an abstract placeholder for various
    predefined Object Effect types (e.g. DataReadEffect,
    ValuesEnumeratedEffect or StateChangeEffect) that can be
    instantiated in its place through extension of the
    DefinedEffectType. This mechanism enables the specification of a
    broad range of types of potential complex action effects on
    Objects. The set of Defined_Effect types (extending the
    DefinedEffectType) are maintained as part of the core CybOX
    schema.The effect_type field specifies the nature of the Defined
    Effect instantiated in the place of the Defined_Effect element."""
    member_data_items_ = {
        'effect_type': MemberSpec_('effect_type', 'cybox:EffectTypeEnum', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, effect_type=None, extensiontype_=None):
        self.effect_type = _cast(None, effect_type)
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if DefinedEffectType.subclass:
            return DefinedEffectType.subclass(*args_, **kwargs_)
        else:
            return DefinedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_effect_type(self): return self.effect_type
    def set_effect_type(self, effect_type): self.effect_type = effect_type
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DefinedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DefinedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DefinedEffectType'):
        if self.effect_type is not None and 'effect_type' not in already_processed:
            already_processed.add('effect_type')
            outfile.write(' effect_type=%s' % (quote_attrib(self.effect_type), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DefinedEffectType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='DefinedEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.effect_type is not None and 'effect_type' not in already_processed:
            already_processed.add('effect_type')
            showIndent(outfile, level)
            outfile.write('effect_type = %s,\n' % (self.effect_type,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('effect_type', node)
        if value is not None and 'effect_type' not in already_processed:
            already_processed.add('effect_type')
            self.effect_type = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DefinedEffectType

class StateChangeEffectType(DefinedEffectType):
    """The StateChangeEffectType is intended as a generic way of
    characterizing the effects of actions upon objects where the
    some state of the object is changed."""
    member_data_items_ = {
        'Old_Object': MemberSpec_('Old_Object', 'ObjectType', 0),
        'New_Object': MemberSpec_('New_Object', 'ObjectType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Old_Object=None, New_Object=None):
        super(StateChangeEffectType, self).__init__(effect_type, )
        self.Old_Object = Old_Object
        self.New_Object = New_Object
    def factory(*args_, **kwargs_):
        if StateChangeEffectType.subclass:
            return StateChangeEffectType.subclass(*args_, **kwargs_)
        else:
            return StateChangeEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Old_Object(self): return self.Old_Object
    def set_Old_Object(self, Old_Object): self.Old_Object = Old_Object
    def get_New_Object(self): return self.New_Object
    def set_New_Object(self, New_Object): self.New_Object = New_Object
    def hasContent_(self):
        if (
            self.Old_Object is not None or
            self.New_Object is not None or
            super(StateChangeEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='StateChangeEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StateChangeEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='StateChangeEffectType'):
        super(StateChangeEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='StateChangeEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='StateChangeEffectType', fromsubclass_=False, pretty_print=True):
        super(StateChangeEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Old_Object is not None:
            self.Old_Object.export(outfile, level, 'cybox:', name_='Old_Object', pretty_print=pretty_print)
        if self.New_Object is not None:
            self.New_Object.export(outfile, level, 'cybox:', name_='New_Object', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='StateChangeEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(StateChangeEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(StateChangeEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Old_Object is not None:
            outfile.write('Old_Object=model_.ObjectType(\n')
            self.Old_Object.exportLiteral(outfile, level, name_='Old_Object')
            outfile.write('),\n')
        if self.New_Object is not None:
            outfile.write('New_Object=model_.ObjectType(\n')
            self.New_Object.exportLiteral(outfile, level, name_='New_Object')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(StateChangeEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Old_Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_Old_Object(obj_)
        elif nodeName_ == 'New_Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_New_Object(obj_)
        super(StateChangeEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class StateChangeEffectType

class DataReadEffectType(DefinedEffectType):
    """The DataReadEffectType type is intended to characterize the effects
    of actions upon objects where some data is read, such as from a
    file or a pipe."""
    member_data_items_ = {
        'Data': MemberSpec_('Data', 'cybox_common.DataSegmentType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataReadEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataReadEffectType.subclass:
            return DataReadEffectType.subclass(*args_, **kwargs_)
        else:
            return DataReadEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataReadEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DataReadEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataReadEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataReadEffectType'):
        super(DataReadEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataReadEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataReadEffectType', fromsubclass_=False, pretty_print=True):
        super(DataReadEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DataReadEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataReadEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataReadEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            outfile.write('Data=model_.cybox_common.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataReadEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataReadEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataReadEffectType

class DataWrittenEffectType(DefinedEffectType):
    """The DataWrittenEffectType type is intended to characterize the
    effects of actions upon objects where some data is written, such
    as to a file or a pipe."""
    member_data_items_ = {
        'Data': MemberSpec_('Data', 'cybox_common.DataSegmentType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataWrittenEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataWrittenEffectType.subclass:
            return DataWrittenEffectType.subclass(*args_, **kwargs_)
        else:
            return DataWrittenEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataWrittenEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DataWrittenEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataWrittenEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataWrittenEffectType'):
        super(DataWrittenEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataWrittenEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataWrittenEffectType', fromsubclass_=False, pretty_print=True):
        super(DataWrittenEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DataWrittenEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataWrittenEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataWrittenEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            outfile.write('Data=model_.cybox_common.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataWrittenEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataWrittenEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataWrittenEffectType

class DataSentEffectType(DefinedEffectType):
    """The DataSentEffectType type is intended to characterize the effects
    of actions upon objects where some data is sent, such as a byte
    sequence on a socket."""
    member_data_items_ = {
        'Data': MemberSpec_('Data', 'cybox_common.DataSegmentType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataSentEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataSentEffectType.subclass:
            return DataSentEffectType.subclass(*args_, **kwargs_)
        else:
            return DataSentEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataSentEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DataSentEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataSentEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataSentEffectType'):
        super(DataSentEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataSentEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataSentEffectType', fromsubclass_=False, pretty_print=True):
        super(DataSentEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DataSentEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataSentEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataSentEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            outfile.write('Data=model_.cybox_common.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataSentEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataSentEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataSentEffectType

class DataReceivedEffectType(DefinedEffectType):
    """The DataReceivedEffectType type is intended to characterize the
    effects of actions upon objects where some data is received,
    such as a byte sequence on a socket."""
    member_data_items_ = {
        'Data': MemberSpec_('Data', 'cybox_common.DataSegmentType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataReceivedEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataReceivedEffectType.subclass:
            return DataReceivedEffectType.subclass(*args_, **kwargs_)
        else:
            return DataReceivedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataReceivedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='DataReceivedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataReceivedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataReceivedEffectType'):
        super(DataReceivedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataReceivedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataReceivedEffectType', fromsubclass_=False, pretty_print=True):
        super(DataReceivedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DataReceivedEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataReceivedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataReceivedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            outfile.write('Data=model_.cybox_common.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataReceivedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataReceivedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataReceivedEffectType

class PropertyReadEffectType(DefinedEffectType):
    """The PropertyReadEffectType type is intended to characterize the
    effects of actions upon objects where some specific property is
    read from an object, such as the current running state of a
    process."""
    member_data_items_ = {
        'Name': MemberSpec_('Name', 'xs:string', 0),
        'Value': MemberSpec_('Value', 'xs:string', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Name=None, Value=None):
        super(PropertyReadEffectType, self).__init__(effect_type, )
        self.Name = Name
        self.Value = Value
    def factory(*args_, **kwargs_):
        if PropertyReadEffectType.subclass:
            return PropertyReadEffectType.subclass(*args_, **kwargs_)
        else:
            return PropertyReadEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Value is not None or
            super(PropertyReadEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='PropertyReadEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyReadEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertyReadEffectType'):
        super(PropertyReadEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyReadEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertyReadEffectType', fromsubclass_=False, pretty_print=True):
        super(PropertyReadEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            outfile.write('<%sName>%s</%sName>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Name).encode(ExternalEncoding), input_name='Name'), 'cybox:', eol_))
        if self.Value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Value).encode(ExternalEncoding), input_name='Value'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='PropertyReadEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(PropertyReadEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(PropertyReadEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Name is not None:
            outfile.write('Name=%s,\n' % quote_python(self.Name).encode(ExternalEncoding))
        if self.Value is not None:
            showIndent(outfile, level)
            outfile.write('Value=%s,\n' % quote_python(self.Value).encode(ExternalEncoding))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PropertyReadEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Value':
            Value_ = child_.text
            Value_ = self.gds_validate_string(Value_, node, 'Value')
            self.Value = Value_
        super(PropertyReadEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class PropertyReadEffectType

class PropertiesEnumeratedEffectType(DefinedEffectType):
    """The PropertiesEnumeratedEffectType type is intended to characterize
    the effects of actions upon objects where some properties of the
    object are enumerated, such as the startup parameters for a
    process."""
    member_data_items_ = {
        'Properties': MemberSpec_('Properties', 'PropertiesType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Properties=None):
        super(PropertiesEnumeratedEffectType, self).__init__(effect_type, )
        self.Properties = Properties
    def factory(*args_, **kwargs_):
        if PropertiesEnumeratedEffectType.subclass:
            return PropertiesEnumeratedEffectType.subclass(*args_, **kwargs_)
        else:
            return PropertiesEnumeratedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Properties(self): return self.Properties
    def set_Properties(self, Properties): self.Properties = Properties
    def hasContent_(self):
        if (
            self.Properties is not None or
            super(PropertiesEnumeratedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='PropertiesEnumeratedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesEnumeratedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertiesEnumeratedEffectType'):
        super(PropertiesEnumeratedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesEnumeratedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertiesEnumeratedEffectType', fromsubclass_=False, pretty_print=True):
        super(PropertiesEnumeratedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Properties is not None:
            self.Properties.export(outfile, level, 'cybox:', name_='Properties', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PropertiesEnumeratedEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(PropertiesEnumeratedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(PropertiesEnumeratedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Properties is not None:
            outfile.write('Properties=model_.PropertiesType(\n')
            self.Properties.exportLiteral(outfile, level, name_='Properties')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PropertiesEnumeratedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Properties':
            obj_ = cybox_common.ObjectPropertiesType.factory()
            obj_.build(child_)
            self.set_Properties(obj_)
        super(PropertiesEnumeratedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class PropertiesEnumeratedEffectType

class PropertiesType(GeneratedsSuper):
    """The PropertiesType specifies the properties that were enumerated as
    a result of the action on the object."""
    member_data_items_ = {
        'Property': MemberSpec_('Property', 'cybox_common.PropertyType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Property=None):
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
    def factory(*args_, **kwargs_):
        if PropertiesType.subclass:
            return PropertiesType.subclass(*args_, **kwargs_)
        else:
            return PropertiesType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespace_='cybox:', name_='PropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertiesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            outfile.write('<%sProperty>%s</%sProperty>%s' % ('cybox:', self.gds_format_string(quote_xml(Property_).encode(ExternalEncoding), input_name='Property'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='PropertiesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Property=[\n')
        level += 1
        for Property_ in self.Property:
            outfile.write('%s,\n' % quote_python(Property_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            obj_ = ActionPertinentObjectPropertyType.factory()
            obj_.build(child_)
            self.Property.append(obj_)
# end class PropertiesType

class ValuesEnumeratedEffectType(DefinedEffectType):
    """The ValuesEnumeratedEffectType type is intended to characterize the
    effects of actions upon objects where some values of the object
    are enumerated, such as the values of a registry key."""
    member_data_items_ = {
        'Values': MemberSpec_('Values', 'ValuesType', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Values=None):
        super(ValuesEnumeratedEffectType, self).__init__(effect_type, )
        self.Values = Values
    def factory(*args_, **kwargs_):
        if ValuesEnumeratedEffectType.subclass:
            return ValuesEnumeratedEffectType.subclass(*args_, **kwargs_)
        else:
            return ValuesEnumeratedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Values(self): return self.Values
    def set_Values(self, Values): self.Values = Values
    def hasContent_(self):
        if (
            self.Values is not None or
            super(ValuesEnumeratedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ValuesEnumeratedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesEnumeratedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ValuesEnumeratedEffectType'):
        super(ValuesEnumeratedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesEnumeratedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ValuesEnumeratedEffectType', fromsubclass_=False, pretty_print=True):
        super(ValuesEnumeratedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Values is not None:
            self.Values.export(outfile, level, 'cybox:', name_='Values', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ValuesEnumeratedEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(ValuesEnumeratedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(ValuesEnumeratedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Values is not None:
            outfile.write('Values=model_.ValuesType(\n')
            self.Values.exportLiteral(outfile, level, name_='Values')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ValuesEnumeratedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Values':
            obj_ = ValuesType.factory()
            obj_.build(child_)
            self.set_Values(obj_)
        super(ValuesEnumeratedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class ValuesEnumeratedEffectType

class ValuesType(GeneratedsSuper):
    """The ValuesType specifies the values that were enumerated as a result
    of the action on the object."""
    member_data_items_ = {
        'Value': MemberSpec_('Value', 'xs:string', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Value=None):
        if Value is None:
            self.Value = []
        else:
            self.Value = Value
    def factory(*args_, **kwargs_):
        if ValuesType.subclass:
            return ValuesType.subclass(*args_, **kwargs_)
        else:
            return ValuesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def add_Value(self, value): self.Value.append(value)
    def insert_Value(self, index, value): self.Value[index] = value
    def hasContent_(self):
        if (
            self.Value
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ValuesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ValuesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ValuesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Value_ in self.Value:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % ('cybox:', self.gds_format_string(quote_xml(Value_).encode(ExternalEncoding), input_name='Value'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='ValuesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Value=[\n')
        level += 1
        for Value_ in self.Value:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Value_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Value':
            Value_ = child_.text
            Value_ = self.gds_validate_string(Value_, node, 'Value')
            self.Value.append(Value_)
# end class ValuesType

class SendControlCodeEffectType(DefinedEffectType):
    """The SendControlCodeEffectType is intended to characterize the
    effects of actions upon objects where some control code, or
    other control-oriented communication signal, is sent to the
    object. For example, an action may send a control code to change
    the running state of a process."""
    member_data_items_ = {
        'Control_Code': MemberSpec_('Control_Code', 'xs:string', 0),
        }
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Control_Code=None):
        super(SendControlCodeEffectType, self).__init__(effect_type, )
        self.Control_Code = Control_Code
    def factory(*args_, **kwargs_):
        if SendControlCodeEffectType.subclass:
            return SendControlCodeEffectType.subclass(*args_, **kwargs_)
        else:
            return SendControlCodeEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Control_Code(self): return self.Control_Code
    def set_Control_Code(self, Control_Code): self.Control_Code = Control_Code
    def hasContent_(self):
        if (
            self.Control_Code is not None or
            super(SendControlCodeEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='SendControlCodeEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SendControlCodeEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='SendControlCodeEffectType'):
        super(SendControlCodeEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SendControlCodeEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='SendControlCodeEffectType', fromsubclass_=False, pretty_print=True):
        super(SendControlCodeEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Control_Code is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sControl_Code>%s</%sControl_Code>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Control_Code).encode(ExternalEncoding), input_name='Control_Code'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='SendControlCodeEffectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(SendControlCodeEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(SendControlCodeEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Control_Code is not None:
            showIndent(outfile, level)
            outfile.write('Control_Code=%s,\n' % quote_python(self.Control_Code).encode(ExternalEncoding))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(SendControlCodeEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Control_Code':
            Control_Code_ = child_.text
            Control_Code_ = self.gds_validate_string(Control_Code_, node, 'Control_Code')
            self.Control_Code = Control_Code_
        super(SendControlCodeEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class SendControlCodeEffectType

class ObservableCompositionType(GeneratedsSuper):
    """The ObservablesCompositionType enables the specification of higher-
    order composite observables composed of logical combinations of
    other observables.The operator field enables the specification
    of complex compositional cyber observables by providing logical
    operators for defining interrelationships between constituent
    cyber observables defined utilizing the recursive Observable
    element."""
    member_data_items_ = {
        'operator': MemberSpec_('operator', 'cybox:OperatorTypeEnum', 0),
        'Observable': MemberSpec_('Observable', 'ObservableType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, operator=None, Observable=None):
        self.operator = _cast(None, operator)
        if Observable is None:
            self.Observable = []
        else:
            self.Observable = Observable
    def factory(*args_, **kwargs_):
        if ObservableCompositionType.subclass:
            return ObservableCompositionType.subclass(*args_, **kwargs_)
        else:
            return ObservableCompositionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def add_Observable(self, value): self.Observable.append(value)
    def insert_Observable(self, index, value): self.Observable[index] = value
    def get_operator(self): return self.operator
    def set_operator(self, operator): self.operator = operator
    def hasContent_(self):
        if (
            self.Observable
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObservableCompositionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservableCompositionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObservableCompositionType'):
        if self.operator is not None and 'operator' not in already_processed:
            already_processed.add('operator')
            outfile.write(' operator=%s' % (quote_attrib(self.operator), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObservableCompositionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Observable_ in self.Observable:
            Observable_.export(outfile, level, 'cybox:', name_='Observable', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObservableCompositionType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.operator is not None and 'operator' not in already_processed:
            already_processed.add('operator')
            showIndent(outfile, level)
            outfile.write('operator = %s,\n' % (self.operator,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Observable=[\n')
        level += 1
        for Observable_ in self.Observable:
            outfile.write('model_.ObservableType(\n')
            Observable_.exportLiteral(outfile, level, name_='ObservableType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('operator', node)
        if value is not None and 'operator' not in already_processed:
            already_processed.add('operator')
            self.operator = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observable':
            obj_ = ObservableType.factory()
            obj_.build(child_)
            self.Observable.append(obj_)
# end class ObservableCompositionType

class PoolsType(GeneratedsSuper):
    """The PoolsType enables the description of Events, Actions, Objects
    and Properties in a space-efficient pooled manner with the
    actual Observable structures defined in the CybOX schema
    containing references to the pooled elements. This reduces
    redundancy caused when identical observable elements occur
    multiple times within a set of defined Observables."""
    member_data_items_ = {
        'Event_Pool': MemberSpec_('Event_Pool', 'EventPoolType', 0),
        'Action_Pool': MemberSpec_('Action_Pool', 'ActionPoolType', 0),
        'Object_Pool': MemberSpec_('Object_Pool', 'ObjectPoolType', 0),
        'Property_Pool': MemberSpec_('Property_Pool', 'PropertyPoolType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, Event_Pool=None, Action_Pool=None, Object_Pool=None, Property_Pool=None):
        self.Event_Pool = Event_Pool
        self.Action_Pool = Action_Pool
        self.Object_Pool = Object_Pool
        self.Property_Pool = Property_Pool
    def factory(*args_, **kwargs_):
        if PoolsType.subclass:
            return PoolsType.subclass(*args_, **kwargs_)
        else:
            return PoolsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Event_Pool(self): return self.Event_Pool
    def set_Event_Pool(self, Event_Pool): self.Event_Pool = Event_Pool
    def get_Action_Pool(self): return self.Action_Pool
    def set_Action_Pool(self, Action_Pool): self.Action_Pool = Action_Pool
    def get_Object_Pool(self): return self.Object_Pool
    def set_Object_Pool(self, Object_Pool): self.Object_Pool = Object_Pool
    def get_Property_Pool(self): return self.Property_Pool
    def set_Property_Pool(self, Property_Pool): self.Property_Pool = Property_Pool
    def hasContent_(self):
        if (
            self.Event_Pool is not None or
            self.Action_Pool is not None or
            self.Object_Pool is not None or
            self.Property_Pool is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='PoolsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PoolsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PoolsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PoolsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Event_Pool is not None:
            self.Event_Pool.export(outfile, level, 'cybox:', name_='Event_Pool', pretty_print=pretty_print)
        if self.Action_Pool is not None:
            self.Action_Pool.export(outfile, level, 'cybox:', name_='Action_Pool', pretty_print=pretty_print)
        if self.Object_Pool is not None:
            self.Object_Pool.export(outfile, level, 'cybox:', name_='Object_Pool', pretty_print=pretty_print)
        if self.Property_Pool is not None:
            self.Property_Pool.export(outfile, level, 'cybox:', name_='Property_Pool', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PoolsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Event_Pool is not None:
            outfile.write('Event_Pool=model_.EventPoolType(\n')
            self.Event_Pool.exportLiteral(outfile, level, name_='Event_Pool')
            outfile.write('),\n')
        if self.Action_Pool is not None:
            outfile.write('Action_Pool=model_.ActionPoolType(\n')
            self.Action_Pool.exportLiteral(outfile, level, name_='Action_Pool')
            outfile.write('),\n')
        if self.Object_Pool is not None:
            outfile.write('Object_Pool=model_.ObjectPoolType(\n')
            self.Object_Pool.exportLiteral(outfile, level, name_='Object_Pool')
            outfile.write('),\n')
        if self.Property_Pool is not None:
            outfile.write('Property_Pool=model_.PropertyPoolType(\n')
            self.Property_Pool.exportLiteral(outfile, level, name_='Property_Pool')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Event_Pool':
            obj_ = EventPoolType.factory()
            obj_.build(child_)
            self.set_Event_Pool(obj_)
        elif nodeName_ == 'Action_Pool':
            obj_ = ActionPoolType.factory()
            obj_.build(child_)
            self.set_Action_Pool(obj_)
        elif nodeName_ == 'Object_Pool':
            obj_ = ObjectPoolType.factory()
            obj_.build(child_)
            self.set_Object_Pool(obj_)
        elif nodeName_ == 'Property_Pool':
            obj_ = PropertyPoolType.factory()
            obj_.build(child_)
            self.set_Property_Pool(obj_)
# end class PoolsType

class EventPoolType(GeneratedsSuper):
    """The EventPoolType enables the description of CybOX Events in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Event elements. This reduces redundancy caused when
    identical Events occur multiple times within a set of defined
    Observables."""
    member_data_items_ = {
        'Event': MemberSpec_('Event', 'EventType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Event=None):
        if Event is None:
            self.Event = []
        else:
            self.Event = Event
    def factory(*args_, **kwargs_):
        if EventPoolType.subclass:
            return EventPoolType.subclass(*args_, **kwargs_)
        else:
            return EventPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def add_Event(self, value): self.Event.append(value)
    def insert_Event(self, index, value): self.Event[index] = value
    def hasContent_(self):
        if (
            self.Event
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='EventPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EventPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='EventPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='EventPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Event_ in self.Event:
            Event_.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='EventPoolType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Event=[\n')
        level += 1
        for Event_ in self.Event:
            outfile.write('model_.EventType(\n')
            Event_.exportLiteral(outfile, level, name_='EventType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.Event.append(obj_)
# end class EventPoolType

class ActionPoolType(GeneratedsSuper):
    """The ActionPoolType enables the description of CybOX Actions in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Action elements. This reduces redundancy caused when
    identical Actions occur multiple times within a set of defined
    Observables."""
    member_data_items_ = {
        'Action': MemberSpec_('Action', 'ActionType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Action=None):
        if Action is None:
            self.Action = []
        else:
            self.Action = Action
    def factory(*args_, **kwargs_):
        if ActionPoolType.subclass:
            return ActionPoolType.subclass(*args_, **kwargs_)
        else:
            return ActionPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action(self): return self.Action
    def set_Action(self, Action): self.Action = Action
    def add_Action(self, value): self.Action.append(value)
    def insert_Action(self, index, value): self.Action[index] = value
    def hasContent_(self):
        if (
            self.Action
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_ in self.Action:
            Action_.export(outfile, level, 'cybox:', name_='Action', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ActionPoolType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action=[\n')
        level += 1
        for Action_ in self.Action:
            outfile.write('model_.ActionType(\n')
            Action_.exportLiteral(outfile, level, name_='ActionType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action':
            obj_ = ActionType.factory()
            obj_.build(child_)
            self.Action.append(obj_)
# end class ActionPoolType

class ObjectPoolType(GeneratedsSuper):
    """The ObjectPoolType enables the description of CybOX Objects in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Object elements. This reduces redundancy caused when
    identical Objects occur multiple times within a set of defined
    Observables."""
    member_data_items_ = {
        'Object': MemberSpec_('Object', 'ObjectType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Object=None):
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
    def factory(*args_, **kwargs_):
        if ObjectPoolType.subclass:
            return ObjectPoolType.subclass(*args_, **kwargs_)
        else:
            return ObjectPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def add_Object(self, value): self.Object.append(value)
    def insert_Object(self, index, value): self.Object[index] = value
    def hasContent_(self):
        if (
            self.Object
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObjectPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObjectPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObjectPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObjectPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Object_ in self.Object:
            Object_.export(outfile, level, 'cybox:', name_='Object', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObjectPoolType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Object=[\n')
        level += 1
        for Object_ in self.Object:
            outfile.write('model_.ObjectType(\n')
            Object_.exportLiteral(outfile, level, name_='ObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_Object(obj_)
# end class ObjectPoolType

class PropertyPoolType(GeneratedsSuper):
    """The PropertyPoolType enables the description of CybOX Properties in
    a space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Properties elements. This reduces redundancy caused
    when identical Properties occur multiple times within a set of
    defined Observables."""
    member_data_items_ = {
        'Property': MemberSpec_('Property', 'cybox_common.PropertyType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Property=None):
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
    def factory(*args_, **kwargs_):
        if PropertyPoolType.subclass:
            return PropertyPoolType.subclass(*args_, **kwargs_)
        else:
            return PropertyPoolType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespace_='cybox:', name_='PropertyPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertyPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertyPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            Property_.export(outfile, level, 'cybox:', name_='Property', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PropertyPoolType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Property=[\n')
        level += 1
        for Property_ in self.Property:
            outfile.write('model_.cybox_common.PropertyType(\n')
            Property_.exportLiteral(outfile, level, name_='cybox_common.PropertyType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            obj_ = ActionPertinentObjectPropertyType.factory()
            obj_.build(child_)
            self.Property.append(obj_)
# end class PropertyPoolType

class ObfuscationTechniquesType(GeneratedsSuper):
    """The ObfuscationTechniquesType enables the description of a set of
    potential techniques an attacker could leverage to obfuscate the
    observability of this Observable."""
    member_data_items_ = {
        'Obfuscation_Technique': MemberSpec_('Obfuscation_Technique', 'ObfuscationTechniqueType', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Obfuscation_Technique=None):
        if Obfuscation_Technique is None:
            self.Obfuscation_Technique = []
        else:
            self.Obfuscation_Technique = Obfuscation_Technique
    def factory(*args_, **kwargs_):
        if ObfuscationTechniquesType.subclass:
            return ObfuscationTechniquesType.subclass(*args_, **kwargs_)
        else:
            return ObfuscationTechniquesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Obfuscation_Technique(self): return self.Obfuscation_Technique
    def set_Obfuscation_Technique(self, Obfuscation_Technique): self.Obfuscation_Technique = Obfuscation_Technique
    def add_Obfuscation_Technique(self, value): self.Obfuscation_Technique.append(value)
    def insert_Obfuscation_Technique(self, index, value): self.Obfuscation_Technique[index] = value
    def hasContent_(self):
        if (
            self.Obfuscation_Technique
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniquesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObfuscationTechniquesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObfuscationTechniquesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniquesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Obfuscation_Technique_ in self.Obfuscation_Technique:
            Obfuscation_Technique_.export(outfile, level, 'cybox:', name_='Obfuscation_Technique', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObfuscationTechniquesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Obfuscation_Technique=[\n')
        level += 1
        for Obfuscation_Technique_ in self.Obfuscation_Technique:
            outfile.write('model_.ObfuscationTechniqueType(\n')
            Obfuscation_Technique_.exportLiteral(outfile, level, name_='ObfuscationTechniqueType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Obfuscation_Technique':
            obj_ = ObfuscationTechniqueType.factory()
            obj_.build(child_)
            self.Obfuscation_Technique.append(obj_)
# end class ObfuscationTechniquesType

class ObfuscationTechniqueType(GeneratedsSuper):
    """The ObfuscationTechniqueType enables the description of a single
    potential technique an attacker could leverage to obfuscate the
    observability of this Observable."""
    member_data_items_ = {
        'Description': MemberSpec_('Description', 'cybox_common.StructuredTextType', 0),
        'Observables': MemberSpec_('Observables', 'ObservablesType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, Description=None, Observables=None):
        self.Description = Description
        self.Observables = Observables
    def factory(*args_, **kwargs_):
        if ObfuscationTechniqueType.subclass:
            return ObfuscationTechniqueType.subclass(*args_, **kwargs_)
        else:
            return ObfuscationTechniqueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Observables(self): return self.Observables
    def set_Observables(self, Observables): self.Observables = Observables
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Observables is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniqueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObfuscationTechniqueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObfuscationTechniqueType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniqueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Observables is not None:
            self.Observables.export(outfile, level, 'cybox:', name_='Observables', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObfuscationTechniqueType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            outfile.write('Description=model_.cybox_common.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.Observables is not None:
            outfile.write('Observables=model_.ObservablesType(\n')
            self.Observables.exportLiteral(outfile, level, name_='Observables')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Observables':
            obj_ = ObservablesType.factory()
            obj_.build(child_)
            self.set_Observables(obj_)
# end class ObfuscationTechniqueType

class KeywordsType(GeneratedsSuper):
    member_data_items_ = {
        'Keyword': MemberSpec_('Keyword', 'xs:string', 1),
        }
    subclass = None
    superclass = None
    def __init__(self, Keyword=None):
        if Keyword is None:
            self.Keyword = []
        else:
            self.Keyword = Keyword
    def factory(*args_, **kwargs_):
        if KeywordsType.subclass:
            return KeywordsType.subclass(*args_, **kwargs_)
        else:
            return KeywordsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Keyword(self): return self.Keyword
    def set_Keyword(self, Keyword): self.Keyword = Keyword
    def add_Keyword(self, value): self.Keyword.append(value)
    def insert_Keyword(self, index, value): self.Keyword[index] = value
    def hasContent_(self):
        if (
            self.Keyword
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='KeywordsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='KeywordsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='KeywordsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='KeywordsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Keyword_ in self.Keyword:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKeyword>%s</%sKeyword>%s' % ('cybox:', self.gds_format_string(quote_xml(Keyword_).encode(ExternalEncoding), input_name='Keyword'), 'cybox:', eol_))
    def exportLiteral(self, outfile, level, name_='KeywordsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Keyword=[\n')
        level += 1
        for Keyword_ in self.Keyword:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Keyword_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Keyword':
            Keyword_ = child_.text
            Keyword_ = self.gds_validate_string(Keyword_, node, 'Keyword')
            self.Keyword.append(Keyword_)
# end class KeywordsType

class PatternFidelityType(GeneratedsSuper):
    member_data_items_ = {
        'Noisiness': MemberSpec_('Noisiness', ['NoisinessEnum', 'xs:string'], 0),
        'Ease_of_Evasion': MemberSpec_('Ease_of_Evasion', ['EaseOfObfuscationEnum', 'xs:string'], 0),
        'Evasion_Techniques': MemberSpec_('Evasion_Techniques', 'ObfuscationTechniquesType', 0),
        }
    subclass = None
    superclass = None
    def __init__(self, Noisiness=None, Ease_of_Evasion=None, Evasion_Techniques=None):
        self.Noisiness = Noisiness
        self.Ease_of_Evasion = Ease_of_Evasion
        self.Evasion_Techniques = Evasion_Techniques
    def factory(*args_, **kwargs_):
        if PatternFidelityType.subclass:
            return PatternFidelityType.subclass(*args_, **kwargs_)
        else:
            return PatternFidelityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Noisiness(self): return self.Noisiness
    def set_Noisiness(self, Noisiness): self.Noisiness = Noisiness
    def validate_NoisinessEnum(self, value):
        # Validate type NoisinessEnum, a restriction on xs:string.
        pass
    def get_Ease_of_Evasion(self): return self.Ease_of_Evasion
    def set_Ease_of_Evasion(self, Ease_of_Evasion): self.Ease_of_Evasion = Ease_of_Evasion
    def validate_EaseOfObfuscationEnum(self, value):
        # Validate type EaseOfObfuscationEnum, a restriction on xs:string.
        pass
    def get_Evasion_Techniques(self): return self.Evasion_Techniques
    def set_Evasion_Techniques(self, Evasion_Techniques): self.Evasion_Techniques = Evasion_Techniques
    def hasContent_(self):
        if (
            self.Noisiness is not None or
            self.Ease_of_Evasion is not None or
            self.Evasion_Techniques is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='PatternFidelityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PatternFidelityType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PatternFidelityType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PatternFidelityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Noisiness is not None:
            outfile.write('<%sNoisiness>%s</%sNoisiness>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Noisiness).encode(ExternalEncoding), input_name='Noisiness'), 'cybox:', eol_))
        if self.Ease_of_Evasion is not None:
            outfile.write('<%sEase_of_Evasion>%s</%sEase_of_Evasion>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Ease_of_Evasion).encode(ExternalEncoding), input_name='Ease_of_Evasion'), 'cybox:', eol_))
        if self.Evasion_Techniques is not None:
            self.Evasion_Techniques.export(outfile, level, 'cybox:', name_='Evasion_Techniques', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PatternFidelityType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Noisiness is not None:
            outfile.write('Noisiness=%s,\n' % quote_python(self.Noisiness).encode(ExternalEncoding))
        if self.Ease_of_Evasion is not None:
            outfile.write('Ease_of_Evasion=%s,\n' % quote_python(self.Ease_of_Evasion).encode(ExternalEncoding))
        if self.Evasion_Techniques is not None:
            outfile.write('Evasion_Techniques=model_.ObfuscationTechniquesType(\n')
            self.Evasion_Techniques.exportLiteral(outfile, level, name_='Evasion_Techniques')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Noisiness':
            text_ = child_.text
            text_ = self.gds_validate_string(text_, node, 'Noisiness')
            self.set_Noisiness(text_)
        elif nodeName_ == 'Ease_of_Evasion':
            text_ = child_.text
            text_ = self.gds_validate_string(text_, node, 'Ease_of_Evasion')
            self.set_Ease_of_Evasion(text_)
        elif nodeName_ == 'Evasion_Techniques':
            text_ = child_.text
            text_ = self.gds_validate_string(text_, node, 'Evasion_Techniques')
            self.set_Evasion_Techniques(text_)
# end class PatternFidelityType

class AssociatedObjectType(ObjectType):
    """The AssociatedObjectType is a complex type representing the
    characterization of a cyber observable Object associated with a
    given cyber observable Action."""
    member_data_items_ = {
        'Association_Type': MemberSpec_('Association_Type', 'cybox_common.ControlledVocabularyStringType', 0),
        'Action_Pertinent_Object_Properties': MemberSpec_('Action_Pertinent_Object_Properties', 'ActionPertinentObjectPropertiesType', 0),
        }
    subclass = None
    superclass = ObjectType
    def __init__(self, has_changed=None, idref=None, id=None, State=None, Description=None, Properties=None, Domain_Specific_Object_Properties=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, Association_Type=None, Action_Pertinent_Object_Properties=None):
        super(AssociatedObjectType, self).__init__(has_changed, idref, id, State, Description, Properties, Domain_Specific_Object_Properties, Related_Objects, Defined_Effect, Discovery_Method, )
        self.Association_Type = Association_Type
        self.Action_Pertinent_Object_Properties = Action_Pertinent_Object_Properties
    def factory(*args_, **kwargs_):
        if AssociatedObjectType.subclass:
            return AssociatedObjectType.subclass(*args_, **kwargs_)
        else:
            return AssociatedObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Association_Type(self): return self.Association_Type
    def set_Association_Type(self, Association_Type): self.Association_Type = Association_Type
    def get_Action_Pertinent_Object_Properties(self): return self.Action_Pertinent_Object_Properties
    def set_Action_Pertinent_Object_Properties(self, Action_Pertinent_Object_Properties): self.Action_Pertinent_Object_Properties = Action_Pertinent_Object_Properties
    def hasContent_(self):
        if (
            self.Association_Type is not None or
            self.Action_Pertinent_Object_Properties is not None or
            super(AssociatedObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AssociatedObjectType'):
        super(AssociatedObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectType', fromsubclass_=False, pretty_print=True):
        super(AssociatedObjectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Association_Type is not None:
            self.Association_Type.export(outfile, level, 'cybox:', name_='Association_Type', pretty_print=pretty_print)
        if self.Action_Pertinent_Object_Properties is not None:
            self.Action_Pertinent_Object_Properties.export(outfile, level, 'cybox:', name_='Action_Pertinent_Object_Properties', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='AssociatedObjectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(AssociatedObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(AssociatedObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Association_Type is not None:
            outfile.write('Association_Type=model_.cybox_common.ControlledVocabularyStringType(\n')
            self.Association_Type.exportLiteral(outfile, level, name_='Association_Type')
            outfile.write('),\n')
        if self.Action_Pertinent_Object_Properties is not None:
            outfile.write('Action_Pertinent_Object_Properties=model_.ActionPertinentObjectPropertiesType(\n')
            self.Action_Pertinent_Object_Properties.exportLiteral(outfile, level, name_='Action_Pertinent_Object_Properties')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AssociatedObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Association_Type':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Association_Type(obj_)
        elif nodeName_ == 'Action_Pertinent_Object_Properties':
            obj_ = ActionPertinentObjectPropertiesType.factory()
            obj_.build(child_)
            self.set_Action_Pertinent_Object_Properties(obj_)
        super(AssociatedObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class AssociatedObjectType

GDSClassesMapping = {
    'Relationships': RelationshipsType,
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Defined_Effect': DefinedEffectType,
    'Action_Argument': ActionArgumentType,
    'Action': ActionType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Object': ObjectType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Observable': ObservableType,
    'SubDatum': cybox_common.MetadataType,
    'Tool_Hashes': cybox_common.HashListType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Evasion_Techniques': ObfuscationTechniquesType,
    'Reference': cybox_common.ReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Associated_Objects': AssociatedObjectsType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Event': EventType,
    'Segments': cybox_common.HashSegmentsType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Domain_Specific_Object_Properties': DomainSpecificObjectPropertiesType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'State': cybox_common.ControlledVocabularyStringType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Action_Arguments': ActionArgumentsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Relationship': cybox_common.ControlledVocabularyStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Obfuscation_Technique': ObfuscationTechniqueType,
    'Observable_Composition': ObservableCompositionType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Action_Pool': ActionPoolType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Observable_Source': cybox_common.MeasureSourceType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Association_Type': cybox_common.ControlledVocabularyStringType,
    'Observable_Package_Source': cybox_common.MeasureSourceType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Associated_Object': AssociatedObjectType,
    'Related_Objects': RelatedObjectsType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Data': cybox_common.DataSegmentType,
    'Properties': PropertiesType,
    'Action_Reference': ActionReferenceType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Pools': PoolsType,
    'Event_Pool': EventPoolType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Old_Object': ObjectType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Object_Pool': ObjectPoolType,
    'Library': cybox_common.LibraryType,
    'Property_Pool': PropertyPoolType,
    'Frequency': FrequencyType,
    'References': cybox_common.ToolReferencesType,
    'Keywords': KeywordsType,
    'Pattern_Fidelity': PatternFidelityType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Time': cybox_common.TimeType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Discovery_Method': cybox_common.MeasureSourceType,
    'Action_Pertinent_Object_Properties': ActionPertinentObjectPropertiesType,
    'Observation_Method': cybox_common.MeasureSourceType,
    'Related_Object': RelatedObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Values': ValuesType,
    'Observables': ObservablesType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'New_Object': ObjectType,
    'Argument_Name': cybox_common.ControlledVocabularyStringType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Actions': ActionsType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Action_Aliases': ActionAliasesType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
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
        rootTag = 'Observables'
        rootClass = ObservablesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = ObservablesType
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
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = ObservablesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout, 0, name_="Observables",
#        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = ObservablesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('from datetime import datetime as datetime_\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
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
    "ObservablesType",
    "ObservableType",
    "EventType",
    "FrequencyType",
    "ActionsType",
    "ActionType",
    "ActionAliasesType",
    "ActionArgumentsType",
    "ActionArgumentType",
    "AssociatedObjectsType",
    "AssociatedObjectType",
    "ActionPertinentObjectPropertiesType",
    "ActionPertinentObjectPropertyType",
    "RelationshipsType",
    "ActionRelationshipType",
    "ActionReferenceType",
    "ObjectType",
    "DomainSpecificObjectPropertiesType",
    "RelatedObjectsType",
    "RelatedObjectType",
    "DefinedEffectType",
    "StateChangeEffectType",
    "DataReadEffectType",
    "DataWrittenEffectType",
    "DataSentEffectType",
    "DataReceivedEffectType",
    "PropertyReadEffectType",
    "PropertiesEnumeratedEffectType",
    "PropertiesType",
    "ValuesEnumeratedEffectType",
    "ValuesType",
    "SendControlCodeEffectType",
    "ObservableCompositionType",
    "PoolsType",
    "EventPoolType",
    "ActionPoolType",
    "ObjectPoolType",
    "PropertyPoolType",
    "ObfuscationTechniquesType",
    "ObfuscationTechniqueType",
    "KeywordsType",
    "PatternFidelityType"
    ]


def add_external_class(klass, name=None):
    """Adds a class implementation to this binding's globals() dict.

    These classes can be used to implement Properties,
    Domain_Specific_Object_Properties, or Defined_Effect fields on an Object.

    Arguments:
    - klass - a Python class that implements the new type
    - name - a string representing the name of the class (as it will appear in
      XML documents to be parsed. (Defaults to klass.__name__)
    """

    if name is None:
        name = klass.__name__

    module = sys.modules[__name__]
    setattr(module, name, klass)
