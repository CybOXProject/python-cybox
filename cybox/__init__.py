from StringIO import StringIO

class Entity(object):
    """Base class for all classes in the Cybox SimpleAPI."""

    def to_xml(self):
        """Export an object as an XML String"""

        s = StringIO()
        self.to_obj().export(s, 0)
        return s.getvalue()
