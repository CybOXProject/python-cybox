import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.pipe_object_1_2 as pipe_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class pipe_object:
    def __init__(self):
        pass
        
    @classmethod
    def create_from_dict(cls, pipe_attributes, pipe_obj = None):
        """Create the Pipe Object object representation from an input dictionary"""
        if pipe_obj == None:
            pipe_obj = pipe_object_binding.PipeObjectType()
            pipe_obj.set_anyAttributes_({'xsi:type' : 'PipeObj:PipeObjectType'})
        
        for key, value in pipe_attributes.items():
            if key == 'name' and common_methods.test_value(value):
                pipe_obj.set_Name(baseobjectattribute.create_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
                pipe_obj.set_named(True)
            elif key == 'named' and common_methods.test_value(value):
                pipe_obj.set_named(value.get('value'))

        return pipe_obj

    @classmethod
    def parse_into_dict(cls, defined_object):
        """Parse and return a dictionary for a Pipe Object object"""
        defined_object_dict = {}
        if defined_object.get_Name() is not None: defined_object_dict['name'] = baseobjectattribute.parse_into_dict(defined_object.get_Name())
        if defined_object.get_named() is not None: defined_object_dict['named'] = {'value' : defined_object.get_named()}
    
        return defined_object_dict