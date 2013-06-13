# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_executable_file_object as win_executable_file_binding
from cybox.objects.win_file_object import WinFile
from cybox.common.digitalsignature import DigitalSignature
from cybox.common import HashList, String, Integer, UnsignedLong, HexBinary, DateTime, NonNegativeInteger, Float, Long

class WinExecutableFile(WinFile):
    _XSI_NS = "WinExecutableFileObj"
    _XSI_TYPE = "WindowsExecutableFileObjectType"

    def __init__(self):
        super(WinExecutableFile, self).__init__()
        self.build_information = None
        self.digital_signature = None
        self.exports = None
        self.extraneous_bytes = None
        self.headers = None
        self.imports = None
        self.pe_checksum = None
        self.resources = None
        self.sections = None
        self.type = None
        
    def to_obj(self):
        win_executable_file_obj = super(WinExecutableFile, self).to_obj(win_executable_file_binding.WindowsExecutableFileObjectType())

        if self.build_information is not None : win_executable_file_obj.set_Build_Information(self.build_information.to_obj())
        if self.digital_signature is not None : win_executable_file_obj.set_Digital_Signature(self.digital_signature.to_obj())
        if self.exports is not None : win_executable_file_obj.set_Exports(self.exports.to_obj())
        if self.extraneous_bytes is not None : win_executable_file_obj.set_Extraneous_Bytes(self.extraneous_bytes.to_obj())
        if self.headers is not None : win_executable_file_obj.set_Headers(self.headers.to_obj())
        if self.imports is not None : win_executable_file_obj.set_Imports(self.imports.to_obj())
        if self.pe_checksum is not None : win_executable_file_obj.set_PE_Checksum(self.pe_checksum.to_obj())
        if self.resources is not None : win_executable_file_obj.set_Resources(self.resources.to_obj())
        if self.sections is not None : win_executable_file_obj.set_Sections(self.sections.to_obj())
        if self.type is not None : win_executable_file_obj.set_Type(self.type.to_obj())
        return win_executable_file_obj

    def to_dict(self):
        win_executable_file_dict = super(WinExecutableFile, self).to_dict()
        if self.build_information is not None : win_executable_file_dict['build_information'] = self.build_information.to_dict()
        if self.digital_signature is not None : win_executable_file_dict['digital_signature'] = self.digital_signature.to_dict()
        if self.exports is not None : win_executable_file_dict['exports'] = self.exports.to_dict()
        if self.extraneous_bytes is not None : win_executable_file_dict['extraneous_bytes'] = self.extraneous_bytes.to_dict()
        if self.headers is not None : win_executable_file_dict['headers'] = self.headers.to_dict()
        if self.imports is not None : win_executable_file_dict['imports'] = self.imports.to_list()
        if self.pe_checksum is not None : win_executable_file_dict['pe_checksum'] = self.pe_checksum.to_dict()
        if self.resources is not None : win_executable_file_dict['resources'] = self.resources.to_list()
        if self.sections is not None : win_executable_file_dict['sections'] = self.sections.to_list()
        if self.type is not None : win_executable_file_dict['type'] = self.type.to_dict()
        return win_executable_file_dict

    @staticmethod
    def from_dict(win_executable_file_dict):
        if not win_executable_file_dict:
            return None
        win_executable_file_ = WinFile.from_dict(win_executable_file_dict, WinExecutableFile())
        win_executable_file_.build_information = PEBuildInformation.from_dict(win_executable_file_dict.get('build_information'))
        win_executable_file_.digital_signature = DigitalSignature.from_dict(win_executable_file_dict.get('digital_signature'))
        win_executable_file_.exports = PEExports.from_dict(win_executable_file_dict.get('exports'))
        win_executable_file_.extraneous_bytes = Integer.from_dict(win_executable_file_dict.get('extraneous_bytes'))
        win_executable_file_.headers = PEHeaders.from_dict(win_executable_file_dict.get('headers'))
        win_executable_file_.imports = PEImportList.from_list(win_executable_file_dict.get('imports'))
        win_executable_file_.pe_checksum = PEChecksum.from_dict(win_executable_file_dict.get('pe_checksum'))
        win_executable_file_.resources = PEResourceList.from_list(win_executable_file_dict.get('resources'))
        win_executable_file_.sections = PESectionList.from_list(win_executable_file_dict.get('sections'))
        win_executable_file_.type = String.from_dict(win_executable_file_dict.get('type'))
        return win_executable_file_

    @staticmethod
    def from_obj(win_executable_file_obj):
        if not win_executable_file_obj:
            return None
        win_executable_file_ = WinFile.from_obj(win_executable_file_obj, WinExecutableFile())
        win_executable_file_.build_information = PEBuildInformation.from_obj(win_executable_file_obj.get_Build_Information())
        win_executable_file_.digital_signature = DigitalSignature.from_obj(win_executable_file_obj.get_Digital_Signature())
        win_executable_file_.exports = PEExports.from_obj(win_executable_file_obj.get_Exports())
        win_executable_file_.extraneous_bytes = Integer.from_obj(win_executable_file_obj.get_Extraneous_Bytes())
        win_executable_file_.headers = PEHeaders.from_obj(win_executable_file_obj.get_Headers())
        win_executable_file_.imports = PEImportList.from_obj(win_executable_file_obj.get_Imports())
        win_executable_file_.pe_checksum = PEChecksum.from_obj(win_executable_file_obj.get_PE_Checksum())
        win_executable_file_.resources = PEResourceList.from_obj(win_executable_file_obj.get_Resources())
        win_executable_file_.sections = PESectionList.from_obj(win_executable_file_obj.get_Sections())
        win_executable_file_.type = String.from_obj(win_executable_file_obj.get_Type())
        return win_executable_file_

class PEBuildInformation(cybox.Entity):
    def __init__(self):
        super(PEBuildInformation, self).__init__()
        self.linker_name = None
        self.linker_version = None
        self.compiler_name = None
        self.compiler_version = None

    def to_obj(self):
        pe_build_information_obj = win_executable_file_binding.PEBuildInformationType()
        if self.linker_name is not None : pe_build_information_obj.set_Linker_Name(self.linker_name.to_obj())
        if self.linker_version is not None : pe_build_information_obj.set_Linker_Version(self.linker_version.to_obj())
        if self.compiler_name is not None : pe_build_information_obj.set_Compiler_Name(self.compiler_name.to_obj())
        if self.compiler_version is not None : pe_build_information_obj.set_Compiler_Version(self.compiler_version.to_obj())
        return pe_build_information_obj

    def to_dict(self):
        pe_build_information_dict = {}
        if self.linker_name is not None : pe_build_information_dict['linker_name'] = self.linker_name.to_dict()
        if self.linker_version is not None : pe_build_information_dict['linker_name'] = self.linker_name.to_dict()
        if self.compiler_name is not None : pe_build_information_dict['linker_name'] = self.linker_name.to_dict()
        if self.compiler_version is not None : pe_build_information_dict['linker_name'] = self.linker_name.to_dict()
        return pe_build_information_dict

    @staticmethod
    def from_dict(pe_build_information_dict):
        if not pe_build_information_dict:
            return
        pe_build_information_ = PEBuildInformation()
        pe_build_information_.linker_name = String.from_dict(pe_build_information_dict.get('linker_name'))
        pe_build_information_.linker_version = String.from_dict(pe_build_information_dict.get('linker_version'))
        pe_build_information_.compiler_name = String.from_dict(pe_build_information_dict.get('compiler_name'))
        pe_build_information_.compiler_version = String.from_dict(pe_build_information_dict.get('compiler_version'))
        return pe_build_information_

    @staticmethod
    def from_obj(pe_build_information_obj):
        if not pe_build_information_obj:
            return
        pe_build_information_ = PEBuildInformation()
        pe_build_information_.linker_name = String.from_obj(pe_build_information_obj.get_Linker_Name())
        pe_build_information_.linker_version = String.from_obj(pe_build_information_obj.get_Linker_Version())
        pe_build_information_.compiler_name = String.from_obj(pe_build_information_obj.get_Compiler_Name())
        pe_build_information_.compiler_version = String.from_obj(pe_build_information_obj.get_Compiler_Version())
        return pe_build_information_

class PEExports(cybox.Entity):
    def __init__(self):
        super(PEExports, self).__init__()
        self.exported_functions = None
        self.exports_time_stamp = None
        self.number_of_addresses = None
        self.number_of_names = None

    def to_obj(self):
        pe_exports_obj = win_executable_file_binding.PEExportsType()
        if self.exported_functions is not None : pe_exports_obj.set_Exported_Functions(self.exported_functions.to_obj())
        if self.exports_time_stamp is not None : pe_exports_obj.set_Exports_Time_Stamp(self.exports_time_stamp.to_obj())
        if self.number_of_addresses is not None : pe_exports_obj.set_Number_Of_Addresses(self.number_of_addresses.to_obj())
        if self.number_of_names is not None : pe_exports_obj.set_Number_Of_Names(self.number_of_names.to_obj())
        return pe_exports_obj

    def to_dict(self):
        pe_exports_dict = {}
        if self.exported_functions is not None : pe_exports_dict['exported_functions'] = self.exported_functions.to_list()
        if self.exports_time_stamp is not None : pe_exports_dict['exports_time_stamp'] = self.exports_time_stamp.to_dict()
        if self.number_of_addresses is not None : pe_exports_dict['number_of_addresses'] = self.number_of_addresses.to_dict()
        if self.number_of_names is not None : pe_exports_dict['number_of_names'] = self.number_of_names.to_dict()
        return pe_exports_dict

    @staticmethod
    def from_dict(pe_exports_dict):
        if not pe_exports_dict:
            return None
        pe_exports_ = PEExports()
        pe_exports_.exported_functions = PEExportedFunctions.from_list(pe_exports_dict.get('exported_functions'))
        pe_exports_.exports_time_stamp = DateTime.from_dict(pe_exports_dict.get('exports_time_stamp'))
        pe_exports_.number_of_addresses = Long.from_dict(pe_exports_dict.get('number_of_addresses'))
        pe_exports_.number_of_names = Long.from_dict(pe_exports_dict.get('number_of_names'))
        return pe_exports_

    @staticmethod
    def from_obj(pe_exports_obj):
        if not pe_exports_obj:
            return None
        pe_exports_ = PEExports()
        pe_exports_.exported_functions = PEExportedFunctions.from_obj(pe_exports_obj.get_Exported_Functions())
        pe_exports_.exports_time_stamp = DateTime.from_obj(pe_exports_obj.get_Exports_Time_Stamp())
        pe_exports_.number_of_addresses = Long.from_obj(pe_exports_obj.get_Number_Of_Addresses())
        pe_exports_.number_of_names = Long.from_obj(pe_exports_obj.get_Number_Of_Names())
        return pe_exports_

