# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.archive_file_object as archive_binding
from cybox.common import BaseProperty, Integer, String
from cybox.common.cipher import Cipher
from cybox.objects.file_object import File


class ArchiveFileFormat(BaseProperty):
    _binding = archive_binding
    _binding_class = archive_binding.ArchiveFileFormatType
    _namespace = 'http://cybox.mitre.org/objects#ArchiveFileObject-1'

    TERM_7ZIP = "7-ZIP"
    TERM_APK = "APK"
    TERM_CAB = "CAB"
    TERM_DMG = "DMG"
    TERM_JAR = "JAR"
    TERM_RAR = "RAR"
    TERM_SIT = "SIT"
    TERM_TGZ = "TGZ"
    TERM_ZIP = "ZIP"


class ArchiveFile(File):
    _binding = archive_binding
    _binding_class = archive_binding.ArchiveFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#ArchiveFileObject-1'
    _XSI_NS = "ArchiveFileObj"
    _XSI_TYPE = "ArchiveFileObjectType"

    archive_format = fields.TypedField("Archive_Format", ArchiveFileFormat)
    version = fields.TypedField("Version", String)
    file_count = fields.TypedField("File_Count", Integer)
    encryption_algorithm = fields.TypedField("Encryption_Algorithm", Cipher)
    decryption_key = fields.TypedField("Decryption_Key", String)
    comment = fields.TypedField("Comment", String)
    archived_file = fields.TypedField("Archived_File", File, multiple=True)
