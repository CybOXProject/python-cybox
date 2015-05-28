# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import copy
import unittest

from mixbox.vendor.six import u

from cybox.bindings.cybox_core import parseString
from cybox.core import Action, ActionRelationship
from cybox.common import VocabString
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
        'type': u("Modify"),
        'name': u("Modify File"),
        'description': {'value': "An action!", 'structuring_format': "Text"},
        'action_aliases': ['an alias', 'another_alias'],
        'action_arguments': [
            {
                'argument_name': u("infile"),
                'argument_value': "/tmp/somefile.txt",
            },
            {
                'argument_name': u("outfile"),
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
                'type': u("Followed_By"),
                'action_reference': [{'action_id': "example:Action-2"}]
            }
        ],
        'frequency': {'rate': 1.0},
    }

    # Test that should be fixed by
    # https://github.com/CybOXProject/python-cybox/pull/236
    def test_tzinfo_copy(self):
        action = Action()
        action.timestamp = "2015-03-28T16:39:28.127296+03:00"
        action_xml = action.to_xml(encoding=None)

        action2 = Action.from_obj(parseString(action_xml))
        action2_copy = copy.deepcopy(action2)
        self.assertEqual(action_xml, action2_copy.to_xml(encoding=None))


class TestActionRelationship(EntityTestCase, unittest.TestCase):
    klass = ActionRelationship

    _full_dict = {
        'type': u("Add"),
        'action_reference': [
            {'action_id': "example:Action-1"},
            {'action_id': "example:Action-3"},
        ]
    }

    def test_nonstandard_type_vocab(self):
        ar = ActionRelationship()
        ar.type = VocabString(u("AddedMultipleTimes"))
        ar.type.vocab_reference = "http://example.com/action-types/"
        ar.type.xsi_type = None
        ar2 = round_trip(ar)
        self.assertEqual(ar.to_dict(), ar2.to_dict())


#TODO: Test AssociateObjects


if __name__ == "__main__":
    unittest.main()
