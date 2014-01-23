# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_file_object as win_file_binding
from cybox.objects.file_object import File
from cybox.common import ObjectProperties, Hash, HashList, String, UnsignedLong, HexBinary, DateTime

class Stream(HashList):
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'
    name = cybox.TypedField("Name", String)
    size_in_bytes = cybox.TypedField("Size_In_Bytes", UnsignedLong)

class StreamList(cybox.EntityList):
    _binding_class = win_file_binding.StreamListType
    _binding_var = "Stream"
    _contained_type = Stream
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'

class WinFile(File):
    _binding = win_file_binding
    _binding_class = win_file_binding.WindowsFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'
    _XSI_NS = "WinFileObj"
    _XSI_TYPE = "WindowsFileObjectType"

    filename_accessed_time = cybox.TypedField("Filename_Accessed_Time", DateTime)
    filename_created_time = cybox.TypedField("Filename_Created_Time", DateTime)
    filename_modified_time = cybox.TypedField("Filename_Modified_Time", DateTime)
    drive = cybox.TypedField("Drive", String)
    security_id = cybox.TypedField("Security_ID", String)
    security_type = cybox.TypedField("Security_Type", String)
    stream_list = cybox.TypedField("Stream_List", StreamList)


