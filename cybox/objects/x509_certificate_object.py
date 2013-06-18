# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.x509_certificate_object as x509_certificate_binding
from cybox.common import ObjectProperties, String, Integer, DateTime, NonNegativeInteger

class X509Certificate(ObjectProperties):
    _XSI_NS = "X509CertificateObj"
    _XSI_TYPE = "X509CertificateObjectType"

    def __init__(self):
        super(X509Certificate, self).__init__()
        self.certificate = None
        self.certificate_signature = None

    def to_obj(self):
        x509_certificate_obj = x509_certificate_binding.X509CertificateObjectType()
        super(X509Certificate, self).to_obj(x509_certificate_obj)

        if self.certificate is not None: x509_certificate_obj.set_Certificate(self.certificate.to_obj())
        if self.certificate_signature is not None: x509_certificate_obj.set_Certificate_Signature(self.certificate_signature.to_obj())

        return x509_certificate_obj

    def to_dict(self):
        x509_certificate_dict = {}
        super(X509Certificate, self).to_dict(x509_certificate_dict)

        if self.certificate is not None: x509_certificate_dict['certificate'] = self.certificate.to_dict()
        if self.certificate_signature is not None: x509_certificate_dict['certificate_signature'] = self.certificate_signature.to_dict()

        return x509_certificate_dict

    @staticmethod
    def from_dict(x509_certificate_dict):
        if not x509_certificate_dict:
            return None
        x509_certificate_ = X509Certificate()
        x509_certificate_.certificate = X509Cert.from_dict(x509_certificate_dict.get('certificate'))
        x509_certificate_.certificate_signature = X509CertificateSignature.from_dict(x509_certificate_dict.get('certificate_signature'))

        return x509_certificate_

    @staticmethod
    def from_obj(x509_certificate_obj):
        if not x509_certificate_obj:
            return None
        x509_certificate_ = X509Certificate()
        x509_certificate_.certificate = X509Cert.from_obj(x509_certificate_obj.get_Certificate())
        x509_certificate_.certificate_signature = X509CertificateSignature.from_obj(x509_certificate_obj.get_Certificate_Signature())

        return x509_certificate_

