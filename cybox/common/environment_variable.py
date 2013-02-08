import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.baseobjectattributetype import Base_Object_Attribute

class Environment_Variable(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, enviroment_variable_dict):
        """Create the Environment Variable object representation from an input dictionary"""
        environment_variable_obj = common_binding.EnvironmentVariableType()
        for key, value in enviroment_variable_dict.items():
            if key == 'name' : 
                environment_variable_obj.set_Name(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'value' : 
                environment_variable_obj.set_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
        return environment_variable_obj

    @classmethod
    def dict_from_object(cls, environment_variable_obj):
        """Parse and return a dictionary for an Environment Variable object"""
        environment_variable_dict = {}
        if environment_variable_obj.get_Name() is not None: environment_variable_dict['name'] = Base_Object_Attribute.dict_from_object(defined_object.get_Name())
        if environment_variable_obj.get_Value() is not None: environment_variable_dict['value'] = Base_Object_Attribute.dict_from_object(defined_object.get_Value())
        return environment_variable_dict