# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.pipe_object as pipe_binding
from cybox.common import ObjectProperties, String

class Pipe(ObjectProperties):
    _namespace = 'http://cybox.mitre.org/objects#PipeObject-2'
    _XSI_NS = "PipeObj"
    _XSI_TYPE = "PipeObjectType"
    _binding = pipe_binding
    _binding_class = pipe_binding.PipeObjectType
    
    name = cybox.TypedField("Name", String)
    named = cybox.TypedField("named")

    def __init__(self):
        super(Pipe, self).__init__()
        self.named = None

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