class X509Cert(cybox.Entity):
    def __init__(self):
        super(X509Cert, self).__init__()
        self.version = None
        self.serial_number = None
        self.signature_algorithm = None
        self.issuer = None
        self.validity = None
        self.subject = None
        self.subject_public_key = None
        self.standard_extensions = None
        self.non_standard_extensions = None

    def to_obj(self):
        x509_cert_obj = x509_certificate_binding.X509CertificateType()
        if self.version is not None : x509_cert_obj.set_Version(self.version.to_obj())
        if self.serial_number is not None : x509_cert_obj.set_Serial_Number(self.serial_number.to_obj())
        if self.signature_algorithm is not None : x509_cert_obj.set_Signature_Algorithm(self.signature_algorithm.to_obj())
        if self.issuer is not None : x509_cert_obj.set_Issuer(self.issuer.to_obj())
        if self.validity is not None : x509_cert_obj.set_Validity(self.validity.to_obj())
        if self.subject is not None : x509_cert_obj.set_Subject(self.subject.to_obj())
        if self.subject_public_key is not None : x509_cert_obj.set_Subject_Public_Key(self.subject_public_key.to_obj())
        if self.standard_extensions is not None : x509_cert_obj.set_Standard_Extensions(self.standard_extensions.to_obj())
        if self.non_standard_extensions is not None : x509_cert_obj.set_Non_Standard_Extensions(self.non_standard_extensions.to_obj())
        return x509_cert_obj

    def to_dict(self):
        x509_cert_dict = {}
        if self.version is not None : x509_cert_dict['version'] = self.version.to_dict()
        if self.serial_number is not None : x509_cert_dict['serial_number'] = self.serial_number.to_dict()
        if self.signature_algorithm is not None : x509_cert_dict['signature_algorithm'] = self.signature_algorithm.to_dict()
        if self.issuer is not None : x509_cert_dict['issuer'] = self.issuer.to_dict()
        if self.validity is not None : x509_cert_dict['validity'] = self.validity.to_dict()
        if self.subject is not None : x509_cert_dict['subject'] = self.subject.to_dict()
        if self.subject_public_key is not None : x509_cert_dict['subject_public_key'] = self.subject_public_key.to_dict()
        if self.standard_extensions is not None : x509_cert_dict['standard_extensions'] = self.standard_extensions.to_dict()
        if self.non_standard_extensions is not None : x509_cert_dict['non_standard_extensions'] = self.non_standard_extensions.to_dict()
        return x509_cert_dict

    @staticmethod
    def from_dict(x509_cert_dict):
        if not x509_cert_dict:
            return None
        x509_cert_ = X509Cert()
        x509_cert_.version = String.from_dict(x509_cert_dict.get('version'))
        x509_cert_.serial_number = String.from_dict(x509_cert_dict.get('serial_number'))
        x509_cert_.signature_algorithm = String.from_dict(x509_cert_dict.get('signature_algorithm'))
        x509_cert_.issuer = String.from_dict(x509_cert_dict.get('issuer'))
        x509_cert_.validity = Validity.from_dict(x509_cert_dict.get('validity'))
        x509_cert_.subject = String.from_dict(x509_cert_dict.get('subject'))
        x509_cert_.subject_public_key = SubjectPublicKey.from_dict(x509_cert_dict.get('subject_public_key'))
        x509_cert_.standard_extensions = X509V3Extensions.from_dict(x509_cert_dict.get('standard_extensions'))
        x509_cert_.non_standard_extensions = X509NonStandardExtensions.from_dict(x509_cert_dict.get('non_standard_extensions'))
        return x509_cert_

    @staticmethod
    def from_obj(x509_cert_obj):
        if not x509_cert_obj:
            return None
        x509_cert_ = X509Cert()
        x509_cert_.version = String.from_obj(x509_cert_obj.get_Version())
        x509_cert_.serial_number = String.from_obj(x509_cert_obj.get_Serial_Number())
        x509_cert_.signature_algorithm = String.from_obj(x509_cert_obj.get_Signature_Algorithm())
        x509_cert_.issuer = String.from_obj(x509_cert_obj.get_Issuer())
        x509_cert_.validity = Validity.from_obj(x509_cert_obj.get_Validity())
        x509_cert_.subject = String.from_obj(x509_cert_obj.get_Subject())
        x509_cert_.subject_public_key = SubjectPublicKey.from_obj(x509_cert_obj.get_Subject_Public_Key())
        x509_cert_.standard_extensions = X509V3Extensions.from_obj(x509_cert_obj.get_Standard_Extensions())
        x509_cert_.non_standard_extensions = X509NonStandardExtensions.from_obj(x509_cert_obj.get_Non_Standard_Extensions())
        return x509_cert_

class SubjectPublicKey(cybox.Entity):
    def __init__(self):
        super(SubjectPublicKey, self).__init__()
        self.public_key_algorithm = None
        self.rsa_public_key = None

    def to_obj(self):
        subject_public_key_obj = x509_certificate_binding.SubjectPublicKeyType()
        if self.public_key_algorithm is not None : subject_public_key_obj.set_Public_Key_Algorithm(self.public_key_algorithm.to_obj())
        if self.rsa_public_key is not None : subject_public_key_obj.set_RSA_Public_Key(self.rsa_public_key.to_obj())
        return subject_public_key_obj

    def to_dict(self):
        subject_public_key_dict = {}
        if self.public_key_algorithm is not None : subject_public_key_dict['public_key_algorithm'] = self.public_key_algorithm.to_dict()
        if self.rsa_public_key is not None : subject_public_key_dict['rsa_public_key'] = self.rsa_public_key.to_dict()
        return subject_public_key_dict

    @staticmethod
    def from_dict(subject_public_key_dict):
        if not subject_public_key_dict:
            return None
        subject_public_key_ = SubjectPublicKey()
        subject_public_key_.public_key_algorithm = String.from_dict(subject_public_key_dict.get('public_key_algorithm'))
        subject_public_key_.rsa_public_key = RSAPublicKey.from_dict(subject_public_key_dict.get('rsa_public_key'))
        return subject_public_key_

    @staticmethod
    def from_obj(subject_public_key_obj):
        if not subject_public_key_obj:
            return None
        subject_public_key_ = SubjectPublicKey()
        subject_public_key_.public_key_algorithm = String.from_obj(subject_public_key_obj.get_Public_Key_Algorithm())
        subject_public_key_.rsa_public_key = RSAPublicKey.from_obj(subject_public_key_obj.get_RSA_Public_Key())
        return subject_public_key_

