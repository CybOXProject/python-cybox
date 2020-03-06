# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_executable_file_object import (
    DataDirectory, DOSHeader, Entropy, PEBuildInformation, PEChecksum,
    PEDataDirectoryStruct, PEExportedFunction, PEExportedFunctions,
    PEExports, PEFileHeader, PEHeaders, PEImport, PEImportedFunction,
    PEImportedFunctions, PEImportList, PEOptionalHeader, PEResource,
    PEResourceList, PESection, PESectionHeaderStruct, PESectionList,
    PEVersionInfoResource, WinExecutableFile
)
from cybox.test import EntityTestCase
from cybox.test.common.hash_test import EMPTY_MD5
from cybox.test.common.digital_signature_test import TestDigitalSignature
from cybox.test.objects import ObjectTestCase


class TestPEDataDirectoryStruct(EntityTestCase, unittest.TestCase):
    klass = PEDataDirectoryStruct

    _full_dict = {
        'virtual_address': u('0xFBCE'),
        'size': 23040,
    }


class TestDataDirectory(EntityTestCase, unittest.TestCase):
    klass = DataDirectory

    _full_dict = {
        'export_table': TestPEDataDirectoryStruct._full_dict,
        'import_table': TestPEDataDirectoryStruct._full_dict,
        'resource_table': TestPEDataDirectoryStruct._full_dict,
        'exception_table': TestPEDataDirectoryStruct._full_dict,
        'certificate_table': TestPEDataDirectoryStruct._full_dict,
        'base_relocation_table': TestPEDataDirectoryStruct._full_dict,
        'debug': TestPEDataDirectoryStruct._full_dict,
        'architecture': TestPEDataDirectoryStruct._full_dict,
        'global_ptr': TestPEDataDirectoryStruct._full_dict,
        'tls_table': TestPEDataDirectoryStruct._full_dict,
        'load_config_table': TestPEDataDirectoryStruct._full_dict,
        'bound_import': TestPEDataDirectoryStruct._full_dict,
        'import_address_table': TestPEDataDirectoryStruct._full_dict,
        'delay_import_descriptor': TestPEDataDirectoryStruct._full_dict,
        'clr_runtime_header': TestPEDataDirectoryStruct._full_dict,
        'reserved': TestPEDataDirectoryStruct._full_dict,
    }


class TestDOSHeader(EntityTestCase, unittest.TestCase):
    klass = DOSHeader

    _full_dict = {
        'e_magic': u('0x1'),
        'e_cblp': u('0x2'),
        'e_cp': u('0x3'),
        'e_crlc': u('0x4'),
        'e_cparhdr': u('0x5'),
        'e_minalloc': u('0x6'),
        'e_maxalloc': u('0x7'),
        'e_ss': u('0x8'),
        'e_sp': u('0x9'),
        'e_csum': u('0x10'),
        'e_ip': u('0x11'),
        'e_cs': u('0x12'),
        'e_lfarlc': u('0x13'),
        'e_ovro': u('0x14'),
        'e_oemid': u('0x15'),
        'e_oeminfo': u('0x16'),
        'reserved2': u('0x17'),
        'e_lfanew': u('0x18'),
        'hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
        ],
        'reserved1': [u('0x20'), u('0x21'), u('0x22')],
    }


class TestEntropy(EntityTestCase, unittest.TestCase):
    klass = Entropy

    _full_dict = {
        'value': 3.45673,
        'min': 2.23467,
        'max': 4.42346,
    }


class TestPEBuildInformation(EntityTestCase, unittest.TestCase):
    klass = PEBuildInformation

    _full_dict = {
        'linker_name': u('lld'),
        'linker_version': u('11'),
        'compiler_name': u('GNU GCC'),
        'compiler_version': u('7.8.4'),
    }


class TestPEChecksum(EntityTestCase, unittest.TestCase):
    klass = PEChecksum

    _full_dict = {
        'pe_computed_api': 120,
        'pe_file_api': 12800,
        'pe_file_raw': 22500,
    }


