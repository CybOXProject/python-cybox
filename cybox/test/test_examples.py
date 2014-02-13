"""Test examples found in the documentation.

This ensures that examples don't get out of date with the library code.
"""

import doctest
from os.path import abspath, dirname, join
import unittest

BASE_DIR = join(dirname(dirname(dirname(__file__))), "doc")


class DocumentationTests(unittest.TestCase):
    """Test example code snippets found in the documentation"""

    def test_examples(self):
        (failure_count, test_count) = doctest.testfile(
                                                join(BASE_DIR, "examples.rst"),
                                                module_relative=False)
        self.assertEqual(0, failure_count)


if __name__ == "__main__":
    unittest.main()
