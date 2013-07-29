# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.file_object as file_binding
from cybox.common.extracted_features import ExtractedFeatures
from cybox.common import (DateTime, HashList, HexBinary, ObjectProperties,
        String, UnsignedLong)

class FilePath(String):
    _binding = file_binding
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    def __init__(self, *args, **kwargs):
        String.__init__(self, *args, **kwargs)
        self.fully_qualified = None

    def _get_binding_class(self):
        return file_binding.FilePathType

    def is_plain(self):
        return (super(FilePath, self).is_plain() and
                self.fully_qualified is None)

    def to_obj(self):
        filepath_obj = String.to_obj(self)
        if self.fully_qualified is not None:
            filepath_obj.set_fully_qualified(self.fully_qualified)
        return filepath_obj

    def to_dict(self):
        filepath_dict = String.to_dict(self)
        if self.fully_qualified is not None:
            filepath_dict['fully_qualified'] = self.fully_qualified
        return filepath_dict

    @staticmethod
    def from_obj(filepath_obj):
        if not filepath_obj:
            return None
        filepath = FilePath()
        filepath._populate_from_obj(filepath_obj)
        filepath.fully_qualified = filepath_obj.get_fully_qualified()
        return filepath

    @staticmethod
    def from_dict(filepath_dict):
        if not filepath_dict:
            return None
        filepath = FilePath()
        # TODO: properly handle plain (non-dict) value
        filepath._populate_from_dict(filepath_dict)
        filepath.fully_qualified = filepath_dict.get('fully_qualified')
        return filepath


class File(ObjectProperties):
    _binding = file_binding
    _binding_class = file_binding.FileObjectType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'
    _XSI_NS = "FileObj"
    _XSI_TYPE = "FileObjectType"

    file_name = cybox.TypedField("File_Name", String)
    file_path = cybox.TypedField("File_Path", FilePath)
    device_path = cybox.TypedField("Device_Path", String)
    full_path = cybox.TypedField("Full_Path", String)
    file_extension = cybox.TypedField("File_Extension", String)
    size_in_bytes = cybox.TypedField("Size_In_Bytes", UnsignedLong)
    magic_number = cybox.TypedField("Magic_Number", HexBinary)
    file_format = cybox.TypedField("File_Format", String)
    modified_time = cybox.TypedField("Modified_Time", String)
    accessed_time = cybox.TypedField("Accessed_Time", String)
    created_time = cybox.TypedField("Created_Time", DateTime)
    hashes = cybox.TypedField("Hashes", HashList)
    extracted_features = cybox.TypedField("Extracted_Features", ExtractedFeatures)

    # Not supported yet:
    # - Digital_Signatures
    # - File_Attributes_List
    # - Permissions
    # - User_Owner
    # - Packer_List
    # - Peak_Entropy
    # - Sym_Links
    # - Extracted_Features
    # - Byte Runs

    def __init__(self):
        super(File, self).__init__()
        self.is_packed = None

    @property
    def hashes(self):
        if self._hashes is None:
            self._hashes = HashList()
        return self._hashes

    @hashes.setter
    def hashes(self, value):
        self._hashes = value

    @property
    def md5(self):
        return self.hashes.md5

    @md5.setter
    def md5(self, value):
        self.hashes.md5 = value

    @property
    def sha1(self):
        return self.hashes.sha1

    @sha1.setter
    def sha1(self, value):
        self.hashes.sha1 = value

    @property
    def sha256(self):
        return self.hashes.sha256

    @sha256.setter
    def sha256(self, value):
        self.hashes.sha256 = value

    @property
    def size(self):
        """`size` is an alias for `size_in_bytes`"""
        return self.size_in_bytes

    @size.setter
    def size(self, value):
        """`size` is an alias for `size_in_bytes`"""
        self.size_in_bytes = value

    def add_hash(self, hash_):
        if hash_ is not None:
            self.hashes.append(hash_)

class Packer(cybox.Entity):
    _binding = file_binding
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    name = cybox.TypedField("Name", String)
    version = cybox.TypedField("Version", String)
    entry_point = cybox.TypedField("Entry_Point", HexBinary)
    signature = cybox.TypedField("Signature", String)
    type_ = cybox.TypedField("Type", String)
    #TODO: add Detected_Entrypoint_Signatures and EP_Jump_Codes

class PackerList(cybox.EntityList):
    _binding_class = file_binding.PackerListType
    _binding_var = "Packer"
    _contained_type = Packer
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'
