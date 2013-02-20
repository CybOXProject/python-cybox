import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_kernel_hook_object_1_3 as win_kernel_hook_binding
import cybox.common.baseobjectattribute as Base_Object_Attribute
import cybox.common.digitalsignature as Digital_Signature

class Win_Kernel_Hook:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_kernel_hook_attributes):
        hookobject = win_kernel_hook_binding.WindowsKernelHookObjectType()
        hookobject.set_anyAttributes_({'xsi:type' : 'WinKernelHookObj:WindowsKernelHookObjectType'})
        
        for key, value in win_kernel_hook_attributes.items():
            if key == 'hooked_function' and utils.test_value(value):
                hookobject.set_Hooked_Function(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'hooked_module_name' and utils.test_value(value):
                hookobject.set_Hooked_Module(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'hooking_module_name' and utils.test_value(value):
                hookobject.set_Hooking_Module(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'description' and utils.test_value(value):
                hookobject.set_Hook_Description(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'address' and utils.test_value(value):
                hookobject.set_Hooking_Address(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'type' and utils.test_value(value):
                hookobject.set_Type(win_kernel_hook_binding.KernelHookType(valueOf_=value))
            elif key == 'digital_signature_hooking' and utils.test_value(value):
                hookobject.set_Digital_Signature_Hooking(Digital_Signature.object_from_dict(value))
            elif key == 'digital_signature_hooked' and utils.test_value(value):
                hookobject.set_Digital_Signature_Hooked(Digital_Signature.object_from_dict(value))
        
        return hookobject
    
    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Win_Kernel_Hook object"""
        defined_object_dict = {}
        
        if defined_object.get_Hooked_Function() is not None:
            defined_object_dict["hooked_function"] = Base_Object_Attribute.dict_from_object(defined_object.get_Hooked_Function())
        if defined_object.get_Hooked_Module_Name() is not None:
            defined_object_dict["hooked_module_name"] = Base_Object_Attribute.dict_from_object(defined_object.get_Hooked_Module_Name())
        if defined_object.get_Hooking_Module_Name() is not None:
            defined_object_dict["hooking_module_name"] = Base_Object_Attribute.dict_from_object(defined_object.get_Hooking_Module_Name())
        if defined_object.get_Description() is not None:
            defined_object_dict["description"] = Base_Object_Attribute.dict_from_object(defined_object.get_Description())
        if defined_object.get_Address() is not None:
            defined_object_dict["address"] = Base_Object_Attribute.dict_from_object(defined_object.get_Address())
        if defined_object.get_Type() is not None:
            defined_object_dict["type"] = defined_object.get_Type().valueOf_
        if defined_object.get_Digital_Signature_Hooking() is not None:
            defined_object_dict["digital_signature_hooking"] = Digital_Signature.dict_from_object(defined_object.get_Digital_Signature_Hooking())
        if defined_object.get_Digital_Signature_Hooked() is not None:
            defined_object_dict["digital_signature_hooked"] = Digital_Signature.dict_from_object(defined_object.get_Digital_Signature_Hooked())
            
        return defined_object_dict