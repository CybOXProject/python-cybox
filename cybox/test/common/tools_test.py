import unittest

from cybox.common import Hash, ToolInformation
import cybox.test
from cybox.test.common.hash_test import EMPTY_MD5


class TestToolInformation(unittest.TestCase):

    def test_round_trip(self):
        info_dict = {
                        'id': "example:Tool-A1",
                        'idref': "example:Tool-A1-ref",
                        'name': "AwesomeTool(tm)",
                        'type': ['NIDS', 'HIPS'],
                        'description': {'structuring_format': 'HTML',
                                        'value': '<p>An awesome tool!</p>'},

                        'vendor': "Awesome Co.",
                        'version': "1.0.0",
                        'service_pack': 'N/A',

                        'tool_hashes': [{'simple_hash_value': EMPTY_MD5,
                                         'type': Hash.TYPE_MD5}],
                    }
        info_dict2 = cybox.test.round_trip_dict(ToolInformation, info_dict)
        self.assertEqual(info_dict, info_dict2)


if __name__ == "__main__":
    unittest.main()
