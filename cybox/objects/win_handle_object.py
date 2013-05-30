# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_handle_object as win_handle_binding
from cybox.common import ObjectProperties, String, UnsignedLong, UnsignedInteger

class WinHandle(ObjectProperties):
    _XSI_NS = "WinHandleObj"
    _XSI_TYPE = "WindowsHandleObjectType"

    def __init__(self):
        super(WinHandle, self).__init__()
        self.id = None
        self.name = None
        self.type = None
        self.object_address = None
        self.access_mask = None
        self.pointer_count = None

    def to_obj(self):
        win_handle_obj = win_handle_binding.WindowsHandleObjectType()
        super(WinHandle, self).to_obj(win_handle_obj)

        if self.id is not None: win_handle_obj.set_ID(self.id.to_obj())
        if self.name is not None: win_handle_obj.set_Name(self.name.to_obj())
        if self.type is not None: win_handle_obj.set_Type(self.type.to_obj())
        if self.object_address is not None: win_handle_obj.set_Object_Address(self.object_address.to_obj())
        if self.access_mask is not None: win_handle_obj.set_Access_Mask(self.access_mask.to_obj())
        if self.pointer_count is not None: win_handle_obj.set_Pointer_Count(self.pointer_count.to_obj())

        return win_handle_obj

    def to_dict(self):
        win_handle_dict = {}
        super(WinHandle, self).to_dict(win_handle_dict)

        if self.id is not None: win_handle_dict['id'] = self.id.to_dict()
        if self.name is not None: win_handle_dict['name'] = self.name.to_dict()
        if self.type is not None: win_handle_dict['type'] = self.type.to_dict()
        if self.object_address is not None: win_handle_dict['object_address'] = self.object_address.to_dict()
        if self.access_mask is not None: win_handle_dict['access_mask'] = self.access_mask.to_dict()
        if self.pointer_count is not None: win_handle_dict['pointer_count'] = self.pointer_count.to_dict()

        return win_handle_dict

    @staticmethod
    def from_dict(win_handle_dict):
        if not win_handle_dict:
            return None
        win_handle_ = WinHandle()
        
        win_handle_.id = UnsignedInteger.from_dict(win_handle_dict.get('id'))        
        win_handle_.name = String.from_dict(win_handle_dict.get('name'))
        win_handle_.type = String.from_dict(win_handle_dict.get('type'))
        win_handle_.object_address = UnsignedLong.from_dict(win_handle_dict.get('id'))
        win_handle_.access_mask = UnsignedLong.from_dict(win_handle_dict.get('access_mask'))
        win_handle_.pointer_count = UnsignedLong.from_dict(win_handle_dict.get('id')) 

        return win_handle_
    
    @staticmethod
    def from_obj(win_handle_obj):
        if not win_handle_obj:
            return None
        win_handle_ = WinHandle()

        win_handle_.id = UnsignedInteger.from_obj(win_handle_obj.get_ID())        
        win_handle_.name = String.from_obj(win_handle_obj.get_Name())
        win_handle_.type = String.from_obj(win_handle_obj.get_Type())
        win_handle_.object_address = UnsignedLong.from_obj(win_handle_obj.get_Object_Address())
        win_handle_.access_mask = UnsignedLong.from_obj(win_handle_obj.get_Access_Mask())
        win_handle_.pointer_count = UnsignedLong.from_obj(win_handle_obj.get_Pointer_Count()) 

        return win_handle_

class WinHandleList(cybox.EntityList):
    _binding_class = win_handle_binding.WindowsHandleListType()
    _contained_type = WinHandle

    def __init__(self):
        super(WinHandleList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Handle(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Handle()
