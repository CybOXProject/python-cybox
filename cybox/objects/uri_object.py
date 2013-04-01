import cybox.bindings.uri_object_1_2 as uri_binding

from cybox.common import DefinedObject, AnyURI


class URI(DefinedObject):
    _XSI_TYPE = "URIObjectType"

    TYPE_URL = "URL"
    TYPE_GENERAL = "General URN"
    TYPE_DOMAIN = "Domain Name"

    TYPES = (TYPE_URL, TYPE_GENERAL, TYPE_DOMAIN)

    def __init__(self, value=None, type_=None):
        super(URI, self).__init__()
        self.value = value
        self.type_ = type_

    # Properties
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, AnyURI):
            self._value = value
        else:
            self._value = AnyURI(value)

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, type_):
        if type_ and type_ not in self.TYPES:
            raise ValueError("Invalid URL Type: {0}".format(type_))
        self._type = type_

    # Import/Export
    def to_obj(self):
        uriobject = uri_binding.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type': 'URIObj:URIObjectType'})
        uriobject.set_type(self.type_)
        uriobject.set_Value(self.value.to_obj())
        return uriobject

    def to_dict(self):
        uri_dict = {}
        super(URI, self)._populate_dict(uri_dict)
        if self.type_ is not None:
            uri_dict['type'] = self.type_
        if self.value is not None:
            uri_dict['value'] = self.value.to_dict()
        return uri_dict

    @staticmethod
    def from_obj(uri_obj):
        uri = URI()
        uri.type_ = uri_obj.get_type()
        uri.value = AnyURI.from_obj(uri_obj.get_Value())
        return uri

    @staticmethod
    def from_dict(uri_dict):
        uri = URI()
        uri.type_ = uri_dict.get('type')
        uri.value = AnyURI.from_dict(uri_dict.get('value'))
        return uri
