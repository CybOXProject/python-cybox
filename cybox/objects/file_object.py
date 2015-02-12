# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.file_object as file_binding
from cybox.common import (ByteRuns, DateTime, DigitalSignatureList, Double,
        ExtractedFeatures, HashList, HexBinary, ObjectProperties, String,
        UnsignedLong, Integer)


class FilePath(String):
    _binding = file_binding
    _binding_class = file_binding.FilePathType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    def __init__(self, *args, **kwargs):
        String.__init__(self, *args, **kwargs)
        self.fully_qualified = None

    def is_plain(self):
        return (super(FilePath, self).is_plain() and
                self.fully_qualified is None)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        filepath_obj = String.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        if self.fully_qualified is not None:
            filepath_obj.fully_qualified = self.fully_qualified
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
        filepath.fully_qualified = filepath_obj.fully_qualified
        return filepath

    @staticmethod
    def from_dict(filepath_dict):
        if not filepath_dict:
            return None
        filepath = FilePath()
        filepath._populate_from_dict(filepath_dict)
        if isinstance(filepath_dict, dict):
            filepath.fully_qualified = filepath_dict.get('fully_qualified')
        return filepath

class EPJumpCode(cybox.Entity):
    _binding = file_binding
    _binding_class = file_binding.EPJumpCodeType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    depth = cybox.TypedField("Depth", Integer)
    opcodes = cybox.TypedField("Opcodes", String)
    
class EntryPointSignature(cybox.Entity):
    _binding = file_binding
    _binding_class = file_binding.EntryPointSignatureType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'
    
    name = cybox.TypedField("Name", String)
    type_ = cybox.TypedField("Type", String)
    
class EntryPointSignatureList(cybox.EntityList):
    _binding = file_binding
    _binding_class = file_binding.EntryPointSignatureListType
    _binding_var = "Entry_Point_Signature"
    _contained_type = EntryPointSignature
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

class Packer(cybox.Entity):
    _binding = file_binding
    _binding_class = file_binding.PackerType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    name = cybox.TypedField("Name", String)
    version = cybox.TypedField("Version", String)
    entry_point = cybox.TypedField("Entry_Point", HexBinary)
    signature = cybox.TypedField("Signature", String)
    type_ = cybox.TypedField("Type", String)
    detected_entrypoint_signatures = cybox.TypedField("Detected_Entrypoint_Signatures", EntryPointSignatureList)
    ep_jump_codes = cybox.TypedField("EP_Jump_Codes", EPJumpCode)


class PackerList(cybox.EntityList):
    _binding = file_binding
    _binding_class = file_binding.PackerListType
    _binding_var = "Packer"
    _contained_type = Packer
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'


class SymLinksList(cybox.EntityList):
    _binding = file_binding
    _binding_class = file_binding.SymLinksListType
    _binding_var = "Sym_Link"
    _contained_type = String
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'


class FileAttribute(cybox.Entity):
    """An abstract class for file attributes."""


class FilePermissions(cybox.Entity):
    """An abstract class for file permissions."""


class File(ObjectProperties):
    _binding = file_binding
    _binding_class = file_binding.FileObjectType
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'
    _XSI_NS = "FileObj"
    _XSI_TYPE = "FileObjectType"

    is_packed = cybox.TypedField("is_packed")
    is_masqueraded = cybox.TypedField("is_masqueraded")
    file_name = cybox.TypedField("File_Name", String)
    file_path = cybox.TypedField("File_Path", FilePath)
    device_path = cybox.TypedField("Device_Path", String)
    full_path = cybox.TypedField("Full_Path", String)
    file_extension = cybox.TypedField("File_Extension", String)
    size_in_bytes = cybox.TypedField("Size_In_Bytes", UnsignedLong)
    magic_number = cybox.TypedField("Magic_Number", HexBinary)
    file_format = cybox.TypedField("File_Format", String)
    hashes = cybox.TypedField("Hashes", HashList)
    digital_signatures = cybox.TypedField("Digital_Signatures",
                                          DigitalSignatureList)
    modified_time = cybox.TypedField("Modified_Time", DateTime)
    accessed_time = cybox.TypedField("Accessed_Time", DateTime)
    created_time = cybox.TypedField("Created_Time", DateTime)
    # Subclasses must redefine these, since the abstract types
    # cannot be instantiated.
    file_attributes_list = cybox.TypedField("File_Attributes_List",
                                            FileAttribute)  # abstract
    permissions = cybox.TypedField("Permissions", FilePermissions) # abstract
    user_owner = cybox.TypedField("User_Owner", String)
    packer_list = cybox.TypedField("Packer_List", PackerList)
    peak_entropy = cybox.TypedField("Peak_Entropy", Double)
    sym_links = cybox.TypedField("Sym_Links", SymLinksList)
    byte_runs = cybox.TypedField("Byte_Runs", ByteRuns)
    extracted_features = cybox.TypedField("Extracted_Features",
                                          ExtractedFeatures)
    encryption_algorithm = cybox.TypedField("Encryption_Algorithm", String)
    decryption_key = cybox.TypedField("Decryption_Key", String)
    compression_method = cybox.TypedField("Compression_Method", String)
    compression_version = cybox.TypedField("Compression_Version", String)
    compression_comment = cybox.TypedField("Compression_Comment", String)

    def __init__(self):
        super(File, self).__init__()
        self.is_packed = None

    @property
    def md5(self):
        if self.hashes is None:
            return None
        return self.hashes.md5

    @md5.setter
    def md5(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.md5 = value

    @property
    def sha1(self):
        if self.hashes is None:
            return None
        return self.hashes.sha1

    @sha1.setter
    def sha1(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.sha1 = value

    @property
    def sha224(self):
        if self.hashes is None:
            return None
        return self.hashes.sha224

    @sha224.setter
    def sha224(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.sha224 = value

    @property
    def sha256(self):
        if self.hashes is None:
            return None
        return self.hashes.sha256

    @sha256.setter
    def sha256(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.sha256 = value

    @property
    def sha384(self):
        if self.hashes is None:
            return None
        return self.hashes.sha384

    @sha384.setter
    def sha384(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.sha384 = value

    @property
    def sha512(self):
        if self.hashes is None:
            return None
        return self.hashes.sha512

    @sha512.setter
    def sha512(self, value):
        if self.hashes is None:
            self.hashes = HashList()
        self.hashes.sha512 = value

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
            if self.hashes is None:
                self.hashes = HashList()
            self.hashes.append(hash_)