class RSAPublicKey(cybox.Entity):
    def __init__(self):
        super(RSAPublicKey, self).__init__()
        self.modulus = None
        self.exponent = None

    def to_obj(self):
        rsa_public_key_obj = x509_certificate_binding.RSAPublicKeyType()
        if self.modulus is not None : rsa_public_key_obj.set_Modulus(self.modulus.to_obj())
        if self.exponent is not None : rsa_public_key_obj.set_Exponent(self.exponent.to_obj())
        return rsa_public_key_obj

    def to_dict(self):
        rsa_public_key_dict = {}
        if self.modulus is not None : subject_public_key_dict['modulus'] = self.modulus.to_dict()
        if self.exponent is not None : subject_public_key_dict['exponent'] = self.exponent.to_dict()
        return rsa_public_key_dict

    @staticmethod
    def from_dict(rsa_public_key_dict):
        if not rsa_public_key_dict:
            return None
        rsa_public_key_ = RSAPublicKey()
        rsa_public_key_.modulus = String.from_dict(rsa_public_key_dict.get('modulus'))
        rsa_public_key_.exponent = Integer.from_dict(rsa_public_key_dict.get('exponent'))
        return rsa_public_key_

    @staticmethod
    def from_obj(rsa_public_key_obj):
        if not rsa_public_key_obj:
            return None
        rsa_public_key_ = RSAPublicKey()
        rsa_public_key_.modulus = String.from_obj(rsa_public_key_obj.get_Modulus())
        rsa_public_key_.exponent = Integer.from_obj(rsa_public_key_obj.get_Exponent())
        return rsa_public_key_

class Validity(cybox.Entity):
    def __init__(self):
        super(Validity, self).__init__()
        self.not_before = None
        self.not_after = None

    def to_obj(self):
        validity_obj = x509_certificate_binding.ValidityType()
        if self.not_before is not None : validity_obj.set_Not_Before(self.not_before.to_obj())
        if self.not_after is not None : validity_obj.set_Not_After(self.not_after.to_obj())
        return validity_obj

    def to_dict(self):
        validity_dict = {}
        if self.not_before is not None : validity_dict['not_before'] = self.not_before.to_dict()
        if self.not_after is not None : validity_dict['not_after'] = self.not_after.to_dict()
        return validity_obj

    @staticmethod
    def from_dict(validity_dict):
        if not validity_dict:
            return None
        validity_ = Validity()
        validity_.not_after = DateTime.from_dict(validity_dict.get('not_after'))
        validity_.not_before = DateTime.from_dict(validity_dict.get('not_before'))
        return validity_

    @staticmethod
    def from_obj(validity_obj):
        if not validity_obj:
            return None
        validity_ = Validity()
        validity_.not_after = DateTime.from_obj(validity_obj.get_Not_After())
        validity_.not_before = DateTime.from_obj(validity_obj.get_Not_Before())
        return validity_

