import unittest

from cybox.objects.uri_object import URI
from cybox.objects.whois_object import WhoisEntry
import cybox.test


class TestWhois(unittest.TestCase, cybox.test.objects.ObjectTestCase):
    object_type = "WhoisObjectType"
    klass = WhoisEntry

    def test_round_trip(self):
        whois_dict = {
                        'domain_name': {'value': "www.google.com",
                                        'type': URI.TYPE_DOMAIN,},
                        'domain_id': 'test_id',
                     }

        whois_dict2 = cybox.test.round_trip_dict(WhoisEntry, whois_dict)
        cybox.test.assert_equal_ignore(whois_dict, whois_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
