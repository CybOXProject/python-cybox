# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_file_object as win_file_binding
from cybox.objects.file_object import File
from cybox.common import ObjectProperties, Hash, HashList, String, UnsignedLong, HexBinary, DateTime

class WinFile(File):
    _XSI_NS = "WinFileObj"
    _XSI_TYPE = "WindowsFileObjectType"

    def __init__(self):
        super(File, self).__init__()
        self.filename_accessed_time = None
        self.filename_created_time = None
        self.filename_modified_time = None
        self.drive = None
        self.security_id = None
        self.security_type = None
        self.stream_list = None

    def to_obj(self, object_type = None):
        if not object_type:
            object_type = win_file_binding.WindowsFileObjectType()
        win_file_obj = super(WinFile, self).to_obj(object_type)

        if self.filename_accessed_time is not None : win_file_obj.set_Filename_Accessed_Time(self.filename_accessed_time.to_obj())
        if self.filename_created_time is not None : win_file_obj.set_Filename_Created_Time(self.filename_created_time.to_obj())
        if self.filename_modified_time is not None : win_file_obj.set_Filename_Modified_Time(self.filename_modified_time.to_obj())
        if self.drive is not None : win_file_obj.set_Drive(self.drive.to_obj())
        if self.security_id is not None : win_file_obj.set_Security_ID(self.security_id.to_obj())
        if self.security_type is not None : win_file_obj.set_Security_Type(self.security_type.to_obj())
        if self.stream_list is not None : win_file_obj.set_Stream_List(self.stream_list.to_obj())
        return win_file_obj

    def to_dict(self):
        win_file_dict = super(WinFile, self).to_dict()
        if self.filename_accessed_time is not None : win_file_dict['filename_accessed_time'] = self.filename_accessed_time.to_dict()
        if self.filename_created_time is not None : win_file_dict['filename_created_time'] = self.filename_created_time.to_dict()
        if self.filename_modified_time is not None : win_file_dict['filename_modified_time'] = self.filename_modified_time.to_dict()
        if self.drive is not None : win_file_dict['drive'] = self.drive.to_dict()
        if self.security_id is not None : win_file_dict['security_id'] = self.security_id.to_dict()
        if self.security_type is not None : win_file_dict['security_type'] = self.security_type.to_dict()
        if self.stream_list is not None : win_file_dict['stream_list'] = self.stream_list.to_list()
        return win_file_dict

    @staticmethod
    def from_obj(win_file_obj, file_class = None):
        if not win_file_obj:
            return None
        if not file_class:
            win_file_ = File.from_obj(win_file_obj, WinFile())
        else:
            win_file_ = File.from_obj(win_file_obj, file_class)
        win_file_.filename_accessed_time = DateTime.from_obj(win_file_obj.get_Filename_Accessed_Time())
        win_file_.filename_created_time = DateTime.from_obj(win_file_obj.get_Filename_Created_Time())
        win_file_.filename_modified_time = DateTime.from_obj(win_file_obj.get_Filename_Modified_Time())
        win_file_.drive = String.from_obj(win_file_obj.get_Drive())
        win_file_.security_id = String.from_obj(win_file_obj.get_Security_ID())
        win_file_.security_type = String.from_obj(win_file_obj.get_Security_Type())
        win_file_.stream_list = StreamList.from_obj(win_file_obj.get_Stream_List())
        return win_file_

    @staticmethod
    def from_dict(win_file_dict, file_class = None):
        if not win_file_dict:
            return None
        if not file_class:
            win_file_ = File.from_dict(win_file_dict, WinFile())
        else:
            win_file_ = File.from_dict(win_file_dict, file_class)
        win_file_.filename_accessed_time = DateTime.from_dict(win_file_dict.get('filename_accessed_time'))
        win_file_.filename_created_time = DateTime.from_dict(win_file_dict.get('filename_created_time'))
        win_file_.filename_modified_time = DateTime.from_dict(win_file_dict.get('filename_modified_time'))
        win_file_.drive = String.from_dict(win_file_dict.get('drive'))
        win_file_.security_id = String.from_dict(win_file_dict.get('security_id'))
        win_file_.security_type = String.from_dict(win_file_dict.get('security_type'))
        win_file_.stream_list = StreamList.from_list(win_file_dict.get('stream_list'))
        return win_file_

class Stream(HashList):
    def __init__(self):
        super(Stream, self).__init__()
        self.name = None
        self.size_in_bytes = None

    def to_obj(self):
        stream_obj = super(Stream, self).to_obj(win_file_binding.StreamObjectType())
        if self.name is not None : stream_obj.set_Name(self.name.to_obj())
        if self.size_in_bytes is not None : stream_obj.set_Size_In_Bytes(self.size_in_bytes.to_obj())
        return stream_obj

    def to_dict(self):
        stream_dict = {}
        hash_list = super(Stream, self).to_list()
        if self.name is not None : stream_dict['name'] = self.name.to_dict()
        if self.size_in_bytes is not None : stream_dict['size_in_bytes'] = self.size_in_bytes.to_dict()
        if len(hash_list) > 0 : stream_dict['hashes'] = hash_list
        return stream_dict
    
    @staticmethod
    def from_dict(stream_dict):
        if not stream_dict:
            return None
        stream_ = Stream()
        for hash_ in stream_dict.get('hashes',[]):
            stream_.add(Hash.from_dict(hash_))
        stream_.name = String.from_dict(stream_dict.get('name'))
        stream_.size_in_bytes = UnsignedLong.from_dict(stream_dict.get('size_in_bytes'))
        return stream_

    @staticmethod
    def from_obj(stream_obj):
        if not stream_obj:
            return None
        stream_ = Stream()
        for hash_ in stream_obj.get_Hash():
            stream_.add(Hash.from_obj(hash_))
        stream_.name = String.from_obj(stream_dict.get('name'))
        stream_.size_in_bytes = UnsignedLong.from_obj(stream_dict.get('size_in_bytes'))
        return stream_

class StreamList(cybox.EntityList):
    _contained_type = Stream
    _binding_class = win_file_binding.StreamListType

    def __init__(self):
        super(StreamList, self).__init__()
       
    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Stream(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Stream()