class X509V3Extensions(cybox.Entity):
    def __init__(self):
        super(X509V3Extensions, self).__init__()
        self.basic_constraints = None
        self.name_constraints = None
        self.policy_constraints = None
        self.key_usage = None
        self.extended_key_usage = None
        self.subject_key_identifier = None
        self.authority_key_identifier = None
        self.subject_alternative_name = None
        self.issuer_alternative_name = None
        self.subject_directory_attributes = None
        self.crl_distribution_points = None
        self.inhibit_any_policy = None
        self.private_key_usage_period = None
        self.certificate_policies = None
        self.policy_mappings = None

    def to_obj(self):
        x509_v3_extensions_obj = x509_certificate_binding.X509V3ExtensionsType()
        if self.basic_constraints is not None : x509_v3_extensions_obj.set_Basic_Constraints(self.basic_constraints.to_obj())
        if self.name_constraints is not None : x509_v3_extensions_obj.set_Name_Constraints(self.name_constraints.to_obj())
        if self.policy_constraints is not None : x509_v3_extensions_obj.set_Policy_Constraints(self.policy_constraints.to_obj())
        if self.key_usage is not None : x509_v3_extensions_obj.set_Key_Usage(self.key_usage.to_obj())
        if self.extended_key_usage is not None : x509_v3_extensions_obj.set_Extended_Key_Usage(self.extended_key_usage.to_obj())
        if self.subject_key_identifier is not None : x509_v3_extensions_obj.set_Subject_Key_Identifier(self.subject_key_identifier.to_obj())
        if self.authority_key_identifier is not None : x509_v3_extensions_obj.set_Authority_Key_Identifier(self.authority_key_identifier.to_obj())
        if self.subject_alternative_name is not None : x509_v3_extensions_obj.set_Subject_Alternative_Name(self.subject_alternative_name.to_obj())
        if self.issuer_alternative_name is not None : x509_v3_extensions_obj.set_Issuer_Alternative_Name(self.issuer_alternative_name.to_obj())
        if self.subject_directory_attributes is not None : x509_v3_extensions_obj.set_Subject_Directory_Attributes(self.subject_directory_attributes.to_obj())
        if self.crl_distribution_points is not None : x509_v3_extensions_obj.set_CRL_Distribution_Points(self.crl_distribution_points.to_obj())
        if self.inhibit_any_policy is not None : x509_v3_extensions_obj.set_Inhibit_Any_Policy(self.inhibit_any_policy.to_obj())
        if self.private_key_usage_period is not None : x509_v3_extensions_obj.set_Private_Key_Usage_Period(self.private_key_usage_period.to_obj())
        if self.certificate_policies is not None : x509_v3_extensions_obj.set_Certificate_Policies(self.certificate_policies.to_obj())
        if self.policy_mappings is not None : x509_v3_extensions_obj.set_Policy_Mappings(self.policy_mappings.to_obj())
        return x509_v3_extensions_obj

    def to_dict(self):
        x509_v3_extensions_dict = {}
        if self.basic_constraints is not None : x509_v3_extensions_dict['basic_constraints'] = self.basic_constraints.to_dict()
        if self.name_constraints is not None : x509_v3_extensions_dict['name_constraints'] = self.name_constraints.to_dict()
        if self.policy_constraints is not None : x509_v3_extensions_dict['policy_constraints'] = self.policy_constraints.to_dict()
        if self.key_usage is not None : x509_v3_extensions_dict['key_usage'] = self.key_usage.to_dict()
        if self.extended_key_usage is not None : x509_v3_extensions_dict['extended_key_usage'] = self.extended_key_usage.to_dict()
        if self.subject_key_identifier is not None : x509_v3_extensions_dict['subject_key_identifier'] = self.subject_key_identifier.to_dict()
        if self.authority_key_identifier is not None : x509_v3_extensions_dict['authority_key_identifier'] = self.authority_key_identifier.to_dict()
        if self.subject_alternative_name is not None : x509_v3_extensions_dict['subject_alternative_name'] = self.subject_alternative_name.to_dict()
        if self.issuer_alternative_name is not None : x509_v3_extensions_dict['issuer_alternative_name'] = self.issuer_alternative_name.to_dict()
        if self.subject_directory_attributes is not None : x509_v3_extensions_dict['subject_directory_attributes'] = self.subject_directory_attributes.to_dict()
        if self.crl_distribution_points is not None : x509_v3_extensions_dict['crl_distribution_points'] = self.crl_distribution_points.to_dict()
        if self.inhibit_any_policy is not None : x509_v3_extensions_dict['inhibit_any_policy'] = self.inhibit_any_policy.to_dict()
        if self.private_key_usage_period is not None : x509_v3_extensions_dict['private_key_usage_period'] = self.private_key_usage_period.to_dict()
        if self.certificate_policies is not None : x509_v3_extensions_dict['certificate_policies'] = self.certificate_policies.to_dict()
        if self.policy_mappings is not None :x509_v3_extensions_dict['policy_mappings'] = self.policy_mappings.to_dict()
        return x509_v3_extensions_dict

    @staticmethod
    def from_dict(x509_v3_extensions_dict):
        if not x509_v3_extensions_dict:
            return None
        x509_v3_extensions_ = X509V3Extensions()
        x509_v3_extensions_.basic_constraints = String.from_dict(x509_v3_extensions_dict.get('basic_constraints'))
        x509_v3_extensions_.name_constraints = String.from_dict(x509_v3_extensions_dict.get('name_constraints'))
        x509_v3_extensions_.policy_constraints = String.from_dict(x509_v3_extensions_dict.get('policy_constraints'))
        x509_v3_extensions_.key_usage = String.from_dict(x509_v3_extensions_dict.get('key_usage'))
        x509_v3_extensions_.extended_key_usage = String.from_dict(x509_v3_extensions_dict.get('extended_key_usage'))
        x509_v3_extensions_.subject_key_identifier = String.from_dict(x509_v3_extensions_dict.get('subject_key_identifier'))
        x509_v3_extensions_.authority_key_identifier = String.from_dict(x509_v3_extensions_dict.get('authority_key_identifier'))
        x509_v3_extensions_.subject_alternative_name = String.from_dict(x509_v3_extensions_dict.get('subject_alternative_name'))
        x509_v3_extensions_.issuer_alternative_name = String.from_dict(x509_v3_extensions_dict.get('issuer_alternative_name'))
        x509_v3_extensions_.subject_directory_attributes = String.from_dict(x509_v3_extensions_dict.get('subject_directory_attributes'))
        x509_v3_extensions_.crl_distribution_points = String.from_dict(x509_v3_extensions_dict.get('crl_distribution_points'))
        x509_v3_extensions_.inhibit_any_policy = NonNegativeInteger.from_dict(x509_v3_extensions_dict.get('inhibit_any_policy'))
        x509_v3_extensions_.private_key_usage_period = Validity.from_dict(x509_v3_extensions_dict.get('private_key_usage_period'))
        x509_v3_extensions_.certificate_policies = String.from_dict(x509_v3_extensions_dict.get('certificate_policies'))
        x509_v3_extensions_.policy_mappings = String.from_dict(x509_v3_extensions_dict.get('policy_mappings'))
        return x509_v3_extensions_

    @staticmethod
    def from_obj(x509_v3_extensions_obj):
        if not x509_v3_extensions_obj:
            return None
        x509_v3_extensions_ = X509V3Extensions()
        x509_v3_extensions_.basic_constraints = String.from_obj(x509_v3_extensions_obj.get_Basic_Constraints())
        x509_v3_extensions_.name_constraints = String.from_obj(x509_v3_extensions_obj.get_Name_Constraints())
        x509_v3_extensions_.policy_constraints = String.from_obj(x509_v3_extensions_obj.get_Policy_Constraints())
        x509_v3_extensions_.key_usage = String.from_obj(x509_v3_extensions_obj.get_Key_Usage())
        x509_v3_extensions_.extended_key_usage = String.from_obj(x509_v3_extensions_obj.get_Extended_Key_Usage())
        x509_v3_extensions_.subject_key_identifier = String.from_obj(x509_v3_extensions_obj.get_Subject_Key_Identifier())
        x509_v3_extensions_.authority_key_identifier = String.from_obj(x509_v3_extensions_obj.get_Authority_Key_Identifier())
        x509_v3_extensions_.subject_alternative_name = String.from_obj(x509_v3_extensions_obj.get_Subject_Alternative_Name())
        x509_v3_extensions_.issuer_alternative_name = String.from_obj(x509_v3_extensions_obj.get_Issuer_Alternative_Name())
        x509_v3_extensions_.subject_directory_attributes = String.from_obj(x509_v3_extensions_obj.get_Subject_Directory_Attributes())
        x509_v3_extensions_.crl_distribution_points = String.from_obj(x509_v3_extensions_obj.get_CRL_Distribution_Points())
        x509_v3_extensions_.inhibit_any_policy = NonNegativeInteger.from_obj(x509_v3_extensions_obj.get_Inhibit_Any_Policy())
        x509_v3_extensions_.private_key_usage_period = Validity.from_obj(x509_v3_extensions_obj.get_Private_Key_Usage_Period())
        x509_v3_extensions_.certificate_policies = String.from_obj(x509_v3_extensions_obj.get_Certificate_Policies())
        x509_v3_extensions_.policy_mappings = String.from_obj(x509_v3_extensions_obj.get_Policy_Mappings())
        return x509_v3_extensions_

