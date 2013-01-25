import maec_bundle_3_0 as maecbundle
import cybox.win_thread_object_1_3 as cybox_win_thread_object

class win_thread_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, thread_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Thread')
        thread_obj = cybox_win_thread_object.WindowsThreadObjectType()
        thread_obj.set_anyAttributes_({'xsi:type' : 'WinThreadObj:WindowsThreadObjectType'})
        
        for key, value in thread_attributes.items():
            if key == 'tid' and self.__value_test(value):
                thread_obj.set_Thread_ID(maecbundle.cybox_common_types_1_0.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger', valueOf_=value))
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if thread_obj.hasContent_():
            cybox_object.set_Defined_Object(thread_obj)
        
        return cybox_object