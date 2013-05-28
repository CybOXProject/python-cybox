# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_mutex_object as win_mutex_binding
from cybox.objects.mutex_object import Mutex
from cybox.objects.win_handle_object import WinHandle
from cybox.common import String

class WinMutex(Mutex):
    _XSI_NS = "WinMutexObj"
    _XSI_TYPE = "WindowsMutexObjectType"

    def __init__(self):
        super(WinMutex, self).__init__()
        self.handle = None
        self.security_attributes = None

    def to_obj(self):
        win_mutex_obj = super(WinMutex, self).to_obj(win_mutex_binding.WindowsMutexObjectType())

        if self.handle is not None: win_mutex_obj.set_Handle(self.handle.to_obj())
        if self.security_attributes is not None: win_mutex_obj.set_Security_Attributes(self.security_attributes.to_obj())

        return win_mutex_obj

    def to_dict(self):
        win_mutex_dict = super(WinMutex, self).to_dict()

        if self.handle is not None: win_mutex_dict['handle'] = self.handle.to_dict()
        if self.security_attributes is not None: win_mutex_dict['security_attributes'] = self.security_attributes.to_dict()
        win_mutex_dict['xsi:type'] = self._XSI_TYPE

        return win_mutex_dict
        
    @staticmethod
    def from_dict(win_mutex_dict):
        if not win_mutex_dict:
            return None

        win_mutex_ = Mutex.from_dict(win_mutex_dict, WinMutex())
        win_mutex_.handle = WinHandle.from_dict(win_mutex_dict.get('handle'))
        win_mutex_.security_attributes = String.from_dict(win_mutex_dict.get('security_attributes'))

        return win_mutex_

    @staticmethod
    def from_obj(win_mutex_obj):
        if not win_mutex_obj:
            return None

        win_mutex_ = Mutex.from_obj(win_mutex_obj, WinMutex())
        win_mutex_.handle = WinHandle.from_obj(win_mutex_obj.get_Handle())
        win_mutex_.security_attributes = String.from_dict(win_mutex_obj.get_Security_Attributes())

        return win_mutex_
