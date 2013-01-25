import maec_bundle_3_0 as maecbundle
import cybox.win_task_object_1_3 as cybox_win_task_object

class win_task_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, task_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Task')
        task_obj = cybox_win_task_object.WindowsTaskObjectType()
        task_obj.set_anyAttributes_({'xsi:type' : 'WinTaskObj:WindowsTaskObjectType'})
        
        for key, value in task_attributes.items():
            if key == 'command' and self.__value_test(value):
                task_obj.set_Parameters(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == '':
                pass
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if task_obj.hasContent_():
            cybox_object.set_Defined_Object(task_obj)
        
        return cybox_object