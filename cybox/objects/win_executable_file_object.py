# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_executable_file_object as win_executable_file_binding
from cybox.common import (DateTime, DigitalSignature, Float, HashList,
        HexBinary, Integer, Long, NonNegativeInteger, String, UnsignedLong, PositiveInteger)
from cybox.objects.win_file_object import WinFile

class Entropy(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.EntropyType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    value = cybox.TypedField("Value", Float)
    min = cybox.TypedField("Min", Float)
    max = cybox.TypedField("Max", Float)

class PEBuildInformation(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEBuildInformationType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    linker_name = cybox.TypedField("Linker_Name", String)
    linker_version = cybox.TypedField("Linker_Version", String)
    compiler_name = cybox.TypedField("Compiler_Name", String)
    compiler_version = cybox.TypedField("Compiler_Version", String)

class PEExportedFunction(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEExportedFunctionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    function_name = cybox.TypedField("Function_Name", String)
    entry_point = cybox.TypedField("Entry_Point", HexBinary)
    ordinal = cybox.TypedField("Ordinal", NonNegativeInteger)

class PEExportedFunctions(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEExportedFunctionsType
    _binding_var = "Exported_Function"
    _contained_type = PEExportedFunction
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

class PEExports(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEExportsType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    name = cybox.TypedField("Name", String)
    exported_functions = cybox.TypedField("Exported_Functions", PEExportedFunctions)
    number_of_functions = cybox.TypedField("Number_Of_Functions", Integer)
    exports_time_stamp = cybox.TypedField("Exports_Time_Stamp", DateTime)
    number_of_addresses = cybox.TypedField("Number_Of_Addresses", Long)
    number_of_names = cybox.TypedField("Number_Of_Names", Long)

class DOSHeader(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.DOSHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    e_magic = cybox.TypedField("e_magic", HexBinary)
    e_cblp = cybox.TypedField("e_cblp", HexBinary)
    e_cp = cybox.TypedField("e_cp", HexBinary)
    e_crlc = cybox.TypedField("e_crlc", HexBinary)
    e_cparhdr = cybox.TypedField("e_cparhdr", HexBinary)
    e_minalloc = cybox.TypedField("e_minalloc", HexBinary)
    e_maxalloc = cybox.TypedField("e_maxalloc", HexBinary)
    e_ss = cybox.TypedField("e_ss", HexBinary)
    e_sp = cybox.TypedField("e_sp", HexBinary)
    e_csum = cybox.TypedField("e_csum", HexBinary)
    e_ip = cybox.TypedField("e_ip", HexBinary)
    e_cs = cybox.TypedField("e_cs", HexBinary)
    e_lfarlc = cybox.TypedField("e_lfarlc", HexBinary)
    e_ovro = cybox.TypedField("e_ovro", HexBinary)
    e_oemid = cybox.TypedField("e_oemid", HexBinary)
    e_oeminfo = cybox.TypedField("e_oeminfo", HexBinary)
    reserved2 = cybox.TypedField("reserved2", HexBinary)
    e_lfanew = cybox.TypedField("e_lfanew", HexBinary)
    hashes = cybox.TypedField("Hashes", HashList)
    #reserved1 = [] unsupported for now

class PEFileHeader(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEFileHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    machine = cybox.TypedField("Machine", HexBinary)
    number_of_sections = cybox.TypedField("Number_Of_Sections", NonNegativeInteger)
    time_date_stamp = cybox.TypedField("Time_Date_Stamp", HexBinary)
    pointer_to_symbol_table = cybox.TypedField("Pointer_To_Symbol_Table", HexBinary)
    number_of_symbols = cybox.TypedField("Number_Of_Symbols", NonNegativeInteger)
    size_of_optional_header = cybox.TypedField("Size_Of_Optional_Header", HexBinary)
    characteristics = cybox.TypedField("Characteristics", HexBinary)
    hashes = cybox.TypedField("Hashes", HashList)

class PEDataDirectoryStruct(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEDataDirectoryStructType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    virtual_address = cybox.TypedField("Virtual_Address", HexBinary)
    size = cybox.TypedField("Size", NonNegativeInteger)

class DataDirectory(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.DataDirectoryType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    export_table = cybox.TypedField("Export_Table", PEDataDirectoryStruct)
    import_table = cybox.TypedField("Import_Table", PEDataDirectoryStruct)
    resource_table = cybox.TypedField("Resource_Table", PEDataDirectoryStruct)
    exception_table = cybox.TypedField("Exception_Table", PEDataDirectoryStruct)
    certificate_table = cybox.TypedField("Certificate_Table", PEDataDirectoryStruct)
    base_relocation_table = cybox.TypedField("Base_Relocation_Table", PEDataDirectoryStruct)
    debug = cybox.TypedField("Debug", PEDataDirectoryStruct)
    architecture = cybox.TypedField("Architecture", PEDataDirectoryStruct)
    global_ptr = cybox.TypedField("Global_Ptr", PEDataDirectoryStruct)
    tls_table = cybox.TypedField("Tls_Table", PEDataDirectoryStruct)
    load_config_table = cybox.TypedField("Load_Config_Table", PEDataDirectoryStruct)
    bound_import = cybox.TypedField("Bound_Import", PEDataDirectoryStruct)
    import_address_table = cybox.TypedField("Import_Address_Table", PEDataDirectoryStruct)
    delay_import_descriptor = cybox.TypedField("Delay_Import_Descriptor", PEDataDirectoryStruct)
    clr_runtime_header = cybox.TypedField("CLR_Runtime_Header", PEDataDirectoryStruct)
    reserved = cybox.TypedField("Reserved", PEDataDirectoryStruct)

class PEOptionalHeader(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEOptionalHeaderType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    magic = cybox.TypedField("Magic", HexBinary)
    major_linker_version = cybox.TypedField("Major_Linker_Version", HexBinary)
    minor_linker_version = cybox.TypedField("Minor_Linker_Version", HexBinary)
    size_of_code = cybox.TypedField("Size_Of_Code", HexBinary)
    size_of_initialized_data = cybox.TypedField("Size_Of_Initialized_Data", HexBinary)
    size_of_uninitialized_data = cybox.TypedField("Size_Of_Uninitialized_Data", HexBinary)
    address_of_entry_point = cybox.TypedField("Address_Of_Entry_Point", HexBinary)
    base_of_code = cybox.TypedField("Base_Of_Code", HexBinary)
    base_of_data = cybox.TypedField("Base_Of_Data", HexBinary)
    image_base = cybox.TypedField("Image_Base", HexBinary)
    section_alignment = cybox.TypedField("Section_Alignment", HexBinary)
    file_alignment = cybox.TypedField("File_Alignment", HexBinary)
    major_os_version = cybox.TypedField("Major_OS_Version", HexBinary)
    minor_os_version = cybox.TypedField("Minor_OS_Version", HexBinary)
    major_image_version = cybox.TypedField("Major_Image_Version", HexBinary)
    minor_image_version = cybox.TypedField("Minor_Image_Version", HexBinary)
    major_subsystem_version = cybox.TypedField("Major_Subsystem_Version", HexBinary)
    minor_subsystem_version = cybox.TypedField("Minor_Subsystem_Version", HexBinary)
    win32_version_value = cybox.TypedField("Win32_Version_Value", HexBinary)
    size_of_image = cybox.TypedField("Size_Of_Image", HexBinary)
    size_of_headers = cybox.TypedField("Size_Of_Headers", HexBinary)
    checksum = cybox.TypedField("Checksum", HexBinary)
    subsystem = cybox.TypedField("Subsystem", HexBinary)
    dll_characteristics = cybox.TypedField("DLL_Characteristics", HexBinary)
    size_of_stack_reserve = cybox.TypedField("Size_Of_Stack_Reserve", HexBinary)
    size_of_stack_commit = cybox.TypedField("Size_Of_Stack_Commit", HexBinary)
    size_of_heap_reserve = cybox.TypedField("Size_Of_Heap_Reserve", HexBinary)
    size_of_heap_commit = cybox.TypedField("Size_Of_Heap_Commit", HexBinary)
    loader_flags = cybox.TypedField("Loader_Flags", HexBinary)
    number_of_rva_and_sizes = cybox.TypedField("Number_Of_Rva_And_Sizes", HexBinary)
    data_directory = cybox.TypedField("Data_Directory", DataDirectory)
    hashes = cybox.TypedField("Hashes", HashList)

class PEHeaders(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEHeadersType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    dos_header = cybox.TypedField("DOS_Header", DOSHeader)
    signature = cybox.TypedField("Signature", HexBinary)
    file_header = cybox.TypedField("File_Header", PEFileHeader)
    optional_header = cybox.TypedField("Optional_Header", PEOptionalHeader)
    entropy = cybox.TypedField("Entropy", Entropy)
    hashes = cybox.TypedField("Hashes", HashList)

class PEImportedFunction(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEImportedFunctionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    function_name = cybox.TypedField("Function_Name", String)
    hint = cybox.TypedField("Hint", HexBinary)
    ordinal = cybox.TypedField("Ordinal", NonNegativeInteger)
    bound = cybox.TypedField("Bound", HexBinary)
    virtual_address = cybox.TypedField("Virtual_Address", HexBinary)

class PEImportedFunctions(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEImportedFunctionsType
    _binding_var = "Imported_Function"
    _contained_type = PEImportedFunction
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

class PEImport(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEImportType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    delay_load = cybox.TypedField("delay_load")
    initially_visible = cybox.TypedField("initially_visible")
    file_name = cybox.TypedField("File_Name", String)
    imported_functions = cybox.TypedField("Imported_Functions", PEImportedFunctions)
    virtual_address = cybox.TypedField("Virtual_Address", HexBinary)

class PEImportList(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEImportListType
    _binding_var = "Import"
    _contained_type = PEImport
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

class PEChecksum(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEChecksumType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    pe_computed_api = cybox.TypedField("PE_Computed_API", Long)
    pe_file_api = cybox.TypedField("PE_File_API", Long)
    pe_file_raw = cybox.TypedField("PE_File_Raw", Long)

class PEResource(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEResourceType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    type_ = cybox.TypedField("Type", String)
    name = cybox.TypedField("Name", String)
    size = cybox.TypedField("Size", PositiveInteger)
    virtual_address = cybox.TypedField("Virtual_Address", HexBinary)
    language = cybox.TypedField("Language", String)
    sub_language = cybox.TypedField("Sub_Language", String)
    hashes = cybox.TypedField("Hashes", HashList)
    data = cybox.TypedField("Data", String)
    
class PEResourceList(cybox.EntityList):
    _binding_class = win_executable_file_binding.PEResourceListType
    _binding_var = "Resource"
    _contained_type = PEResource
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

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

class PESectionHeaderStruct(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PESectionHeaderStructType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    name = cybox.TypedField("Name", String)
    virtual_size = cybox.TypedField("Virtual_Size", HexBinary)
    virtual_address = cybox.TypedField("Virtual_Address", HexBinary)
    size_of_raw_data = cybox.TypedField("Size_Of_Raw_Data", HexBinary)
    pointer_to_raw_data = cybox.TypedField("Pointer_To_Raw_Data", HexBinary)
    pointer_to_relocations = cybox.TypedField("Pointer_To_Relocations", HexBinary)
    pointer_to_linenumbers = cybox.TypedField("Pointer_To_Linenumbers", HexBinary)
    number_of_relocations = cybox.TypedField("Number_Of_Relocations", NonNegativeInteger)
    number_of_linenumbers = cybox.TypedField("Number_Of_Linenumbers", NonNegativeInteger)
    characteristics = cybox.TypedField("Characteristics", HexBinary)

class PESection(cybox.Entity):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PESectionType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    section_header = cybox.TypedField("Section_Header", PESectionHeaderStruct)
    data_hashes = cybox.TypedField("Data_Hashes", HashList)
    entropy = cybox.TypedField("Entropy", Entropy)
    header_hashes = cybox.TypedField("Header_Hashes", HashList)

class PESectionList(cybox.EntityList):
    _binding_class = win_executable_file_binding.PESectionListType
    _binding_var = "Section"
    _contained_type = PESection
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

class PEVersionInfoResource(PEResource):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.PEVersionInfoResourceType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"

    comments = cybox.TypedField("Comments", String)
    companyname = cybox.TypedField("CompanyName", String)
    filedescription = cybox.TypedField("FileDescription", String)
    fileversion = cybox.TypedField("FileVersion", String)
    internalname = cybox.TypedField("InternalName", String)
    langid = cybox.TypedField("LangID", String)
    legalcopyright = cybox.TypedField("LegalCopyright", String)
    legaltrademarks = cybox.TypedField("LegalTrademarks", String)
    originalfilename = cybox.TypedField("OriginalFilename", String)
    privatebuild = cybox.TypedField("PrivateBuild", String)
    productname = cybox.TypedField("ProductName", String)
    productversion = cybox.TypedField("ProductVersion", String)
    specialbuild = cybox.TypedField("SpecialBuild", String)

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

class WinExecutableFile(WinFile):
    _binding = win_executable_file_binding
    _binding_class = win_executable_file_binding.WindowsExecutableFileObjectType
    _namespace = "http://cybox.mitre.org/objects#WinExecutableFileObject-2"
    _XSI_NS = "WinExecutableFileObj"
    _XSI_TYPE = "WindowsExecutableFileObjectType"

    build_information = cybox.TypedField("Build_Information", PEBuildInformation)
    digital_signature = cybox.TypedField("Digital_Signature", DigitalSignature)
    exports = cybox.TypedField("Exports", PEExports)
    extraneous_bytes = cybox.TypedField("Extraneous_Bytes", Integer)
    headers = cybox.TypedField("Headers", PEHeaders)
    imports = cybox.TypedField("Imports", PEImportList)
    pe_checksum = cybox.TypedField("PE_Checksum", PEChecksum)
    resources = cybox.TypedField("Resources", PEResourceList)
    sections = cybox.TypedField("Sections", PESectionList)
    type_ = cybox.TypedField("Type", String)


