# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import String


class DigitalSignature(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DigitalSignatureInfoType
    _namespace = 'http://cybox.mitre.org/common-2'

    signature_exists = fields.TypedField("signature_exists")
    signature_verified = fields.TypedField("signature_verified")
    certificate_issuer = fields.TypedField("Certificate_Issuer", String)
    certificate_subject = fields.TypedField("Certificate_Subject", String)
    signature_description = fields.TypedField("Signature_Description", String)


class DigitalSignatureList(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.DigitalSignaturesType
    _namespace = 'http://cybox.mitre.org/common-2'
    digital_signature = fields.TypedField("Digital_Signature", DigitalSignature, multiple=True)