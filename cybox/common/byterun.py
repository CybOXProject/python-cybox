import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common import HashList

class ByteRun(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, byterun_dict):
        """Create the ByteRun object representation from an input dictionary"""
        byterun_obj = common_types_binding.ByteRunType()
        for key, value in byterun_dict.items():
            if key == 'offset' :
                byterun_obj.set_Offset(Base_Object_Attribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'),value))
            elif key == 'file_system_offset' :
                byterun_obj.set_File_System_Offset(Base_Object_Attribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'),value))
            elif key == 'image_offset' :
                byterun_obj.set_Image_Offset(Base_Object_Attribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'),value))
            elif key == 'length' :
                byterun_obj.set_Offset(Base_Object_Attribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'),value))
            elif key == 'hashes' :
                byterun_obj.set_Hashes(HashList.object_from_dict(value))
            elif key == 'byte_run_data':
                byterun_obj.set_Byte_Run_Data(value)
        return byterun_obj

    @classmethod
    def dict_from_object(cls, byterun_obj):
        """Parse and return a dictionary for a ByteRun object"""
        byterun_dict = {}
        if byterun_obj.get_Offset() is not None: byterun_dict['offset'] = Base_Object_Attribute.dict_from_object(byterun_obj.get_Offset())
        if byterun_obj.get_File_System_Offset() is not None: byterun_dict['file_system_offset'] = Base_Object_Attribute.dict_from_object(byterun_obj.get_File_System_Offset())  
        if byterun_obj.get_Image_Offset() is not None: byterun_dict['image_offset'] = Base_Object_Attribute.dict_from_object(byterun_obj.get_Image_Offset())
        if byterun_obj.get_Length() is not None: byterun_dict['length'] = Base_Object_Attribute.dict_from_object(byterun_obj.get_Length())
        if byterun_obj.get_Hashes() is not None: byterun_dict['hashes'] = HashList.dict_from_object(byterun_obj.get_Hashes())
        if byterun_obj.get_Byte_Run_Data() is not None: byterun_dict['byte_run_data'] = {'value' : byterun_obj.get_Byte_Run_Data()}
        return byterun_dict

class ByteRuns(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, byteruns_list):
        """Create the ByteRuns object representation from an input list of ByteRun dictionaries"""
        byteruns_obj = common_types_binding.ByteRunsType()
        for byterun_dict in byteruns_list():
            byterun_obj = ByteRun.object_from_dict(byterun_dict)
            if byterun_obj.hasContent_() : byteruns_obj.add_Byte_Run(byterun_obj)
        return byteruns_obj

    @classmethod
    def dict_from_object(cls, byteruns_obj):
        """Parse and return a list of ByteRun dictionaries for a ByteRuns object"""
        byteruns_list = []
        for byterun_obj in byteruns_obj.get_Byte_Run():
           byteruns_list.append(ByteRun.dict_from_object(byterun_obj))
        return byteruns_dict
