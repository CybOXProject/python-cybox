import cybox
import cybox.utils as utils
import cybox.bindings.mutex_object_1_3 as mutex_binding
from cybox.common import DefinedObject, String

class Mutex(DefinedObject):
    _XSI_TYPE = "MutexObjectType"

    def __init__(self):
        self.named = None
        self.name = None

    def to_obj(self, mutex_obj = None):
        if mutex_obj == None:
            mutex_obj = mutex_binding.MutexObjectType()
            mutex_obj.set_anyAttributes_({'xsi:type' : 'MutexObj:MutexObjectType'})

        if self.named is not None: mutex_obj.set_named(self.named)
        if self.name is not None: mutex_obj.set_Name(self.name.to_obj())

        return mutex_obj

    def to_dict(self):
        mutex_dict = {}

        if self.named is not None: mutex_dict['named'] = self.named
        if self.name is not None: mutex_dict['name'] = self.name.to_dict()
        mutex_dict['xsi:type'] = self._XSI_TYPE

        return mutex_dict
        
    @staticmethod
    def from_dict(mutex_dict, mutex_cls = None):
        if not mutex_dict:
            return None
        if mutex_cls == None:
            mutex_ = Mutex()
        else:
            mutex_ = mutex_cls

        mutex_.named = mutex_dict.get('named')
        mutex_.name = String.from_dict(mutex_dict.get('name'))

        return mutex_
    
    
    @staticmethod
    def from_obj(mutex_obj, mutex_cls = None):
        if not mutex_obj:
            return None
        if mutex_cls == None:
            mutex_ = Mutex()
        else:
            mutex_ = mutex_cls

        mutex_.named = mutex_obj.get_named()
        mutex_.name = String.from_obj(mutex_obj.get_Name())

        return mutex_
