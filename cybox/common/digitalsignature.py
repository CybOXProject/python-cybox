# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.cybox_common as common_types_binding
from cybox.common import String

class DigitalSignature(cybox.Entity):
    def __init__(self):
        self.signature_exists = None
        self.signature_verified = None
        self.certificate_issuer = None
        self.certificate_subject = None
        self.signature_description = None

    def to_obj(self):
        digital_signature_obj = common_types_binding.DigitalSignatureInfoType()

        if self.signature_exists is not None: digital_signature_obj.set_signature_exists(self.signature_exists)
        if self.signature_verified is not None: digital_signature_obj.set_signature_verified(self.signature_verified)
        if self.certificate_issuer is not None: digital_signature_obj.set_certificate_issuer(self.certificate_issuer.to_obj())
        if self.certificate_subject is not None: digital_signature_obj.set_certificate_subject(self.certificate_subject.to_obj())
        if self.signature_description is not None: digital_signature_obj.set_signature_description(self.signature_description.to_obj())

        return digital_signature_obj

    def to_dict(self):
        digital_signature_dict = {}

        if self.signature_exists is not None: digital_signature_dict['signature_exists'] = self.signature_exists
        if self.signature_verified is not None: digital_signature_dict['signature_verified'] = self.signature_verified
        if self.certificate_issuer is not None: digital_signature_dict['certificate_issuer'] = self.certificate_issuer.to_dict()
        if self.certificate_subject is not None: digital_signature_dict['certificate_subject'] = self.certificate_subject.to_dict()
        if self.signature_description is not None: digital_signature_dict['signature_description'] = self.signature_description.to_dict()

        return digital_signature_dict

    @staticmethod
    def from_dict(digital_signature_dict):
        if not digital_signature_dict:
            return None

        digital_signature_ = DigitalSignature()
        digital_signature_.signature_exists = digital_signature_dict.get('signature_exists')
        digital_signature_.signature_verified = digital_signature_dict.get('signature_verified')
        digital_signature_.certificate_issuer = String.from_dict(digital_signature_dict.get('certificate_issuer'))
        digital_signature_.certificate_subject = String.from_dict(digital_signature_dict.get('certificate_subject'))
        digital_signature_.signature_description = String.from_dict(digital_signature_dict.get('signature_description'))

        return digital_signature_

    @staticmethod
    def from_obj(digital_signature_obj):
        if not digital_signature_obj:
            return None

        digital_signature_ = DigitalSignature()
        digital_signature_.signature_exists = digital_signature_obj.get_signature_exists()
        digital_signature_.signature_verified = digital_signature_obj.get_signature_verified()
        digital_signature_.certificate_issuer = String.from_obj(digital_signature_obj.get_Certificate_Issuer())
        digital_signature_.certificate_subject = String.from_obj(digital_signature_obj.get_Certificate_Subject())
        digital_signature_.signature_description = String.from_obj(digital_signature_obj.get_Signature_Description())

        return digital_signature_

class DigitalSignatureList(cybox.Entity):
    def __init__(self):
        self.digital_signatures = []

    def add_digital_signature(self, digital_signature):
        self.digital_signatures.append(digital_signature)

    def to_obj(self):
        digital_signatures_obj = common_types_binding.DigitalSignaturesType()

        for digital_signature in self.digital_signatures:
            digital_signatures_obj.add_Digital_Signature(digital_signature.to_obj())

        return digital_signatures_obj

    def to_list(self):
        return [x.to_dict() for x in self.digital_signatures]

    @staticmethod
    def from_list(digital_signatures_list):
        if not digital_signatures_list:
            return None

        digital_signature_list_ = DigitalSignatureList()
        digital_signature_list_.digital_signatures = [x.from_dict() for x in digital_signatures_list]

        return digital_signature_list_

    @staticmethod
    def from_obj(digital_signatures_obj):
        if not digital_signatures_obj:
            return None

        digital_signature_list_ = DigitalSignatureList()
        digital_signature_list_.digital_signatures = [x.from_obj() for x in digital_signatures_obj.get_Digital_Signature()]

        return digital_signature_list_
