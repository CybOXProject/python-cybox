# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_driver_object import WinDriver

from cybox.compat import long
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
        'irp_mj_cleanup': long(1),
        'irp_mj_close': long(2),
        'irp_mj_create': long(3),
        'irp_mj_create_mailslot': long(4),
        'irp_mj_create_named_pipe': long(5),
        'irp_mj_device_change': long(6),
        'irp_mj_device_control': long(7),
        'irp_mj_directory_control': long(8),
        'irp_mj_file_system_control': long(9),
        'irp_mj_flush_buffers': long(11),
        'irp_mj_internal_device_control': long(12),
        'irp_mj_lock_control': long(13),
        'irp_mj_pnp': long(14),
        'irp_mj_power': long(15),
        'irp_mj_query_ea': long(16),
        'irp_mj_query_information': long(17),
        'irp_mj_query_quota': long(22),
        'irp_mj_query_security': long(23),
        'irp_mj_query_volume_information': long(24),
        'irp_mj_read': long(25),
        'irp_mj_set_ea': long(26),
        'irp_mj_set_information': long(27),
        'irp_mj_set_quota': long(33),
        'irp_mj_set_security': long(34),
        'irp_mj_set_volume_information': long(35),
        'irp_mj_shutdown': long(36),
        'irp_mj_system_control': long(37),
        'irp_mj_write': long(38),
        #TODO: add 'device_object_list'
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
