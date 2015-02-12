# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import HexBinary, String, VocabString


class HashName(VocabString):
    _XSI_TYPE = 'cyboxVocabs:HashNameVocab-1.0'


class Hash(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.HashType
    _namespace = 'http://cybox.mitre.org/common-2'

    def _auto_type(self):
        """Attempt to determine the hash type if `type_` is None"""
        if self.simple_hash_value and not self.type_:
            val = self.simple_hash_value.value
            if not val:
                # If not provided or an empty string, don't assign the type
                self.type_ = None
            elif len(val) == 32:
                self.type_ = Hash.TYPE_MD5
            elif len(val) == 40:
                self.type_ = Hash.TYPE_SHA1
            elif len(val) == 56:
                self.type_ = Hash.TYPE_SHA224
            elif len(val) == 64:
                self.type_ = Hash.TYPE_SHA256
            elif len(val) == 96:
                self.type_ = Hash.TYPE_SHA384
            elif len(val) == 128:
                self.type_ = Hash.TYPE_SHA512
            else:
                self.type_ = Hash.TYPE_OTHER

    type_ = cybox.TypedField("Type", HashName)
    simple_hash_value = cybox.TypedField("Simple_Hash_Value", HexBinary,
                                         callback_hook=_auto_type)
    fuzzy_hash_value = cybox.TypedField("Fuzzy_Hash_Value", String)

    TYPE_MD5 = u"MD5"
    TYPE_MD6 = u"MD6"
    TYPE_SHA1 = u"SHA1"
    TYPE_SHA224 = u"SHA224"
    TYPE_SHA256 = u"SHA256"
    TYPE_SHA384 = u"SHA384"
    TYPE_SHA512 = u"SHA512"
    TYPE_SSDEEP = u"SSDEEP"
    TYPE_OTHER = u"Other"

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


class HashList(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.HashListType
    _binding_var = "Hash"
    _contained_type = Hash
    _namespace = 'http://cybox.mitre.org/common-2'

    def _fix_value(self, value):
        # If the user tries to put a string into a list, convert it to a Hash.
        if isinstance(value, basestring):
            return Hash(value)

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
