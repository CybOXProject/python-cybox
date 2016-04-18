# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_driver_object as win_driver_binding
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.common import String, HexBinary, UnsignedLong


class DeviceObjectStruct(entities.Entity):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.DeviceObjectStructType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "DeviceObjectStructType"

    attached_device_name = fields.TypedField("Attached_Device_Name", String)
    attached_device_object = fields.TypedField("Attached_Device_Object", UnsignedLong)
    attached_to_device_name = fields.TypedField("Attached_To_Device_Name", String)
    attached_to_device_object = fields.TypedField("Attached_To_Device_Object", UnsignedLong)
    attached_to_driver_name = fields.TypedField("Attached_To_Driver_Name", String)
    attached_to_driver_object = fields.TypedField("Attached_To_Driver_Object", UnsignedLong)
    device_name = fields.TypedField("Device_Name", String)
    device_object = fields.TypedField("Device_Object", UnsignedLong)


class DeviceObjectList(entities.EntityList):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.DeviceObjectListType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "DeviceObjectListType"
    device_object_struct = fields.TypedField("Device_Object_Struct", DeviceObjectStruct, multiple=True)


class WinDriver(WinExecutableFile):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.WindowsDriverObjectType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "WindowsDriverObjectType"

    driver_init = fields.TypedField("Driver_Init", UnsignedLong)
    driver_name = fields.TypedField("Driver_Name", String)
    driver_object_address = fields.TypedField("Driver_Object_Address", HexBinary)
    driver_start_io = fields.TypedField("Driver_Start_IO", HexBinary)
    driver_unload = fields.TypedField("Driver_Unload", HexBinary)
    device_object_list = fields.TypedField("Device_Object_List", DeviceObjectList)

    image_base = fields.TypedField("Image_Base", HexBinary)
    image_size = fields.TypedField("Image_Size", HexBinary)

    irp_mj_cleanup = fields.TypedField("IRP_MJ_CLEANUP", UnsignedLong)
    irp_mj_close = fields.TypedField("IRP_MJ_CLOSE", UnsignedLong)
    irp_mj_create = fields.TypedField("IRP_MJ_CREATE", UnsignedLong)
    irp_mj_create_mailslot = fields.TypedField("IRP_MJ_CREATE_MAILSLOT", UnsignedLong)
    irp_mj_create_named_pipe = fields.TypedField("IRP_MJ_CREATE_NAMED_PIPE", UnsignedLong)
    irp_mj_device_change = fields.TypedField("IRP_MJ_DEVICE_CHANGE", UnsignedLong)
    irp_mj_device_control = fields.TypedField("IRP_MJ_DEVICE_CONTROL", UnsignedLong)
    irp_mj_directory_control = fields.TypedField("IRP_MJ_DIRECTORY_CONTROL", UnsignedLong)
    irp_mj_file_system_control = fields.TypedField("IRP_MJ_FILE_SYSTEM_CONTROL", UnsignedLong)
    irp_mj_flush_buffers = fields.TypedField("IRP_MJ_FLUSH_BUFFERS", UnsignedLong)
    irp_mj_internal_device_control = fields.TypedField("IRP_MJ_INTERNAL_DEVICE_CONTROL", UnsignedLong)
    irp_mj_lock_control = fields.TypedField("IRP_MJ_LOCK_CONTROL", UnsignedLong)
    irp_mj_pnp = fields.TypedField("IRP_MJ_PNP", UnsignedLong)
    irp_mj_power = fields.TypedField("IRP_MJ_POWER", UnsignedLong)
    irp_mj_query_ea = fields.TypedField("IRP_MJ_QUERY_EA", UnsignedLong)
    irp_mj_query_information = fields.TypedField("IRP_MJ_QUERY_INFORMATION", UnsignedLong)
    irp_mj_query_quota = fields.TypedField("IRP_MJ_QUERY_QUOTA", UnsignedLong)
    irp_mj_query_security = fields.TypedField("IRP_MJ_QUERY_SECURITY", UnsignedLong)
    irp_mj_query_volume_information = fields.TypedField("IRP_MJ_QUERY_VOLUME_INFORMATION", UnsignedLong)
    irp_mj_read = fields.TypedField("IRP_MJ_READ", UnsignedLong)
    irp_mj_set_ea = fields.TypedField("IRP_MJ_SET_EA", UnsignedLong)
    irp_mj_set_information = fields.TypedField("IRP_MJ_SET_INFORMATION", UnsignedLong)
    irp_mj_set_quota = fields.TypedField("IRP_MJ_SET_QUOTA", UnsignedLong)
    irp_mj_set_security = fields.TypedField("IRP_MJ_SET_SECURITY", UnsignedLong)
    irp_mj_set_volume_information = fields.TypedField("IRP_MJ_SET_VOLUME_INFORMATION", UnsignedLong)
    irp_mj_shutdown = fields.TypedField("IRP_MJ_SHUTDOWN", UnsignedLong)
    irp_mj_system_control = fields.TypedField("IRP_MJ_SYSTEM_CONTROL", UnsignedLong)
    irp_mj_write = fields.TypedField("IRP_MJ_WRITE", UnsignedLong)
