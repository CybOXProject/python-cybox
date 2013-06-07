# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.file_object as file_binding
from cybox.common.extracted_features import ExtractedFeatures
from cybox.common import (DateTime, HashList, HexBinary, ObjectProperties,
        String, UnsignedLong)
#from cybox.common.byterun import ByteRuns
#from cybox.common.digitalsignature import Digital_Signature_List

import cybox.utils as utils


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

    def __init__(self):
        super(File, self).__init__()

        self.is_packed = None
        self.hashes = None
        self.extracted_features = None

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

    def to_obj(self, object_type=None):
        if not object_type:
            file_obj = file_binding.FileObjectType()
        else:
            file_obj = object_type
        super(File, self).to_obj(file_obj)

        if self.is_packed is not None:
            file_obj.set_is_packed(self.is_packed)
        if self.file_name is not None:
            file_obj.set_File_Name(self.file_name.to_obj())
        if self.file_path is not None:
            file_obj.set_File_Path(self.file_path.to_obj())
        if self.device_path is not None:
            file_obj.set_Device_Path(self.device_path.to_obj())
        if self.full_path is not None:
            file_obj.set_Full_Path(self.full_path.to_obj())
        if self.file_extension is not None:
            file_obj.set_File_Extension(self.file_extension.to_obj())
        if self.size_in_bytes is not None:
            file_obj.set_Size_In_Bytes(self.size_in_bytes.to_obj())
        if self.magic_number is not None:
            file_obj.set_Magic_Number(self.magic_number.to_obj())
        if self.file_format is not None:
            file_obj.set_File_Format(self.file_format.to_obj())
        if self.hashes:
            file_obj.set_Hashes(self.hashes.to_obj())
        if self.extracted_features is not None:
            file_obj.set_Extracted_Features(self.extracted_features.to_obj())
        if self.modified_time is not None:
            file_obj.set_Modified_Time(self.modified_time.to_obj())
        if self.accessed_time is not None:
            file_obj.set_Accessed_Time(self.accessed_time.to_obj())
        if self.created_time is not None:
            file_obj.set_Created_Time(self.created_time.to_obj())

        return file_obj

    def to_dict(self):
        file_dict = {}
        super(File, self).to_dict(file_dict)

        if self.is_packed is not None:
            file_dict['is_packed'] = self.is_packed
        if self.file_name is not None:
            file_dict['file_name'] = self.file_name.to_dict()
        if self.file_path is not None:
            file_dict['file_path'] = self.file_path.to_dict()
        if self.device_path is not None:
            file_dict['device_path'] = self.device_path.to_dict()
        if self.full_path is not None:
            file_dict['full_path'] = self.full_path.to_dict()
        if self.file_extension is not None:
            file_dict['file_extension'] = self.file_extension.to_dict()
        if self.size_in_bytes is not None:
            file_dict['size_in_bytes'] = self.size_in_bytes.to_dict()
        if self.magic_number is not None:
            file_dict['magic_number'] = self.magic_number.to_dict()
        if self.file_format is not None:
            file_dict['file_format'] = self.file_format.to_dict()
        if self.hashes:
            file_dict['hashes'] = self.hashes.to_list()
        if self.extracted_features is not None:
            file_dict['extracted_features'] = self.extracted_features.to_dict()
        if self.modified_time is not None:
            file_dict['modified_time'] = self.modified_time.to_dict()
        if self.accessed_time is not None:
            file_dict['accessed_time'] = self.accessed_time.to_dict()
        if self.created_time is not None:
            file_dict['created_time'] = self.created_time.to_dict()

        return file_dict

    @staticmethod
    def from_obj(file_obj, file_class=None):
        if not file_obj:
            return None
        if not file_class:
            file_ = File()
        else:
            file_ = file_class
        ObjectProperties.from_obj(file_obj, file_)

        file_.is_packed = file_obj.get_is_packed()
        file_.file_name = String.from_obj(file_obj.get_File_Name())
        file_.file_path = FilePath.from_obj(file_obj.get_File_Path())
        file_.device_path = String.from_obj(file_obj.get_Device_Path())
        file_.full_path = String.from_obj(file_obj.get_Full_Path())
        file_.file_extension = String.from_obj(file_obj.get_File_Extension())
        file_.size_in_bytes = UnsignedLong.from_obj(file_obj.get_Size_In_Bytes())
        file_.magic_number = HexBinary.from_obj(file_obj.get_Magic_Number())
        file_.file_format = String.from_obj(file_obj.get_File_Format())
        file_.hashes = HashList.from_obj(file_obj.get_Hashes())
        file_.extracted_features = ExtractedFeatures.from_obj(file_obj.get_Extracted_Features())
        #TODO: why are there two Strings and one DateTime here?
        file_.modified_time = String.from_obj(file_obj.get_Modified_Time())
        file_.accessed_time = String.from_obj(file_obj.get_Accessed_Time())
        file_.created_time = DateTime.from_obj(file_obj.get_Created_Time())

        return file_

    @staticmethod
    def from_dict(file_dict, file_class=None):
        if not file_dict:
            return None
        if not file_class:
            file_ = File()
        else:
            file_ = file_class
        ObjectProperties.from_dict(file_dict, file_)

        file_.is_packed = file_dict.get('is_packed')
        file_.file_name = String.from_dict(file_dict.get('file_name'))
        file_.file_path = FilePath.from_dict(file_dict.get('file_path'))
        file_.device_path = String.from_dict(file_dict.get('device_path'))
        file_.full_path = String.from_dict(file_dict.get('full_path'))
        file_.file_extension = String.from_dict(file_dict.get('file_extension'))
        file_.size_in_bytes = UnsignedLong.from_dict(file_dict.get('size_in_bytes'))
        file_.magic_number = HexBinary.from_dict(file_dict.get('magic_number'))
        file_.file_format = String.from_dict(file_dict.get('file_format'))
        file_.hashes = HashList.from_list(file_dict.get('hashes'))
        file_.extracted_features = ExtractedFeatures.from_dict(file_dict.get('extracted_features'))
        file_.modified_time = String.from_dict(file_dict.get('modified_time'))
        file_.accessed_time = String.from_dict(file_dict.get('accessed_time'))
        file_.created_time = DateTime.from_dict(file_dict.get('created_time'))

        return file_

