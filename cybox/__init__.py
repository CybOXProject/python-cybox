import json
from StringIO import StringIO

class Entity(object):
    """Base class for all classes in the Cybox SimpleAPI."""

    def to_xml(self):
        """Export an object as an XML String"""

        s = StringIO()
        self.to_obj().export(s, 0)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def object_from_dict(cls, entity_dict):
        """Convert from dict representation to object representation."""
        return cls.from_dict(entity_dict).to_obj()

    @classmethod
    def dict_from_object(cls, entity_obj):
        """Convert from object representation to dict representation."""
        return cls.from_obj(entity_obj).to_dict()
