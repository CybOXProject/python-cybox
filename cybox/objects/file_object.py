import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.file_object_1_3 as file_binding

class file_object(object):
    def __init__(self):
        pass
        
    @classmethod
    def create_from_dict(cls, file_attributes):
        fileobj = file_binding.FileObjectType()
        fileobj.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
        fs_hashes = cybox_common.HashListType()
        
        for key, value in file_attributes.items():
            if key == 'md5' and common_methods.test_value(value):
                hash_value = common_methods.create_element_from_dict(cybox_common.HexBinaryObjectAttributeType(datatype='hexBinary'), value)
                hash_type = cybox_common.HashNameType(datatype='String', valueOf_='MD5')
                hash = cybox_common.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash)
            elif key == 'sha1' and common_methods.test_value(value):
                hash_value = common_methods.create_element_from_dict(cybox_common.HexBinaryObjectAttributeType(datatype='hexBinary'), value)
                hash_type = cybox_common.HashNameType(datatype='String', valueOf_='SHA1')
                hash_obj = cybox_common.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash_obj)
            elif key == 'packer' and common_methods.test_value(value):
                packer_list = file_binding.PackerListType()
                packer = file_binding.PackerType(Name=common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
                packer_list.add_Packer(packer)
                fileobj.set_Packer_List(packer_list)
            elif key == 'file_name' and common_methods.test_value(value):
                fileobj.set_File_Name(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_path':
                filepath = common_methods.create_element_from_dict(file_binding.FilePathType(datatype='String'),value)
                if value.fully_qualified is not None:
                    filepath.set_fully_qualified(value.fully_qualified)
                fileobj.set_File_Path(filepath)
            elif key == 'device_path' and common_methods.test_value(value):
                fileobj.set_Device_Path(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'full_path' and common_methods.test_value(value):
                fileobj.set_Full_Path(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'file_extension' and common_methods.test_value(value):
                fileobj.set_File_Extension(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'size_in_bytes' and common_methods.test_value(value):
                fileobj.set_Size_In_Bytes(common_methods.create_element_from_dict(cybox_common.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'magic_number' and common_methods.test_value(value):
                fileobj.set_Magic_Number(common_methods.create_element_from_dict(cybox_common.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'file_format' and common_methods.test_value(value):
                fileobj.set_File_Format(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'created_time' and common_methods.test_value(value):
                fileobj.set_Creation_Time(common_methods.create_element_from_dict(cybox_common.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'accessed_time' and common_methods.test_value(value):
                fileobj.set_Accessed_Time(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'modified_time' and common_methods.test_value(value):
                fileobj.set_Modified_Time(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'user_owner' and common_methods.test_value(value):
                fileobj.set_User_Owner(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            elif key == 'peak_entropy' and common_methods.test_value(value):
                fileobj.set_Peak_Entropy(common_methods.create_element_from_dict(cybox_common.DoubleObjectAttributeType(datatype='Double'), value))

        if fs_hashes.hasContent_():
            fileobj.set_Hashes(fs_hashes)

        return fileobj
    
    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
            
        for hashval in defined_object.get_Hashes():
            if(hashval.get_Type().valueOf_ == 'MD5'):
                defined_object_dict['md5'] = common_methods.parse_element_into_dict(hashval.get_Simple_Hash_Value())
            elif(hashval.get_Type().valueOf_ == 'SHA1'):
                defined_object_dict['sha1'] = common_methods.parse_element_into_dict(hashval.get_Simple_Hash_Value())
        
        packer = defined_object.get_Packer_List.get_Packer()
        if packer is not None and packer.length > 0:
            defined_object_dict['packer'] = packer[0]
        
        if defined_object.get_File_Name() is not None:
            defined_object_dict['filename'] = common_methods.parse_element_into_dict(defined_object.get_File_Name())
        if defined_object.get_File_Path() is not None:
            path = defined_object.get_File_Path()
            defined_object_dict['filepath'] = common_methods.parse_element_into_dict(path)
            if path.get_fully_qualified() is not None:
                defined_object_dict['filepath']['fully_qualified'] = path.get_fully_qualified()
        if defined_object.get_Device_Path() is not None:
            defined_object_dict['device_path'] = common_methods.parse_element_into_dict(defined_object.get_Device_Path())
        if defined_object.get_Full_Path() is not None:
            defined_object_dict['full_path'] = common_methods.parse_element_into_dict(defined_object.get_Full_Path())
        if defined_object.get_File_Extension() is not None:
            defined_object_dict['file_extension'] = common_methods.parse_element_into_dict(defined_object.get_File_Extension())
        if defined_object.get_Size_In_Bytes() is not None:
            defined_object_dict['size_in_bytes'] = common_methods.parse_element_into_dict(defined_object.get_Size_In_Bytes())
        if defined_object.get_Magic_Number() is not None:
            defined_object_dict['magic_number'] = common_methods.parse_element_into_dict(defined_object.get_Magic_Number())
        if defined_object.get_File_Format() is not None:
            defined_object_dict['file_format'] = common_methods.parse_element_into_dict(defined_object.get_File_Format())
        if defined_object.get_Created_Time() is not None:
            defined_object_dict['created_time'] = common_methods.parse_element_into_dict(defined_object.get_Created_Time())
        if defined_object.get_Accessed_Time() is not None:
            defined_object_dict['accessed_time'] = common_methods.parse_element_into_dict(defined_object.get_Accessed_Time())
        if defined_object.get_Modified_Time() is not None:
            defined_object_dict['modified_time'] = common_methods.parse_element_into_dict(defined_object.get_Modified_Time())
        if defined_object.get_User_Owner() is not None:
            defined_object_dict['user_owner'] = common_methods.parse_element_into_dict(defined_object.get_User_Owner())
            
        return defined_object_dict