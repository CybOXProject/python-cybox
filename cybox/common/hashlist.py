import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.hash import hash

class hashlist(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, hashlist_attributes):
        """Create the HashList object representation from an input dictionary"""
        hashlist = common_binding.HashListType()
        for cybox_hash in hashlist_attributes:
            hash_object = hash.create_from_dict(cybox_hash)
            if hash_object.hasContent_():
                hashlist.add_Hash(hash_object)
        return hashlist

    @classmethod
    def parse_into_dict(cls, element):
        """Parse and return a dictionary for a HashList object"""
        hashlist = []
        for cybox_hash in element.get_Hash():
            hash_dict = hash.parse_into_dict(cybox_hash)
            hashlist.append(hash_dict)
        return hashlist
