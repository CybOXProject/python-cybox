import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.pipe_object_1_2 as pipe_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Pipe:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, pipe_dict, pipe_obj = None):
        """Create the Pipe Object object representation from an input dictionary"""
        if pipe_obj == None:
            pipe_obj = pipe_binding.PipeObjectType()
            pipe_obj.set_anyAttributes_({'xsi:type' : 'PipeObj:PipeObjectType'})
        
        for key, value in pipe_dict.items():
            if key == 'name' and utils.test_value(value):
                pipe_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
                pipe_obj.set_named(True)
            elif key == 'named' and utils.test_value(value):
                pipe_obj.set_named(value.get('value'))

        return pipe_obj

    @classmethod
    def dict_from_object(cls, pipe_obj):
        """Parse and return a dictionary for a Pipe Object object"""
        pipe_dict = {}
        if pipe_obj.get_Name() is not None: pipe_dict['name'] = Base_Object_Attribute.dict_from_object(pipe_obj.get_Name())
        if pipe_obj.get_named() is not None: pipe_dict['named'] = pipe_obj.get_named()
    
        return pipe_dict