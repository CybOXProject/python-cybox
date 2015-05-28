# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.win_task_object import WinTask
from cybox.test.common.hash_test import TEST_HASH_LIST
from cybox.test.objects import ObjectTestCase


class TestWinTask(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsTaskObjectType"
    klass = WinTask

    _full_dict = {
        'status': u("SCHED_S_TASK_RUNNING"),
        'priority': u("NORMAL_PRIORITY_CLASS"),
        'name': u("Find all the malware"),
        'application_name': u("Windows Defender"),
        'parameters': u("C:\\\\"),
        'flags': u("/DEEP"),
        'account_name': u("SYSTEM"),
        'account_run_level': u("ARunLevel"),
        'account_logon_type': u("S4U"),
        'creator': u("TheCreator"),
        'creation_date': "2012-04-26T15:30:45-05:00",
        'most_recent_run_time': "2013-06-26T10:20:30-05:00",
        'exit_code': long(0),
        'max_run_time': long(15000),
        'next_run_time': "2013-06-27T10:20:30-05:00",
        'action_list': [
            {
                'action_type': u("TASK_ACTION_SEND_EMAIL"),
                'action_id': u("Action #1"),
                'iemailaction': {
                    'raw_body': u("Task Completed!"),
                    'xsi:type': "EmailMessageObjectType",
                },
            },
            {
                'action_type': u("TASK_ACTION_COM_HANDLER"),
                'action_id': u("Action #2"),
                'icomhandleraction': {
                    'com_data': u("COMDATA"),
                    'com_class_id': u("CLASSID")
                },
            },
            {
                'action_type': u("TASK_ACTION_EXEC"),
                'action_id': u("Action #3"),
                'iexecaction': {
                    'exec_arguments': u("ARGS"),
                    'exec_program_path': u("C:\\\\temp\\\\cmd.exe"),
                    'exec_working_directory': u("C:\\\\temp\\\\"),
                    'exec_program_hashes': TEST_HASH_LIST,
                },
            },
            {
                'action_type': u("TASK_ACTION_SHOW_MESSAGE"),
                'action_id': u("Action #4"),
                'ishowmessageaction': {
                    'show_message_body': u("Task completed."),
                    'show_message_title': u("Task Complete"),
                },
            },
        ],
        'trigger_list': [
            {
                'trigger_begin': "2013-05-05T01:02:03-04:00",
                'trigger_delay': u("PT5M"),
                'trigger_end': "2013-05-05T01:02:10-04:00",
                'trigger_frequency':
                    u("TASK_TIME_TRIGGER_DAILY"),
                'trigger_max_run_time': u("PT1M"),
                'trigger_session_change_type':
                    u("TASK_REMOTE_CONNECT"),
                #TODO: Add trigger_type
            },
            {
                'trigger_max_run_time': u("PT10M"),
            },
        ],
        'comment': u("This is a useless task."),
        'working_directory': u("C:\\\\WINDOWS\\\\system32\\\\"),
        'work_item_data': u("AAAAn34lq21b4m2nbvoi345"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
