# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.core import Frequency
from cybox.test import EntityTestCase


class TestFrequency(EntityTestCase, unittest.TestCase):
    klass = Frequency

    _full_dict = {
        'rate': 1.2,
        'units': u("per hour"),
        'scale': "weekly",
        'trend': "Increasing",
    }


if __name__ == "__main__":
    unittest.main()