class PEExportedFunction(cybox.Entity):
    def __init__(self):
        super(PEExportedFunction, self).__init__()
        self.function_name = None
        self.entry_point = None
        self.ordinal = None

    def to_obj(self):
        pe_exported_function_obj = win_executable_file_binding.PEExportedFunctionType()
        if self.function_name is not None : pe_exported_function_obj.set_Function_Name(self.function_name.to_obj())
        if self.entry_point is not None : pe_exported_function_obj.set_Entry_Point(self.entry_point.to_obj())
        if self.ordinal is not None : pe_exported_function_obj.set_Ordinal(self.ordinal.to_obj())
        return pe_exported_function_obj

    def to_dict(self):
        pe_exported_function_dict = {}
        if self.function_name is not None : pe_exported_function_dict['function_name'] = self.function_name.to_dict()
        if self.entry_point is not None : pe_exported_function_dict['entry_point'] = self.entry_point.to_dict()
        if self.ordinal is not None : pe_exported_function_dict['ordinal'] = self.ordinal.to_dict()
        return pe_exported_function_dict

    @staticmethod
    def from_dict(pe_exported_function_dict):
        if not pe_exported_function_dict:
            return None
        pe_exported_function_ = PEExportedFunction()
        pe_exported_function_.function_name = String.from_dict(pe_exported_function_dict.get('function_name'))
        pe_exported_function_.entry_point = HexBinary.from_dict(pe_exported_function_dict.get('entry_point'))
        pe_exported_function_.ordinal = NonNegativeInteger.from_dict(pe_exported_function_dict.get('ordinal'))
        return pe_exported_function_

    @staticmethod
    def from_obj(pe_exported_function_obj):
        pe_exported_function_ = PEExportedFunction()
        pe_exported_function_.function_name = String.from_obj(pe_exported_function_obj.get_Function_Name())
        pe_exported_function_.entry_point = HexBinary.from_obj(pe_exported_function_obj.get_Entry_Point())
        pe_exported_function_.ordinal = NonNegativeInteger.from_obj(pe_exported_function_obj.get_Ordinal())
        return pe_exported_function_

