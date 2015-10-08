# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.product_object as product_binding
from cybox.common import ObjectProperties, String
from cybox.common.object_properties import ObjectPropertiesFactory


class Product(ObjectProperties):
    _binding = product_binding
    _binding_class = product_binding.ProductObjectType
    _namespace = 'http://cybox.mitre.org/objects#ProductObject-2'
    _XSI_NS = 'ProductObj'
    _XSI_TYPE = "ProductObjectType"

    edition = fields.TypedField("Edition", String)
    language = fields.TypedField("Language", String)
    product = fields.TypedField("Product", String)
    update = fields.TypedField("Update", String)
    vendor = fields.TypedField("Vendor", String)
    version = fields.TypedField("Version", String)
    device_details = fields.TypedField("Device_Details", ObjectProperties, factory=ObjectPropertiesFactory)
