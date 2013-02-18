import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.file_object_1_3 as file_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.hashlist import Hash_List
from cybox.common.byterun import ByteRuns
from cybox.common.digitalsignature import Digital_Signature_List

class File(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, file_dict, file_obj = None):
        """Create the File Object object representation from an input dictionary"""
        if file_obj == None:
            file_obj = file_binding.FileObjectType()
            file_obj.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
        
        for key, value in file_dict.items():
            if key == 'is_packed' and utils.test_value(value):
                file_obj.set_is_packed(value.get('value'))
            elif key == 'hashes':
                hashes_obj = Hash_List.object_from_dict(value)
                if hashes_obj.hasContent_() : file_obj.set_Hashes(hashes_obj)
            elif key == 'digital_signatures':
                digital_signatures_obj = Digital_Signature_List.object_from_list(value)
                if digital_signatures_obj.hasContent_() : file_obj.set_Digital_Signatures(digital_signatures_obj)
            elif key == 'packer_list':
                 packer_list_obj = Packer_List.object_from_list(value)
                 if packer_list_obj.hasContent_() : file_obj.set_Packer_List(packer_list_obj)
            elif key == 'file_name' and utils.test_value(value):
                file_obj.set_File_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_path':
                filepath = Base_Object_Attribute.object_from_dict(file_binding.FilePathType(datatype='String'),value)
                if value.fully_qualified is not None:
                    filepath.set_fully_qualified(value.fully_qualified)
                file_obj.set_File_Path(filepath)
            elif key == 'device_path' and utils.test_value(value):
                file_obj.set_Device_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'full_path' and utils.test_value(value):
                file_obj.set_Full_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_extension' and utils.test_value(value):
                file_obj.set_File_Extension(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'size_in_bytes' and utils.test_value(value):
                file_obj.set_Size_In_Bytes(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'magic_number' and utils.test_value(value):
                file_obj.set_Magic_Number(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'file_format' and utils.test_value(value):
                file_obj.set_File_Format(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'created_time' and utils.test_value(value):
                file_obj.set_Creation_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'accessed_time' and utils.test_value(value):
                file_obj.set_Accessed_Time(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'modified_time' and utils.test_value(value):
                file_obj.set_Modified_Time(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'user_owner' and utils.test_value(value):
                file_obj.set_User_Owner(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'peak_entropy' and utils.test_value(value):
                file_obj.set_Peak_Entropy(Base_Object_Attribute.object_from_dict(common_types_binding.DoubleObjectAttributeType(datatype='Double'), value))
            elif key == 'sym_links':
                sym_links_obj = file_binding.SymLinksListType()
                for sym_link in value:
                    sym_link_obj = Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), sym_link)
                    sym_links_obj.add_Sym_Link(sym_link_obj)
                if sym_links_obj.hasContent_() : file_obj.set_Sym_Links(sym_links_obj)
            elif key == 'byte_runs':
                byte_runs_obj = ByteRuns.object_from_dict(value)
                if byte_runs_obj.hasContent_() : file_obj.set_Byte_Runs(byte_runs_obj)
        return file_obj
    
    @classmethod
    def dict_from_object(cls, file_obj):
        """Parse and return a dictionary for a File Object object"""
        file_dict = {}  
        if file_obj.get_is_packed() is not None: file_dict['is_packed'] = {'value' : file_obj.get_is_packed()}
        if file_obj.get_Hashes() is not None:
            file_dict['hashes'] = Hash_List.dict_from_object(file_obj.get_Hashes())
        if file_obj.get_Digital_Signatures() is not None:
            file_dict['digital_signatures'] = Digital_Signature_List.list_from_object(file_obj.get_Digital_Signatures())
        if file_obj.get_Packer_List() is not None: file_dict['packer_list'] = Packer_List.list_from_object(file_obj.get_Packer_List())
        if file_obj.get_File_Name() is not None:
            file_dict['filename'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Name())
        if file_obj.get_File_Path() is not None:
            path = file_obj.get_File_Path()
            file_dict['filepath'] = Base_Object_Attribute.dict_from_object(path)
            if path.get_fully_qualified() is not None:
                file_dict['filepath']['fully_qualified'] = path.get_fully_qualified()
        if file_obj.get_Device_Path() is not None:
            file_dict['device_path'] = Base_Object_Attribute.dict_from_object(file_obj.get_Device_Path())
        if file_obj.get_Full_Path() is not None:
            file_dict['full_path'] = Base_Object_Attribute.dict_from_object(file_obj.get_Full_Path())
        if file_obj.get_File_Extension() is not None:
            file_dict['file_extension'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Extension())
        if file_obj.get_Size_In_Bytes() is not None:
            file_dict['size_in_bytes'] = Base_Object_Attribute.dict_from_object(file_obj.get_Size_In_Bytes())
        if file_obj.get_Magic_Number() is not None:
            file_dict['magic_number'] = Base_Object_Attribute.dict_from_object(file_obj.get_Magic_Number())
        if file_obj.get_File_Format() is not None:
            file_dict['file_format'] = Base_Object_Attribute.dict_from_object(file_obj.get_File_Format())
        if file_obj.get_Created_Time() is not None:
            file_dict['created_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Created_Time())
        if file_obj.get_Accessed_Time() is not None:
            file_dict['accessed_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Accessed_Time())
        if file_obj.get_Modified_Time() is not None:
            file_dict['modified_time'] = Base_Object_Attribute.dict_from_object(file_obj.get_Modified_Time())
        if file_obj.get_User_Owner() is not None:
            file_dict['user_owner'] = Base_Object_Attribute.dict_from_object(file_obj.get_User_Owner())
        if file_obj.get_Sym_Links() is not None:
            sym_links_list = []
            for sym_link in file_obj.get_Sym_Links().get_Sym_Link():
                sym_links_list.append(Base_Object_Attribute.dict_from_object(sym_link))
            file_dict['sym_links'] = sym_links_list
        if file_obj.get_Byte_Runs() is not None: file_dict['byte_runs'] = ByteRuns.dict_from_object(file_obj.get_Byte_Runs())
        return file_dict

class Packer(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, packer_dict):
        """Create the Packer object representation from an input dictionary"""
        packer_obj = file_binding.PackerType()
        for key, value in packer_dict.items():
            if key == 'name' and utils.test_value(value):
                packer_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'version' and utils.test_value(value):
                packer_obj.set_Version(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))            
            elif key == 'peid' and utils.test_value(value):
                packer_obj.set_PEiD(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'type' and utils.test_value(value):
                packer_obj.set_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
        return packer_obj    

    @classmethod
    def dict_from_object(cls, packer_obj):
        """Parse and return a dictionary for a Packer object"""
        packer_dict = {}
        if packer_obj.get_Name() is not None: packer_dict['name'] = Base_Object_Attribute.dict_from_object(packer_obj.get_Name())
        if packer_obj.get_Version() is not None: packer_dict['version'] = Base_Object_Attribute.dict_from_object(packer_obj.get_Version())
        if packer_obj.get_PEiD() is not None: packer_dict['peid'] = Base_Object_Attribute.dict_from_object(packer_obj.get_PEiD())
        if packer_obj.get_Type() is not None: packer_dict['type'] = Base_Object_Attribute.dict_from_object(packer_obj.get_Type())
        return packer_dict

class Packer_List(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, packer_list):
        """Create the Packer List object representation from an input dictionary"""
        packer_list_obj = file_binding.PackerListType()
        for packer_dict in packer_list:
            packer_obj = Packer.object_from_dict(packer_dict)
            if packer_obj.hasContent_() : packer_list_obj.add_Packer(packer_obj)
        return packer_list_obj

    @classmethod
    def list_from_object(cls, packer_list_obj):
        """Parse and return a list of Packer dictionaries for a Packer List object"""
        packer_list = []
        for packer_obj in packer_list_obj.get_Packer():
            packer_list.append(Packer.dict_from_object(packer_obj))
        return packer_list