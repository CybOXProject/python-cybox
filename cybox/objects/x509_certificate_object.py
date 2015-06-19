# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.x509_certificate_object as x509_certificate_binding
from cybox.common import ObjectProperties, String, Integer, DateTime, NonNegativeInteger


class Validity(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.ValidityType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    not_before = fields.TypedField("Not_Before", DateTime)
    not_after = fields.TypedField("Not_After", DateTime)

class RSAPublicKey(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.RSAPublicKeyType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    modulus = fields.TypedField("Modulus", String)
    exponent = fields.TypedField("Exponent", Integer)


class SubjectPublicKey(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.SubjectPublicKeyType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    public_key_algorithm = fields.TypedField("Public_Key_Algorithm", String)
    rsa_public_key = fields.TypedField("RSA_Public_Key", RSAPublicKey)


class X509V3Extensions(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509V3ExtensionsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    basic_constraints = fields.TypedField("Basic_Constraints", String)
    name_constraints = fields.TypedField("Name_Constraints", String)
    policy_constraints = fields.TypedField("Policy_Constraints", String)
    key_usage = fields.TypedField("Key_Usage", String)
    extended_key_usage = fields.TypedField("Extended_Key_Usage", String)
    subject_key_identifier = fields.TypedField("Subject_Key_Identifier", String)
    authority_key_identifier = fields.TypedField("Authority_Key_Identifier", String)
    subject_alternative_name = fields.TypedField("Subject_Alternative_Name", String)
    issuer_alternative_name = fields.TypedField("Issuer_Alternative_Name", String)
    subject_directory_attributes = fields.TypedField("Subject_Directory_Attributes", String)
    crl_distribution_points = fields.TypedField("CRL_Distribution_Points", String)
    inhibit_any_policy = fields.TypedField("Inhibit_Any_Policy", NonNegativeInteger)
    private_key_usage_period = fields.TypedField("Private_Key_Usage_Period", Validity)
    certificate_policies = fields.TypedField("Certificate_Policies", String)
    policy_mappings = fields.TypedField("Policy_Mappings", String)


class X509NonStandardExtensions(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509NonStandardExtensionsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    netscape_comment = fields.TypedField("Netscape_Comment", String)
    netscape_certificate_type = fields.TypedField("Netscape_Certificate_Type", String)
    old_authority_key_identifier = fields.TypedField("Old_Authority_Key_Identifier", String)
    old_primary_key_attributes = fields.TypedField("Old_Primary_Key_Attributes", String)


class X509Cert(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateContentsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    version = fields.TypedField("Version", Integer)
    serial_number = fields.TypedField("Serial_Number", String)
    signature_algorithm = fields.TypedField("Signature_Algorithm", String)
    issuer = fields.TypedField("Issuer", String)
    validity = fields.TypedField("Validity", Validity)
    subject = fields.TypedField("Subject", String)
    subject_public_key = fields.TypedField("Subject_Public_Key", SubjectPublicKey)
    standard_extensions = fields.TypedField("Standard_Extensions", X509V3Extensions)
    non_standard_extensions = fields.TypedField("Non_Standard_Extensions", X509NonStandardExtensions)


class X509CertificateSignature(entities.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateSignatureType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    signature_algorithm = fields.TypedField("Signature_Algorithm", String)
    signature = fields.TypedField("Signature", String)


class X509Certificate(ObjectProperties):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateObjectType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'
    _XSI_NS = "X509CertificateObj"
    _XSI_TYPE = "X509CertificateObjectType"

    certificate = fields.TypedField("Certificate", X509Cert)
    raw_certificate = fields.TypedField("Raw_Certificate", String)
    certificate_signature = fields.TypedField("Certificate_Signature", X509CertificateSignature)
