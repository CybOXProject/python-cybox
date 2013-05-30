# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.library_object as library_binding
from cybox.common import ObjectProperties, HashList, String, UnsignedLong, HexBinary

class Library(ObjectProperties):
    _XSI_NS = "LibraryObj"
    _XSI_TYPE = "LibraryObjectType"

    def __init__(self):
        super(Library, self).__init__()
        self.name = None
        self.path = None
        self.size = None
        self.type = None
        self.version = None
        self.base_address = None
        self.extracted_features = None

    def to_obj(self):
        lib_obj = library_binding.LibraryObjectType()
        super(Library, self).to_obj(lib_obj)

        if self.name is not None : lib_object.set_Name(self.name.to_obj())
        if self.path is not None : lib_object.set_Path(self.path.to_obj())
        if self.size is not None : lib_object.set_Size(self.size.to_obj())
        if self.type is not None : lib_object.set_Type(self.type.to_obj())
        if self.version is not None : lib_object.set_Version(self.version.to_obj())
        if self.base_address is not None : lib_object.set_Base_Address(self.base_address.to_obj())
        if self.extracted_features is not None : lib_object.set_Extracted_Features(self.extracted_features.to_obj())

        return lib_obj

    def to_dict(self):
        lib_dict = {}
        super(Library, self).to_dict(lib_dict)

        if self.name is not None : lib_dict['name'] = self.name.to_dict()
        if self.path is not None : lib_dict['path'] = self.path.to_dict()
        if self.size is not None : lib_dict['size'] = self.size.to_dict()
        if self.type is not None : lib_dict['type'] = self.type.to_dict()
        if self.version is not None : lib_dict['version'] = self.version.to_dict()
        if self.base_address is not None : lib_dict['base_address'] = self.base_address.to_dict()
        if self.extracted_features is not None : lib_dict['extracted_features'] = self.extracted_features.to_dict()

        return lib_obj

    @staticmethod
    def from_dict(library_dict):
        if not library_dict:
            return None
        library_ = Library()
        library_.name = String.from_dict(library_dict.get('name'))
        library_.path = String.from_dict(library_dict.get('path'))
        library_.size = UnsignedLong.from_dict(library_dict.get('size'))
        library_.type = String.from_dict(library_dict.get('type'))
        library_.version = String.from_dict(library_dict.get('version'))
        library_.base_address = HexBinary.from_dict(library_dict.get('base_address'))
        library_.extracted_features = None
        return library_

    @staticmethod
    def from_obj(library_obj):
        if not library_obj:
            return None
        library_ = Library()
        library_.name = String.from_obj(library_obj.get_Name())
        library_.path = String.from_obj(library_obj.get_Path())
        library_.size = UnsignedLong.from_obj(library_obj.get_Size())
        library_.type = String.from_obj(library_obj.get_Type())
        library_.version = String.from_obj(library_obj.get_Version())
        library_.base_address = HexBinary.from_obj(library_obj.get_Base_Address())
        library_.extracted_features = None
        return library_
                                  