class PEExportedFunctions(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEExportedFunctionsType
    _contained_type = PEExportedFunction

    def __init__(self):
        super(PEExportedFunctions, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Exported_Function(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Exported_Function()

class PEHeaders(cybox.Entity):
    def __init__(self):
        super(PEHeaders, self).__init__()
        self.dos_header = None
        self.signature = None
        self.file_header = None
        self.optional_header = None
        self.entropy = None
        self.hashes = None

    def to_obj(self):
        pe_headers_obj = win_executable_file_binding.PEHeadersType()
        if self.dos_header is not None : pe_headers_obj.set_DOS_Header(self.dos_header.to_obj())
        if self.signature is not None : pe_headers_obj.set_Signature(self.signature.to_obj())
        if self.file_header is not None : pe_headers_obj.set_File_Header(self.file_header.to_obj())
        if self.optional_header is not None : pe_headers_obj.set_Optional_Header(self.optional_header.to_obj())
        if self.entropy is not None : pe_headers_obj.set_Entropy(self.entropy.to_obj())
        if self.hashes is not None : pe_headers_obj.set_Hashes(self.hashes.to_obj())
        return pe_headers_obj

    def to_dict(self):
        pe_headers_dict = {}
        if self.dos_header is not None : pe_headers_dict['dos_header'] = self.dos_header.to_dict()
        if self.signature is not None : pe_headers_dict['signature'] = self.signature.to_dict()
        if self.file_header is not None : pe_headers_dict['file_header'] = self.file_header.to_dict()
        if self.optional_header is not None : pe_headers_dict['optional_header'] = self.optional_header.to_dict()
        if self.entropy is not None : pe_headers_dict['entropy'] = self.entropy.to_dict()
        if self.hashes is not None : pe_headers_dict['hashes'] = self.hashes.to_list()
        return pe_headers_dict

    @staticmethod
    def from_dict(pe_headers_dict):
        if not pe_headers_dict:
            return None
        pe_headers_ = PEHeaders()
        pe_headers_.dos_header = DOSHeader.from_dict(pe_headers_dict.get('dos_header'))
        pe_headers_.signature = HexBinary.from_dict(pe_headers_dict.get('signature'))
        pe_headers_.file_header = PEFileHeader.from_dict(pe_headers_dict.get('file_header'))
        pe_headers_.optional_header = PEOptionalHeader.from_dict(pe_headers_dict.get('optional_header'))
        pe_headers_.entropy = Entropy.from_dict(pe_headers_dict.get('entropy'))
        pe_headers_.hashes = HashList.from_list(pe_headers_dict.get('hashes'))
        return pe_headers_

    @staticmethod
    def from_obj(pe_headers_obj):
        if not pe_headers_obj:
            return None
        pe_headers_ = PEHeaders()
        pe_headers_.dos_header = DOSHeader.from_obj(pe_headers_obj.get_DOS_Header())
        pe_headers_.signature = HexBinary.from_obj(pe_headers_obj.get_Signature())
        pe_headers_.file_header = PEFileHeader.from_obj(pe_headers_obj.get_File_Header())
        pe_headers_.optional_header = PEOptionalHeader.from_obj(pe_headers_obj.get_Optional_Header())
        pe_headers_.entropy = Entropy.from_obj(pe_headers_obj.get_Entropy())
        pe_headers_.hashes = HashList.from_obj(pe_headers_obj.get_Hashes())
        return pe_headers_

class DOSHeader(cybox.Entity):
    def __init__(self):
        super(DOSHeader, self).__init__()
        self.e_magic = None
        self.e_cblp = None
        self.e_cp = None
        self.e_crlc = None
        self.e_cparhdr = None
        self.e_minalloc = None
        self.e_maxalloc = None
        self.e_ss = None
        self.e_sp = None
        self.e_csum = None
        self.e_ip = None
        self.e_cs = None
        self.e_lfarlc = None
        self.e_ovro = None
        self.reserved1 = []
        self.e_oemid = None
        self.e_oeminfo = None
        self.reserved2 = None
        self.e_lfanew = None
        self.hashes = None

    def to_obj(self):
        dos_header_obj = win_executable_file_binding.DOSHeaderType()
        if self.e_magic is not None : dos_header_obj.set_e_magic(self.e_magic.to_obj())
        if self.e_cblp is not None : dos_header_obj.set_e_cblp(self.e_cblp.to_obj())
        if self.e_cp is not None : dos_header_obj.set_e_cp(self.e_cp.to_obj())
        if self.e_crlc is not None : dos_header_obj.set_e_crlc(self.e_cblp.to_obj())
        if self.e_cparhdr is not None : dos_header_obj.set_e_cparhdr(self.e_cparhdr.to_obj())
        if self.e_minalloc is not None : dos_header_obj.set_e_minalloc(self.e_minalloc.to_obj())
        if self.e_maxalloc is not None : dos_header_obj.set_e_maxalloc(self.e_maxalloc.to_obj())
        if self.e_ss is not None : dos_header_obj.set_e_ss(self.e_ss.to_obj())
        if self.e_sp is not None : dos_header_obj.set_e_sp(self.e_sp.to_obj())
        if self.e_ip is not None : dos_header_obj.set_e_ip(self.e_ip.to_obj())
        if self.e_cs is not None : dos_header_obj.set_e_cs(self.e_cs.to_obj())
        if self.e_lfarlc is not None : dos_header_obj.set_e_lfarlc(self.e_lfarlc.to_obj())
        if self.e_ovro is not None : dos_header_obj.set_e_ovro(self.e_ovro.to_obj())
        if len(self.reserved1) > 0 : 
            for reserved in self.reserved1: dos_header_obj.add_reserved1(reserved.to_obj())
        if self.e_oemid is not None : dos_header_obj.set_e_oemid(self.e_oemid.to_obj())
        if self.e_oeminfo is not None : dos_header_obj.set_e_oeminfo(self.e_oeminfo.to_obj())
        if self.reserved2 is not None : dos_header_obj.set_reserved2(self.reserved2.to_obj())
        if self.e_lfanew is not None : dos_header_obj.set_e_lfanew(self.e_lfanew.to_obj())
        if self.hashes is not None : dos_header_obj.set_Hashes(self.hashes.to_obj())
        return dos_header_obj

    def to_dict(self):
        dos_header_dict = {}
        if self.e_magic is not None : dos_header_dict['e_magic'] = self.e_magic.to_dict()
        if self.e_cblp is not None : dos_header_dict['e_cblp'] = self.e_cblp.to_dict()
        if self.e_cp is not None : dos_header_dict['e_cp'] = self.e_cp.to_dict()
        if self.e_crlc is not None : dos_header_dict['e_crlc'] = self.e_crlc.to_dict()
        if self.e_cparhdr is not None : dos_header_dict['e_cparhdr'] = self.e_cparhdr.to_dict()
        if self.e_minalloc is not None : dos_header_dict['e_minalloc'] = self.e_minalloc.to_dict()
        if self.e_maxalloc is not None : dos_header_dict['e_maxalloc'] = self.e_maxalloc.to_dict()
        if self.e_ss is not None : dos_header_dict['e_ss'] = self.e_ss.to_dict()
        if self.e_sp is not None : dos_header_dict['e_sp'] = self.e_sp.to_dict()
        if self.e_ip is not None : dos_header_dict['e_ip'] = self.e_ip.to_dict()
        if self.e_cs is not None : dos_header_dict['e_cs'] = self.e_cs.to_dict()
        if self.e_lfarlc is not None : dos_header_dict['e_lfarlc'] = self.e_lfarlc.to_dict()
        if self.e_ovro is not None : dos_header_dict['e_ovro'] = self.e_ovro.to_dict()
        if len(self.reserved1) > 0 :
            reserved_list = []
            for reserved in self.reserved1: reserved_list.append(reserved.to_dict())
            dos_header_dict['reserved1'] = reserved_list
        if self.e_oemid is not None : dos_header_dict['e_oemid'] = self.e_oemid.to_dict()
        if self.e_oeminfo is not None : dos_header_dict['e_oeminfo'] = self.e_oeminfo.to_dict()
        if self.reserved2 is not None : dos_header_dict['reserved2'] = self.reserved2.to_dict()
        if self.e_lfanew is not None : dos_header_dict['e_lfanew'] = self.e_lfanew.to_dict()
        if self.hashes is not None : dos_header_dict['hashes'] = self.hashes.to_dict()
        return dos_header_dict

    @staticmethod
    def from_dict(dos_header_dict):
        if not dos_header_dict:
            return None
        dos_header_ = DOSHeader()
        dos_header_.e_magic = HexBinary.from_dict(dos_header_dict.get('e_magic'))
        dos_header_.e_cblp = HexBinary.from_dict(dos_header_dict.get('e_cblp'))
        dos_header_.e_cp = HexBinary.from_dict(dos_header_dict.get('e_cp'))
        dos_header_.e_crlc = HexBinary.from_dict(dos_header_dict.get('e_crlc'))
        dos_header_.e_cparhdr = HexBinary.from_dict(dos_header_dict.get('e_cparhdr'))
        dos_header_.e_minalloc = HexBinary.from_dict(dos_header_dict.get('e_minalloc'))
        dos_header_.e_maxalloc = HexBinary.from_dict(dos_header_dict.get('e_maxalloc'))
        dos_header_.e_ss = HexBinary.from_dict(dos_header_dict.get('e_ss'))
        dos_header_.e_sp = HexBinary.from_dict(dos_header_dict.get('e_sp'))
        dos_header_.e_csum = HexBinary.from_dict(dos_header_dict.get('e_csum'))
        dos_header_.e_ip = HexBinary.from_dict(dos_header_dict.get('e_ip'))
        dos_header_.e_cs = HexBinary.from_dict(dos_header_dict.get('e_cs'))
        dos_header_.e_lfarlc = HexBinary.from_dict(dos_header_dict.get('e_lfarlc'))
        dos_header_.e_ovro = HexBinary.from_dict(dos_header_dict.get('e_ovro'))
        dos_header_.e_oemid = HexBinary.from_dict(dos_header_dict.get('e_oemid'))
        dos_header_.e_oeminfo = HexBinary.from_dict(dos_header_dict.get('e_oeminfo'))
        dos_header_.reserved2 = HexBinary.from_dict(dos_header_dict.get('reserved2'))
        dos_header_.e_lfanew = HexBinary.from_dict(dos_header_dict.get('e_lfanew'))
        dos_header_.hashes = HashList.from_list(dos_header_dict.get('hashes'))
        if dos_header_dict.get('reserved1') is not None:
            for reserved in dos_header_dict.get('reserved1') : dos_header_.reserved1.append(HexBinary.from_dict(reserved))
        return dos_header_

    @staticmethod
    def from_obj(dos_header_obj):
        if not dos_header_dict:
            return None
        dos_header_ = DOSHeader()
        dos_header_.e_magic = HexBinary.from_obj(dos_header_obj.get_e_magic())
        dos_header_.e_cblp = HexBinary.from_obj(dos_header_obj.get_e_cblp())
        dos_header_.e_cp = HexBinary.from_obj(dos_header_obj.get_e_cp())
        dos_header_.e_crlc = HexBinary.from_obj(dos_header_obj.get_e_crlc())
        dos_header_.e_cparhdr = HexBinary.from_obj(dos_header_obj.get_e_cparhdr())
        dos_header_.e_minalloc = HexBinary.from_obj(dos_header_obj.get_e_minalloc())
        dos_header_.e_maxalloc = HexBinary.from_obj(dos_header_obj.get_e_maxalloc())
        dos_header_.e_ss = HexBinary.from_obj(dos_header_obj.get_e_ss())
        dos_header_.e_sp = HexBinary.from_obj(dos_header_obj.get_e_sp())
        dos_header_.e_csum = HexBinary.from_obj(dos_header_obj.get_e_csum())
        dos_header_.e_ip = HexBinary.from_obj(dos_header_obj.get_e_ip())
        dos_header_.e_cs = HexBinary.from_obj(dos_header_obj.get_e_cs())
        dos_header_.e_lfarlc = HexBinary.from_obj(dos_header_obj.get_e_lfarlc())
        dos_header_.e_ovro = HexBinary.from_obj(dos_header_obj.get_e_ovro())
        dos_header_.e_oemid = HexBinary.from_obj(dos_header_obj.get_e_oemid())
        dos_header_.e_oeminfo = HexBinary.from_obj(dos_header_obj.get_e_oeminfo())
        dos_header_.reserved2 = HexBinary.from_obj(dos_header_obj.get_reserved2())
        dos_header_.e_lfanew = HexBinary.from_obj(dos_header_obj.get_e_lfanew())
        dos_header_.hashes = HashList.from_obj(dos_header_obj.get_Hashes())
        if len(dos_header_obj.get_reserved1()) > 0:
            for reserved in dos_header_obj.get_reserved1() : dos_header_.reserved1.append(HexBinary.from_obj(reserved))
        return dos_header_

class PEFileHeader(cybox.Entity):
    def __init__(self):
        super(PEFileHeader, self).__init__()
        self.machine = None
        self.number_of_sections = None
        self.time_date_stamp = None
        self.pointer_to_symbol_table = None
        self.number_of_symbols = None
        self.size_of_optional_header = None
        self.characteristics = None
        self.hashes = None

    def to_obj(self):
        pe_file_header_obj = win_executable_file_binding.PEFileHeaderType()
        if self.machine is not None : pe_file_header_obj.set_Machine(self.machine.to_obj())
        if self.number_of_sections is not None : pe_file_header_obj.set_Number_Of_Sections(self.number_of_sections.to_obj())
        if self.time_date_stamp is not None : pe_file_header_obj.set_Time_Date_Stamp(self.time_date_stamp.to_obj())
        if self.pointer_to_symbol_table is not None : pe_file_header_obj.set_Pointer_To_Symbol_Table(self.pointer_to_symbol_table.to_obj())
        if self.number_of_symbols is not None : pe_file_header_obj.set_Number_Of_Symbols(self.number_of_symbols.to_obj())
        if self.size_of_optional_header is not None : pe_file_header_obj.set_Size_Of_Optional_Header(self.size_of_optional_header.to_obj())
        if self.characteristics is not None : pe_file_header_obj.set_Characteristics(self.characteristics.to_obj())
        return pe_file_header_obj

    def to_dict(self):
        pe_file_header_dict = {}
        if self.machine is not None : pe_file_header_dict['machine'] = self.machine.to_dict()
        if self.number_of_sections is not None : pe_file_header_dict['number_of_sections'] = self.number_of_sections.to_dict()
        if self.time_date_stamp is not None : pe_file_header_dict['time_date_stamp'] = self.time_date_stamp.to_dict()
        if self.pointer_to_symbol_table is not None : pe_file_header_dict['pointer_to_symbol_table'] = self.pointer_to_symbol_table.to_dict()
        if self.number_of_symbols is not None : pe_file_header_dict['number_of_symbols'] = self.number_of_symbols.to_dict()
        if self.size_of_optional_header is not None : pe_file_header_dict['size_of_optional_header'] = self.size_of_optional_header.to_dict()
        if self.characteristics is not None : ppe_file_header_dict['characteristics'] = self.characteristics.to_dict()
        return pe_file_header_dict

    @staticmethod
    def from_dict(pe_file_header_dict):
        if not pe_file_header_dict:
            return None
        pe_file_header_ = PEFileHeader()
        pe_file_header_.machine = HexBinary.from_dict(pe_file_header_dict.get('machine'))
        pe_file_header_.number_of_sections = NonNegativeInteger.from_dict(pe_file_header_dict.get('number_of_sections'))
        pe_file_header_.time_date_stamp = HexBinary.from_dict(pe_file_header_dict.get('time_date_stamp'))
        pe_file_header_.pointer_to_symbol_table = HexBinary.from_dict(pe_file_header_dict.get('pointer_to_symbol_table'))
        pe_file_header_.number_of_symbols = NonNegativeInteger.from_dict(pe_file_header_dict.get('number_of_symbols'))
        pe_file_header_.size_of_optional_header = HexBinary.from_dict(pe_file_header_dict.get('size_of_optional_header'))
        pe_file_header_.characteristics = HexBinary.from_dict(pe_file_header_dict.get('characteristics'))
        pe_file_header_.hashes = HashList.from_list(pe_file_header_dict.get('hashes'))
        return pe_file_header_

    @staticmethod
    def from_obj(pe_file_header_obj):
        if not pe_file_header_obj:
            return None
        pe_file_header_ = PEFileHeader()
        pe_file_header_.machine = HexBinary.from_obj(pe_file_header_obj.get_Machine())
        pe_file_header_.number_of_sections = NonNegativeInteger.from_obj(pe_file_header_obj.get_Number_Of_Sections())
        pe_file_header_.time_date_stamp = HexBinary.from_obj(pe_file_header_obj.get_Time_Date_Stamp())
        pe_file_header_.pointer_to_symbol_table = HexBinary.from_obj(pe_file_header_obj.get_Pointer_To_Symbol_Table())
        pe_file_header_.number_of_symbols = NonNegativeInteger.from_obj(pe_file_header_obj.get_Number_Of_Symbols())
        pe_file_header_.size_of_optional_header = HexBinary.from_obj(pe_file_header_obj.get_Size_Of_Optional_Header())
        pe_file_header_.characteristics = HexBinary.from_obj(pe_file_header_obj.get_Characteristics())
        pe_file_header_.hashes = HashList.from_obj(pe_file_header_obj.get_Hashes())
        return pe_file_header_

class PEOptionalHeader(cybox.Entity):
    def __init__(self):
        super(PEOptionalHeader, self).__init__()
        self.magic = None
        self.major_linker_version = None
        self.minor_linker_version = None
        self.size_of_code = None
        self.size_of_initialized_data = None
        self.size_of_uninitialized_data = None
        self.address_of_entry_point = None
        self.base_of_code = None
        self.base_of_data = None
        self.image_base = None
        self.section_alignment = None
        self.file_alignment = None
        self.major_os_version = None
        self.minor_os_version = None
        self.major_image_version = None
        self.minor_image_version = None
        self.major_subsystem_version = None
        self.minor_subsystem_version = None
        self.win32_version_value = None
        self.size_of_image = None
        self.size_of_headers = None
        self.checksum = None
        self.subsystem = None
        self.dll_characteristics = None
        self.size_of_stack_reserve = None
        self.size_of_stack_commit = None
        self.size_of_heap_reserve = None
        self.size_of_heap_commit = None
        self.loader_flags = None
        self.number_of_rva_and_sizes = None
        self.data_directory = None
        self.hashes = None

    def to_obj(self):
        pe_optional_header_obj = win_executable_file_binding.PEOptionalHeaderType()
        if self.magic is not None : pe_optional_header_obj.set_Magic(self.magic.to_obj())
        if self.major_linker_version is not None : pe_optional_header_obj.set_Major_Linker_Version(self.major_linker_version.to_obj())
        if self.minor_linker_version is not None : pe_optional_header_obj.set_Minor_Linker_Version(self.minor_linker_version.to_obj())
        if self.size_of_code is not None : pe_optional_header_obj.set_Size_Of_Code(self.size_of_code.to_obj())
        if self.size_of_initialized_data is not None : pe_optional_header_obj.set_Size_Of_Initialized_Data(self.size_of_initialized_data.to_obj())
        if self.size_of_uninitialized_data is not None : pe_optional_header_obj.set_Size_Of_Unitialized_Data(self.size_of_uninitialized_data.to_obj())
        if self.address_of_entry_point is not None : pe_optional_header_obj.set_Address_Of_Entry_Point(self.address_of_entry_point.to_obj())
        if self.base_of_code is not None : pe_optional_header_obj.set_Base_Of_Code(self.base_of_code.to_obj())
        if self.base_of_data is not None : pe_optional_header_obj.set_Base_Of_Data(self.base_of_data.to_obj())
        if self.image_base is not None : pe_optional_header_obj.set_Image_Base(self.image_base.to_obj())
        if self.section_alignment is not None : pe_optional_header_obj.set_Section_Alignment(self.section_alignment.to_obj())
        if self.file_alignment is not None : pe_optional_header_obj.set_File_Alignment(self.file_alignment.to_obj())
        if self.major_os_version is not None : pe_optional_header_obj.set_Major_OS_Version(self.major_os_version.to_obj())
        if self.minor_os_version is not None : pe_optional_header_obj.set_Minor_OS_Version(self.minor_os_version.to_obj())
        if self.major_image_version is not None : pe_optional_header_obj.set_Major_Image_Version(self.major_image_version.to_obj())
        if self.minor_image_version is not None : pe_optional_header_obj.set_Minor_Image_Version(self.minor_image_version.to_obj())
        if self.major_subsystem_version is not None : pe_optional_header_obj.set_Major_Subsystem_Version(self.major_subsystem_version.to_obj())
        if self.minor_subsystem_version is not None : pe_optional_header_obj.set_Minor_Subsystem_Version(self.minor_subsystem_version.to_obj())
        if self.win32_version_value is not None : pe_optional_header_obj.set_Win32_Version_Value(self.win32_version_value.to_obj())
        if self.size_of_image is not None : pe_optional_header_obj.set_Size_Of_Image(self.size_of_image.to_obj())
        if self.size_of_headers is not None : pe_optional_header_obj.set_Size_Of_Headers(self.size_of_headers.to_obj())
        if self.checksum is not None : pe_optional_header_obj.set_Checksum(self.checksum.to_obj())
        if self.subsystem is not None : pe_optional_header_obj.set_Subsystem(self.subsystem.to_obj())
        if self.dll_characteristics is not None : pe_optional_header_obj.set_DLL_Characteristics(self.dll_characteristics.to_obj())
        if self.size_of_stack_reserve is not None : pe_optional_header_obj.set_Size_Of_Stack_Reserve(self.size_of_stack_reserve.to_obj())
        if self.size_of_stack_commit is not None : pe_optional_header_obj.set_Size_Of_Stack_Commit(self.size_of_stack_commit.to_obj())
        if self.size_of_heap_reserve is not None : pe_optional_header_obj.set_Size_Of_Heap_Reserve(self.size_of_heap_reserve.to_obj())
        if self.size_of_heap_commit is not None : pe_optional_header_obj.set_Size_Of_Heap_Commit(self.size_of_heap_commit.to_obj())
        if self.loader_flags is not None : pe_optional_header_obj.set_Loader_Flags(self.loader_flags.to_obj())
        if self.number_of_rva_and_sizes is not None : pe_optional_header_obj.set_Number_Of_Rva_And_Size(self.number_of_rva_and_sizes.to_obj())
        if self.data_directory is not None : pe_optional_header_obj.set_Data_Directory(self.data_directory.to_obj())
        if self.hashes is not None : pe_optional_header_obj.set_Hashes(self.hashes.to_obj())
        return pe_optional_header_obj

    def to_dict(self):
        pe_optional_header_dict = {}
        if self.magic is not None : pe_optional_header_dict['magic'] = self.magic.to_dict()
        if self.major_linker_version is not None : pe_optional_header_dict['major_linker_version'] = self.major_linker_version.to_dict()
        if self.minor_linker_version is not None : pe_optional_header_dict['minor_linker_version'] = self.minor_linker_version.to_dict()
        if self.size_of_code is not None : pe_optional_header_dict['size_of_code'] = self.size_of_code.to_dict()
        if self.size_of_initialized_data is not None : pe_optional_header_dict['size_of_initialized_data'] = self.size_of_initialized_data.to_dict()
        if self.size_of_uninitialized_data is not None : pe_optional_header_dict['size_of_uninitialized_data'] = self.size_of_uninitialized_data.to_dict()
        if self.address_of_entry_point is not None : pe_optional_header_dict['address_of_entry_point'] = self.address_of_entry_point.to_dict()
        if self.base_of_code is not None : pe_optional_header_dict['base_of_code'] = self.base_of_code.to_dict()
        if self.base_of_data is not None : pe_optional_header_dict['base_of_data'] = self.base_of_data.to_dict()
        if self.image_base is not None : pe_optional_header_dict['image_base'] = self.image_base.to_dict()
        if self.section_alignment is not None : pe_optional_header_dict['section_alignment'] = self.section_alignment.to_dict()
        if self.file_alignment is not None : pe_optional_header_dict['file_alignment'] = self.file_alignment.to_dict()
        if self.major_os_version is not None : pe_optional_header_dict['major_os_version'] = self.major_os_version.to_dict()
        if self.minor_os_version is not None : pe_optional_header_dict['minor_os_version'] = self.minor_os_version.to_dict()
        if self.major_image_version is not None : pe_optional_header_dict['major_image_version'] = self.major_image_version.to_dict()
        if self.minor_image_version is not None : pe_optional_header_dict['minor_image_version'] = self.minor_image_version.to_dict()
        if self.major_subsystem_version is not None : pe_optional_header_dict['major_subsystem_version'] = self.major_subsystem_version.to_dict()
        if self.minor_subsystem_version is not None : pe_optional_header_dict['minor_subsystem_version'] = self.minor_subsystem_version.to_dict()
        if self.win32_version_value is not None : pe_optional_header_dict['win32_version_value'] = self.win32_version_value.to_dict()
        if self.size_of_image is not None : pe_optional_header_dict['size_of_image'] = self.size_of_image.to_dict()
        if self.size_of_headers is not None : pe_optional_header_dict['size_of_headers'] = self.size_of_headers.to_dict()
        if self.checksum is not None : pe_optional_header_dict['checksum'] = self.checksum.to_dict()
        if self.subsystem is not None : pe_optional_header_dict['subsystem'] = self.subsystem.to_dict()
        if self.dll_characteristics is not None : pe_optional_header_dict['dll_characteristics'] = self.dll_characteristics.to_dict()
        if self.size_of_stack_reserve is not None : pe_optional_header_dict['size_of_stack_reserve'] = self.size_of_stack_reserve.to_dict()
        if self.size_of_stack_commit is not None : pe_optional_header_dict['size_of_stack_commit'] = self.size_of_stack_commit.to_dict()
        if self.size_of_heap_reserve is not None : pe_optional_header_dict['size_of_heap_reserve'] = self.size_of_heap_reserve.to_dict()
        if self.size_of_heap_commit is not None : pe_optional_header_dict['size_of_heap_commit'] = self.size_of_heap_commit.to_dict()
        if self.loader_flags is not None : pe_optional_header_dict['loader_flags'] = self.loader_flags.to_dict()
        if self.number_of_rva_and_sizes is not None : pe_optional_header_dict['number_of_rva_and_sizes'] = self.number_of_rva_and_sizes.to_dict()
        if self.data_directory is not None : pe_optional_header_dict['data_directory'] = self.data_directory.to_dict()
        if self.hashes is not None : pe_optional_header_dict['hashes'] = self.hashes.to_list()
        return pe_optional_header_dict

    @staticmethod
    def from_dict(pe_optional_header_dict):
        if not pe_optional_header_dict:
            return None
        pe_optional_header_ = PEOptionalHeader()
        pe_optional_header_.magic = HexBinary.from_dict(pe_optional_header_dict.get('magic'))
        pe_optional_header_.major_linker_version = HexBinary.from_dict(pe_optional_header_dict.get('major_linker_version'))
        pe_optional_header_.minor_linker_version = HexBinary.from_dict(pe_optional_header_dict.get('minor_linker_version'))
        pe_optional_header_.size_of_code = HexBinary.from_dict(pe_optional_header_dict.get('size_of_code'))
        pe_optional_header_.size_of_initialized_data = HexBinary.from_dict(pe_optional_header_dict.get('size_of_initialized_data'))
        pe_optional_header_.size_of_uninitialized_data = HexBinary.from_dict(pe_optional_header_dict.get('size_of_uninitialized_data'))
        pe_optional_header_.address_of_entry_point = HexBinary.from_dict(pe_optional_header_dict.get('address_of_entry_point'))
        pe_optional_header_.base_of_code = HexBinary.from_dict(pe_optional_header_dict.get('base_of_code'))
        pe_optional_header_.base_of_data = HexBinary.from_dict(pe_optional_header_dict.get('base_of_data'))
        pe_optional_header_.image_base = HexBinary.from_dict(pe_optional_header_dict.get('image_base'))
        pe_optional_header_.section_alignment = HexBinary.from_dict(pe_optional_header_dict.get('section_alignment'))
        pe_optional_header_.file_alignment = HexBinary.from_dict(pe_optional_header_dict.get('file_alignment'))
        pe_optional_header_.major_os_version = HexBinary.from_dict(pe_optional_header_dict.get('major_os_version'))
        pe_optional_header_.minor_os_version = HexBinary.from_dict(pe_optional_header_dict.get('minor_os_version'))
        pe_optional_header_.major_image_version = HexBinary.from_dict(pe_optional_header_dict.get('major_image_version'))
        pe_optional_header_.minor_image_version = HexBinary.from_dict(pe_optional_header_dict.get('minor_image_version'))
        pe_optional_header_.major_subsystem_version = HexBinary.from_dict(pe_optional_header_dict.get('major_subsystem_version'))
        pe_optional_header_.minor_subsystem_version = HexBinary.from_dict(pe_optional_header_dict.get('minor_subsystem_version'))
        pe_optional_header_.win32_version_value = HexBinary.from_dict(pe_optional_header_dict.get('win32_version_value'))
        pe_optional_header_.size_of_image = HexBinary.from_dict(pe_optional_header_dict.get('size_of_image'))
        pe_optional_header_.size_of_headers = HexBinary.from_dict(pe_optional_header_dict.get('size_of_headers'))
        pe_optional_header_.checksum = HexBinary.from_dict(pe_optional_header_dict.get('checksum'))
        pe_optional_header_.subsystem = HexBinary.from_dict(pe_optional_header_dict.get('subsystem'))
        pe_optional_header_.dll_characteristics = HexBinary.from_dict(pe_optional_header_dict.get('dll_characteristics'))
        pe_optional_header_.size_of_stack_reserve = HexBinary.from_dict(pe_optional_header_dict.get('size_of_stack_reserve'))
        pe_optional_header_.size_of_stack_commit = HexBinary.from_dict(pe_optional_header_dict.get('size_of_stack_commit'))
        pe_optional_header_.size_of_heap_reserve = HexBinary.from_dict(pe_optional_header_dict.get('size_of_heap_reserve'))
        pe_optional_header_.size_of_heap_commit = HexBinary.from_dict(pe_optional_header_dict.get('size_of_heap_commit'))
        pe_optional_header_.loader_flags = HexBinary.from_dict(pe_optional_header_dict.get('loader_flags'))
        pe_optional_header_.number_of_rva_and_sizes = HexBinary.from_dict(pe_optional_header_dict.get('number_of_rva_and_sizes'))
        pe_optional_header_.data_directory = DataDirectory.from_dict(pe_optional_header_dict.get('data_directory'))
        pe_optional_header_.hashes = HashList.from_list(pe_optional_header_dict.get('hashes'))
        return pe_optional_header_

    @staticmethod
    def from_obj(pe_optional_header_obj):
        if not pe_optional_header_obj:
            return None
        pe_optional_header_ = PEOptionalHeader()
        pe_optional_header_.magic = HexBinary.from_obj(pe_optional_header_obj.get_Magic())
        pe_optional_header_.major_linker_version = HexBinary.from_obj(pe_optional_header_obj.get_Major_Linker_Version())
        pe_optional_header_.minor_linker_version = HexBinary.from_obj(pe_optional_header_obj.get_Minor_Linker_Version())
        pe_optional_header_.size_of_code = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Code())
        pe_optional_header_.size_of_initialized_data = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Initialized_Data())
        pe_optional_header_.size_of_uninitialized_data = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Uninitialized_Data())
        pe_optional_header_.address_of_entry_point = HexBinary.from_obj(pe_optional_header_obj.get_Address_Of_Entry_Point())
        pe_optional_header_.base_of_code = HexBinary.from_obj(pe_optional_header_obj.get_Base_Of_Code())
        pe_optional_header_.base_of_data = HexBinary.from_obj(pe_optional_header_obj.get_Base_Of_Data())
        pe_optional_header_.image_base = HexBinary.from_obj(pe_optional_header_obj.get_Image_Base())
        pe_optional_header_.section_alignment = HexBinary.from_obj(pe_optional_header_obj.get_Section_Alignment())
        pe_optional_header_.file_alignment = HexBinary.from_obj(pe_optional_header_obj.get_File_Alignment())
        pe_optional_header_.major_os_version = HexBinary.from_obj(pe_optional_header_obj.get_Major_OS_Version())
        pe_optional_header_.minor_os_version = HexBinary.from_obj(pe_optional_header_obj.get_Minor_OS_Version())
        pe_optional_header_.major_image_version = HexBinary.from_obj(pe_optional_header_obj.get_Major_Image_Version())
        pe_optional_header_.minor_image_version = HexBinary.from_obj(pe_optional_header_obj.get_Minor_Image_Version())
        pe_optional_header_.major_subsystem_version = HexBinary.from_obj(pe_optional_header_obj.get_Major_Subsystem_Version())
        pe_optional_header_.minor_subsystem_version = HexBinary.from_obj(pe_optional_header_obj.get_Minor_Subsystem_Version())
        pe_optional_header_.win32_version_value = HexBinary.from_obj(pe_optional_header_obj.get_Win32_Version_Value())
        pe_optional_header_.size_of_image = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Image())
        pe_optional_header_.size_of_headers = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Headers())
        pe_optional_header_.checksum = HexBinary.from_obj(pe_optional_header_obj.get_Checksum())
        pe_optional_header_.subsystem = HexBinary.from_obj(pe_optional_header_obj.get_Subsystem())
        pe_optional_header_.dll_characteristics = HexBinary.from_obj(pe_optional_header_obj.get_DLL_Characteristics())
        pe_optional_header_.size_of_stack_reserve = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Stack_Reserve())
        pe_optional_header_.size_of_stack_commit = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Stack_Commit())
        pe_optional_header_.size_of_heap_reserve = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Heap_Reserve())
        pe_optional_header_.size_of_heap_commit = HexBinary.from_obj(pe_optional_header_obj.get_Size_Of_Heap_Commit())
        pe_optional_header_.loader_flags = HexBinary.from_obj(pe_optional_header_obj.get_Loader_Flags())
        pe_optional_header_.number_of_rva_and_sizes = HexBinary.from_obj(pe_optional_header_obj.get_Number_Of_Rva_And_Sizes())
        pe_optional_header_.data_directory = DataDirectory.from_obj(pe_optional_header_obj.get_Data_Directory())
        pe_optional_header_.hashes = HashList.from_obj(pe_optional_header_dict.get_Hashes())
        return pe_optional_header_

