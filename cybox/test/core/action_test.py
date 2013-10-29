# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.core import Action
from cybox.test import EntityTestCase


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


#TODO: Test AssociateObjects and ActionRelationships


if __name__ == "__main__":
    unittest.main()
