import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_file_object_1_3 as win_file_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.hash import Hash
from cybox.objects.file_object import File

class Win_File(object):
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, win_file_dict, win_file_obj = None):
        """Create the Win File Object object representation from an input dictionary"""
        if win_file_obj == None:
            win_file_obj = File.object_from_dict(win_file_doct, win_file_binding.WindowsFileObjectType())
            win_file_obj.set_anyAttributes_({'xsi:type' : 'WinFileObj:WinFileObjectType'})
        
        for key, value in win_file_dict.items():
            if key == 'filename_accesssed_time' and utils.test_value(value): 
                win_file_obj.set_Filename_Accessed_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'filename_created_time' and utils.test_value(value): 
                win_file_obj.set_Filename_Created_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'filename_modified_time' and utils.test_value(value): 
                win_file_obj.set_Filename_Modified_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'drive' and utils.test_value(value): 
                win_file_obj.set_Drive(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'security_id' and utils.test_value(value): 
                win_file_obj.set_Security_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'security_type' and utils.test_value(value): 
                win_file_obj.set_Security_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'stream_list':
                stream_list_obj = win_file_binding.StreamListType()
                for stream_dict in value:
                    stream_obj = Stream.object_from_dict(stream_dict)
                    if stream_obj.hasContent_() : stream_list_obj.add_Stream(stream_obj)
                if stream_list_obj.hasContent_() : win_file_obj.set_Stream_List(stream_list_obj)

        return win_file_obj

    @classmethod
    def dict_from_object(cls, win_file_obj):
        """Parse and return a dictionary for a Win File Object object"""
        win_file_dict = File.dict_from_object(win_file_obj)
        if win_file_obj.get_Filename_Accessed_Time() is not None: win_file_dict['filename_accessed_time'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Filename_Accessed_Time())
        if win_file_obj.get_Filename_Created_Time() is not None: win_file_dict['filename_created_time'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Filename_Created_Time())
        if win_file_obj.get_Filename_Modified_Time() is not None: win_file_dict['filename_modified_time'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Filename_Modified_Time())
        if win_file_obj.get_Drive() is not None: win_file_dict['drive'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Drive())
        if win_file_obj.get_Security_ID() is not None: win_file_dict['security_id'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Security_ID())
        if win_file_obj.get_Security_Type() is not None: win_file_dict['security_type'] = Base_Object_Attribute.dict_from_object(win_file_obj.get_Security_Type())
        if win_file_obj.get_Stream_List() is not None:
            stream_list = [] 
            for stream_obj in win_file_obj.get_Stream_List().get_Stream():
                stream_list.append(Stream.dict_from_object(stream_obj))
            win_file_dict['stream_list'] = stream_list
        return win_file_dict

class Stream(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, stream_dict):
        """Create the Stream Object object representation from an input dictionary"""
        stream_obj = win_file_binding.StreamObjectType()
        for key, value in stream_dict:
            if key == 'Hashes' : 
                for Hash_dict in value:
                    Hash_obj = Hash.object_from_dict(Hash_dict)
                    if Hash_obj.hasContent_() : stream_obj.add_Hash(Hash_obj)
            elif key == 'name' and utils.test_value(value):
                stream_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'size_in_bytes' and utils.test_value(value):
                stream_obj.set_Size_In_Bytes(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'),value))       
        return stream_obj

    @classmethod
    def dict_from_object(cls, stream_obj):
        """Parse and return a dictionary for a Stream Object object"""
        stream_dict = {}
        if stream_obj.get_Hash() is not None:
            Hashes = []
            for Hash_obj in stream_obj.get_Hash():
                Hashes.append(Hash.dict_from_object(Hash_obj))
            stream_dict['Hashes'] = Hashes
        if stream_obj.get_Name() is not None: stream_dict['name'] = Base_Object_Attribute.dict_from_object(stream_obj.get_Name())
        if stream_obj.get_Size_In_Bytes() is not None: stream_dict['size_in_bytes'] = Base_Object_Attribute.dict_from_object(stream_obj.get_Size_In_Bytes())
        return stream_dict   