class DataDirectory(cybox.Entity):
    def __init__(self):
        super(DataDirectory, self).__init__()
        self.export_table = None
        self.import_table = None
        self.resource_table = None
        self.exception_table = None
        self.certificate_table = None
        self.base_relocation_table = None
        self.debug = None
        self.architecture = None
        self.global_ptr = None
        self.tls_table = None
        self.load_config_table = None
        self.bound_import = None
        self.import_address_table = None
        self.delay_import_descriptor = None
        self.clr_runtime_header = None
        self.reserved = None

    def to_obj(self):
        data_directory_obj = win_executable_file_binding.DataDirectoryType()
        if self.export_table is not None : data_directory_obj.set_Export_Table(self.export_table.to_obj())
        if self.import_table is not None : data_directory_obj.set_Import_Table(self.import_table.to_obj())
        if self.resource_table is not None : data_directory_obj.set_Resource_Table(self.resource_table.to_obj())
        if self.exception_table is not None : data_directory_obj.set_Exception_Table(self.exception_table.to_obj())
        if self.certificate_table is not None : data_directory_obj.set_Certificate_Table(self.certificate_table.to_obj())
        if self.base_relocation_table is not None : data_directory_obj.set_Base_Relocation_Table(self.base_relocation_table.to_obj())
        if self.debug is not None : data_directory_obj.set_Debug(self.debug.to_obj())
        if self.architecture is not None : data_directory_obj.set_Architecture(self.architecture.to_obj())
        if self.global_ptr is not None : data_directory_obj.set_Global_Ptr(self.global_ptr.to_obj())
        if self.tls_table is not None : data_directory_obj.set_TLS_Table(self.tls_table.to_obj())
        if self.load_config_table is not None : data_directory_obj.set_Load_Config_Table(self.load_config_table.to_obj())
        if self.bound_import is not None : data_directory_obj.set_Bound_Import(self.bound_import.to_obj())
        if self.import_address_table is not None : data_directory_obj.set_Import_Address_Table(self.import_address_table.to_obj())
        if self.delay_import_descriptor is not None : data_directory_obj.set_Delay_Import_Descriptor(self.dict_from_object.to_obj())
        if self.clr_runtime_header is not None : data_directory_obj.set_CLR_Runtime_Header(self.clr_runtime_header.to_obj())
        if self.reserved is not None : data_directory_obj.set_Reserved(self.reserved.to_obj())
        return data_directory_obj

    def to_dict(self):
        data_directory_dict = {}
        if self.export_table is not None : data_directory_dict['export_table'] = self.export_table.to_dict()
        if self.import_table is not None : data_directory_dict['import_table'] = self.import_table.to_dict()
        if self.resource_table is not None : data_directory_dict['resource_table'] = self.resource_table.to_dict()
        if self.exception_table is not None : data_directory_dict['exception_table'] = self.exception_table.to_dict()
        if self.certificate_table is not None : data_directory_dict['certificate_table'] = self.certificate_table.to_dict()
        if self.base_relocation_table is not None : data_directory_dict['base_relocation_table'] = self.base_relocation_table.to_dict()
        if self.debug is not None : data_directory_dict['debug'] = self.debug.to_dict()
        if self.architecture is not None : data_directory_dict['architecture'] = self.architecture.to_dict()
        if self.global_ptr is not None : data_directory_dict['global_ptr'] = self.global_ptr.to_dict()
        if self.tls_table is not None : data_directory_dict['tls_table'] = self.tls_table.to_dict()
        if self.load_config_table is not None : data_directory_dict['load_config_table'] = self.load_config_table.to_dict()
        if self.bound_import is not None : data_directory_dict['bound_import'] = self.bound_import.to_dict()
        if self.import_address_table is not None : data_directory_dict['import_address_table'] = self.import_address_table.to_dict()
        if self.delay_import_descriptor is not None : data_directory_dict['delay_import_descriptor'] = self.delay_import_descriptor.to_dict()
        if self.clr_runtime_header is not None : data_directory_dict['clr_runtime_header'] = self.clr_runtime_header.to_dict()
        if self.reserved is not None : data_directory_dict['reserved'] = self.reserved.to_dict()
        data_directory_dict = {}

    @staticmethod
    def from_dict(data_directory_dict):
        if not data_directory_dict:
            return None
        data_directory_ = DataDirectory()
        data_directory_.export_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('export_table'))
        data_directory_.import_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('import_table'))
        data_directory_.resource_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('resource_table'))
        data_directory_.exception_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('exception_table'))
        data_directory_.certificate_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('certificate_table'))
        data_directory_.base_relocation_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('base_relocation_table'))
        data_directory_.debug = PEDataDirectoryStruct.from_dict(data_directory_dict.get('debug'))
        data_directory_.architecture = PEDataDirectoryStruct.from_dict(data_directory_dict.get('architecture'))
        data_directory_.global_ptr = PEDataDirectoryStruct.from_dict(data_directory_dict.get('global_ptr'))
        data_directory_.tls_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('tls_table'))
        data_directory_.load_config_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('load_config_table'))
        data_directory_.bound_import = PEDataDirectoryStruct.from_dict(data_directory_dict.get('bound_import'))
        data_directory_.import_address_table = PEDataDirectoryStruct.from_dict(data_directory_dict.get('import_address_table'))
        data_directory_.delay_import_descriptor = PEDataDirectoryStruct.from_dict(data_directory_dict.get('delay_import_descriptor'))
        data_directory_.clr_runtime_header = PEDataDirectoryStruct.from_dict(data_directory_dict.get('clr_runtime_header'))
        data_directory_.reserved = PEDataDirectoryStruct.from_dict(data_directory_dict.get('reserved'))
        return data_directory_

    @staticmethod
    def from_obj(data_directory_obj):
        if not data_directory_obj:
            return None
        data_directory_ = DataDirectory()
        data_directory_.export_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Export_Table())
        data_directory_.import_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Import_Table())
        data_directory_.resource_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Resource_Table())
        data_directory_.exception_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Exception_Table())
        data_directory_.certificate_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Certificate_Table())
        data_directory_.base_relocation_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Base_Relocation_Table())
        data_directory_.debug = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Debug())
        data_directory_.architecture = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Architecture())
        data_directory_.global_ptr = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Global_Ptr())
        data_directory_.tls_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_TLS_Table())
        data_directory_.load_config_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Load_Config_Table())
        data_directory_.bound_import = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Bound_Import())
        data_directory_.import_address_table = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Import_Address_Table())
        data_directory_.delay_import_descriptor = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Delay_Import_Descriptor())
        data_directory_.clr_runtime_header = PEDataDirectoryStruct.from_obj(data_directory_obj.get_CLR_Runtime_Header())
        data_directory_.reserved = PEDataDirectoryStruct.from_obj(data_directory_obj.get_Reserved())
        return data_directory_

