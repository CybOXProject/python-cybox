import cybox
import cybox.bindings.file_object_1_3 as file_binding
from cybox.common import DefinedObject, HashList, String, UnsignedLong, HexBinary
#from cybox.common.byterun import ByteRuns
#from cybox.common.digitalsignature import Digital_Signature_List

import cybox.utils as utils


class FilePath(String):
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
        filepath._populate_from_dict(filepath_dict)
        filepath.fully_qualified = filepath_dict.get('fully_qualified')
        return filepath


class File(DefinedObject):
    _XSI_TYPE = "FileObjectType"

    def __init__(self):
        super(File, self).__init__()
        self.is_packed = None
        self.file_name = None
        self.file_path = None
        self.device_path = None
        self.full_path = None
        self.file_extension = None
        self.size_in_bytes = None
        self.magic_number = None
        self.file_format = None
        self.hashes = None

        # Not supported yet:
        # - Digital_Signatures
        # - Modified_Time
        # - Accessed_Time
        # - Created_Time
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
    def md5(self,value):
        self.hashes.md5 = value

    @property
    def sha1(self):
        return self.hashes.sha1

    @sha1.setter
    def sha1(self,value):
        self.hashes.sha1 = value

    @property
    def sha256(self):
        return self.hashes.sha256

    @sha256.setter
    def sha256(self,value):
        self.hashes.sha256 = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._file_name = value

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if value is not None and not isinstance(value, FilePath):
            value = FilePath(value)
        self._file_path = value

    def add_hash(self, hash_):
        self.hashes.add(hash_)

    def to_obj(self):
        file_obj = file_binding.FileObjectType()
        file_obj.set_anyAttributes_({'xsi:type': 'FileObj:FileObjectType'})

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

        return file_obj

    def to_dict(self):
        file_dict = {}
        super(File, self)._populate_dict(file_dict)

        if self.is_packed is not None:
            file_dict['is_packed'] = self.is_packed,
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
            file_dict['hashes'] = self.hashes.to_dict()

        return file_dict

    @staticmethod
    def from_obj(file_obj):
        if not file_obj:
            return None

        file_ = File()

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

        return file_

    @staticmethod
    def from_dict(file_dict):
        if not file_dict:
            return None

        file_ = File()

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
    def __init__(self):
        self.name = None
        self.version = None
        self.peid = None
        self.type = None

    def to_obj(self):
        packer_obj = file_binding.PackerType()
        if self.name is not None: packer_obj.set_Name(self.name.to_obj())
        if self.version is not None: packer_obj.set_Version(self.version.to_obj())
        if self.peid is not None: packer_obj.set_PEiD(self.peid.to_obj())
        if self.type is not None: packer_obj.set_Type(self.type.to_obj())
        return packer_obj

    def to_dict(self):
        packer_dict = {}
        if self.name is not None: packer_dict['name'] = self.name.to_dict()
        if self.version is not None: packer_dict['version'] = self.version.to_dict()
        if self.peid is not None: packer_dict['peid'] = self.peid.to_dict()
        if self.type is not None: packer_dict['type'] = self.type.to_dict()
        return packer_dict

    @staticmethod
    def from_dict(packer_dict):
        if not packer_dict:
            return packer_dict
        packer_ = Packer()
        packer_.name = String.from_dict(packer_dict.get('name'))
        packer_.version = String.from_dict(packer_dict.get('version'))
        packer_.peid = String.from_dict(packer_dict.get('peid'))
        packer_.type = String.from_dict(packer_dict.get('type'))
        return packer_

    @staticmethod
    def from_obj(packer_obj):
        if not packer_obj:
            return packer_obj
        packer_ = Packer()
        packer_.name = String.from_obj(packer_obj.get_Name())
        packer_.version = String.from_obj(packer_obj.get_Version())
        packer_.peid = String.from_obj(packer_obj.get_PEiD())
        packer_.type = String.from_obj(packer_obj.get_Type())
        return packer_

class PackerList(cybox.Entity):
    def __init__(self):
        self.packer_list = []

    def add_packer(self, packer):
        self.packer_list.append(packer)

    def to_obj(self):
        packer_list_obj = file_binding.PackerListType()
        for packer in self.packer_list:
            packer_list_obj.add_Packer(packer.to_obj())
        return packer_list_obj 

    def to_list(self):
        packer_list = [x.to_dict() for x in self.packer_list]
        return packer_list

    @staticmethod
    def from_list(packer_list):
        if not packer_list:
            return None
        packer_list_ = PackerList()
        packer_list_.packer_list = [Packer.from_dict(x) for x in packer_list]
        return packer_list_

    @staticmethod
    def from_obj(packer_list_obj):
        if not packer_list_obj:
            return None
        packer_list_ = PackerList()
        packer_list_.packer_list = [Packer.from_obj(x) for x in packer_list_obj.get_Packer()]
        return packer_list_