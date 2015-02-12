# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.core import Action, ActionRelationship, ActionType
from cybox.test import EntityTestCase, round_trip


class TestAction(EntityTestCase, unittest.TestCase):
    klass = Action

    _full_dict = {
        'id': "example:Action-1",
        'idref': "example:Action-2",
        'ordinal_position': 42,
        'action_status': "Success",
        'context': "Host",
        'timestamp': "2013-10-24T09:54:13",
        'type': u"Modify",
        'name': u"Modify File",
        'description': {'value': "An action!", 'structuring_format': "Text"},
        'action_aliases': ['an alias', 'another_alias'],
        'action_arguments': [
            {
                'argument_name': u"infile",
                'argument_value': "/tmp/somefile.txt",
            },
            {
                'argument_name': u"outfile",
                'argument_value': "/tmp/someotherfile.txt",
            }
        ],
        'discovery_method': {'name': "A tool"},
        'associated_objects': [
            {
                'idref': "example:File-1",
            }
        ],
        'relationships': [
            {
                'type': u"Followed_By",
                'action_reference': [{'action_id': "example:Action-2"}]
            }
        ],
        'frequency': {'rate': 1.0},
    }


class TestActionRelationship(EntityTestCase, unittest.TestCase):
    klass = ActionRelationship

    _full_dict = {
        'type': u"Add",
        'action_reference': [
            {'action_id': "example:Action-1"},
            {'action_id': "example:Action-3"},
        ]
    }

    def test_nonstandard_type_vocab(self):
        ar = ActionRelationship()
        ar.type = ActionType(u"AddedMultipleTimes")
        ar.type.vocab_reference = "http://example.com/action-types/"
        ar.type.xsi_type = None
        ar2 = round_trip(ar)
        self.assertEqual(ar.to_dict(), ar2.to_dict())


#TODO: Test AssociateObjects


if __name__ == "__main__":
    unittest.main()
