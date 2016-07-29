# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_executable_file_object as win_executable_file_binding
from cybox.common import (DateTime, DigitalSignature, Float, HashList,
        HexBinary, Integer, Long, NonNegativeInteger, String, UnsignedLong, PositiveInteger)
from cybox.objects.win_file_object import WinFile


class Entropy(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.EntropyType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    value = fields.TypedField("Value", Float)
    min = fields.TypedField("Min", Float)
    max = fields.TypedField("Max", Float)


class PEBuildInformation(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEBuildInformationType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    linker_name = fields.TypedField("Linker_Name", String)
    linker_version = fields.TypedField("Linker_Version", String)
    compiler_name = fields.TypedField("Compiler_Name", String)
    compiler_version = fields.TypedField("Compiler_Version", String)


class PEExportedFunction(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEExportedFunctionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    function_name = fields.TypedField("Function_Name", String)
    entry_point = fields.TypedField("Entry_Point", HexBinary)
    ordinal = fields.TypedField("Ordinal", NonNegativeInteger)


class PEExportedFunctions(entities.EntityList):
    _binding_class = win_executable_file_binding.PEExportedFunctionsType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    exported_function = fields.TypedField("Exported_Function", PEExportedFunction, multiple=True)


class PEExports(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEExportsType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    name = fields.TypedField("Name", String)
    exported_functions = fields.TypedField("Exported_Functions", PEExportedFunctions)
    number_of_functions = fields.TypedField("Number_Of_Functions", Integer)
    exports_time_stamp = fields.TypedField("Exports_Time_Stamp", DateTime)
    number_of_addresses = fields.TypedField("Number_Of_Addresses", Long)
    number_of_names = fields.TypedField("Number_Of_Names", Long)


class DOSHeader(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.DOSHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    e_magic = fields.TypedField("e_magic", HexBinary)
    e_cblp = fields.TypedField("e_cblp", HexBinary)
    e_cp = fields.TypedField("e_cp", HexBinary)
    e_crlc = fields.TypedField("e_crlc", HexBinary)
    e_cparhdr = fields.TypedField("e_cparhdr", HexBinary)
    e_minalloc = fields.TypedField("e_minalloc", HexBinary)
    e_maxalloc = fields.TypedField("e_maxalloc", HexBinary)
    e_ss = fields.TypedField("e_ss", HexBinary)
    e_sp = fields.TypedField("e_sp", HexBinary)
    e_csum = fields.TypedField("e_csum", HexBinary)
    e_ip = fields.TypedField("e_ip", HexBinary)
    e_cs = fields.TypedField("e_cs", HexBinary)
    e_lfarlc = fields.TypedField("e_lfarlc", HexBinary)
    e_ovro = fields.TypedField("e_ovro", HexBinary)
    e_oemid = fields.TypedField("e_oemid", HexBinary)
    e_oeminfo = fields.TypedField("e_oeminfo", HexBinary)
    reserved2 = fields.TypedField("reserved2", HexBinary)
    e_lfanew = fields.TypedField("e_lfanew", HexBinary)
    hashes = fields.TypedField("Hashes", HashList)
    #reserved1 = [] unsupported for now


class PEFileHeader(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEFileHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    machine = fields.TypedField("Machine", HexBinary)
    number_of_sections = fields.TypedField("Number_Of_Sections", NonNegativeInteger)
    time_date_stamp = fields.TypedField("Time_Date_Stamp", HexBinary)
    pointer_to_symbol_table = fields.TypedField("Pointer_To_Symbol_Table", HexBinary)
    number_of_symbols = fields.TypedField("Number_Of_Symbols", NonNegativeInteger)
    size_of_optional_header = fields.TypedField("Size_Of_Optional_Header", HexBinary)
    characteristics = fields.TypedField("Characteristics", HexBinary)
    hashes = fields.TypedField("Hashes", HashList)


class PEDataDirectoryStruct(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEDataDirectoryStructType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    virtual_address = fields.TypedField("Virtual_Address", HexBinary)
    size = fields.TypedField("Size", NonNegativeInteger)


class DataDirectory(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.DataDirectoryType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    export_table = fields.TypedField("Export_Table", PEDataDirectoryStruct)
    import_table = fields.TypedField("Import_Table", PEDataDirectoryStruct)
    resource_table = fields.TypedField("Resource_Table", PEDataDirectoryStruct)
    exception_table = fields.TypedField("Exception_Table", PEDataDirectoryStruct)
    certificate_table = fields.TypedField("Certificate_Table", PEDataDirectoryStruct)
    base_relocation_table = fields.TypedField("Base_Relocation_Table", PEDataDirectoryStruct)
    debug = fields.TypedField("Debug", PEDataDirectoryStruct)
    architecture = fields.TypedField("Architecture", PEDataDirectoryStruct)
    global_ptr = fields.TypedField("Global_Ptr", PEDataDirectoryStruct)
    tls_table = fields.TypedField("Tls_Table", PEDataDirectoryStruct)
    load_config_table = fields.TypedField("Load_Config_Table", PEDataDirectoryStruct)
    bound_import = fields.TypedField("Bound_Import", PEDataDirectoryStruct)
    import_address_table = fields.TypedField("Import_Address_Table", PEDataDirectoryStruct)
    delay_import_descriptor = fields.TypedField("Delay_Import_Descriptor", PEDataDirectoryStruct)
    clr_runtime_header = fields.TypedField("CLR_Runtime_Header", PEDataDirectoryStruct)
    reserved = fields.TypedField("Reserved", PEDataDirectoryStruct)


class PEOptionalHeader(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEOptionalHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    magic = fields.TypedField("Magic", HexBinary)
    major_linker_version = fields.TypedField("Major_Linker_Version", HexBinary)
    minor_linker_version = fields.TypedField("Minor_Linker_Version", HexBinary)
    size_of_code = fields.TypedField("Size_Of_Code", HexBinary)
    size_of_initialized_data = fields.TypedField("Size_Of_Initialized_Data", HexBinary)
    size_of_uninitialized_data = fields.TypedField("Size_Of_Uninitialized_Data", HexBinary)
    address_of_entry_point = fields.TypedField("Address_Of_Entry_Point", HexBinary)
    base_of_code = fields.TypedField("Base_Of_Code", HexBinary)
    base_of_data = fields.TypedField("Base_Of_Data", HexBinary)
    image_base = fields.TypedField("Image_Base", HexBinary)
    section_alignment = fields.TypedField("Section_Alignment", HexBinary)
    file_alignment = fields.TypedField("File_Alignment", HexBinary)
    major_os_version = fields.TypedField("Major_OS_Version", HexBinary)
    minor_os_version = fields.TypedField("Minor_OS_Version", HexBinary)
    major_image_version = fields.TypedField("Major_Image_Version", HexBinary)
    minor_image_version = fields.TypedField("Minor_Image_Version", HexBinary)
    major_subsystem_version = fields.TypedField("Major_Subsystem_Version", HexBinary)
    minor_subsystem_version = fields.TypedField("Minor_Subsystem_Version", HexBinary)
    win32_version_value = fields.TypedField("Win32_Version_Value", HexBinary)
    size_of_image = fields.TypedField("Size_Of_Image", HexBinary)
    size_of_headers = fields.TypedField("Size_Of_Headers", HexBinary)
    checksum = fields.TypedField("Checksum", HexBinary)
    subsystem = fields.TypedField("Subsystem", HexBinary)
    dll_characteristics = fields.TypedField("DLL_Characteristics", HexBinary)
    size_of_stack_reserve = fields.TypedField("Size_Of_Stack_Reserve", HexBinary)
    size_of_stack_commit = fields.TypedField("Size_Of_Stack_Commit", HexBinary)
    size_of_heap_reserve = fields.TypedField("Size_Of_Heap_Reserve", HexBinary)
    size_of_heap_commit = fields.TypedField("Size_Of_Heap_Commit", HexBinary)
    loader_flags = fields.TypedField("Loader_Flags", HexBinary)
    number_of_rva_and_sizes = fields.TypedField("Number_Of_Rva_And_Sizes", HexBinary)
    data_directory = fields.TypedField("Data_Directory", DataDirectory)
    hashes = fields.TypedField("Hashes", HashList)


class PEHeaders(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEHeadersType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    dos_header = fields.TypedField("DOS_Header", DOSHeader)
    signature = fields.TypedField("Signature", HexBinary)
    file_header = fields.TypedField("File_Header", PEFileHeader)
    optional_header = fields.TypedField("Optional_Header", PEOptionalHeader)
    entropy = fields.TypedField("Entropy", Entropy)
    hashes = fields.TypedField("Hashes", HashList)


class PEImportedFunction(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEImportedFunctionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    function_name = fields.TypedField("Function_Name", String)
    hint = fields.TypedField("Hint", HexBinary)
    ordinal = fields.TypedField("Ordinal", NonNegativeInteger)
    bound = fields.TypedField("Bound", HexBinary)
    virtual_address = fields.TypedField("Virtual_Address", HexBinary)


class PEImportedFunctions(entities.EntityList):
    _binding_class = win_executable_file_binding.PEImportedFunctionsType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    imported_function = fields.TypedField("Imported_Function", PEImportedFunction, multiple=True)


class PEImport(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEImportType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    delay_load = fields.TypedField("delay_load")
    initially_visible = fields.TypedField("initially_visible")
    file_name = fields.TypedField("File_Name", String)
    imported_functions = fields.TypedField("Imported_Functions", PEImportedFunctions)
    virtual_address = fields.TypedField("Virtual_Address", HexBinary)


class PEImportList(entities.EntityList):
    _binding_class = win_executable_file_binding.PEImportListType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    import_ = fields.TypedField("Import", PEImport, multiple=True)


class PEChecksum(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEChecksumType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    pe_computed_api = fields.TypedField("PE_Computed_API", Long)
    pe_file_api = fields.TypedField("PE_File_API", Long)
    pe_file_raw = fields.TypedField("PE_File_Raw", Long)


class PEResource(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEResourceType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    type_ = fields.TypedField("Type", String)
    name = fields.TypedField("Name", String)
    size = fields.TypedField("Size", PositiveInteger)
    virtual_address = fields.TypedField("Virtual_Address", HexBinary)
    language = fields.TypedField("Language", String)
    sub_language = fields.TypedField("Sub_Language", String)
    hashes = fields.TypedField("Hashes", HashList)
    data = fields.TypedField("Data", String)


class PEResourceList(entities.EntityList):
    _binding_class = win_executable_file_binding.PEResourceListType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    resource = fields.TypedField("Resource", PEResource, multiple=True)

    #VersionInfoResource temporary fix
    @classmethod
    def from_list(cls, seq):
        if not seq:
            return None

        # TODO (bworrell): Should this just call cls(). Does this class need
        # an EntityFactory?
        pe_resource_list_ = super(PEResourceList, cls).from_list(seq)

        for pe_resource_dict in seq:
            if PEVersionInfoResource.keyword_test(pe_resource_dict):
                pe_resource_list_.append(PEVersionInfoResource.from_dict(pe_resource_dict))
            else:
                pe_resource_list_.append(PEResource.from_dict(pe_resource_dict))
        return pe_resource_list_


class PESectionHeaderStruct(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PESectionHeaderStructType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    name = fields.TypedField("Name", String)
    virtual_size = fields.TypedField("Virtual_Size", HexBinary)
    virtual_address = fields.TypedField("Virtual_Address", HexBinary)
    size_of_raw_data = fields.TypedField("Size_Of_Raw_Data", HexBinary)
    pointer_to_raw_data = fields.TypedField("Pointer_To_Raw_Data", HexBinary)
    pointer_to_relocations = fields.TypedField("Pointer_To_Relocations", HexBinary)
    pointer_to_linenumbers = fields.TypedField("Pointer_To_Linenumbers", HexBinary)
    number_of_relocations = fields.TypedField("Number_Of_Relocations", NonNegativeInteger)
    number_of_linenumbers = fields.TypedField("Number_Of_Linenumbers", NonNegativeInteger)
    characteristics = fields.TypedField("Characteristics", HexBinary)


class PESection(entities.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PESectionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    section_header = fields.TypedField("Section_Header", PESectionHeaderStruct)
    data_hashes = fields.TypedField("Data_Hashes", HashList)
    entropy = fields.TypedField("Entropy", Entropy)
    header_hashes = fields.TypedField("Header_Hashes", HashList)


class PESectionList(entities.EntityList):
    _binding_class = win_executable_file_binding.PESectionListType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    section = fields.TypedField("Section", PESection, multiple=True)


class PEVersionInfoResource(PEResource):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEVersionInfoResourceType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    comments = fields.TypedField("Comments", String)
    companyname = fields.TypedField("CompanyName", String)
    filedescription = fields.TypedField("FileDescription", String)
    fileversion = fields.TypedField("FileVersion", String)
    internalname = fields.TypedField("InternalName", String)
    langid = fields.TypedField("LangID", String)
    legalcopyright = fields.TypedField("LegalCopyright", String)
    legaltrademarks = fields.TypedField("LegalTrademarks", String)
    originalfilename = fields.TypedField("OriginalFilename", String)
    privatebuild = fields.TypedField("PrivateBuild", String)
    productname = fields.TypedField("ProductName", String)
    productversion = fields.TypedField("ProductVersion", String)
    specialbuild = fields.TypedField("SpecialBuild", String)

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

        return any(key in keywords_list for key in pe_resource_dict)


class WinExecutableFile(WinFile):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.WindowsExecutableFileObjectType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    _XSI_NS = "WinExecutableFileObj"
    _XSI_TYPE = "WindowsExecutableFileObjectType"

    build_information = fields.TypedField("Build_Information", PEBuildInformation)
    digital_signature = fields.TypedField("Digital_Signature", DigitalSignature)
    exports = fields.TypedField("Exports", PEExports)
    extraneous_bytes = fields.TypedField("Extraneous_Bytes", Integer)
    headers = fields.TypedField("Headers", PEHeaders)
    imports = fields.TypedField("Imports", PEImportList)
    pe_checksum = fields.TypedField("PE_Checksum", PEChecksum)
    resources = fields.TypedField("Resources", PEResourceList)
    sections = fields.TypedField("Sections", PESectionList)
    type_ = fields.TypedField("Type", String)