class X509NonStandardExtensions(cybox.Entity):
    def __init__(self):
        super(X509NonStandardExtensions, self).__init__()
        self.netscape_comment = None
        self.netscape_certificate_type = None
        self.old_authority_key_identifier = None
        self.old_primary_key_attributes = None

    def to_obj(self):
        x509_non_standard_extensions_obj = x509_certificate_binding.X509NonStandardExtensionsType()
        if self.netscape_comment is not None : x509_non_standard_extensions_obj.set_Netscape_Comment(self.netscape_comment.to_obj())
        if self.netscape_certificate_type is not None : x509_non_standard_extensions_obj.set_Netscape_Certificate_Type(self.netscape_certificate_type.to_obj())
        if self.old_authority_key_identifier is not None : x509_non_standard_extensions_obj.set_Old_Authority_Key_Identifier(self.old_authority_key_identifier.to_obj())
        if self.old_primary_key_attributes is not None : x509_non_standard_extensions_obj.set_Old_Primary_Key_Attributes(self.old_primary_key_attributes.to_obj())
        return x509_non_standard_extensions_obj

    def to_dict(self):
        x509_non_standard_extensions_dict = {}
        if self.netscape_comment is not None : x509_non_standard_extensions_dict['netscape_comment'] = self.netscape_comment.to_dict()
        if self.netscape_certificate_type is not None : x509_non_standard_extensions_dict['netscape_certificate_type'] = self.netscape_certificate_type.to_dict()
        if self.old_authority_key_identifier is not None : x509_non_standard_extensions_dict['old_authority_key_identifier'] = self.old_authority_key_identifier.to_dict()
        if self.old_primary_key_attributes is not None : x509_non_standard_extensions_dict['old_primary_key_attributes'] = self.old_primary_key_attributes.to_dict()
        return x509_non_standard_extensions_dict

    @staticmethod
    def from_dict(x509_non_standard_extensions_dict):
        if not x509_non_standard_extensions_dict:
            return None
        x509_non_standard_extensions_ = X509NonStandardExtensions()
        x509_non_standard_extensions_.netscape_comment = String.from_dict(x509_non_standard_extensions_dict.get('netscape_comment'))
        x509_non_standard_extensions_.netscape_certificate_type = String.from_dict(x509_non_standard_extensions_dict.get('netscape_certificate_type'))
        x509_non_standard_extensions_.old_authority_key_identifier = String.from_dict(x509_non_standard_extensions_dict.get('old_authority_key_identifier'))
        x509_non_standard_extensions_.old_primary_key_attributes = String.from_dict(x509_non_standard_extensions_dict.get('old_primary_key_attributes'))
        return x509_non_standard_extensions_

    @staticmethod
    def from_obj(x509_non_standard_extensions_obj):
        if not x509_non_standard_extensions_obj:
            return None
        x509_non_standard_extensions_ = X509NonStandardExtensions()
        x509_non_standard_extensions_.netscape_comment = String.from_obj(x509_non_standard_extensions_obj.get_Netscape_Comment())
        x509_non_standard_extensions_.netscape_certificate_type = String.from_obj(x509_non_standard_extensions_obj.get_Netscape_Certificate_Type())
        x509_non_standard_extensions_.old_authority_key_identifier = String.from_obj(x509_non_standard_extensions_obj.get_Old_Authority_Key_Identifier())
        x509_non_standard_extensions_.old_primary_key_attributes = String.from_obj(x509_non_standard_extensions_obj.get_Old_Primary_Key_Attributes())
        return x509_non_standard_extensions_

