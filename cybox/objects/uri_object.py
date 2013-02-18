from cybox.bindings.cybox_common_types_1_0 import AnyURIObjectAttributeType as AnyURI
import cybox.bindings.uri_object_1_2 as uri_binding

from cybox.common import DefinedObject

class Uri(DefinedObject):
    TYPE_URL = "URL"
    TYPE_GENERAL = "General URN"
    TYPE_DOMAIN = "Domain Name"

    TYPES = (TYPE_URL, TYPE_GENERAL, TYPE_DOMAIN)

    def __init__(self):
        pass

    # Properties
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, type_):
        if type_ not in self.TYPES:
            raise ValueError("Invalid URL Type: {0}".format(type_))
        self._type = type_

    # Import/Export
    def to_obj(self):
        uriobject = uri_binding.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        uriobject.set_type(self.type_)
        # Only handle value of BaseObjectAttributeType for now
        uriobject.set_Value(AnyURI(valueOf_=self.value))
        return uriobject

    def to_dict(self):
        return {
            'type': self.type_,
            'Value': self.value,
        }

    @staticmethod
    def from_obj(uri_obj):
        uri = Uri()
        uri.type_ = uri_obj.get_type()
        # Only worry about the value for now.
        uri.value = uri_obj.get_Value().get_valueOf_()
        return uri

    @staticmethod
    def from_dict(uri_dict):
        uri = Uri()
        if 'type' in uri_dict:
            uri.type_ = uri_dict['type']
        if 'Value' in uri_dict:
            uri.value = uri_dict['Value']

        return uri

    # Conversion
    @classmethod
    def object_from_dict(cls, uri_attributes):
        """Create the URI Object object representation from an input dictionary"""
        return cls.from_dict(uri_attributes).to_obj()

    @classmethod
    def dict_from_object(cls, uri_obj):
        """Parse and return a dictionary for an URI Object object"""
        return cls.from_obj(defined_object).to_dict()

