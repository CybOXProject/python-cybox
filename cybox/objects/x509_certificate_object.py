# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.x509_certificate_object as x509_certificate_binding
from cybox.common import ObjectProperties, String, Integer, DateTime, NonNegativeInteger

class Validity(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.ValidityType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    not_before = cybox.TypedField("Not_Before", DateTime)
    not_after = cybox.TypedField("Not_After", DateTime)

class RSAPublicKey(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.RSAPublicKeyType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    modulus = cybox.TypedField("Modulus", String)
    exponent = cybox.TypedField("Exponent", Integer)

class SubjectPublicKey(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.SubjectPublicKeyType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    public_key_algorithm = cybox.TypedField("Public_Key_Algorithm", String)
    rsa_public_key = cybox.TypedField("RSA_Public_Key", RSAPublicKey)

class X509V3Extensions(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509V3ExtensionsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    basic_constraints = cybox.TypedField("Basic_Constraints", String)
    name_constraints = cybox.TypedField("Name_Constraints", String)
    policy_constraints = cybox.TypedField("Policy_Constraints", String)
    key_usage = cybox.TypedField("Key_Usage", String)
    extended_key_usage = cybox.TypedField("Extended_Key_Usage", String)
    subject_key_identifier = cybox.TypedField("Subject_Key_Identifier", String)
    authority_key_identifier = cybox.TypedField("Authority_Key_Identifier", String)
    subject_alternative_name = cybox.TypedField("Subject_Alternative_Name", String)
    issuer_alternative_name = cybox.TypedField("Issuer_Alternative_Name", String)
    subject_directory_attributes = cybox.TypedField("Subject_Directory_Attributes", String)
    crl_distribution_points = cybox.TypedField("CRL_Distribution_Points", String)
    inhibit_any_policy = cybox.TypedField("Inhibit_Any_Policy", NonNegativeInteger)
    private_key_usage_period = cybox.TypedField("Private_Key_Usage_Period", Validity)
    certificate_policies = cybox.TypedField("Certificate_Policies", String)
    policy_mappings = cybox.TypedField("Policy_Mappings", String)

class X509NonStandardExtensions(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509NonStandardExtensionsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    netscape_comment = cybox.TypedField("Netscape_Comment", String)
    netscape_certificate_type = cybox.TypedField("Netscape_Certificate_Type", String)
    old_authority_key_identifier = cybox.TypedField("Old_Authority_Key_Identifier", String)
    old_primary_key_attributes = cybox.TypedField("Old_Primary_Key_Attributes", String)

class X509Cert(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateContentsType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    version = cybox.TypedField("Version", Integer)
    serial_number = cybox.TypedField("Serial_Number", String)
    signature_algorithm = cybox.TypedField("Signature_Algorithm", String)
    issuer = cybox.TypedField("Issuer", String)
    validity = cybox.TypedField("Validity", Validity)
    subject = cybox.TypedField("Subject", String)
    subject_public_key = cybox.TypedField("Subject_Public_Key", SubjectPublicKey)
    standard_extensions = cybox.TypedField("Standard_Extensions", X509V3Extensions)
    non_standard_extensions = cybox.TypedField("Non_Standard_Extensions", X509NonStandardExtensions)

class X509CertificateSignature(cybox.Entity):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateSignatureType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'

    signature_algorithm = cybox.TypedField("Signature_Algorithm", String)
    signature = cybox.TypedField("Signature", String)

class X509Certificate(ObjectProperties):
    _binding = x509_certificate_binding
    _binding_class = x509_certificate_binding.X509CertificateObjectType
    _namespace = 'http://cybox.mitre.org/objects#X509CertificateObject-2'
    _XSI_NS = "X509CertificateObj"
    _XSI_TYPE = "X509CertificateObjectType"

    certificate = cybox.TypedField("Certificate", X509Cert)
    raw_certificate = cybox.TypedField("Raw_Certificate", String)
    certificate_signature = cybox.TypedField("Certificate_Signature", X509CertificateSignature)