class PEDataDirectoryStruct(cybox.Entity):
    def __init__(self):
        super(PEDataDirectoryStruct, self).__init__()
        self.virtual_address = None
        self.size = None

    def to_obj(self):
        pe_data_directory_obj = win_executable_file_binding.PEDataDirectoryStructType()
        if self.virtual_address is not None : pe_data_directory_obj.set_Virtual_Address(self.virtual_address.to_obj())
        if self.size is not None : pe_data_directory_obj.set_Size(self.size.to_obj())
        return pe_data_directory_obj

    def to_dict(self):
        pe_data_directory_dict = {}
        if self.virtual_address is not None : pe_data_directory_dict['virtual_address'] = self.virtual_address.to_dict()
        if self.size is not None : pe_data_directory_dict['size'] = self.size.to_dict()
        return pe_data_directory_dict

    @staticmethod
    def from_dict(pe_data_directory_dict):
        if not pe_data_directory_dict:
            return None
        pe_data_directory_struct_ = PEDataDirectoryStruct()
        pe_data_directory_struct_.virtual_address = HexBinary.from_dict(pe_data_directory_dict.get('virtual_address'))
        pe_data_directory_struct_.size = NonNegativeInteger.from_dict(pe_data_directory_dict.get('size'))
        return pe_data_directory_struct_

    @staticmethod
    def from_obj(pe_data_directory_obj):
        if not pe_data_directory_obj:
            return None
        pe_data_directory_struct_ = PEDataDirectoryStruct()
        pe_data_directory_struct_.virtual_address = HexBinary.from_obj(pe_data_directory_obj.get_Virtual_Address())
        pe_data_directory_struct_.size = NonNegativeInteger.from_obj(pe_data_directory_obj.get_Size())
        return pe_data_directory_struct_

