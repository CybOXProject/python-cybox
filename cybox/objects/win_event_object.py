# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_event_object as win_event_binding
from cybox.objects.win_handle_object import WinHandle
from cybox.common import ObjectProperties, String

class WinEvent(ObjectProperties):
    _XSI_NS = "WinEventObj"
    _XSI_TYPE = "WindowsEventObjectType"

    def __init__(self):
        super(WinEvent, self).__init__()
        self.name = None
        self.handle = None
        self.type = None

    def to_obj(self):
        win_event_obj = win_event_binding.WindowsEventObjectType()
        super(WinEvent, self).to_obj(win_event_obj)
        
        if self.name is not None: win_event_obj.set_Name(self.name.to_obj())
        if self.handle is not None: win_event_obj.set_Handle(self.handle.to_obj())
        if self.type is not None: win_event_obj.set_Type(self.type.to_obj())

        return win_event_obj

    def to_dict(self):
        win_event_dict = {}
        super(WinEvent, self).to_dict(win_event_dict)

        if self.name is not None: win_event_dict['name'] = self.name.to_dict()
        if self.handle is not None: win_event_dict['handle'] = self.handle.to_dict()
        if self.type is not None: win_event_dict['type'] = self.type.to_dict()

        return win_event_dict

    @staticmethod
    def from_dict(win_event_dict):
        if not win_event_dict:
            return None
        win_event_ = WinEvent()

        win_event_.handle = WinHandle.from_dict(win_event_dict.get('handle'))
        win_event_.name = String.from_dict(win_event_dict.get('name'))
        win_event_.type = String.from_dict(win_event_dict.get('type'))

        return win_event_    
    
    @staticmethod
    def from_obj(win_event_obj):
        if not win_event_obj:
            return None
        win_event_ = WinEvent()

        win_event_.handle = WinHandle.from_obj(win_event_obj.get_Handle())
        win_event_.name = String.from_obj(win_event_obj.get_Name())
        win_event_.type = String.from_obj(win_event_obj.get_Type())

        return win_event_
       