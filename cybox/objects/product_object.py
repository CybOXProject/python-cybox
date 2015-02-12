# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.product_object as product_binding
from cybox.common import ObjectProperties, String


class Product(ObjectProperties):
    _binding = product_binding
    _binding_class = product_binding.ProductObjectType
    _namespace = 'http://cybox.mitre.org/objects#ProductObject-2'
    _XSI_NS = 'ProductObj'
    _XSI_TYPE = "ProductObjectType"

    edition = cybox.TypedField("Edition", String)
    language = cybox.TypedField("Language", String)
    product = cybox.TypedField("Product", String)
    update = cybox.TypedField("Update", String)
    vendor = cybox.TypedField("Vendor", String)
    version = cybox.TypedField("Version", String)
