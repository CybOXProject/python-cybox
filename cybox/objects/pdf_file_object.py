# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.pdf_file_object as pdf_file_binding
from cybox.objects.file_object import File
from cybox.common import DateTime, PositiveInteger, String, NonNegativeInteger, Double

class PDFKeywordCount(cybox.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFKeywordCountType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    non_obfuscated_count = cybox.TypedField("Non_Obfuscated_Count", NonNegativeInteger)
    obfuscated_count = cybox.TypedField("Obfuscated_Count", NonNegativeInteger)

class PDFKeywordCounts(cybox.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFKeywordCountsType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    page_count = cybox.TypedField("Page_Count", PDFKeywordCount)
    encrypt_count = cybox.TypedField("Encrypt_Count", PDFKeywordCount)
    objstm_count = cybox.TypedField("ObjStm_Count", PDFKeywordCount)
    js_count = cybox.TypedField("JS_Count", PDFKeywordCount)
    javascript_count = cybox.TypedField("JavaScript_Count", PDFKeywordCount)
    aa_count = cybox.TypedField("AA_Count", PDFKeywordCount)
    openaction_count = cybox.TypedField("OpenAction_Count", PDFKeywordCount)
    asciihexdecode_count = cybox.TypedField("ASCIIHexDecode_Count", PDFKeywordCount)
    ascii85decode_count = cybox.TypedField("ASCII85Decode_Count", PDFKeywordCount)
    lzwdecode_count = cybox.TypedField("LZWDecode_Count", PDFKeywordCount)
    flatedecode_count = cybox.TypedField("FlateDecode_Count", PDFKeywordCount)
    runlengthdecode_count = cybox.TypedField("RunLengthDecode_Count", PDFKeywordCount)
    jbig2decode_count = cybox.TypedField("JBIG2Decode_Count", PDFKeywordCount)
    dctdecode_count = cybox.TypedField("DCTDecode_Count", PDFKeywordCount)
    richmedia_count = cybox.TypedField("RichMedia_Count", PDFKeywordCount)
    ccittfaxdecode_count = cybox.TypedField("CCITTFaxDecode_Count", PDFKeywordCount)
    launch_count = cybox.TypedField("Launch_Count", PDFKeywordCount)
    xfa_count = cybox.TypedField("XFA_Count", PDFKeywordCount)

class PDFDocumentInformationDictionary(cybox.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFDocumentInformationDictionaryType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    title = cybox.TypedField("Title", String)
    author = cybox.TypedField("Author", String)
    subject = cybox.TypedField("Subject", String)
    keywords = cybox.TypedField("Keywords", String)
    creator = cybox.TypedField("Creator", String)
    producer = cybox.TypedField("Producer", String)
    creationdate = cybox.TypedField("CreationDate", DateTime)
    moddate = cybox.TypedField("ModDate", DateTime)
    trapped = cybox.TypedField("Trapped", String)

class PDFFileMetadata(cybox.Entity):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileMetadataType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'

    encrypted = cybox.TypedField("encrypted")
    optimized = cybox.TypedField("optimized")
    document_information_dictionary = cybox.TypedField("Document_Information_Dictionary", PDFDocumentInformationDictionary)
    number_of_indirect_objects = cybox.TypedField("Number_Of_Indirect_Objects", PositiveInteger)
    number_of_trailers = cybox.TypedField("Number_Of_Trailers", PositiveInteger)
    number_of_cross_reference_tables = cybox.TypedField("Number_Of_Cross_Reference_Tables", PositiveInteger)
    keyword_counts = cybox.TypedField("Keyword_Counts", PDFKeywordCounts)

class PDFFile(File):
    _binding = pdf_file_binding
    _binding_class = pdf_file_binding.PDFFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#PDFFileObject-1'
    _XSI_NS = "PDFFileObj"
    _XSI_TYPE = "PDFFileObjectType"

    metadata = cybox.TypedField("Metadata", PDFFileMetadata)
    version = cybox.TypedField("Version", Double)
    #TODO: implement remaining elements
    #indirect_objects = cybox.TypedField("Indirect_Objects", PDFIndirectObjectList)
    #cross_reference_tables = cybox.TypedField("Cross_Reference_Tables", PDFXrefTableList)
    #trailers = cybox.TypedField("Trailers", PDFTrailerList)