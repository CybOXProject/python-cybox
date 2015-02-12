# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_driver_object as win_driver_binding
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.common import ObjectProperties, String, HexBinary, UnsignedLong
from cybox import TypedField

class DeviceObjectStruct(cybox.Entity):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.DeviceObjectStructType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "DeviceObjectStructType"
    
    attached_device_name = TypedField("Attached_Device_Name", String)
    attached_device_object = TypedField("Attached_Device_Object", UnsignedLong)
    attached_to_device_name = TypedField("Attached_To_Device_Name", String)
    attached_to_device_object = TypedField("Attached_To_Device_Object", UnsignedLong)
    attached_to_driver_name = TypedField("Attached_To_Driver_Name", String)
    attached_to_driver_object = TypedField("Attached_To_Driver_Object", UnsignedLong)
    device_name = TypedField("Device_Name", String)
    device_object = TypedField("Device_Object", UnsignedLong)

class DeviceObjectList(cybox.EntityList):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.DeviceObjectListType
    _binding_var = "Device_Object_Struct"
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "DeviceObjectListType"
    _contained_type = DeviceObjectStruct

class WinDriver(WinExecutableFile):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.WindowsDriverObjectType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-3"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "WindowsDriverObjectType"

    driver_init = TypedField("Driver_Init", UnsignedLong)
    driver_name = TypedField("Driver_Name", String)
    driver_object_address = TypedField("Driver_Object_Address", HexBinary)
    driver_start_io = TypedField("Driver_Start_IO", HexBinary)
    driver_unload = TypedField("Driver_Unload", HexBinary)
    device_object_list = TypedField("Device_Object_List", DeviceObjectList)
    
    image_base = TypedField("Image_Base", HexBinary)
    image_size = TypedField("Image_Size", HexBinary)
    
    irp_mj_cleanup = TypedField("IRP_MJ_CLEANUP", UnsignedLong)
    irp_mj_close = TypedField("IRP_MJ_CLOSE", UnsignedLong)
    irp_mj_create = TypedField("IRP_MJ_CREATE", UnsignedLong)
    irp_mj_create_mailslot = TypedField("IRP_MJ_CREATE_MAILSLOT", UnsignedLong)
    irp_mj_create_named_pipe = TypedField("IRP_MJ_CREATE_NAMED_PIPE", UnsignedLong)
    irp_mj_device_change = TypedField("IRP_MJ_DEVICE_CHANGE", UnsignedLong)
    irp_mj_device_control = TypedField("IRP_MJ_DEVICE_CONTROL", UnsignedLong)
    irp_mj_directory_control = TypedField("IRP_MJ_DIRECTORY_CONTROL", UnsignedLong)
    irp_mj_file_system_control = TypedField("IRP_MJ_FILE_SYSTEM_CONTROL", UnsignedLong)
    irp_mj_flush_buffers = TypedField("IRP_MJ_FLUSH_BUFFERS", UnsignedLong)
    irp_mj_internal_device_control = TypedField("IRP_MJ_INTERNAL_DEVICE_CONTROL", UnsignedLong)
    irp_mj_lock_control = TypedField("IRP_MJ_LOCK_CONTROL", UnsignedLong)
    irp_mj_pnp = TypedField("IRP_MJ_PNP", UnsignedLong)
    irp_mj_power = TypedField("IRP_MJ_POWER", UnsignedLong)
    irp_mj_query_ea = TypedField("IRP_MJ_QUERY_EA", UnsignedLong)
    irp_mj_query_information = TypedField("IRP_MJ_QUERY_INFORMATION", UnsignedLong)
    irp_mj_query_quota = TypedField("IRP_MJ_QUERY_QUOTA", UnsignedLong)
    irp_mj_query_security = TypedField("IRP_MJ_QUERY_SECURITY", UnsignedLong)
    irp_mj_query_volume_information = TypedField("IRP_MJ_QUERY_VOLUME_INFORMATION", UnsignedLong)
    irp_mj_read = TypedField("IRP_MJ_READ", UnsignedLong)
    irp_mj_set_ea = TypedField("IRP_MJ_SET_EA", UnsignedLong)
    irp_mj_set_information = TypedField("IRP_MJ_SET_INFORMATION", UnsignedLong)
    irp_mj_set_quota = TypedField("IRP_MJ_SET_QUOTA", UnsignedLong)
    irp_mj_set_security = TypedField("IRP_MJ_SET_SECURITY", UnsignedLong)
    irp_mj_set_volume_information = TypedField("IRP_MJ_SET_VOLUME_INFORMATION", UnsignedLong)
    irp_mj_shutdown = TypedField("IRP_MJ_SHUTDOWN", UnsignedLong)
    irp_mj_system_control = TypedField("IRP_MJ_SYSTEM_CONTROL", UnsignedLong)
    irp_mj_write = TypedField("IRP_MJ_WRITE", UnsignedLong)
    
    def __init__(self):
        super(WinDriver, self).__init__()
