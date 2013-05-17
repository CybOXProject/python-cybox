# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.properties import HexBinary, String
from cybox.common.vocabs import VocabString


class HashName(VocabString):
    _XSI_TYPE = 'cyboxVocabs:HashNameVocab-1.0'


class Hash(cybox.Entity):
    _binding = common_binding
    _namespace = 'http://cybox.mitre.org/common-2'

    TYPE_MD5 = "MD5"
    TYPE_MD6 = "MD6"
    TYPE_SHA1 = "SHA1"
    TYPE_SHA256 = "SHA256"
    TYPE_SSDEEP = "SSDEEP"
    TYPE_OTHER = "Other"

    def __init__(self, hash_value=None, type_=None, exact=False):
        """Create a new Hash Object

        If exact=True, add 'condition="Equals"' to the hash_value
        """
        # Set type_ first so that auto-typing will work.
        self.type_ = type_
        self.simple_hash_value = hash_value
        self.fuzzy_hash_value = None

        if exact and self.simple_hash_value:
            self.simple_hash_value.condition = "Equals"

    def __str__(self):
        return str(self.simple_hash_value)

    # Properties
    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if value and not isinstance(value, HashName):
            value = HashName(value)
        self._type = value

    @property
    def simple_hash_value(self):
        return self._simple_hash_value

    @simple_hash_value.setter
    def simple_hash_value(self, hash_value):
        if hash_value and not isinstance(hash_value, HexBinary):
            hash_value = HexBinary(hash_value)
        self._simple_hash_value = hash_value

        # Attempt to determine the hash type if `type_` is None
        if self._simple_hash_value and not self.type_:
            val = self._simple_hash_value.value
            if not val:
                # If not provided or an empty string, don't assign the type
                self.type_ = None
            elif len(val) == 32:
                self.type_ = Hash.TYPE_MD5
            elif len(val) == 40:
                self.type_ = Hash.TYPE_SHA1
            elif len(val) == 64:
                self.type_ = Hash.TYPE_SHA256
            else:
                self.type_ = Hash.TYPE_OTHER

    # Other_Type and FuzzyHashes not yet supported.

    # Import/Export
    def to_obj(self, object_type=None):
        if not object_type:
            hashobj = common_binding.HashType()
        else:
            hashobj = object_type

        if self.type_ is not None:
            hashobj.set_Type(self.type_.to_obj())
        if self.simple_hash_value is not None:
            hashobj.set_Simple_Hash_Value(self.simple_hash_value.to_obj())
        if self.fuzzy_hash_value is not None:
            hashobj.set_Fuzzy_Hash_Value(self.fuzzy_hash_value.to_obj())

        return hashobj

    def to_dict(self):
        hash_dict = {}

        if self.type_ is not None:
            hash_dict['type'] = self.type_.to_dict()
        if self.simple_hash_value is not None:
            hash_dict['simple_hash_value'] = self.simple_hash_value.to_dict()
        if self.fuzzy_hash_value is not None:
            hash_dict['fuzzy_hash_value'] = self.fuzzy_hash_value.to_dict()

        return hash_dict

    @staticmethod
    def from_obj(hash_obj, object_class=None):
        if not hash_obj:
            return None

        if not object_class:
            hash_ = Hash()
        else:
            hash_ = object_class

        hash_.type_ = HashName.from_obj(hash_obj.get_Type())
        hash_.simple_hash_value = HexBinary.from_obj(hash_obj.get_Simple_Hash_Value())
        hash_.fuzzy_hash_value = String.from_obj(hash_obj.get_Fuzzy_Hash_Value())

        return hash_

    @staticmethod
    def from_dict(hash_dict, object_class=None):
        if not hash_dict:
            return None

        if not object_class:
            hash_ = Hash()
        else:
            hash_ = object_class

        hash_.type_ = HashName.from_dict(hash_dict.get('type'))
        hash_.simple_hash_value = HexBinary.from_dict(hash_dict.get('simple_hash_value'))
        hash_.fuzzy_hash_value = String.from_dict(hash_dict.get('fuzzy_hash_value'))

        return hash_

