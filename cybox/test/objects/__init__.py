import cybox.utils


class ObjectTestCase(object):
    """A base class for testing all subclasses of DefinedObject.

    Each subclass of ObjectTestCase should subclass both unittest.TestCase
    and ObjectTestCase, and defined two class-level fields:
    - klass: the DefinedObject subclass being tested
    - object_type: The name prefix used in the XML Schema bindings for the
      object.
    """

    def test_type_exists(self):
        # Verify that the correct class has been added to the OBJECTS
        # dictionary in cybox.utils
        print(type(self))
        if type(self) == type(ObjectTestCase):
            return
        t = self.__class__.object_type
        c = self.__class__.klass
        self.assertEqual(cybox.utils.get_class_for_object_type(t), c)
