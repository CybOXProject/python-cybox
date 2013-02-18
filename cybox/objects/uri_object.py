import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.uri_object_1_2 as uri_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class URI(object):
    def __init__(self):
        pass
    
    @classmethod    
    def object_from_dict(cls, uri_dict):
        """Create the URI Object object representation from an input dictionary"""
        uri_obj = uri_binding.URIObjectType()
        uri_obj.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        
        for key, value in uri_dict.items():
            if key == 'type' and utils.test_value(value):
                uri_obj.set_type(value)
            elif key == 'value' and utils.test_value(value):
                uri_obj.set_Value(Base_Object_Attribute.object_from_dict(common_types_binding.AnyURIObjectAttributeType(datatype='AnyURI'), value))
        
        return uri_obj

    @classmethod
    def dict_from_object(cls, uri_obj):
        """Parse and return a dictionary for an URI Object object"""
        uri_dict = {}
        if uri_obj.get_type() is not None: uri_dict['type'] = uri_obj.get_type()
        if uri_obj.get_Value() is not None: uri_dict['value'] = Base_Object_Attribute.dict_from_object(uri_obj.get_Value())
        return uri_dict