class Entropy(cybox.Entity):
    def __init__(self):
        super(Entropy, self).__init__()
        self.value = None
        self.min = None
        self.max = None

    def to_obj(self):
        entropy_obj = win_executable_file_binding.EntropyType()
        if self.value is not None : entropy_obj.set_Value(self.value.to_obj())
        if self.min is not None : entropy_obj.set_Min(self.min.to_obj())
        if self.max is not None : entropy_obj.set_Max(self.max.to_obj())
        return entropy_obj

    def to_dict(self):
        entropy_dict = {}
        if self.value is not None : entropy_dict['value'] = self.value.to_dict()
        if self.min is not None : entropy_dict['min'] = self.min.to_dict()
        if self.max is not None : entropy_dict['max'] = self.max.to_dict()
        return entropy_dict

    @staticmethod
    def from_dict(entropy_dict):
        if not entropy_dict:
            return None
        entropy_ = Entropy()
        entropy_.value = Float.from_dict(entropy_dict.get('value'))
        entropy_.min = Float.from_dict(entropy_dict.get('min'))
        entropy_.max = Float.from_dict(entropy_dict.get('max'))
        return entropy_

    @staticmethod
    def from_obj(entropy_obj):
        if not entropy_obj:
            return None
        entropy_ = Entropy()
        entropy_.value = Float.from_obj(entropy_obj.get_Value())
        entropy_.min = Float.from_obj(entropy_obj.get_Min())
        entropy_.max = Float.from_obj(entropy_obj.get_Max())
        return entropy_

class PEImport(cybox.Entity):
    def __init__(self):
        super(PEImport, self).__init__()
        self.delay_load = None
        self.initially_visible = None
        self.file_name = None
        self.imported_functions = None
        self.virtual_address = None

    def to_obj(self):
        pe_import_obj = win_executable_file_binding.PEImportType()
        if self.delay_load is not None : pe_import_obj.set_delay_load(self.delay_load)
        if self.initially_visible is not None : pe_import_obj.set_initially_visible(self.initially_visible)
        if self.file_name is not None : pe_import_obj.set_File_Name(self.file_name.to_obj())
        if self.imported_functions is not None : pe_import_obj.set_Imported_Functions(self.imported_functions.to_obj())
        if self.virtual_address is not None : pe_import_obj.set_Virtual_Address(self.virtual_address.to_obj())
        return pe_import_obj

    def to_dict(self):
        pe_import_dict = {}
        if self.delay_load is not None : pe_import_dict['delay_load'] = self.delay_load
        if self.initially_visible is not None : pe_import_dict['delay_load'] = self.intially_visible
        if self.file_name is not None : pe_import_dict['file_name'] = self.file_name.to_dict()
        if self.imported_functions is not None : pe_import_dict['imported_functions'] = self.imported_functions.to_list()
        if self.virtual_address is not None : pe_import_dict['virtual_address'] = self.virtual_address.to_dict()
        return pe_import_dict

    @staticmethod
    def from_dict(pe_import_dict):
        if not pe_import_dict:
            return None
        pe_import_ = PEImport()
        pe_import_.delay_load = pe_import_dict.get('delay_load')
        pe_import_.initially_visible = pe_import_dict.get('initially_visible')
        pe_import_.file_name = String.from_dict(pe_import_dict.get('file_name'))
        pe_import_.imported_functions = PEImportedFunctions.from_list(pe_import_dict.get('imported_functions'))
        pe_import_.virtual_address = HexBinary.from_dict(pe_import_dict.get('virtual_address'))
        return pe_import_

    @staticmethod
    def from_obj(pe_import_obj):
        if not pe_import_obj:
            return None
        pe_import_ = PEImport()
        pe_import_.delay_load = pe_import_obj.get_delay_load()
        pe_import_.initially_visible = pe_import_obj.get_initially_visible()
        pe_import_.file_name = String.from_obj(pe_import_obj.get_File_Name())
        pe_import_.imported_functions = PEImportedFunctions.from_obj(pe_import_obj.get_Imported_Functions())
        pe_import_.virtual_address = HexBinary.from_obj(pe_import_obj.get_Virtual_Address())
        return pe_import_

