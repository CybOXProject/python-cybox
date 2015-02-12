# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import String


class DigitalSignature(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.DigitalSignatureInfoType
    _namespace = 'http://cybox.mitre.org/common-2'

    signature_exists = cybox.TypedField("signature_exists")
    signature_verified = cybox.TypedField("signature_verified")
    certificate_issuer = cybox.TypedField("Certificate_Issuer", String)
    certificate_subject = cybox.TypedField("Certificate_Subject", String)
    signature_description = cybox.TypedField("Signature_Description", String)


class DigitalSignatureList(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.DigitalSignaturesType
    _binding_var = "Digital_Signature"
    _contained_type = DigitalSignature
    _namespace = 'http://cybox.mitre.org/common-2'