#    @classmethod
#    def object_from_dict(cls, file_dict):
#        """Create the File Object object representation from an input dictionary"""
#        if file_obj == None:
#            file_obj = file_binding.FileObjectType()
#            file_obj.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
#
#        for key, value in file_dict.items():
#            if key == 'is_packed' and utils.test_value(value):
#                file_obj.set_is_packed(value.get('value'))
#            elif key == 'hashes':
#                hashes_obj = HashList.object_from_dict(value)
#                if hashes_obj.hasContent_() : file_obj.set_Hashes(hashes_obj)
#            elif key == 'digital_signatures':
#                digital_signatures_obj = Digital_Signature_List.object_from_list(value)
#                if digital_signatures_obj.hasContent_() : file_obj.set_Digital_Signatures(digital_signatures_obj)
#            elif key == 'packer_list':
#                 packer_list_obj = Packer_List.object_from_list(value)
#                 if packer_list_obj.hasContent_() : file_obj.set_Packer_List(packer_list_obj)
#            elif key == 'file_name' and utils.test_value(value):
#                file_obj.set_File_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'file_path':
#                filepath = Base_Object_Attribute.object_from_dict(file_binding.FilePathType(datatype='String'),value)
#                if value.get('fully_qualified') is not None:
#                    filepath.set_fully_qualified(value.get('fully_qualified'))
#                file_obj.set_File_Path(filepath)
#            elif key == 'device_path' and utils.test_value(value):
#                file_obj.set_Device_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'full_path' and utils.test_value(value):
#                file_obj.set_Full_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'file_extension' and utils.test_value(value):
#                file_obj.set_File_Extension(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'size_in_bytes' and utils.test_value(value):
#                file_obj.set_Size_In_Bytes(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
#            elif key == 'magic_number' and utils.test_value(value):
#                file_obj.set_Magic_Number(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
#            elif key == 'file_format' and utils.test_value(value):
#                file_obj.set_File_Format(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'created_time' and utils.test_value(value):
#                file_obj.set_Creation_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
#            elif key == 'accessed_time' and utils.test_value(value):
#                file_obj.set_Accessed_Time(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'modified_time' and utils.test_value(value):
#                file_obj.set_Modified_Time(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'user_owner' and utils.test_value(value):
#                file_obj.set_User_Owner(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
#            elif key == 'peak_entropy' and utils.test_value(value):
#                file_obj.set_Peak_Entropy(Base_Object_Attribute.object_from_dict(common_types_binding.DoubleObjectAttributeType(datatype='Double'), value))
#            elif key == 'sym_links':
#                sym_links_obj = file_binding.SymLinksListType()
#                for sym_link in value:
#                    sym_link_obj = Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), sym_link)
#                    sym_links_obj.add_Sym_Link(sym_link_obj)
#                if sym_links_obj.hasContent_() : file_obj.set_Sym_Links(sym_links_obj)
#            elif key == 'byte_runs':
#                byte_runs_obj = ByteRuns.object_from_dict(value)
#                if byte_runs_obj.hasContent_() : file_obj.set_Byte_Runs(byte_runs_obj)
#        return file_obj