class TestPEExportedFunction(EntityTestCase, unittest.TestCase):
    klass = PEExportedFunction

    _full_dict = {
        'function_name': u('important_calculation'),
        'entry_point': u('0x000ECB99'),
        'ordinal': 1,
    }


class TestPEExportedFunctions(EntityTestCase, unittest.TestCase):
    klass = PEExportedFunctions

    _full_dict = [
        TestPEExportedFunction._full_dict,
        TestPEExportedFunction._full_dict,
    ]


class TestPEExports(EntityTestCase, unittest.TestCase):
    klass = PEExports

    _full_dict = {
        'name': u('PE Export Name'),
        'exported_functions': TestPEExportedFunctions._full_dict,
        'number_of_functions': 250,
        'exports_time_stamp': '2013-08-08T15:15:15-04:00',
        'number_of_addresses': 55000,
        'number_of_names': 10,
    }


class TestPEFileHeader(EntityTestCase, unittest.TestCase):
    klass = PEFileHeader

    _full_dict = {
        'machine': u('0xAA'),
        'number_of_sections': 3500,
        'time_date_stamp': u('0x000000005E619BF6'),
        'pointer_to_symbol_table': u('0x00023FEBB'),
        'number_of_symbols': 300,
        'size_of_optional_header': u('0x000CE'),
        'characteristics': u('0x4C'),
        'hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
        ],
    }


class TestPEImportedFunction(EntityTestCase, unittest.TestCase):
    klass = PEImportedFunction

    _full_dict = {
        'function_name': u('important_calculation_2'),
        'hint': u('0xEEFB'),
        'ordinal': 2,
        'bound': u('0x213EFB'),
        'virtual_address': u('0x000AB12'),
    }


class TestPEImportedFunctions(EntityTestCase, unittest.TestCase):
    klass = PEImportedFunctions

    _full_dict = [
        TestPEImportedFunction._full_dict,
        TestPEImportedFunction._full_dict,
    ]


class TestPEImport(EntityTestCase, unittest.TestCase):
    klass = PEImport

    _full_dict = {
        'delay_load': True,
        'initially_visible': True,
        'file_name': u('KERNEL32.GetModuleHandle'),
        'imported_functions': TestPEImportedFunctions._full_dict,
        'virtual_address': u('0x000000007B0D0000'),
    }


class TestPEOptionalHeader(EntityTestCase, unittest.TestCase):
    klass = PEOptionalHeader

    _full_dict = {
        'magic': u('0xECBA'),
        'major_linker_version': u('0x11'),
        'minor_linker_version': u('0x0'),
        'size_of_code': u('0x57E4'),
        'size_of_initialized_data': u('0x8CBA'),
        'size_of_uninitialized_data': u('0xEECB'),
        'address_of_entry_point': u('0x2345'),
        'base_of_code': u('0x0B35'),
        'base_of_data': u('0x0234'),
        'image_base': u('0xFFEE'),
        'section_alignment': u('0x00BC'),
        'file_alignment': u('0xBBEE'),
        'major_os_version': u('0x0011'),
        'minor_os_version': u('0x1001'),
        'major_image_version': u('0xEFD2'),
        'minor_image_version': u('0x328F'),
        'major_subsystem_version': u('0x5544'),
        'minor_subsystem_version': u('0x40FB'),
        'win32_version_value': u('0xAB0E'),
        'size_of_image': u('0xDE55'),
        'size_of_headers': u('0x34FF'),
        'checksum': u('0xABCDEF123456'),
        'subsystem': u('0xBC39012'),
        'dll_characteristics': u('0xDB45E'),
        'size_of_stack_reserve': u('0xAABB'),
        'size_of_stack_commit': u('0xEFFC'),
        'size_of_heap_reserve': u('0x2345'),
        'size_of_heap_commit': u('0xDEED'),
        'loader_flags': u('0xBEAD'),
        'number_of_rva_and_sizes': u('0x9823'),
        'data_directory': TestDataDirectory._full_dict,
        'hashes': [
            {
                'type': u("MD5"),
                'simple_hash_value': EMPTY_MD5,
            }
        ],
    }


