import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.uri_object_1_2 as uri_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class uri_object(object):
    def __init__(self):
        pass
    
    @classmethod    
    def create_from_dict(cls, uri_attributes):
        """Create the URI Object object representation from an input dictionary"""
        uriobject = uri_object_binding.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        
        for key, value in uri_attributes.items():
            if key == 'type' and common_methods.test_value(value):
                uriobject.set_type(value)
            elif key == 'value' and common_methods.test_value(value):
                uriobject.set_Value(baseobjectattribute.create_from_dict(common_types_binding.AnyURIObjectAttributeType(datatype='AnyURI'), value))
        
        return uriobject

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        """Parse and return a dictionary for an URI Object object"""
        if defined_object_dict == None:
            defined_object_dict = {}
        if defined_object.get_type() is not None:
            defined_object_dict['type'] = defined_object.get_type()
        if defined_object.get_Value() is not None:
            defined_object_dict['value'] = baseobjectattribute.parse_into_dict(defined_object.get_Value())
        return defined_object_dict