#    @classmethod
#    def dict_from_object(cls, file_obj):
#        """Parse and return a dictionary for a File Object object"""
#        file_dict = {}
#        if file_obj.get_is_packed() is not None: file_dict['is_packed'] = {'value' : file_obj.get_is_packed()}
#        if file_obj.get_Hashes() is not None:
#            file_dict['hashes'] = HashList.dict_from_object(file_obj.get_Hashes())
#        if file_obj.get_Digital_Signatures() is not None:
#            file_dict['digital_signatures'] = Digital_Signature_List.list_from_object(file_obj.get_Digital_Signatures())
#        if file_obj.get_Packer_List() is not None: file_dict['packer_list'] = Packer_List.list_from_object(file_obj.get_Packer_List())
#        if file_obj.get_File_Name() is not None:
#            file_dict['filename'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Name())
#        if file_obj.get_File_Path() is not None:
#            path = file_obj.get_File_Path()
#            file_dict['filepath'] = Base_Object_Attribute.dict_from_object(path)
#            if path.get_fully_qualified() is not None:
#                file_dict['filepath']['fully_qualified'] = path.get_fully_qualified()
#        if file_obj.get_Device_Path() is not None:
#            file_dict['device_path'] = Base_Object_Attribute.dict_from_object(file_obj.get_Device_Path())
#        if file_obj.get_Full_Path() is not None:
#            file_dict['full_path'] = Base_Object_Attribute.dict_from_object(file_obj.get_Full_Path())
#        if file_obj.get_File_Extension() is not None:
#            file_dict['file_extension'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Extension())
#        if file_obj.get_Size_In_Bytes() is not None:
#            file_dict['size_in_bytes'] = Base_Object_Attribute.dict_from_object(file_obj.get_Size_In_Bytes())
#        if file_obj.get_Magic_Number() is not None:
#            file_dict['magic_number'] = Base_Object_Attribute.dict_from_object(file_obj.get_Magic_Number())
#        if file_obj.get_File_Format() is not None:
#            file_dict['file_format'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Format())
#        if file_obj.get_Created_Time() is not None:
#            file_dict['created_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Created_Time())
#        if file_obj.get_Accessed_Time() is not None:
#            file_dict['accessed_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Accessed_Time())
#        if file_obj.get_Modified_Time() is not None:
#            file_dict['modified_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Modified_Time())
#        if file_obj.get_User_Owner() is not None:
#            file_dict['user_owner'] = Base_Object_Attribute.dict_from_object(file_obj.get_User_Owner())
#        if file_obj.get_Sym_Links() is not None:
#            sym_links_list = []
#            for sym_link in file_obj.get_Sym_Links().get_Sym_Link():
#                sym_links_list.append(Base_Object_Attribute.dict_from_object(sym_link))
#            file_dict['sym_links'] = sym_links_list
#        if file_obj.get_Byte_Runs() is not None: file_dict['byte_runs'] = ByteRuns.dict_from_object(file_obj.get_Byte_Runs())
#        return file_dict


class Packer(cybox.Entity):
    _binding = file_binding
    _namespace = 'http://cybox.mitre.org/objects#FileObject-2'

    name = cybox.TypedField("Name", String)
    version = cybox.TypedField("Version", String)
    entry_point = cybox.TypedField("Entry_Point", HexBinary)
    signature = cybox.TypedField("Signature", String)
    type_ = cybox.TypedField("Type", String)
    #TODO: add Detected_Entrypoint_Signatures and EP_Jump_Codes

    def to_obj(self):
        packer_obj = file_binding.PackerType()

        if self.name is not None:
            packer_obj.set_Name(self.name.to_obj())
        if self.version is not None:
            packer_obj.set_Version(self.version.to_obj())
        if self.entry_point is not None:
            packer_obj.set_Entry_Point(self.entry_point.to_obj())
        if self.signature is not None:
            packer_obj.set_Signature(self.signature.to_obj())
        if self.type_ is not None:
            packer_obj.set_Type(self.type_.to_obj())

        return packer_obj

    def to_dict(self):
        packer_dict = {}

        if self.name is not None:
            packer_dict['name'] = self.name.to_dict()
        if self.version is not None:
            packer_dict['version'] = self.version.to_dict()
        if self.entry_point is not None:
            packer_dict['entry_point'] = self.entry_point.to_dict()
        if self.signature is not None:
            packer_dict['signature'] = self.signature.to_dict()
        if self.type_ is not None:
            packer_dict['type'] = self.type_.to_dict()

        return packer_dict

    @staticmethod
    def from_dict(packer_dict):
        if not packer_dict:
            return None

        packer = Packer()

        packer.name = String.from_dict(packer_dict.get('name'))
        packer.version = String.from_dict(packer_dict.get('version'))
        packer.entry_point = HexBinary.from_dict(packer_dict.get('entry_point'))
        packer.signature = String.from_dict(packer_dict.get('signature'))
        packer.type_ = String.from_dict(packer_dict.get('type'))

        return packer

    @staticmethod
    def from_obj(packer_obj):
        if not packer_obj:
            return None

        packer = Packer()

        packer.name = String.from_obj(packer_obj.get_Name())
        packer.version = String.from_obj(packer_obj.get_Version())
        packer.entry_point = HexBinary.from_obj(packer_obj.get_Entry_Point())
        packer.signature = String.from_obj(packer_obj.get_Signature())
        packer.type_ = String.from_obj(packer_obj.get_Type())

        return packer


class PackerList(cybox.EntityList):
    _binding_class = file_binding.PackerListType
    _contained_type = Packer

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Packer(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Packer()
