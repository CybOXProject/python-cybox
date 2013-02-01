import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.uri_object_1_2 as uri_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class Uri(object):
    def __init__(self):
        pass
    
    @classmethod    
    def object_from_dict(cls, uri_attributes):
        """Create the URI Object object representation from an input dictionary"""
        uriobject = uri_binding.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        
        for key, value in uri_attributes.items():
            if key == 'type' and common_methods.test_value(value):
                uriobject.set_type(value)
            elif key == 'value' and common_methods.test_value(value):
                uriobject.set_Value(baseobjectattribute.object_from_dict(common_types_binding.AnyURIObjectAttributeType(datatype='AnyURI'), value))
        
        return uriobject

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for an URI Object object"""
        if defined_object.get_type() is not None:
            defined_object_dict['type'] = defined_object.get_type()
        if defined_object.get_Value() is not None:
            defined_object_dict['value'] = baseobjectattribute.dict_from_object(defined_object.get_Value())
        return defined_object_dict