class X509CertificateSignature(cybox.Entity):
    def __init__(self):
        super(X509CertificateSignature, self).__init__()
        self.signature_algorithm = None
        self.signature = None

    def to_obj(self):
        x509_certificate_signature_obj = x509_certificate_binding.X509CertificateSignatureType()
        if self.signature_algorithm is not None : x509_certificate_signature_obj.set_Signature_Algorithm(self.signature_algorithm.to_obj())
        if self.signature is not None : x509_certificate_signature_obj.set_Signature(self.signature.to_obj())
        return x509_certificate_signature_obj

    def to_dict(self):
        x509_certificate_signature_dict = {}
        if self.signature_algorithm is not None : x509_certificate_signature_dict['signature_algorithm'] = self.signature_algorithm.to_dict()
        if self.signature is not None : x509_certificate_signature_dict['signature'] = self.signature.to_dict()
        return x509_certificate_signature_dict

    @staticmethod
    def from_dict(x509_certificate_signature_dict):
        if not x509_certificate_signature_dict:
            return None
        x509_certificate_signature_ = X509CertificateSignature()
        x509_certificate_signature_.signature_algorithm = String.from_dict(x509_certificate_signature_dict.get('signature_algorithm'))
        x509_certificate_signature_.signature = String.from_dict(x509_certificate_signature_dict.get('signature'))
        return x509_certificate_signature_

    @staticmethod
    def from_obj(x509_certificate_signature_obj):
        if not x509_certificate_signature_obj:
            return None
        x509_certificate_signature_ = X509CertificateSignature()
        x509_certificate_signature_.signature_algorithm = String.from_obj(x509_certificate_signature_obj.get_Signature_Algorithm())
        x509_certificate_signature_.signature = String.from_obj(x509_certificate_signature_obj.get_Signature())
        return x509_certificate_signature_