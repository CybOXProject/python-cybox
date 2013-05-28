# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_pipe_object as win_pipe_binding
from cybox.objects.pipe_object import Pipe
from cybox.objects.win_handle_object import WinHandle
from cybox.common import String, NonNegativeInteger, HexBinary

class WinPipe(Pipe):
    _XSI_NS = "WinPipeObj"
    _XSI_TYPE = "WindowsPipeObjectType"

    def __init__(self):
        super(WinPipe, self).__init__()
        self.default_time_out = None
        self.handle = None
        self.in_buffer_size = None
        self.max_instances = None
        self.open_mode = None
        self.out_buffer_size = None
        self.pipe_mode = None
        self.security_attributes = None

    def to_obj(self):
        win_pipe_obj = super(WinPipe, self).to_obj(win_pipe_binding.WindowsPipeObjectType())
        
        if self.default_time_out is not None : win_pipe_obj.set_Default_Time_Out(self.default_time_out.to_obj())
        if self.handle is not None : win_pipe_obj.set_Handle(self.handle.to_obj())
        if self.in_buffer_size is not None : win_pipe_obj.set_In_Buffer_Size(self.in_buffer_size.to_obj())
        if self.max_instances is not None : win_pipe_obj.set_Max_Instances(self.max_instances.to_obj())
        if self.open_mode is not None : win_pipe_obj.set_Open_Mode(self.open_mode.to_obj())
        if self.out_buffer_size is not None : win_pipe_obj.set_Out_Buffer_Size(self.out_buffer_size.to_obj())
        if self.pipe_mode is not None : win_pipe_obj.set_Pipe_Mode(self.pipe_mode.to_obj())
        if self.security_attributes is not None : win_pipe_obj.set_Security_Attributes(self.security_attributes.to_obj())
        return win_pipe_obj

    def to_dict(self):
        win_pipe_dict = super(WinPipe, self).to_dict()
        if self.default_time_out is not None : win_pipe_dict['default_time_out'] = self.default_time_out.to_dict()
        if self.handle is not None : win_pipe_dict['handle'] = self.handle.to_dict()
        if self.in_buffer_size is not None : win_pipe_dict['in_buffer_size'] = self.in_buffer_size.to_dict()
        if self.max_instances is not None : win_pipe_dict['max_instances'] = self.max_instances.to_dict()
        if self.open_mode is not None : win_pipe_dict['open_mode'] = self.open_mode.to_dict()
        if self.out_buffer_size is not None : win_pipe_dict['out_buffer_size'] = self.out_buffer_size.to_dict()
        if self.pipe_mode is not None : win_pipe_dict['pipe_mode'] = self.pipe_mode.to_dict()
        if self.security_attributes is not None : win_pipe_dict['security_attributes'] = self.security_attributes.to_dict()
        return win_pipe_dict

    @staticmethod
    def from_dict(win_pipe_dict):
        if not win_pipe_dict:
            return None
        win_pipe_ = Pipe.from_dict(win_pipe_dict, WinPipe())
        win_pipe_.default_time_out = NonNegativeInteger.from_dict(win_pipe_dict.get('default_time_out'))
        win_pipe_.handle = WinHandle.from_dict(win_pipe_dict.get('handle'))
        win_pipe_.in_buffer_Size = NonNegativeInteger.from_dict(win_pipe_dict.get('in_buffer_size'))
        win_pipe_.max_instances = NonNegativeInteger.from_dict(win_pipe_dict.get('max_instances'))
        win_pipe_.open_mode = HexBinary.from_dict(win_pipe_dict.get('open_mode'))
        win_pipe_.out_buffer_size = NonNegativeInteger.from_dict(win_pipe_dict.get('out_buffer_size'))
        win_pipe_.pipe_mode = HexBinary.from_dict(win_pipe_dict.get('pipe_mode'))
        win_pipe_.security_attributes = String.from_dict(win_pipe_dict.get('security_attributes'))
        return win_pipe_

    @staticmethod
    def from_obj(win_pipe_obj):
        if not win_pipe_obj:
            return None
        win_pipe_ = Pipe.from_obj(win_pipe_obj, WinPipe())
        win_pipe_.default_time_out = NonNegativeInteger.from_obj(win_pipe_obj.get_Default_Time_Out())
        win_pipe_.handle = WinHandle.from_obj(win_pipe_obj.get_Handle())
        win_pipe_.in_buffer_Size = NonNegativeInteger.from_obj(win_pipe_obj.get_In_Buffer_Size())
        win_pipe_.max_instances = NonNegativeInteger.from_obj(win_pipe_obj.get_Max_Instances())
        win_pipe_.open_mode = HexBinary.from_obj(win_pipe_obj.get_Open_Mode())
        win_pipe_.out_buffer_size = NonNegativeInteger.from_obj(win_pipe_obj.get_Out_Buffer_Size())
        win_pipe_.pipe_mode = HexBinary.from_obj(win_pipe_obj.get_Pipe_Mode())
        win_pipe_.security_attributes = String.from_obj(win_pipe_obj.get_Security_Attributes())
        return win_pipe_



