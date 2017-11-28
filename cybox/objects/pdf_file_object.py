# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.pdf_file_object as pdf_file_binding
from cybox.objects.file_object import File
from cybox.common import (DateTime, HashList, PositiveInteger, String,
                          NonNegativeInteger, Double, HexBinary, Integer)


def validate_pdf_object_type(instance, value):
    if value is None:
        return
    elif value in PDFIndirectObject.TYPES:
        return
    else:
        err = "Type must be one of %s. Received '%s'." % (PDFIndirectObject.TYPES, value)
        raise ValueError(err)


def validate_pdf_ref_entry_type(instance, value):
    if value is None:
        return
    elif value in PDFXrefEntry.TYPES:
        return
    else:
        err = "Type must be one of %s. Received '%s'." % (PDFXrefEntry.TYPES, value)
        raise ValueError(err)


def validate_id_string(instance, value):
    if value is None:
        return
    elif len(instance.id_string) >= 2:
        err = "ID_String only has a max occurrence of 2."
        raise ValueError(err)
    else:
        return


class PDFKeywordCount(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFKeywordCountType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    non_obfuscated_count = fields.TypedField("Non_Obfuscated_Count", NonNegativeInteger)
    obfuscated_count = fields.TypedField("Obfuscated_Count", NonNegativeInteger)


class PDFKeywordCounts(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFKeywordCountsType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    page_count = fields.TypedField("Page_Count", PDFKeywordCount)
    encrypt_count = fields.TypedField("Encrypt_Count", PDFKeywordCount)
    objstm_count = fields.TypedField("ObjStm_Count", PDFKeywordCount)
    js_count = fields.TypedField("JS_Count", PDFKeywordCount)
    javascript_count = fields.TypedField("JavaScript_Count", PDFKeywordCount)
    aa_count = fields.TypedField("AA_Count", PDFKeywordCount)
    openaction_count = fields.TypedField("OpenAction_Count", PDFKeywordCount)
    asciihexdecode_count = fields.TypedField("ASCIIHexDecode_Count", PDFKeywordCount)
    ascii85decode_count = fields.TypedField("ASCII85Decode_Count", PDFKeywordCount)
    lzwdecode_count = fields.TypedField("LZWDecode_Count", PDFKeywordCount)
    flatedecode_count = fields.TypedField("FlateDecode_Count", PDFKeywordCount)
    runlengthdecode_count = fields.TypedField("RunLengthDecode_Count", PDFKeywordCount)
    jbig2decode_count = fields.TypedField("JBIG2Decode_Count", PDFKeywordCount)
    dctdecode_count = fields.TypedField("DCTDecode_Count", PDFKeywordCount)
    richmedia_count = fields.TypedField("RichMedia_Count", PDFKeywordCount)
    ccittfaxdecode_count = fields.TypedField("CCITTFaxDecode_Count", PDFKeywordCount)
    launch_count = fields.TypedField("Launch_Count", PDFKeywordCount)
    xfa_count = fields.TypedField("XFA_Count", PDFKeywordCount)


class PDFDocumentInformationDictionary(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFDocumentInformationDictionaryType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    title = fields.TypedField("Title", String)
    author = fields.TypedField("Author", String)
    subject = fields.TypedField("Subject", String)
    keywords = fields.TypedField("Keywords", String)
    creator = fields.TypedField("Creator", String)
    producer = fields.TypedField("Producer", String)
    creationdate = fields.TypedField("CreationDate", DateTime)
    moddate = fields.TypedField("ModDate", DateTime)
    trapped = fields.TypedField("Trapped", String)


class PDFFileMetadata(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileMetadataType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    encrypted = fields.TypedField("encrypted")
    optimized = fields.TypedField("optimized")
    document_information_dictionary = fields.TypedField("Document_Information_Dictionary", PDFDocumentInformationDictionary)
    number_of_indirect_objects = fields.TypedField("Number_Of_Indirect_Objects", PositiveInteger)
    number_of_trailers = fields.TypedField("Number_Of_Trailers", PositiveInteger)
    number_of_cross_reference_tables = fields.TypedField("Number_Of_Cross_Reference_Tables", PositiveInteger)
    keyword_counts = fields.TypedField("Keyword_Counts", PDFKeywordCounts)


class PDFFileID(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileIDType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    id_string = fields.TypedField("ID_String", String, multiple=True, preset_hook=validate_id_string)


class PDFIndirectObjectID(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFIndirectObjectIDType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    object_number = fields.TypedField("Object_Number", PositiveInteger)
    generation_number = fields.TypedField("Generation_Number", NonNegativeInteger)


class PDFDictionary(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFDictionaryType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    # TODO: xs:choice
    object_reference = fields.TypedField("Object_Reference", PDFIndirectObjectID)
    raw_contents = fields.TypedField("Raw_Contents", String)


class PDFStream(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFStreamType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    raw_stream = fields.TypedField("Raw_Stream", String)
    raw_stream_hashes = fields.TypedField("Raw_Stream_Hashes", HashList)
    decoded_stream = fields.TypedField("Decoded_Stream", HexBinary)
    decoded_stream_hashes = fields.TypedField("Decoded_Stream_Hashes", HashList)


class PDFIndirectObjectContents(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFIndirectObjectContentsType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    non_stream_contents = fields.TypedField("Non_Stream_Contents", String)
    stream_contents = fields.TypedField("Stream_Contents", PDFStream)


class PDFIndirectObject(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFIndirectObjectType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    TYPE_BOOLEAN = "Boolean"
    TYPE_INTEGER = "Integer"
    TYPE_STRING = "String"
    TYPE_NAME = "Name"
    TYPE_ARRAY = "Array"
    TYPE_DICTIONARY = "Dictionary"
    TYPE_STREAM = "Stream"
    TYPE_NULL = "Null"
    TYPES = (TYPE_BOOLEAN, TYPE_INTEGER, TYPE_STRING, TYPE_NAME, TYPE_ARRAY,
             TYPE_DICTIONARY, TYPE_STREAM, TYPE_NULL)

    type_ = fields.TypedField("type_", key_name="type", preset_hook=validate_pdf_object_type)
    id_ = fields.TypedField("ID", PDFIndirectObjectID)
    contents = fields.TypedField("Contents", PDFIndirectObjectContents)
    offset = fields.TypedField("Offset", PositiveInteger)
    hashes = fields.TypedField("Hashes", HashList)


class PDFIndirectObjectList(entities.EntityList):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFIndirectObjectListType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    indirect_object = fields.TypedField("Indirect_Object", PDFIndirectObject, multiple=True)


class PDFTrailer(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFTrailerType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    size = fields.TypedField("Size", PositiveInteger)
    prev = fields.TypedField("Prev", PositiveInteger)
    root = fields.TypedField("Root", PDFIndirectObjectID)
    encrypt = fields.TypedField("Encrypt", PDFDictionary)
    info = fields.TypedField("Info", PDFIndirectObjectID)
    id_ = fields.TypedField("ID", PDFFileID)
    last_cross_reference_offset = fields.TypedField("Last_Cross_Reference_Offset", PositiveInteger)
    offset = fields.TypedField("Offset", PositiveInteger)
    hashes = fields.TypedField("Hashes", HashList)


class PDFTrailerList(entities.EntityList):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFTrailerListType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    trailer = fields.TypedField("Trailer", PDFTrailer, multiple=True)


class PDFXrefEntry(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXrefEntryType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    TYPE_USE = "In-Use"
    TYPE_FREE = "Free"
    TYPES = (TYPE_USE, TYPE_FREE)

    type_ = fields.TypedField("type_", key_name="type", preset_hook=validate_pdf_ref_entry_type)
    # TODO: Byte_Offset and Object_Number xs:choice
    byte_offset = fields.TypedField("Byte_Offset", Integer)
    object_number = fields.TypedField("Object_Number", NonNegativeInteger)
    generation_number = fields.TypedField("Generation_Number", NonNegativeInteger)


class PDFXrefEntryList(entities.EntityList):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXrefEntryListType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    cross_reference_entry = fields.TypedField("Cross_Reference_Entry", PDFXrefEntry, multiple=True)


class PDFXrefTableSubsection(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXrefTableSubsectionType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    first_object_number = fields.TypedField("First_Object_Number", NonNegativeInteger)
    number_of_objects = fields.TypedField("Number_Of_Objects", NonNegativeInteger)
    cross_reference_entries = fields.TypedField("Cross_Reference_Entries", PDFXrefEntryList)


class PDFXrefTableSubsectionList(entities.EntityList):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXrefTableSubsectionListType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    subsection = fields.TypedField("Subsection", PDFXrefTableSubsection, multiple=True)


class PDFXRefTable(entities.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXRefTableType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    subsections = fields.TypedField("Subsections", PDFXrefTableSubsectionList)
    offset = fields.TypedField("Offset", PositiveInteger)
    hashes = fields.TypedField("Hashes", HashList)


class PDFXRefTableList(entities.EntityList):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFXRefTableListType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    cross_reference_table = fields.TypedField("Cross_Reference_Table", PDFXRefTable, multiple=True)


class PDFFile(File):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'
    _XSI_NS = "PDFFileObj"
    _XSI_TYPE = "PDFFileObjectType"

    metadata = fields.TypedField("Metadata", PDFFileMetadata)
    version = fields.TypedField("Version", Double)
    indirect_objects = fields.TypedField("Indirect_Objects", PDFIndirectObjectList)
    cross_reference_tables = fields.TypedField("Cross_Reference_Tables", PDFXRefTableList)
    trailers = fields.TypedField("Trailers", PDFTrailerList)