#    @classmethod
#    def object_from_dict(cls, hash_dict):
#        """Create the Hash object representation from an input dictionary"""
#        hash = common_binding.HashType()
#        for hash_key, hash_value in hash_dict.items():
#            if hash_key == 'type' : hash.set_Type(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'other_type' : hash.set_Type(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'simple_hash_value' : hash.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value))
#            if hash_key == 'fuzzy_hash_value' : hash.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'fuzzy_hash_structure':
#                for fuzzy_hash_structure_dict in hash_value:
#                    fuzzy_hash_structure_object = common_binding.FuzzyHashStructureType()
#                    for fuzzy_key, fuzzy_value in fuzzy_hash_structure_dict.items():
#                        if fuzzy_key == 'block_size' : fuzzy_hash_structure_object.set_Block_Size(Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),fuzzy_value))
#                        if fuzzy_key == 'block_hash' :
#                            block_hash_dict = fuzzy_value
#                            block_hash_object = common_binding.FuzzyHashBlockType()
#                            for block_hash_key, block_hash_value in block_hash_dict.items():
#                                if block_hash_key == 'segment_count' : block_hash_object.set_Segment_Count(Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),block_hash_value))
#                                if block_hash_key == 'block_hash_value' :
#                                    hash_value_dict = block_hash_value
#                                    hash_value_object = common_binding.HashValueType()
#                                    for hash_value_key, hash_value_value in hash_value_dict.items():
#                                        if hash_value_key == 'simple_hash_value' : hash_value_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value_value))
#                                        if hash_value_key == 'fuzzy_hash_value' : hash_value_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value_value))
#                                    if hash_value_object.hasContent_(): block_hash_object.set_Block_Hash_Value(hash_value_object)
#                                if block_hash_key == 'segments' :
#                                    segments_dict = block_hash_value
#                                    segments_object = common_binding.HashSegmentsType()
#                                    for segment in segments_dict:
#                                        hash_segment_object = common_binding.HashSegmentType()
#                                        for segment_key, segment_value in segment.items():
#                                            if segment_key == 'trigger_point' : hash_segment_object.set_Trigger_Point(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_value))
#                                            if segment_key == 'segment_hash' :
#                                                segment_hash_dict = segment_value
#                                                segment_hash_object = common_binding.HashValueType()
#                                                for segment_hash_key, segment_hash_value in segment_hash_dict.items():
#                                                    if segment_hash_key == 'simple_hash_value' : segment_hash_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_hash_value))
#                                                    if segment_hash_key == 'fuzzy_hash_value' : segment_hash_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),segment_hash_value))
#                                                if segment_hash_object.hasContent_(): hash_segment_object.set_Segment_Hash(segment_hash_object)
#                                            if segment_key == 'raw_segment_content' : hash_segment_object.set_Raw_Segment_Content(segment_value)
#                                        if hash_segment_object.hasContent_() : segments_object.add_Segment(hash_segment_object)
#                                    if segments_object.hasContent_() : block_hash_object.set_Segments(segments_object)
#                            if block_hash_object.hasContent_() : fuzzy_hash_structure_object.set_Block_Hash(block_hash_object)
#                    if fuzzy_hash_structure_object.hasContent_() : hash.add_Fuzzy_Hash_Structure(fuzzy_hash_structure_object)
#
#        return hash


class HashList(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.HashListType
    _contained_type = Hash

    def __init__(self):
        super(HashList, self).__init__()

    def _fix_value(self, value):
        # If the user tries to put a string into a list, convert it to a Hash.
        if isinstance(value, basestring):
            return Hash(value)

    @property
    def md5(self):
        return self._hash_lookup(Hash.TYPE_MD5).value

    @md5.setter
    def md5(self, value):
        self._set_hash(Hash.TYPE_MD5, value)

    @property
    def sha1(self):
        return self._hash_lookup(Hash.TYPE_SHA1).value

    @sha1.setter
    def sha1(self, value):
        self._set_hash(Hash.TYPE_SHA1, value)

    @property
    def sha256(self):
        return self._hash_lookup(Hash.TYPE_SHA256).value

    @sha256.setter
    def sha256(self, value):
        self._set_hash(Hash.TYPE_SHA256, value)

    def _hash_lookup(self, type_):
        for h in self:
            if h.type_ == type_:
                return h.simple_hash_value
        return None

    def _set_hash(self, type_, value):
        h = self._hash_lookup(type_)
        if h:
            h.simple_hash_value = value
        else:
            self.append(Hash(value, type_))

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Hash(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Hash()
