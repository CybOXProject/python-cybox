import maec_bundle_3_0 as maecbundle
import cybox.win_file_object_1_3 as win_file_binding
import cybox.file_object_1_3 as file_binding
import cybox.uri_object_1_2 as uri_binding
import cybox_helper.objects.file_object.file_object as file_object

class win_file_object(file_object):
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, file_attributes):
        fileobj = super(win_file_object, cls).object_from_dict(file_attributes)
        fileobj.set_anyAttributes_({'xsi:type' : 'WinFileObj:WinFileObjectType'})
        
        for key, value in file_attributes.items():
            pass

    @classmethod
    def dict_from_object(cls, defined_object, defined_object_dict = None):
        defined_object_dict = super(win_file_object, cls).dict_from_object(defined_object, defined_object_dict)
        
        