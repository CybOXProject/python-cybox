import cybox.utils


class ObjectTestCase(object):
    """A base class for testing all subclasses of ObjectProperties.

    Each subclass of ObjectTestCase should subclass both unittest.TestCase
    and ObjectTestCase, and defined two class-level fields:
    - klass: the ObjectProperties subclass being tested
    - object_type: The name prefix used in the XML Schema bindings for the
      object.
    """

    def test_type_exists(self):
        # Verify that the correct class has been added to the OBJECT_TYPES_DICT
        # dictionary in cybox.utils.nsparser

        # Skip this base class
        if type(self) == type(ObjectTestCase):
            return

        t = self.__class__.object_type

        expected_class = cybox.utils.get_class_for_object_type(t)
        actual_class = self.__class__.klass

        self.assertEqual(expected_class, actual_class)

        expected_namespace = expected_class._XSI_NS
        actual_namespace = cybox.utils.nsparser.OBJECT_TYPES_DICT.get(t).get('namespace_prefix')
        self.assertEqual(expected_namespace, actual_namespace)

        self.assertEqual(expected_class._XSI_TYPE, t)
