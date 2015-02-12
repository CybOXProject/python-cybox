# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.device_object as device_binding
from cybox.common import ObjectProperties, String, StructuredText


class Device(ObjectProperties):
    _binding = device_binding
    _binding_class = device_binding.DeviceObjectType
    _namespace = "http://cybox.mitre.org/objects#DeviceObject-2"
    _XSI_NS = "DeviceObj"
    _XSI_TYPE = "DeviceObjectType"

    description = cybox.TypedField("Description", StructuredText)
    device_type = cybox.TypedField("Device_Type", String)
    manufacturer = cybox.TypedField("Manufacturer", String)
    model = cybox.TypedField("Model", String)
    serial_number = cybox.TypedField("Serial_Number", String)
    firmware_version = cybox.TypedField("Firmware_Version", String)
    # system_details TODO: add PlatformSpecificationType
