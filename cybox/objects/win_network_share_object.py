import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_network_share_object_1_3 as win_network_share_binding
import cybox.common.baseobjectattribute as Base_Object_Attribute

class Win_Network_Share:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, share_attributes):
        share_obj = win_network_share_binding.WindowsNetworkShareObjectType()
        share_obj.set_anyAttributes_({'xsi:type' : 'WinNetworkShareObj:WindowsNetworkShareObjectType'})
        
        for key, value in share_attributes.items():
            if key == 'netname' and utils.test_value(value):
                share_obj.set_Netname(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'local_path' and utils.test_value(value):
                share_obj.set_Local_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'type' and utils.test_value(value):
                share_obj.set_Type(win_network_share_binding.SharedResourceType(valueOf_=value))
            elif key == 'current_uses' and utils.test_value(value):
                share_obj.set_Current_Uses(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'), value))
            elif key == 'max_uses' and utils.test_value(value):
                share_obj.set_Max_Uses(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'), value))
            
        return share_obj
    
    
    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Win_Netowrk_Share object"""
        defined_object_dict = {}
        
        if defined_object.get_Netname() is not None:
            defined_object_dict['netname'] = Base_Object_Attribute.dict_from_object(defined_object.get_Netname())
        if defined_object.get_Local_Path() is not None:
            defined_object_dict['local_path'] = Base_Object_Attribute.dict_from_object(defined_object.get_Local_Path())
        if defined_object.get_type() is not None:
            defined_object_dict['type'] = Base_Object_Attribute.dict_from_object(defined_object.get_type())
        if defined_object.get_Current_Uses() is not None:
            defined_object_dict['current_uses'] = Base_Object_Attribute.dict_from_object(defined_object.get_Current_Uses())
        if defined_object.get_Max_Uses() is not None:
            defined_object_dict['max_uses'] = Base_Object_Attribute.dict_from_object(defined_object.get_Max_Uses())
        return defined_object_dict