# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.pipe_object as pipe_binding
from cybox.common import ObjectProperties, String

class Pipe(ObjectProperties):
    _XSI_NS = "PipeObj"
    _XSI_TYPE = "PipeObjectType"

    def __init__(self):
        super(Pipe, self).__init__()
        self.named = None
        self.name = None

    def to_obj(self, object_type = None):
        if not object_type:
            pipe_obj = pipe_binding.PipeObjectType()
            pipe_obj.set_xsi_type(self._XSI_NS + ':' + self._XSI_TYPE)
        else:
            pipe_obj = object_type
        super(Pipe, self).to_obj(pipe_obj)
        if self.named is not None : pipe_obj.set_named(self.named)
        if self.name is not None : pipe_obj.set_Name(self.name.to_obj())
        return pipe_obj

    def to_dict(self):
        pipe_dict = {}
        super(Pipe, self).to_dict(pipe_dict)

        if self.named is not None : pipe_dict['named'] = self.named
        if self.name is not None : pipe_dict['name'] = self.name.to_dict()
        return pipe_dict

    @staticmethod
    def from_dict(pipe_dict, pipe_class = None):
        if not pipe_dict:
            return None
        if not pipe_class:
            pipe_ = Pipe()
        else:
            pipe_ = pipe_class
        pipe_.named = pipe_dict.get('named')
        pipe_.name = String.from_dict(pipe_dict.get('named'))
        return pipe_

    @staticmethod
    def from_obj(pipe_obj, pipe_class = None):
        if not pipe_obj:
            return None
        if not pipe_class:
            pipe_ = Pipe()
        else:
            pipe_ = pipe_class
        pipe_.named = pipe_obj.get_named()
        pipe_.name = String.from_obj(pipe_obj.get_Name())
        return pipe_
