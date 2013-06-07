# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import MeasureSource
import cybox.test


class TestMeasureSource(unittest.TestCase):

    def test_round_trip(self):
        #TODO: add remaining properties
        ms_dict = {
                    'class': "Software",
                    'source_type': "Information Source",
                    'name': "ASource",
                    'information_source_type': "Web Logs",
                    'description': 'A description of the source',
                  }
        ms_dict2 = cybox.test.round_trip_dict(MeasureSource, ms_dict)
        self.assertEqual(ms_dict, ms_dict2)


if __name__ == "__main__":
    unittest.main()
