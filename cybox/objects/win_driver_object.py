import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_driver_object_1_2 as win_driver_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Driver:
    def __init__(self):
        pass
        
    def object_from_dict(self, driver_attributes):
        driver_obj = win_driver_binding.WindowsDriverObjectType()
        driver_obj.set_anyAttributes_({'xsi:type' : 'WinDriverObj:WindowsDriverObjectType'})
        
        for key, value in driver_attributes.items():
            if key == 'driver_name' and utils.test_value(value):
                driver_obj.set_Driver_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'driver_init' and utils.test_value(value):
                driver_obj.set_Driver_Init(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'driver_object_address' and utils.test_value(value):
                driver_obj.set_Driver_Object_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'driver_start_io' and utils.test_value(value):
                driver_obj.set_Driver_Start_IO(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'driver_unload' and utils.test_value(value):
                driver_obj.set_Driver_Unload(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'image_base' and utils.test_value(value):
                driver_obj.set_Image_Base(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'image_size' and utils.test_value(value):
                driver_obj.set_Image_Size(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), value))
            elif key == 'irp_mj_cleanup' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CLEANUP(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_close' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CLOSE(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_create' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CREATE(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_create_mailslot' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CREATE_MAILSLOT(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_create_named_pipe' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CREATE_NAMED_PIPE(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_device_change' and utils.test_value(value):
                driver_obj.set_IRP_MJ_DEVICE_CHANGE(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_device_control' and utils.test_value(value):
                driver_obj.set_IRP_MJ_DEVICE_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_directory_control' and utils.test_value(value):
                driver_obj.set_IRP_MJ_DIRECTORY_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_file_system' and utils.test_value(value):
                driver_obj.set_IRP_MJ_FILE_SYSTEM_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_flush_buffers' and utils.test_value(value):
                driver_obj.set_IRP_MJ_FLUSH_BUFFERS(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_internal_device_control' and utils.test_value(value):
                driver_obj.set_IRP_MJ_INTERNAL_DEVICE_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_lock_control' and utils.test_value(value):
                driver_obj.set_IRP_MJ_LOCK_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_pnp' and utils.test_value(value):
                driver_obj.set_IRP_MJ_PNP(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_power' and utils.test_value(value):
                driver_obj.set_IRP_MJ_POWER(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_query_ea' and utils.test_value(value):
                driver_obj.set_IRP_MJ_QUERY_EA(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_query_information' and utils.test_value(value):
                driver_obj.set_IRP_MJ_QUERY_INFORMATION(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_query_quota' and utils.test_value(value):
                driver_obj.set_IRP_MJ_QUERY_QUOTA(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_query_security' and utils.test_value(value):
                driver_obj.set_IRP_MJ_QUERY_SECURITY(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_query_volume_information' and utils.test_value(value):
                driver_obj.set_IRP_MJ_QUERY_VOLUME_INFORMATION(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_read' and utils.test_value(value):
                driver_obj.set_IRP_MJ_READ(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_set_ea' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SET_EA(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_set_information' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SET_INFORMATION(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_set_quota' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SET_QUOTA(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_set_security' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SET_SECURITY(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_volume_information' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SET_VOLUME_INFORMATION(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_shutdown' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SHUTDOWN(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_system_control' and utils.test_value(value):
                driver_obj.set_IRP_MJ_SYSTEM_CONTROL(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_writep' and utils.test_value(value):
                driver_obj.set_IRP_MJ_WRITE(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'irp_mj_cleanup' and utils.test_value(value):
                driver_obj.set_IRP_MJ_CLEANUP(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            elif key == 'device_object_list':
                device_list = win_driver_binding.DeviceObjectListType()
                for device_list_item in value:
                    for dev_key, dev_value in device_list_item.items():
                        device = win_driver_binding.DeviceObjectStructType()
                        if dev_key == 'attached_device_name':
                            device.set_Attached_Device_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), dev_value))
                        elif dev_key == 'attached_device_object':
                            device.set_Attached_Device_Object(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), dev_value))
                        elif dev_key == 'attached_to_device_name':
                            device.set_Attached_To_Device_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), dev_value))
                        elif dev_key == 'attached_to_device_object':
                            device.set_Attached_To_Device_Object(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), dev_value))
                        elif dev_key == 'attached_to_driver_name':
                            device.set_Attached_To_Driver_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), dev_value))
                        elif dev_key == 'attached_to_driver_object':
                            device.set_Attached_To_Driver_Object(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), dev_value))
                        if dev_key == 'device_name':
                            device.set_Device_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), dev_value))
                        elif dev_key == 'device_object':
                            device.set_Device_Object(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), dev_value))
                driver_obj.set_Device_Object_List(device_list)
                
        return driver_obj
