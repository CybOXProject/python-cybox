# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.common import Hash, ToolInformation, ToolInformationList
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.common.hash_test import EMPTY_MD5


class TestToolInformation(EntityTestCase, unittest.TestCase):
    klass = ToolInformation

    _full_dict = {
        'id': "example:Tool-A1",
        # 'idref': "example:Tool-A1-ref",  # CAnnot set both an id and idref
        'name': "AwesomeTool(tm)",
        'type': [u('NIDS'), u('HIPS')],
        'description': {'structuring_format': 'HTML',
                        'value': '<p>An awesome tool!</p>'},

        'vendor': "Awesome Co.",
        'version': "1.0.0",
        'service_pack': 'N/A',

        'tool_hashes': [{'simple_hash_value': EMPTY_MD5,
                            'type': Hash.TYPE_MD5}],
    }


class TestHashList(unittest.TestCase):

    def test_round_trip(self):
        toolinfolist_list = [
                {'id': "example:Tool-A1", 'name': "Tool 1"},
                {'id': "example:Tool-A2", 'name': "Tool 2"},
            ]
        toolinfolist_list2 = cybox.test.round_trip_list(ToolInformationList,
                                                       toolinfolist_list)
        self.assertEqual(toolinfolist_list, toolinfolist_list2)


if __name__ == "__main__":
    unittest.main()
