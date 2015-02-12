# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.code_object as code_binding
from cybox.common import ObjectProperties, String, HexBinary, StructuredText,\
                         MeasureSource, PlatformSpecification, ExtractedFeatures,\
                         DigitalSignatureList

class CodeSegmentXOR(String):
    _binding = code_binding
    _binding_class = code_binding.CodeSegmentXORType
    _namespace = "http://cybox.mitre.org/objects#CodeObject-2"

    xor_pattern = cybox.TypedField('xor_pattern')

class TargetedPlatforms(cybox.EntityList):
    _binding = code_binding
    _binding_class = code_binding.TargetedPlatformsType
    _binding_var = "Targeted_Platform"
    _contained_type = PlatformSpecification
    _namespace = "http://cybox.mitre.org/objects#CodeObject-2"

class Code(ObjectProperties):
    _binding = code_binding
    _binding_class = code_binding.CodeObjectType
    _namespace = "http://cybox.mitre.org/objects#CodeObject-2"
    _XSI_NS = "CodeObj"
    _XSI_TYPE = "CodeObjectType"

    description = cybox.TypedField('Description', StructuredText)
    type_ = cybox.TypedField('Type', String)
    purpose = cybox.TypedField('Purpose', String)
    code_language = cybox.TypedField('Code_Language', String)
    targeted_platforms = cybox.TypedField('Targeted_Platforms', TargetedPlatforms)
    processor_family = cybox.TypedField('Processor_Family', String, multiple=True)
    discovery_method = cybox.TypedField('Discovery_Method', MeasureSource)
    start_address = cybox.TypedField('Start_Address', HexBinary)
    code_segment = cybox.TypedField('Code_Segment', String)
    code_segment_xor = cybox.TypedField('Code_Segment_XOR', CodeSegmentXOR)
    digital_signatures = cybox.TypedField('Digital_Signatures', DigitalSignatureList)
    extracted_features = cybox.TypedField('Extracted_Features', ExtractedFeatures)
