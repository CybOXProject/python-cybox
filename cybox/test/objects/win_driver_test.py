# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_driver_object import WinDriver

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinDriver(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsDriverObjectType"
    klass = WinDriver

    _full_dict = {
        'driver_init': 123,
        'driver_name': "A driver name",
        'driver_object_address': "abcde12345",
        'driver_start_io': "abcce4321",
        'driver_unload': "ab3234dec",
        'image_base': "12345abc",
        'image_size': "12ff",
        'irp_mj_cleanup': 1L,
        'irp_mj_close': 2L,
        'irp_mj_create': 3L,
        'irp_mj_create_mailslot': 4L,
        'irp_mj_create_named_pipe': 5L,
        'irp_mj_device_change': 6L,
        'irp_mj_device_control': 7L,
        'irp_mj_directory_control': 8L,
        'irp_mj_file_system_control': 9L,
        'irp_mj_flush_buffers': 11L,
        'irp_mj_internal_device_control': 12L,
        'irp_mj_lock_control': 13L,
        'irp_mj_pnp': 14L,
        'irp_mj_power': 15L,
        'irp_mj_query_ea': 16L,
        'irp_mj_query_information': 17L,
        'irp_mj_query_quota': 22L,
        'irp_mj_query_security': 23L,
        'irp_mj_query_volume_information': 24L,
        'irp_mj_read': 25L,
        'irp_mj_set_ea': 26L,
        'irp_mj_set_information': 27L,
        'irp_mj_set_quota': 33L,
        'irp_mj_set_security': 34L,
        'irp_mj_set_volume_information': 35L,
        'irp_mj_shutdown': 36L,
        'irp_mj_system_control': 37L,
        'irp_mj_write': 38L,   
        #'device_object_list' = TypedField("Device_Object_List", DeviceObjectList)
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
