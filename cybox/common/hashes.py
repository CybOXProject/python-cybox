# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields
from mixbox.vendor import six
from mixbox.vendor.six import u

import cybox.bindings.cybox_common as common_binding
from cybox.common import HexBinary, String, VocabString
from cybox.common.vocabs import HashName, VocabField


def _set_hash_type(entity, value):
    """Callback hook to set the hash type based on the length of the value.

    If the `Hash` object already has a type, it is not changed.

    Args:
        entity (Hash): The Hash object being modified.
        value (str): The hash value
    """
    # If the Hash already has a defined type_, exit early:
    if entity.type_:
        return
    if not value:
        return
    # The `value` argument should be a HexBinary object, so we look at the
    # string in its `value` field.
    hashlen = len(value.value)
    if hashlen == 32:
        entity.type_ = Hash.TYPE_MD5
    elif hashlen == 40:
        entity.type_ = Hash.TYPE_SHA1
    elif hashlen == 56:
        entity.type_ = Hash.TYPE_SHA224
    elif hashlen == 64:
        entity.type_ = Hash.TYPE_SHA256
    elif hashlen == 96:
        entity.type_ = Hash.TYPE_SHA384
    elif hashlen == 128:
        entity.type_ = Hash.TYPE_SHA512
    else:
        entity.type_ = Hash.TYPE_OTHER


