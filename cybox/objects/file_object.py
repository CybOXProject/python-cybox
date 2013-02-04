import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.file_object_1_3 as file_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.common.hashlist import hashlist
from cybox.common.byterun import ByteRuns

class File(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, file_dict):
        """Create the File Object object representation from an input dictionary"""
        file_obj = file_binding.file_objectType()
        file_obj.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
        
        for key, value in file_dict.items():
            if key == 'is_packed' and utils.test_value(value):
                file_obj.set_is_packed(value.get('value'))
            if key == 'hashes':
                hashes_obj = hashlist.object_from_dict(value)
                if hashes_obj.hasContent_() : file_obj.set_Hashes(hashes_obj)
            elif key == 'packer_list':
                packer_list = file_binding.PackerListType()
                for packer in value:
                    packer_obj = cls.__packer_obj_from_dict(packer)
                    if packer_obj.hasContent_() : packer_list.add_Packer(packer_obj)
                if packer_list.hasContent_() : file_obj.set_Packer_List(packer_list)
            elif key == 'file_name' and utils.test_value(value):
                file_obj.set_File_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_path':
                filepath = baseobjectattribute.object_from_dict(file_binding.FilePathType(datatype='String'),value)
                if value.fully_qualified is not None:
                    filepath.set_fully_qualified(value.fully_qualified)
                file_obj.set_File_Path(filepath)
            elif key == 'device_path' and utils.test_value(value):
                file_obj.set_Device_Path(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'full_path' and utils.test_value(value):
                file_obj.set_Full_Path(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_extension' and utils.test_value(value):
                file_obj.set_File_Extension(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'size_in_bytes' and utils.test_value(value):
                file_obj.set_Size_In_Bytes(baseobjectattribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'magic_number' and utils.test_value(value):
                file_obj.set_Magic_Number(baseobjectattribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'file_format' and utils.test_value(value):
                file_obj.set_File_Format(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'created_time' and utils.test_value(value):
                file_obj.set_Creation_Time(baseobjectattribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'accessed_time' and utils.test_value(value):
                file_obj.set_Accessed_Time(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'modified_time' and utils.test_value(value):
                file_obj.set_Modified_Time(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'user_owner' and utils.test_value(value):
                file_obj.set_User_Owner(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'peak_entropy' and utils.test_value(value):
                file_obj.set_Peak_Entropy(baseobjectattribute.object_from_dict(common_types_binding.DoubleObjectAttributeType(datatype='Double'), value))
            elif key == 'sym_links':
                sym_links_obj = file_binding.SymLinksListType()
                for sym_link in value:
                    sym_link_obj = baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), sym_link)
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
            file_dict['hashes'] = hashlist.dict_from_object(file_obj.get_Hashes())
        if file_obj.get_Packer_List() is not None:
            packer_list = []
            for packer_obj in file_obj.get_Packer_List().get_Packer():
                packer_list.append(cls.__packer_dict_from_obj(packer_obj))
            file_dict['packer_list'] = packer_list
        if file_obj.get_File_Name() is not None:
            file_dict['filename'] = baseobjectattribute.dict_from_object(file_obj.get_File_Name())
        if file_obj.get_File_Path() is not None:
            path = file_obj.get_File_Path()
            file_dict['filepath'] = baseobjectattribute.dict_from_object(path)
            if path.get_fully_qualified() is not None:
                file_dict['filepath']['fully_qualified'] = path.get_fully_qualified()
        if file_obj.get_Device_Path() is not None:
            file_dict['device_path'] = baseobjectattribute.dict_from_object(file_obj.get_Device_Path())
        if file_obj.get_Full_Path() is not None:
            file_dict['full_path'] = baseobjectattribute.dict_from_object(file_obj.get_Full_Path())
        if file_obj.get_File_Extension() is not None:
            file_dict['file_extension'] = baseobjectattribute.dict_from_object(file_obj.get_File_Extension())
        if file_obj.get_Size_In_Bytes() is not None:
            file_dict['size_in_bytes'] = baseobjectattribute.dict_from_object(file_obj.get_Size_In_Bytes())
        if file_obj.get_Magic_Number() is not None:
            file_dict['magic_number'] = baseobjectattribute.dict_from_object(file_obj.get_Magic_Number())
        if file_obj.get_File_Format() is not None:
            file_dict['file_format'] = baseobjectattribute.dict_from_object(file_obj.get_File_Format())
        if file_obj.get_Created_Time() is not None:
            file_dict['created_time'] = baseobjectattribute.dict_from_object(file_obj.get_Created_Time())
        if file_obj.get_Accessed_Time() is not None:
            file_dict['accessed_time'] = baseobjectattribute.dict_from_object(file_obj.get_Accessed_Time())
        if file_obj.get_Modified_Time() is not None:
            file_dict['modified_time'] = baseobjectattribute.dict_from_object(file_obj.get_Modified_Time())
        if file_obj.get_User_Owner() is not None:
            file_dict['user_owner'] = baseobjectattribute.dict_from_object(file_obj.get_User_Owner())
        if file_obj.get_Sym_Links() is not None:
            sym_links_list = []
            for sym_link in file_obj.get_Sym_Links().get_Sym_Link():
                sym_links_list.append(baseobjectattribute.dict_from_object(sym_link))
            file_dict['sym_links'] = sym_links_list
        if file_obj.get_Byte_Runs() is not None: file_dict['byte_runs'] = ByteRuns.dict_from_object(file_obj.get_Byte_Runs())
        return file_dict

    @classmethod
    def __packer_obj_from_dict(cls, packer_dict):
        packer_obj = file_binding.PackerType()
        for key, value in packer_dict.items():
            if key == 'name' and utils.test_value(value):
                packer_obj.set_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'version' and utils.test_value(value):
                packer_obj.set_Version(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))            
            elif key == 'peid' and utils.test_value(value):
                packer_obj.set_PEiD(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'type' and utils.test_value(value):
                packer_obj.set_Type(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
        return packer_obj    

    @classmethod
    def __packer_dict_from_obj(cls, packer_obj):
        packer_dict = {}
        if packer_obj.get_Name() is not None: packer_dict['name'] = baseobjectattribute.dict_from_object(packer_obj.get_Name())
        if packer_obj.get_Version() is not None: packer_dict['version'] = baseobjectattribute.dict_from_object(packer_obj.get_Version())
        if packer_obj.get_PEiD() is not None: packer_dict['peid'] = baseobjectattribute.dict_from_object(packer_obj.get_PEiD())
        if packer_obj.get_Type() is not None: packer_dict['type'] = baseobjectattribute.dict_from_object(packer_obj.get_Type())
        return packer_dict

