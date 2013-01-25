import maec_bundle_3_0 as maecbundle
import cybox.win_kernel_hook_object_1_3 as cybox_win_kernel_hook_object

class win_kernel_hook_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, win_kernel_hook_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id()) # type_="Hook"
        hookobject = cybox_win_kernel_hook_object.WindowsKernelHookObjectType()
        hookobject.set_anyAttributes_({'xsi:type' : 'WinKernelHookObj:WindowsKernelHookObjectType'})
        
        for key, value in win_kernel_hook_attributes.items():
            if key == 'function_name' and self.__value_test(value):
                hookobject.set_Hooked_Function(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            if key == 'hooked_module_name' and self.__value_test(value):
                hookobject.set_Hooked_Module(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            if key == 'hooking_module_name' and self.__value_test(value):
                hookobject.set_Hooking_Module(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'description' and self.__value_test(value):
                hookobject.set_Hook_Description(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'address' and self.__value_test(value):
                hookobject.set_Hooking_Address(maecbundle.cybox_common_types_1_0.UnsignedLongObjectAttributeType(valueOf_=maecbundle.quote_xml(value)))
            elif key == 'type' and self.__value_test(value):
                if value == 'IAT_API':
                    hookobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="IAT_API"))
                elif value == 'inline':
                    hookobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Inline_Function"))
                elif value == 'instruction hooking':
                    hookobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Instruction_Hooking"))
            elif key == 'hooking_signature' and self.__value_test(value):
                hookobject.set_Digital_Signature_Hooking(value) # TODO: maecbundle.cybox_common_types_1_0.DigitalSignatureInfoType
            elif key == 'hooked_signature' and self.__value_test(value):
                hookobject.set_Digital_Signature_Hooked(value) # TODO: maecbundle.cybox_common_types_1_0.DigitalSignatureInfoType
            elif key == 'association' and self.__value_test(value):
                cybox_object.set_association_type(value)
        
        if hookobject.hasContent_():
            cybox_object.set_Defined_Object(hookobject)
        
        return cybox_object