class PEImportList(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEImportListType
    _contained_type = PEImport

    def __init__(self):
        super(PEImportList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Import(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Import()

class PEImportedFunction(cybox.Entity):
    def __init__(self):
        super(PEImportedFunction, self).__init__()
        self.function_name = None
        self.hint = None
        self.ordinal = None
        self.bound = None
        self.virtual_address = None

    def to_obj(self):
        pe_imported_function_obj = win_executable_file_binding.PEImportedFunctionType()
        if self.function_name is not None : pe_imported_function_obj.set_Function_Name(self.function_name.to_obj())
        if self.hint is not None : pe_imported_function_obj.set_Hint(self.hint.to_obj())
        if self.ordinal is not None : pe_imported_function_obj.set_Ordinal(self.ordinal.to_obj())
        if self.bound is not None : pe_imported_function_obj.set_Bound(self.bound.to_obj())
        if self.virtual_address is not None : pe_imported_function_obj.set_Virtual_Address(self.virtual_address.to_obj())
        return pe_imported_function_obj

    def to_dict(self):
        pe_imported_function_dict = {}
        if self.function_name is not None : pe_imported_function_dict['function_name'] = self.function_name.to_dict()
        if self.hint is not None : pe_imported_function_dict['hint'] = self.hint.to_dict()
        if self.ordinal is not None : pe_imported_function_dict['ordinal'] = self.ordinal.to_dict()
        if self.bound is not None : pe_imported_function_dict['bound'] = self.bound.to_dict()
        if self.virtual_address is not None : pe_imported_function_dict['virtual_address'] = self.virtual_address.to_dict()
        return pe_imported_function_dict

    @staticmethod
    def from_dict(pe_imported_function_dict):
        if not pe_imported_function_dict:
            return None
        pe_imported_function_ = PEImportedFunction()
        pe_imported_function_.function_name = String.from_dict(pe_imported_function_dict.get('function_name'))
        pe_imported_function_.hint = HexBinary.from_dict(pe_imported_function_dict.get('hint'))
        pe_imported_function_.ordinal = NonNegativeInteger.from_dict(pe_imported_function_dict.get('ordinal'))
        pe_imported_function_.bound = HexBinary.from_dict(pe_imported_function_dict.get('bound'))
        pe_imported_function_.virtual_address = HexBinary.from_dict(pe_imported_function_dict.get('virtual_address'))
        return pe_imported_function_

    @staticmethod
    def from_obj(pe_imported_function_obj):
        if not pe_imported_function_obj:
            return None
        pe_imported_function_ = PEImportedFunction()
        pe_imported_function_.function_name = String.from_obj(pe_imported_function_obj.get_Function_Name())
        pe_imported_function_.hint = HexBinary.from_obj(pe_imported_function_obj.get_Hint())
        pe_imported_function_.ordinal = NonNegativeInteger.from_obj(pe_imported_function_obj.get_Ordinal())
        pe_imported_function_.bound = HexBinary.from_obj(pe_imported_function_obj.get_Bound())
        pe_imported_function_.virtual_address = HexBinary.from_obj(pe_imported_function_obj.get_Virtual_Address())
        return pe_imported_function_

class PEImportedFunctions(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEImportedFunctionsType
    _contained_type = PEImportedFunction

    def __init__(self):
        super(PEImportedFunctions, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Imported_Function(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Exported_Function()

class PEChecksum(cybox.Entity):
    def __init__(self):
        super(PEChecksum, self).__init__()
        self.pe_computed_api = None
        self.pe_file_api = None
        self.pe_file_raw = None

    def to_obj(self):
        pe_checksum_obj = win_executable_file_binding.PEChecksumType()
        if self.pe_computed_api is not None : pe_checksum_obj.set_PE_Computed_API(self.pe_computed_api.to_obj())
        if self.pe_file_api is not None : pe_checksum_obj.set_PE_File_API(self.pe_file_api.to_obj())
        if self.pe_file_raw is not None : pe_checksum_obj.set_PE_File_Raw(self.pe_file_raw.to_obj())
        return pe_checksum_obj

    def to_dict(self):
        pe_checksum_dict = {}
        if self.pe_computed_api is not None : pe_checksum_obj.set_PE_Computed_API(self.pe_computed_api.to_obj())
        if self.pe_file_api is not None : pe_checksum_obj.set_PE_File_API(self.pe_file_api.to_obj())
        if self.pe_file_raw is not None : pe_checksum_obj.set_PE_File_Raw(self.pe_file_raw.to_obj())
        return pe_checksum_dict

    @staticmethod
    def from_dict(pe_checksum_dict):
        if not pe_checksum_dict:
            return None
        pe_checksum_ = PEChecksum()
        pe_checksum_.pe_computed_api = Long.from_dict(pe_checksum_dict.get('pe_computed_api'))
        pe_checksum_.pe_file_api = Long.from_dict(pe_checksum_dict.get('pe_file_api'))
        pe_checksum_.pe_file_raw = Long.from_dict(pe_checksum_dict.get('pe_file_raw'))
        return pe_checksum_

    @staticmethod
    def from_obj(pe_checksum_obj):
        if not pe_checksum_obj:
            return None
        pe_checksum_ = PEChecksum()
        pe_checksum_.pe_computed_api = Long.from_obj(pe_checksum_obj.get_PE_Computed_API())
        pe_checksum_.pe_file_api = Long.from_obj(pe_checksum_obj.get_PE_File_API())
        pe_checksum_.pe_file_raw = Long.from_obj(pe_checksum_obj.get_PE_File_Raw())
        return pe_checksum_

class PEResource(cybox.Entity):
    def __init__(self):
        super(PEResource, self).__init__()
        self.type = None
        self.name = None
        self.hashes = None

    def to_obj(self, object_type = None):
        if not object_type:
            pe_resource_obj = win_executable_file_binding.PEResourceType()
        else:
            pe_resource_obj = object_type
        if self.type is not None : pe_resource_obj.set_Type(self.type)
        if self.name is not None : pe_resource_obj.set_Name(self.name.to_obj())
        if self.hashes is not None : pe_resource_obj.set_Hashes(self.hashes.to_obj())
        return pe_resource_obj

    def to_dict(self):
        pe_resource_dict = {}
        if self.type is not None : pe_resource_dict['type'] = self.type
        if self.name is not None : pe_resource_dict['name'] = self.name.to_dict()
        if self.hashes is not None : pe_resource_dict['hashes'] = self.hashes.to_list()
        return pe_resource_dict

    @staticmethod
    def from_dict(pe_resource_dict, resource_class = None):
        if not pe_resource_dict:
            return None
        if not resource_class: 
            pe_resource_ = PEResource()
        else:
            pe_resource_ = resource_class

        pe_resource_.type = pe_resource_dict.get('type')
        pe_resource_.name = String.from_dict(pe_resource_dict.get('name'))
        pe_resource_.hashes = HashList.from_list(pe_resource_dict.get('hashes'))
        return pe_resource_

    @staticmethod
    def from_obj(pe_resource_obj, resource_class = None):
        if not pe_resource_obj:
            return None
        if not resource_class: 
            pe_resource_ = PEResource()
        else:
            pe_resource_ = resource_class
        pe_resource_.type = pe_resource_obj.get_Type()
        pe_resource_.name = String.from_obj(pe_resource_obj.get_Name())
        pe_resource_.hashes = HashList.from_obj(pe_resource_obj.get_Hashes())
        return pe_resource_

class PEResourceList(cybox.EntityList):
    _contained_type = PEResource
    _binding_class = win_executable_file_binding.PEResourceListType

    def __init__(self):
        super(PEResourceList, self).__init__()

    #VersionInfoResource temporary fix
    @staticmethod
    def from_list(pe_resource_list):
        if not pe_resource_list:
            return None
        pe_resource_list_ = PEResourceList()
        for pe_resource_dict in pe_resource_list:
            if PEVersionInfoResource.keyword_test(pe_resource_dict):
                pe_resource_list_.append(PEVersionInfoResource.from_dict(pe_resource_dict))
            else:
                pe_resource_list_.append(PEResource.from_dict(pe_resource_dict))
        return pe_resource_list_

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Resource(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Resource()

class PESection(cybox.Entity):
    def __init__(self):
        super(PESection, self).__init__()
        self.section_header = None
        self.data_hashes = None
        self.entropy = None
        self.header_hashes = None
        self.type = None

    def to_obj(self):
        pe_section_obj = win_executable_file_binding.PESectionType()
        if self.section_header is not None : pe_section_obj.set_Section_Header(self.section_header.to_obj())
        if self.data_hashes is not None : pe_section_obj.set_Data_Hashes(self.data_hashes.to_obj())
        if self.entropy is not None : pe_section_obj.set_Entropy(self.entropy.to_obj())
        if self.header_hashes is not None : pe_section_obj.set_Header_Hashes(self.header_hashes.to_obj())
        if self.type is not None : pe_section_obj.set_Type(self.type.to_obj())
        return pe_section_obj

    def to_dict(self):
        pe_section_dict = {}
        if self.section_header is not None : pe_section_dict['section_header'] = self.section_header.to_dict()
        if self.data_hashes is not None : pe_section_dict['data_hashes'] = self.data_hashes.to_list()
        if self.entropy is not None : pe_section_dict['entropy'] = self.entropy.to_dict()
        if self.header_hashes is not None : pe_section_dict['header_hashes'] = self.header_hashes.to_list()
        if self.type is not None : pe_section_dict['type'] = self.type.to_dict()
        return pe_section_dict

    @staticmethod
    def from_dict(pe_section_dict):
        if not pe_section_dict:
            return None
        pe_section_ = PESection()
        pe_section_.section_header = PESectionHeaderStruct.from_dict(pe_section_dict.get('section_header'))
        pe_section_.data_hashes = HashList.from_list(pe_section_dict.get('data_hashes'))
        pe_section_.entropy = Entropy.from_dict(pe_section_dict.get('entropy'))
        pe_section_.header_hashes = HashList.from_list(pe_section_dict.get('header_hashes'))
        pe_section_.type = String.from_dict(pe_section_dict.get('header_hashes'))
        return pe_section_

    @staticmethod
    def from_obj(pe_section_obj):
        if not pe_section_obj:
            return None
        pe_section_ = PESection()
        pe_section_.section_header = PESectionHeaderStruct.from_obj(pe_section_obj.get_Section_Header())
        pe_section_.data_hashes = HashList.from_obj(pe_section_obj.get_Data_Hashes())
        pe_section_.entropy = Entropy.from_obj(pe_section_obj.get_Entropy())
        pe_section_.header_hashes = HashList.from_obj(pe_section_obj.get_Header_Hashes())
        pe_section_.type = String.from_obj(pe_section_obj.get_Type())
        return pe_section_

class PESectionHeaderStruct(cybox.Entity):

    def __init__(self):
        super(PESectionHeaderStruct, self).__init__()
        self.name = None
        self.virtual_size = None
        self.virtual_address = None
        self.size_of_raw_data = None
        self.pointer_to_raw_data = None
        self.pointer_to_relocations = None
        self.pointer_to_linenumbers = None
        self.number_of_relocations = None
        self.number_of_linenumbers = None
        self.characteristics = None

    def to_obj(self):
        pe_section_header_struct_obj = win_executable_file_binding.PESectionHeaderStructType()
        if self.name is not None : pe_section_header_struct_obj.set_Name(self.name.to_obj())
        if self.virtual_size is not None : pe_section_header_struct_obj.set_Virtual_Size(self.virtual_size.to_obj())
        if self.virtual_address is not None : pe_section_header_struct_obj.set_Virtual_Address(self.virtual_address.to_obj())
        if self.size_of_raw_data is not None : pe_section_header_struct_obj.set_Size_Of_Raw_Data(self.size_of_raw_data.to_obj())
        if self.pointer_to_raw_data is not None : pe_section_header_struct_obj.set_Pointer_To_Raw_Data(self.pointer_to_raw_data.to_obj())
        if self.pointer_to_relocations is not None : pe_section_header_struct_obj.set_Pointer_To_Relocations(self.pointer_to_relocations.to_obj())
        if self.pointer_to_linenumbers is not None : pe_section_header_struct_obj.set_Pointer_To_Linenumbers(self.pointer_to_linenumbers.to_obj())
        if self.number_of_relocations is not None : pe_section_header_struct_obj.set_Number_Of_Relocations(self.number_of_relocations.to_obj())
        if self.number_of_linenumbers is not None : pe_section_header_struct_obj.set_Number_Of_Linenumbers(self.number_of_linenumbers.to_obj())
        if self.characteristics is not None : pe_section_header_struct_obj.set_Characteristics(self.characteristics.to_obj())
        return pe_section_header_struct_obj

    def to_dict(self):
        pe_section_header_struct_dict = {}
        if self.name is not None : pe_section_header_struct_obj.set_Name(self.name.to_obj())
        if self.virtual_size is not None : pe_section_header_struct_obj.set_Virtual_Size(self.virtual_size.to_obj())
        if self.virtual_address is not None : pe_section_header_struct_obj.set_Virtual_Address(self.virtual_address.to_obj())
        if self.size_of_raw_data is not None : pe_section_header_struct_obj.set_Size_Of_Raw_Data(self.size_of_raw_data.to_obj())
        if self.pointer_to_raw_data is not None : pe_section_header_struct_obj.set_Pointer_To_Raw_Data(self.pointer_to_raw_data.to_obj())
        if self.pointer_to_relocations is not None : pe_section_header_struct_obj.set_Pointer_To_Relocations(self.pointer_to_relocations.to_obj())
        if self.pointer_to_linenumbers is not None : pe_section_header_struct_obj.set_Pointer_To_Linenumbers(self.pointer_to_linenumbers.to_obj())
        if self.number_of_relocations is not None : pe_section_header_struct_obj.set_Number_Of_Relocations(self.number_of_relocations.to_obj())
        if self.number_of_linenumbers is not None : pe_section_header_struct_obj.set_Number_Of_Linenumbers(self.number_of_linenumbers.to_obj())
        if self.characteristics is not None : pe_section_header_struct_obj.set_Characteristics(self.characteristics.to_obj())
        return pe_section_header_struct_dict

    @staticmethod
    def from_dict(pe_section_header_struct_dict):
        if not pe_section_header_struct_dict:
            return None
        pe_section_header_struct_ = PESectionHeaderStruct()
        pe_section_header_struct_.name = HexBinary.from_dict(pe_section_header_struct_dict.get('name'))
        pe_section_header_struct_.virtual_size = HexBinary.from_dict(pe_section_header_struct_dict.get('virtual_size'))
        pe_section_header_struct_.virtual_address = HexBinary.from_dict(pe_section_header_struct_dict.get('virtual_address'))
        pe_section_header_struct_.size_of_raw_data = HexBinary.from_dict(pe_section_header_struct_dict.get('size_of_raw_data'))
        pe_section_header_struct_.pointer_to_raw_data = HexBinary.from_dict(pe_section_header_struct_dict.get('pointer_to_raw_data'))
        pe_section_header_struct_.pointer_to_relocations = HexBinary.from_dict(pe_section_header_struct_dict.get('pointer_to_relocations'))
        pe_section_header_struct_.pointer_to_linenumbers = HexBinary.from_dict(pe_section_header_struct_dict.get('pointer_to_linenumbers'))
        pe_section_header_struct_.number_of_relocations = NonNegativeInteger.from_dict(pe_section_header_struct_dict.get('number_of_relocations'))
        pe_section_header_struct_.number_of_linenumbers = NonNegativeInteger.from_dict(pe_section_header_struct_dict.get('number_of_linenumbers'))
        pe_section_header_struct_.characteristics = HexBinary.from_dict(pe_section_header_struct_dict.get('characteristics'))
        return pe_section_header_struct_

    @staticmethod
    def from_obj(pe_section_header_obj):
        if not pe_section_header_obj:
            return None
        pe_section_header_struct_ = PESectionHeaderStruct()
        pe_section_header_struct_.name = HexBinary.from_obj(pe_section_header_obj.get_Name())
        pe_section_header_struct_.virtual_size = HexBinary.from_obj(pe_section_header_obj.get_Virtual_Size())
        pe_section_header_struct_.virtual_address = HexBinary.from_obj(pe_section_header_obj.get_Virtual_Address())
        pe_section_header_struct_.size_of_raw_data = HexBinary.from_obj(pe_section_header_obj.get_Size_Of_Raw_Data())
        pe_section_header_struct_.pointer_to_raw_data = HexBinary.from_obj(pe_section_header_obj.get_Pointer_To_Raw_Data())
        pe_section_header_struct_.pointer_to_relocations = HexBinary.from_obj(pe_section_header_obj.get_Pointer_To_Relocations())
        pe_section_header_struct_.pointer_to_linenumbers = HexBinary.from_obj(pe_section_header_obj.get_Pointer_To_Linenumbers())
        pe_section_header_struct_.number_of_relocations = NonNegativeInteger.from_obj(pe_section_header_obj.get_Number_Of_Relocations())
        pe_section_header_struct_.number_of_linenumbers = NonNegativeInteger.from_obj(pe_section_header_obj.get_Number_Of_Linenumbers())
        pe_section_header_struct_.characteristics = HexBinary.from_obj(pe_section_header_obj.get_Characteristics())
        return pe_section_header_struct_

class PESectionList(cybox.EntityList):
    _binding_class = win_executable_file_binding.PESectionListType
    _contained_type = PESection

    def __init__(self):
        super(PESectionList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Section(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Section()

class PEVersionInfoResource(PEResource):

    def __init__(self):
        super(PEVersionInfoResource, self).__init__()
        self.comments = None
        self.companyname = None
        self.filedescription = None
        self.fileversion = None
        self.internalname = None
        self.langid = None
        self.legalcopyright = None
        self.legaltrademarks = None
        self.originalfilename = None
        self.privatebuild = None
        self.productname = None
        self.productversion = None
        self.specialbuild = None

    def to_obj(self):
        pe_version_info_resource_obj = super(PEVersionInfoResource, self).to_obj(win_executable_file_binding.PEVersionInfoResourceType())
        if self.comments is not None : pe_version_info_resource_obj.set_Comments(self.comments.to_obj())
        if self.companyname is not None : pe_version_info_resource_obj.set_CompanyName(self.companyname.to_obj())
        if self.filedescription is not None : pe_version_info_resource_obj.set_FileDescription(self.filedescription.to_obj())
        if self.fileversion is not None : pe_version_info_resource_obj.set_FileVersion(self.fileversion.to_obj())
        if self.internalname is not None : pe_version_info_resource_obj.set_InternalName(self.internalname.to_obj())
        if self.langid is not None : pe_version_info_resource_obj.set_LangID(self.langid.to_obj())
        if self.legalcopyright is not None : pe_version_info_resource_obj.set_LegalCopyright(self.legalcopyright.to_obj())
        if self.legaltrademarks is not None : pe_version_info_resource_obj.set_LegalTrademarks(self.legaltrademarks.to_obj())
        if self.originalfilename is not None : pe_version_info_resource_obj.set_OriginalFilename(self.originalfilename.to_obj())
        if self.privatebuild is not None : pe_version_info_resource_obj.set_PrivateBuild(self.privatebuild.to_obj())
        if self.productname is not None : pe_version_info_resource_obj.set_ProductName(self.productname.to_obj())
        if self.productversion is not None : pe_version_info_resource_obj.set_ProductVersion(self.productversion.to_obj())
        if self.specialbuild is not None : pe_version_info_resource_obj.set_SpecialBuild(self.specialbuild.to_obj())
        return pe_version_info_resource_obj

    def to_dict(self):
        pe_version_info_resource_dict = super(PEVersionInfoResource, self).to_dict()
        if self.comments is not None : pe_version_info_resource_dict['comments'] = self.comments.to_dict()
        if self.companyname is not None : pe_version_info_resource_dict['companyname'] = self.companyname.to_dict()
        if self.filedescription is not None : pe_version_info_resource_dict['filedescription'] = self.filedescription.to_dict()
        if self.fileversion is not None : pe_version_info_resource_dict['fileversion'] = self.fileversion.to_dict()
        if self.internalname is not None : pe_version_info_resource_dict['internalname'] = self.internalname.to_dict()
        if self.langid is not None : pe_version_info_resource_dict['langid'] = self.langid.to_dict()
        if self.legalcopyright is not None : pe_version_info_resource_dict['legalcopyright'] = self.legalcopyright.to_dict()
        if self.legaltrademarks is not None : pe_version_info_resource_dict['legaltrademarks'] = self.legaltrademarks.to_dict()
        if self.originalfilename is not None : pe_version_info_resource_dict['originalfilename'] = self.originalfilename.to_dict()
        if self.privatebuild is not None : pe_version_info_resource_dict['privatebuild'] = self.privatebuild.to_dict()
        if self.productname is not None : pe_version_info_resource_dict['productname'] = self.productname.to_dict()
        if self.productversion is not None : pe_version_info_resource_dict['productversion'] = self.productversion.to_dict()
        if self.specialbuild is not None : pe_version_info_resource_dict['specialbuild'] = self.specialbuild.to_dict()
        return pe_version_info_resource_dict

    @staticmethod
    def from_dict(pe_version_info_resource_dict):
        if not pe_version_info_resource_dict:
            return None
        pe_version_info_resource_ = PEResource.from_dict(pe_version_info_resource_dict, PEVersionInfoResource())
        pe_version_info_resource_.comments = String.from_dict(pe_version_info_resource_dict.get('comments'))
        pe_version_info_resource_.companyname = String.from_dict(pe_version_info_resource_dict.get('companyname'))
        pe_version_info_resource_.filedescription = String.from_dict(pe_version_info_resource_dict.get('filedescription'))
        pe_version_info_resource_.fileversion = String.from_dict(pe_version_info_resource_dict.get('fileversion'))
        pe_version_info_resource_.internalname = String.from_dict(pe_version_info_resource_dict.get('internalname'))
        pe_version_info_resource_.langid = String.from_dict(pe_version_info_resource_dict.get('langid'))
        pe_version_info_resource_.legalcopyright = String.from_dict(pe_version_info_resource_dict.get('legalcopyright'))
        pe_version_info_resource_.legaltrademarks = String.from_dict(pe_version_info_resource_dict.get('legaltrademarks'))
        pe_version_info_resource_.originalfilename = String.from_dict(pe_version_info_resource_dict.get('originalfilename'))
        pe_version_info_resource_.privatebuild = String.from_dict(pe_version_info_resource_dict.get('privatebuild'))
        pe_version_info_resource_.productname = String.from_dict(pe_version_info_resource_dict.get('productname'))
        pe_version_info_resource_.productversion = String.from_dict(pe_version_info_resource_dict.get('productversion'))
        pe_version_info_resource_.specialbuild = String.from_dict(pe_version_info_resource_dict.get('specialbuild'))
        return pe_version_info_resource_

    @staticmethod
    def from_obj(pe_version_info_resource_obj):
        if not pe_version_info_resource_obj:
            return None
        pe_version_info_resource_ = PEResource.from_obj(pe_version_info_resource_obj, PEVersionInfoResource())
        pe_version_info_resource_.comments = String.from_obj(pe_version_info_resource_obj.get_Comments())
        pe_version_info_resource_.companyname = String.from_obj(pe_version_info_resource_obj.get_CompanyName())
        pe_version_info_resource_.filedescription = String.from_obj(pe_version_info_resource_obj.get_FileDescription())
        pe_version_info_resource_.fileversion = String.from_obj(pe_version_info_resource_obj.get_FileVersion())
        pe_version_info_resource_.internalname = String.from_obj(pe_version_info_resource_obj.get_InternalName())
        pe_version_info_resource_.langid = String.from_obj(pe_version_info_resource_obj.get_LangID())
        pe_version_info_resource_.legalcopyright = String.from_obj(pe_version_info_resource_obj.get_LegalCopyright())
        pe_version_info_resource_.legaltrademarks = String.from_obj(pe_version_info_resource_obj.get_LegalTrademarks())
        pe_version_info_resource_.originalfilename = String.from_obj(pe_version_info_resource_obj.get_OriginalFilename())
        pe_version_info_resource_.privatebuild = String.from_obj(pe_version_info_resource_obj.get_PrivateBuild())
        pe_version_info_resource_.productname = String.from_obj(pe_version_info_resource_obj.get_ProductName())
        pe_version_info_resource_.productversion = String.from_obj(pe_version_info_resource_obj.get_ProductVersion())
        pe_version_info_resource_.specialbuild = String.from_obj(pe_version_info_resource_obj.get_SpecialBuild())
        return pe_version_info_resource_

    @staticmethod
    def keyword_test(pe_resource_dict):
        keywords_list = ['comments',
                         'companyname',
                         'filedescription',
                         'fileversion',
                         'internalname',
                         'langid',
                         'legalcopyright',
                         'originalfilename',
                         'privatebuild',
                         'productname',
                         'productversion',
                         'specialbuild']
        for key in pe_resource_dict:
            if key in keywords_list:
                return True
        return False
