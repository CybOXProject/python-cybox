import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_registry_key_object_1_3 as win_registry_key_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.byterun import ByteRuns
from cybox.objects.win_handle_object import Win_Handle_List

class Registry_Key:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, registry_key_dict):
        """Create the Win Registry Key Object object representation from an input dictionary"""
        registry_key_obj = win_registry_key_binding.WindowsRegistryKeyObjectType()
        registry_key_obj.set_anyAttributes_({'xsi:type' : 'WinRegistryKeyObj:WindowsRegistryKeyObjectType'})
        registry_value = win_registry_key_binding.RegistryValueType()

        for key, value in registry_key_dict.items():
            if key == 'hive' and utils.test_value(value):
                registry_key_obj.set_Hive(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'key' and utils.test_value(value):
                registry_key_obj.set_Key(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'number_values' and utils.test_value(value):
                registry_key_obj.set_Number_Values(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'), value))
            elif key == 'values' :
                registry_values_obj = win_registry_key_binding.RegistryValuesType()
                for registry_value_dict in value:
                    registry_value_obj = cls.__registry_value_object_from_dict(registry_value_dict)
                    if registry_value_obj.hasContent_() : registry_values_obj.add_Value(registry_value_obj)
                if registry_values_obj.hasContent_() : registry_key_obj.set_Values(registry_values_obj)
            elif key == 'modified_time' and utils.test_value(value):
                registry_key_obj.set_Modified_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), value))
            elif key == 'creator_username' and utils.test_value(value):
                registry_key_obj.set_Creator_Username(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))                
            elif key == 'handle_list':
                registry_key_obj.set_Handle_List(Win_Handle_List.object_from_dict(value))
            elif key == 'number_subkeys' and utils.test_value(value):
                registry_key_obj.set_Number_Subkeys(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'), value))                
            elif key == 'subkeys' :
                subkeys_obj = win_registry_key_binding.RegistrySubkeysType()
                for sub_registry_key_dict in value:
                    sub_registry_key_obj = cls.object_from_dict(sub_registry_key_dict)
                    if sub_registry_key_obj.hasContent_() : subkeys_obj.add_Subkey(sub_registry_key_obj)
                if subkeys_obj.hasContent_() : registry_key_obj.set_Subkeys(subkeys_obj)
            elif key == 'byte_runs' : 
                  registry_key_obj.set_Byte_Runs(ByteRuns.object_from_dict(value))
        return registry_key_obj

    @classmethod
    def dict_from_object(cls, registry_key_obj):
        """Parse and return a dictionary for a Win Registry Key Object object"""  
        registry_key_dict = {}
        if registry_key_obj.get_Key() is not None: registry_key_dict['key'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Key())
        if registry_key_obj.get_Hive() is not None: registry_key_dict['hive'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Hive())
        if registry_key_obj.get_Number_Values() is not None: registry_key_dict['number_values'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Number_Values())
        if registry_key_obj.get_Values() is not None: registry_key_dict['values'] = cls.__registry_value_dict_from_object(registry_key_obj.get_Values())
        if registry_key_obj.get_Modified_Time() is not None: registry_key_dict['modified_time'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Modified_Time())
        if registry_key_obj.get_Creator_Username() is not None: registry_key_dict['creator_username'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Creator_Username())
        if registry_key_obj.get_Handle_List() is not None: registry_key_dict['handle_list'] = Win_Handle_List.dict_from_object(registry_key_obj.get_Handle_List())
        if registry_key_obj.get_Number_Subkeys() is not None: registry_key_dict['number_subkeys'] = Base_Object_Attribute.dict_from_object(registry_key_obj.get_Number_Subkeys())
        if registry_key_obj.get_Subkeys() is not None:
            subkeys_list = []
            for subkey_obj in registry_key_obj.get_Subkeys().get_Subkey():
                subkey_dict = cls.dict_from_object(subkey_obj)
                subkeys_list.append(subkey_dict)
            registry_key_dict['subkeys'] = subkeys_list
        if registry_key_obj.get_Byte_Runs() is not None: registry_key_dict['byte_runs'] = ByteRuns.dict_from_object(registry_key_obj.get_Byte_Runs())
        return registry_key_dict

    @classmethod
    def __registry_value_object_from_dict(cls, registry_value_dict):
        registry_value_obj = win_registry_key_binding.RegistryValueType()
        for key, value in registry_value_dict.items():
            if key == 'name' and utils.test_value(value):
                registry_value_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'data' and utils.test_value(value):
                registry_value_obj.set_Data(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'datatype' and utils.test_value(value):
                registry_value_obj.set_Datatype(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'byte_runs' : ByteRuns.object_from_dict(value)
        return registry_value_obj

    @classmethod
    def __registry_value_dict_from_object(cls, registry_value_obj):
        registry_value_dict = {}
        if registry_value_obj.get_Name() is not None: registry_value_dict['name'] = Base_Object_Attribute.dict_from_object(registry_value_obj.get_Name())
        if registry_value_obj.get_Data() is not None: registry_value_dict['data'] = Base_Object_Attribute.dict_from_object(registry_value_obj.get_Data())
        if registry_value_obj.get_Datatype() is not None: registry_value_dict['datatype'] = Base_Object_Attribute.dict_from_object(registry_value_obj.get_Datatype())
        if registry_value_obj.get_Byte_Runs() is not None: registry_value_dict['byte_runs'] = ByteRuns.dict_from_object(registry_value_obj.get_Byte_Runs())
        return registry_value_dict