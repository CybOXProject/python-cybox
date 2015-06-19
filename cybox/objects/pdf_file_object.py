# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.pdf_file_object as pdf_file_binding
from cybox.objects.file_object import File
from cybox.common import DateTime, PositiveInteger, String, NonNegativeInteger, Double


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


class PDFFile(File):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'
    _XSI_NS = "PDFFileObj"
    _XSI_TYPE = "PDFFileObjectType"

    metadata = fields.TypedField("Metadata", PDFFileMetadata)
    version = fields.TypedField("Version", Double)
    #TODO: implement remaining elements
    #indirect_objects = fields.TypedField("Indirect_Objects", PDFIndirectObjectList)
    #cross_reference_tables = fields.TypedField("Cross_Reference_Tables", PDFXrefTableList)
    #trailers = fields.TypedField("Trailers", PDFTrailerList)
