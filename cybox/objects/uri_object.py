import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.uri_object_1_2 as uri_binding

class uri_object(object):
    def __init__(self):
        pass
    
    @classmethod    
    def create_from_dict(cls, uri_attributes):
        uriobject = uri_binding.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        
        for key, value in uri_attributes.items():
            if key == 'type' and common_methods.test_value(value):
                uriobject.set_type(value)
            elif key == 'value' and common_methods.test_value(value):
                uriobject.set_Value(common_methods.create_element_from_dict(cybox_common.AnyURIObjectAttributeType(datatype='AnyURI'), value))
        
        return uriobject

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
        if defined_object.get_type() is not None:
            defined_object_dict['type'] = defined_object.get_type()
        if defined_object.get_Value() is not None:
            defined_object_dict['value'] = common_methods.parse_element_into_dict(defined_object.get_Value())
        return defined_object_dict