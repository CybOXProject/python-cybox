# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import base64
import bz2
import zlib

from mixbox import fields

import cybox
import cybox.bindings.archive_file_object as archive_binding
from cybox.common import ObjectProperties, String, Integer
from cybox.objects.file_object import File


class ArchiveFile(File):
    _binding = archive_binding
    _namespace = 'http://cybox.mitre.org/objects#ArchiveFileObject-1'
    _XSI_NS = "ArchiveFileObj"
    _XSI_TYPE = "ArchiveFileObjectType"

    archive_format = fields.TypedField("Archive_Format", String)
    version = fields.TypedField("Version", String)
    file_count = fields.TypedField("File_Count", Integer)
    encryption_algorithm = fields.TypedField("Encryption_Algorithm", String) # TODO: Cipher may need its own class
    decryption_key = fields.TypedField("Decryption_Key", String)
    comment = fields.TypedField("Comment", String)
    archived_file = fields.TypedField("Archived_File", File, multiple=True)