class TestPEHeaders(EntityTestCase, unittest.TestCase):
    klass = PEHeaders

    _full_dict = {
        'dos_header': TestDOSHeader._full_dict,
        'signature': u('0x00000000ABAB045D'),
        'file_header': TestPEFileHeader._full_dict,
        'optional_header': TestPEOptionalHeader._full_dict,
        'entropy': TestEntropy._full_dict,
        'hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
        ],
    }


class TestPEImportList(EntityTestCase, unittest.TestCase):
    klass = PEImportList

    _full_dict = [
        TestPEImport._full_dict,
        TestPEImport._full_dict,
    ]


class TestPEResource(EntityTestCase, unittest.TestCase):
    klass = PEResource

    _full_dict = {
        'type': u('TypeLib'),
        'name': u('Some type lib'),
        'size': 12800,
        'virtual_address': u('0xDEADBEEF'),
        'language': u('en'),
        'sub_language': u('en_us'),
        'hashes': [
            {
                'type': u("MD5"),
                'simple_hash_value': EMPTY_MD5,
            }
        ],
        'data': u('Z2xlA2NvbQAADwABwAwADwABAAACKAAKACgFc210cDTADMAMAA8AAQAAAigACgAK'),
    }


class TestPEVersionInfoResource(EntityTestCase, unittest.TestCase):
    klass = PEVersionInfoResource

    _full_dict = {
        'comments': u('Some PE Comments'),
        'companyname': u('Fabrikam Corp'),
        'filedescription': u('Some File Description'),
        'fileversion': u('V1.0.0.1'),
        'internalname': u('Frabik'),
        'langid': u('0x0409'),
        'legalcopyright': u('(C)2011 Fabrikam Corp'),
        'legaltrademarks': u('Frabrik is a trademark of Fabrikam'),
        'originalfilename': u('testfile.sys'),
        'privatebuild': u('4352.54'),
        'productname': u('Fabrikam Driver'),
        'productversion': u('V1.0.0.1'),
        'specialbuild': u('V1.0.0.1a54'),
        'xsi:type': 'WinExecutableFileObj:PEVersionInfoResourceType',
    }


class TestPEResourceList(EntityTestCase, unittest.TestCase):
    klass = PEResourceList

    mixed_dict = TestPEVersionInfoResource._full_dict
    mixed_dict.update(TestPEResource._full_dict)

    _full_dict = [
        TestPEResource._full_dict,
        TestPEVersionInfoResource._full_dict,
        mixed_dict,
    ]


class TestPESectionHeaderStruct(EntityTestCase, unittest.TestCase):
    klass = PESectionHeaderStruct

    _full_dict = {
        'name': u('Section Header Name'),
        'virtual_size': u('0xECBA5'),
        'virtual_address': u('0x00000002EF599'),
        'size_of_raw_data': u('0xFEB5503'),
        'pointer_to_raw_data': u('0x00FB'),
        'pointer_to_relocations': u('0xEEBC'),
        'pointer_to_linenumbers': u('0x00000635D'),
        'number_of_relocations': 5,
        'number_of_linenumbers': 200,
        'characteristics': u('0xABCD'),
    }


class TestPESection(EntityTestCase, unittest.TestCase):
    klass = PESection

    _full_dict = {
        'section_header': TestPESectionHeaderStruct._full_dict,
        'data_hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
        ],
        'entropy': TestEntropy._full_dict,
        'header_hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5},
        ],
    }


class TestPESectionList(EntityTestCase, unittest.TestCase):
    klass = PESectionList

    _full_dict = [
        TestPESection._full_dict,
        TestPESection._full_dict,
    ]


class TestWinExecutableFile(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsExecutableFileObjectType"
    klass = WinExecutableFile

    _full_dict = {
        'build_information': TestPEBuildInformation._full_dict,
        'digital_signature': TestDigitalSignature._full_dict,
        'exports': TestPEExports._full_dict,
        'extraneous_bytes': 345,
        'headers': TestPEHeaders._full_dict,
        'imports': TestPEImportList._full_dict,
        'pe_checksum': TestPEChecksum._full_dict,
        'resources': TestPEResourceList._full_dict,
        'sections': TestPESectionList._full_dict,
        'type': u('Executable'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