class Hash(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.HashType
    _namespace = 'http://cybox.mitre.org/common-2'

    type_ = VocabField("Type", HashName)
    simple_hash_value = fields.TypedField("Simple_Hash_Value", HexBinary,
                                          postset_hook=_set_hash_type)
    fuzzy_hash_value = fields.TypedField("Fuzzy_Hash_Value", String)

    TYPE_MD5 = u("MD5")
    TYPE_MD6 = u("MD6")
    TYPE_SHA1 = u("SHA1")
    TYPE_SHA224 = u("SHA224")
    TYPE_SHA256 = u("SHA256")
    TYPE_SHA384 = u("SHA384")
    TYPE_SHA512 = u("SHA512")
    TYPE_SSDEEP = u("SSDEEP")
    TYPE_OTHER = VocabString(u("Other"))

    def __init__(self, hash_value=None, type_=None, exact=False):
        """Create a new Hash Object

        If exact=True, add 'condition="Equals"' to the hash value and type.
        """
        super(Hash, self).__init__()
        # Set type_ first so that auto-typing will work.
        self.type_ = type_
        self.simple_hash_value = hash_value

        if exact:
            if self.simple_hash_value:
                self.simple_hash_value.condition = "Equals"
            if self.type_:
                self.type_.condition = "Equals"

    def __str__(self):
        return str(self.simple_hash_value)

    # Other_Type and FuzzyHashes not yet supported.

#    @classmethod
#    def object_from_dict(cls, hash_dict):
#        """Create the Hash object representation from an input dictionary"""
#        hash = common_binding.HashType()
#        for hash_key, hash_value in hash_dict.items():
#            if hash_key == 'type' : hash.Type = Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value)
#            if hash_key == 'other_type' : hash.Type = Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value)
#            if hash_key == 'simple_hash_value' : hash.Simple_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value)
#            if hash_key == 'fuzzy_hash_value' : hash.Fuzzy_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value)
#            if hash_key == 'fuzzy_hash_structure':
#                for fuzzy_hash_structure_dict in hash_value:
#                    fuzzy_hash_structure_object = common_binding.FuzzyHashStructureType()
#                    for fuzzy_key, fuzzy_value in fuzzy_hash_structure_dict.items():
#                        if fuzzy_key == 'block_size' : fuzzy_hash_structure_object.Block_Size = Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),fuzzy_value)
#                        if fuzzy_key == 'block_hash' :
#                            block_hash_dict = fuzzy_value
#                            block_hash_object = common_binding.FuzzyHashBlockType()
#                            for block_hash_key, block_hash_value in block_hash_dict.items():
#                                if block_hash_key == 'segment_count' : block_hash_object.Segment_Count = Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),block_hash_value)
#                                if block_hash_key == 'block_hash_value' :
#                                    hash_value_dict = block_hash_value
#                                    hash_value_object = common_binding.HashValueType()
#                                    for hash_value_key, hash_value_value in hash_value_dict.items():
#                                        if hash_value_key == 'simple_hash_value' : hash_value_object.Simple_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value_value)
#                                        if hash_value_key == 'fuzzy_hash_value' : hash_value_object.Fuzzy_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value_value)
#                                    if hash_value_object.hasContent_(): block_hash_object.Block_Hash_Value = hash_value_object
#                                if block_hash_key == 'segments' :
#                                    segments_dict = block_hash_value
#                                    segments_object = common_binding.HashSegmentsType()
#                                    for segment in segments_dict:
#                                        hash_segment_object = common_binding.HashSegmentType()
#                                        for segment_key, segment_value in segment.items():
#                                            if segment_key == 'trigger_point' : hash_segment_object.Trigger_Point = Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_value)
#                                            if segment_key == 'segment_hash' :
#                                                segment_hash_dict = segment_value
#                                                segment_hash_object = common_binding.HashValueType()
#                                                for segment_hash_key, segment_hash_value in segment_hash_dict.items():
#                                                    if segment_hash_key == 'simple_hash_value' : segment_hash_object.Simple_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_hash_value)
#                                                    if segment_hash_key == 'fuzzy_hash_value' : segment_hash_object.Fuzzy_Hash_Value = Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),segment_hash_value)
#                                                if segment_hash_object.hasContent_(): hash_segment_object.Segment_Hash = segment_hash_object
#                                            if segment_key == 'raw_segment_content' : hash_segment_object.Raw_Segment_Content = segment_value
#                                        if hash_segment_object.hasContent_() : segments_object.add_Segment(hash_segment_object)
#                                    if segments_object.hasContent_() : block_hash_object.Segments = segments_object
#                            if block_hash_object.hasContent_() : fuzzy_hash_structure_object.Block_Hash = block_hash_object
#                    if fuzzy_hash_structure_object.hasContent_() : hash.add_Fuzzy_Hash_Structure(fuzzy_hash_structure_object)
#
#        return hash


class HashList(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.HashListType
    _namespace = 'http://cybox.mitre.org/common-2'
    hashes = fields.TypedField("Hash", Hash, multiple=True)

    @property
    def md5(self):
        return self._get_hash_value(Hash.TYPE_MD5)

    @md5.setter
    def md5(self, value):
        self._set_hash(Hash.TYPE_MD5, value)

    @property
    def sha1(self):
        return self._get_hash_value(Hash.TYPE_SHA1)

    @sha1.setter
    def sha1(self, value):
        self._set_hash(Hash.TYPE_SHA1, value)

    @property
    def sha224(self):
        return self._get_hash_value(Hash.TYPE_SHA224)

    @sha224.setter
    def sha224(self, value):
        self._set_hash(Hash.TYPE_SHA224, value)

    @property
    def sha256(self):
        return self._get_hash_value(Hash.TYPE_SHA256)

    @sha256.setter
    def sha256(self, value):
        self._set_hash(Hash.TYPE_SHA256, value)

    @property
    def sha384(self):
        return self._get_hash_value(Hash.TYPE_SHA384)

    @sha384.setter
    def sha384(self, value):
        self._set_hash(Hash.TYPE_SHA384, value)

    @property
    def sha512(self):
        return self._get_hash_value(Hash.TYPE_SHA512)

    @sha512.setter
    def sha512(self, value):
        self._set_hash(Hash.TYPE_SHA512, value)

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

    def _get_hash_value(self, type_):
        """Return the hash with a given type_, or None"""
        h = self._hash_lookup(type_)
        if h:
            return h.value
        return None
