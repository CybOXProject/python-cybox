# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import base64
import bz2
import zlib

import cybox
import cybox.bindings.image_file_object as image_binding
from cybox.common import ObjectProperties, String, Integer, PositiveInteger
from cybox.objects.file_object import File


class ImageFile(File):
    _binding = image_binding
    _namespace = 'http://cybox.mitre.org/objects#ImageFileObject-1'
    _XSI_NS = "ImageFileObj"
    _XSI_TYPE = "ImageFileObjectType"

    image_is_compressed = cybox.TypedField("image_is_compressed")
    image_file_format = cybox.TypedField("Image_File_Format", String)
    image_height = cybox.TypedField("Image_Height", Integer)
    image_width = cybox.TypedField("Image_Width", Integer)
    bits_per_pixel = cybox.TypedField("Bits_Per_Pixel", PositiveInteger)
    compression_algorithm = cybox.TypedField("Compression_Algorithm", String)
