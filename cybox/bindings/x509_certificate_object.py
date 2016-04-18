# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class X509CertificateContentsType(GeneratedsSuper):
    """The X509CertificateContentsType type represents the contents of an X.509
    certificate, including items such as issuer, subject, and
    others."""

    subclass = None
    superclass = None
    def __init__(self, Version=None, Serial_Number=None, Signature_Algorithm=None, Issuer=None, Validity=None, Subject=None, Subject_Public_Key=None, Standard_Extensions=None, Non_Standard_Extensions=None):
        self.Version = Version
        self.Serial_Number = Serial_Number
        self.Signature_Algorithm = Signature_Algorithm
        self.Issuer = Issuer
        self.Validity = Validity
        self.Subject = Subject
        self.Subject_Public_Key = Subject_Public_Key
        self.Standard_Extensions = Standard_Extensions
        self.Non_Standard_Extensions = Non_Standard_Extensions
    def factory(*args_, **kwargs_):
        if X509CertificateContentsType.subclass:
            return X509CertificateContentsType.subclass(*args_, **kwargs_)
        else:
            return X509CertificateContentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Serial_Number(self): return self.Serial_Number
    def set_Serial_Number(self, Serial_Number): self.Serial_Number = Serial_Number
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Signature_Algorithm(self): return self.Signature_Algorithm
    def set_Signature_Algorithm(self, Signature_Algorithm): self.Signature_Algorithm = Signature_Algorithm
    def get_Issuer(self): return self.Issuer
    def set_Issuer(self, Issuer): self.Issuer = Issuer
    def get_Validity(self): return self.Validity
    def set_Validity(self, Validity): self.Validity = Validity
    def get_Subject(self): return self.Subject
    def set_Subject(self, Subject): self.Subject = Subject
    def get_Subject_Public_Key(self): return self.Subject_Public_Key
    def set_Subject_Public_Key(self, Subject_Public_Key): self.Subject_Public_Key = Subject_Public_Key
    def get_Standard_Extensions(self): return self.Standard_Extensions
    def set_Standard_Extensions(self, Standard_Extensions): self.Standard_Extensions = Standard_Extensions
    def get_Non_Standard_Extensions(self): return self.Non_Standard_Extensions
    def set_Non_Standard_Extensions(self, Non_Standard_Extensions): self.Non_Standard_Extensions = Non_Standard_Extensions
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Serial_Number is not None or
            self.Signature_Algorithm is not None or
            self.Issuer is not None or
            self.Validity is not None or
            self.Subject is not None or
            self.Subject_Public_Key is not None or
            self.Standard_Extensions is not None or
            self.Non_Standard_Extensions is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateContentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='X509CertificateContentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='X509CertificateContentsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateContentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            self.Version.export(lwrite, level, 'X509CertificateObj:', name_='Version', pretty_print=pretty_print)
        if self.Serial_Number is not None:
            self.Serial_Number.export(lwrite, level, 'X509CertificateObj:', name_='Serial_Number', pretty_print=pretty_print)
        if self.Signature_Algorithm is not None:
            self.Signature_Algorithm.export(lwrite, level, 'X509CertificateObj:', name_='Signature_Algorithm', pretty_print=pretty_print)
        if self.Issuer is not None:
            self.Issuer.export(lwrite, level, 'X509CertificateObj:', name_='Issuer', pretty_print=pretty_print)
        if self.Validity is not None:
            self.Validity.export(lwrite, level, 'X509CertificateObj:', name_='Validity', pretty_print=pretty_print)
        if self.Subject is not None:
            self.Subject.export(lwrite, level, 'X509CertificateObj:', name_='Subject', pretty_print=pretty_print)
        if self.Subject_Public_Key is not None:
            self.Subject_Public_Key.export(lwrite, level, 'X509CertificateObj:', name_='Subject_Public_Key', pretty_print=pretty_print)
        if self.Standard_Extensions is not None:
            self.Standard_Extensions.export(lwrite, level, 'X509CertificateObj:', name_='Standard_Extensions', pretty_print=pretty_print)
        if self.Non_Standard_Extensions is not None:
            self.Non_Standard_Extensions.export(lwrite, level, 'X509CertificateObj:', name_='Non_Standard_Extensions', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Version':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Serial_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Serial_Number(obj_)
        elif nodeName_ == 'Signature_Algorithm':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature_Algorithm(obj_)
        elif nodeName_ == 'Issuer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Issuer(obj_)
        elif nodeName_ == 'Validity':
            obj_ = ValidityType.factory()
            obj_.build(child_)
            self.set_Validity(obj_)
        elif nodeName_ == 'Subject':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject(obj_)
        elif nodeName_ == 'Subject_Public_Key':
            obj_ = SubjectPublicKeyType.factory()
            obj_.build(child_)
            self.set_Subject_Public_Key(obj_)
        elif nodeName_ == 'Standard_Extensions':
            obj_ = X509V3ExtensionsType.factory()
            obj_.build(child_)
            self.set_Standard_Extensions(obj_)
        elif nodeName_ == 'Non_Standard_Extensions':
            obj_ = X509NonStandardExtensionsType.factory()
            obj_.build(child_)
            self.set_Non_Standard_Extensions(obj_)
# end class X509CertificateContentsType

class X509CertificateSignatureType(GeneratedsSuper):
    """The X509CertificateSignatureType contains the signature and
    signature algorithm of this X.509 certificate."""

    subclass = None
    superclass = None
    def __init__(self, Signature_Algorithm=None, Signature=None):
        self.Signature_Algorithm = Signature_Algorithm
        self.Signature = Signature
    def factory(*args_, **kwargs_):
        if X509CertificateSignatureType.subclass:
            return X509CertificateSignatureType.subclass(*args_, **kwargs_)
        else:
            return X509CertificateSignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Signature_Algorithm(self): return self.Signature_Algorithm
    def set_Signature_Algorithm(self, Signature_Algorithm): self.Signature_Algorithm = Signature_Algorithm
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Signature(self): return self.Signature
    def set_Signature(self, Signature): self.Signature = Signature
    def hasContent_(self):
        if (
            self.Signature_Algorithm is not None or
            self.Signature is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateSignatureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='X509CertificateSignatureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='X509CertificateSignatureType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateSignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Signature_Algorithm is not None:
            self.Signature_Algorithm.export(lwrite, level, 'X509CertificateObj:', name_='Signature_Algorithm', pretty_print=pretty_print)
        if self.Signature is not None:
            self.Signature.export(lwrite, level, 'X509CertificateObj:', name_='Signature', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Signature_Algorithm':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature_Algorithm(obj_)
        elif nodeName_ == 'Signature':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Signature(obj_)
# end class X509CertificateSignatureType

class SubjectPublicKeyType(GeneratedsSuper):
    """The SubjectPublicKeyType is used to carry the public key and
    identify the algorithm with which the key is used."""

    subclass = None
    superclass = None
    def __init__(self, Public_Key_Algorithm=None, RSA_Public_Key=None):
        self.Public_Key_Algorithm = Public_Key_Algorithm
        self.RSA_Public_Key = RSA_Public_Key
    def factory(*args_, **kwargs_):
        if SubjectPublicKeyType.subclass:
            return SubjectPublicKeyType.subclass(*args_, **kwargs_)
        else:
            return SubjectPublicKeyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Public_Key_Algorithm(self): return self.Public_Key_Algorithm
    def set_Public_Key_Algorithm(self, Public_Key_Algorithm): self.Public_Key_Algorithm = Public_Key_Algorithm
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_RSA_Public_Key(self): return self.RSA_Public_Key
    def set_RSA_Public_Key(self, RSA_Public_Key): self.RSA_Public_Key = RSA_Public_Key
    def hasContent_(self):
        if (
            self.Public_Key_Algorithm is not None or
            self.RSA_Public_Key is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='SubjectPublicKeyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SubjectPublicKeyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='SubjectPublicKeyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='SubjectPublicKeyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Public_Key_Algorithm is not None:
            self.Public_Key_Algorithm.export(lwrite, level, 'X509CertificateObj:', name_='Public_Key_Algorithm', pretty_print=pretty_print)
        if self.RSA_Public_Key is not None:
            self.RSA_Public_Key.export(lwrite, level, 'X509CertificateObj:', name_='RSA_Public_Key', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Public_Key_Algorithm':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Public_Key_Algorithm(obj_)
        elif nodeName_ == 'RSA_Public_Key':
            obj_ = RSAPublicKeyType.factory()
            obj_.build(child_)
            self.set_RSA_Public_Key(obj_)
# end class SubjectPublicKeyType

class ValidityType(GeneratedsSuper):
    """The ValidityType type is the time interval during which the issuer
    warrants that it will maintain information about the status of
    the certificate."""

    subclass = None
    superclass = None
    def __init__(self, Not_Before=None, Not_After=None):
        self.Not_Before = Not_Before
        self.Not_After = Not_After
    def factory(*args_, **kwargs_):
        if ValidityType.subclass:
            return ValidityType.subclass(*args_, **kwargs_)
        else:
            return ValidityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Not_Before(self): return self.Not_Before
    def set_Not_Before(self, Not_Before): self.Not_Before = Not_Before
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Not_After(self): return self.Not_After
    def set_Not_After(self, Not_After): self.Not_After = Not_After
    def hasContent_(self):
        if (
            self.Not_Before is not None or
            self.Not_After is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='ValidityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ValidityType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='ValidityType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='ValidityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Not_Before is not None:
            self.Not_Before.export(lwrite, level, 'X509CertificateObj:', name_='Not_Before', pretty_print=pretty_print)
        if self.Not_After is not None:
            self.Not_After.export(lwrite, level, 'X509CertificateObj:', name_='Not_After', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Not_Before':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Not_Before(obj_)
        elif nodeName_ == 'Not_After':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Not_After(obj_)
# end class ValidityType

class RSAPublicKeyType(GeneratedsSuper):
    """The RSAPublicKeyType captures details of RSA public keys."""

    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None):
        self.Modulus = Modulus
        self.Exponent = Exponent
    def factory(*args_, **kwargs_):
        if RSAPublicKeyType.subclass:
            return RSAPublicKeyType.subclass(*args_, **kwargs_)
        else:
            return RSAPublicKeyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Modulus(self): return self.Modulus
    def set_Modulus(self, Modulus): self.Modulus = Modulus
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Exponent(self): return self.Exponent
    def set_Exponent(self, Exponent): self.Exponent = Exponent
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='RSAPublicKeyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RSAPublicKeyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='RSAPublicKeyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='RSAPublicKeyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            self.Modulus.export(lwrite, level, 'X509CertificateObj:', name_='Modulus', pretty_print=pretty_print)
        if self.Exponent is not None:
            self.Exponent.export(lwrite, level, 'X509CertificateObj:', name_='Exponent', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Modulus':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Modulus(obj_)
        elif nodeName_ == 'Exponent':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exponent(obj_)
# end class RSAPublicKeyType

class X509V3ExtensionsType(GeneratedsSuper):
    """The X509V3ExtensionsType captures the standard X509 V3 Extensions
    that may be used in X509 certificates. Based on RFC 3280,
    "Standard Extensions": http://www.ietf.org/rfc/rfc3280.txt"""

    subclass = None
    superclass = None
    def __init__(self, Basic_Constraints=None, Name_Constraints=None, Policy_Constraints=None, Key_Usage=None, Extended_Key_Usage=None, Subject_Key_Identifier=None, Authority_Key_Identifier=None, Subject_Alternative_Name=None, Issuer_Alternative_Name=None, Subject_Directory_Attributes=None, CRL_Distribution_Points=None, Inhibit_Any_Policy=None, Private_Key_Usage_Period=None, Certificate_Policies=None, Policy_Mappings=None):
        self.Basic_Constraints = Basic_Constraints
        self.Name_Constraints = Name_Constraints
        self.Policy_Constraints = Policy_Constraints
        self.Key_Usage = Key_Usage
        self.Extended_Key_Usage = Extended_Key_Usage
        self.Subject_Key_Identifier = Subject_Key_Identifier
        self.Authority_Key_Identifier = Authority_Key_Identifier
        self.Subject_Alternative_Name = Subject_Alternative_Name
        self.Issuer_Alternative_Name = Issuer_Alternative_Name
        self.Subject_Directory_Attributes = Subject_Directory_Attributes
        self.CRL_Distribution_Points = CRL_Distribution_Points
        self.Inhibit_Any_Policy = Inhibit_Any_Policy
        self.Private_Key_Usage_Period = Private_Key_Usage_Period
        self.Certificate_Policies = Certificate_Policies
        self.Policy_Mappings = Policy_Mappings
    def factory(*args_, **kwargs_):
        if X509V3ExtensionsType.subclass:
            return X509V3ExtensionsType.subclass(*args_, **kwargs_)
        else:
            return X509V3ExtensionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Basic_Constraints(self): return self.Basic_Constraints
    def set_Basic_Constraints(self, Basic_Constraints): self.Basic_Constraints = Basic_Constraints
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Name_Constraints(self): return self.Name_Constraints
    def set_Name_Constraints(self, Name_Constraints): self.Name_Constraints = Name_Constraints
    def get_Policy_Constraints(self): return self.Policy_Constraints
    def set_Policy_Constraints(self, Policy_Constraints): self.Policy_Constraints = Policy_Constraints
    def get_Key_Usage(self): return self.Key_Usage
    def set_Key_Usage(self, Key_Usage): self.Key_Usage = Key_Usage
    def get_Extended_Key_Usage(self): return self.Extended_Key_Usage
    def set_Extended_Key_Usage(self, Extended_Key_Usage): self.Extended_Key_Usage = Extended_Key_Usage
    def get_Subject_Key_Identifier(self): return self.Subject_Key_Identifier
    def set_Subject_Key_Identifier(self, Subject_Key_Identifier): self.Subject_Key_Identifier = Subject_Key_Identifier
    def get_Authority_Key_Identifier(self): return self.Authority_Key_Identifier
    def set_Authority_Key_Identifier(self, Authority_Key_Identifier): self.Authority_Key_Identifier = Authority_Key_Identifier
    def get_Subject_Alternative_Name(self): return self.Subject_Alternative_Name
    def set_Subject_Alternative_Name(self, Subject_Alternative_Name): self.Subject_Alternative_Name = Subject_Alternative_Name
    def get_Issuer_Alternative_Name(self): return self.Issuer_Alternative_Name
    def set_Issuer_Alternative_Name(self, Issuer_Alternative_Name): self.Issuer_Alternative_Name = Issuer_Alternative_Name
    def get_Subject_Directory_Attributes(self): return self.Subject_Directory_Attributes
    def set_Subject_Directory_Attributes(self, Subject_Directory_Attributes): self.Subject_Directory_Attributes = Subject_Directory_Attributes
    def get_CRL_Distribution_Points(self): return self.CRL_Distribution_Points
    def set_CRL_Distribution_Points(self, CRL_Distribution_Points): self.CRL_Distribution_Points = CRL_Distribution_Points
    def get_Inhibit_Any_Policy(self): return self.Inhibit_Any_Policy
    def set_Inhibit_Any_Policy(self, Inhibit_Any_Policy): self.Inhibit_Any_Policy = Inhibit_Any_Policy
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Private_Key_Usage_Period(self): return self.Private_Key_Usage_Period
    def set_Private_Key_Usage_Period(self, Private_Key_Usage_Period): self.Private_Key_Usage_Period = Private_Key_Usage_Period
    def get_Certificate_Policies(self): return self.Certificate_Policies
    def set_Certificate_Policies(self, Certificate_Policies): self.Certificate_Policies = Certificate_Policies
    def get_Policy_Mappings(self): return self.Policy_Mappings
    def set_Policy_Mappings(self, Policy_Mappings): self.Policy_Mappings = Policy_Mappings
    def hasContent_(self):
        if (
            self.Basic_Constraints is not None or
            self.Name_Constraints is not None or
            self.Policy_Constraints is not None or
            self.Key_Usage is not None or
            self.Extended_Key_Usage is not None or
            self.Subject_Key_Identifier is not None or
            self.Authority_Key_Identifier is not None or
            self.Subject_Alternative_Name is not None or
            self.Issuer_Alternative_Name is not None or
            self.Subject_Directory_Attributes is not None or
            self.CRL_Distribution_Points is not None or
            self.Inhibit_Any_Policy is not None or
            self.Private_Key_Usage_Period is not None or
            self.Certificate_Policies is not None or
            self.Policy_Mappings is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509V3ExtensionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='X509V3ExtensionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='X509V3ExtensionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509V3ExtensionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Basic_Constraints is not None:
            self.Basic_Constraints.export(lwrite, level, 'X509CertificateObj:', name_='Basic_Constraints', pretty_print=pretty_print)
        if self.Name_Constraints is not None:
            self.Name_Constraints.export(lwrite, level, 'X509CertificateObj:', name_='Name_Constraints', pretty_print=pretty_print)
        if self.Policy_Constraints is not None:
            self.Policy_Constraints.export(lwrite, level, 'X509CertificateObj:', name_='Policy_Constraints', pretty_print=pretty_print)
        if self.Key_Usage is not None:
            self.Key_Usage.export(lwrite, level, 'X509CertificateObj:', name_='Key_Usage', pretty_print=pretty_print)
        if self.Extended_Key_Usage is not None:
            self.Extended_Key_Usage.export(lwrite, level, 'X509CertificateObj:', name_='Extended_Key_Usage', pretty_print=pretty_print)
        if self.Subject_Key_Identifier is not None:
            self.Subject_Key_Identifier.export(lwrite, level, 'X509CertificateObj:', name_='Subject_Key_Identifier', pretty_print=pretty_print)
        if self.Authority_Key_Identifier is not None:
            self.Authority_Key_Identifier.export(lwrite, level, 'X509CertificateObj:', name_='Authority_Key_Identifier', pretty_print=pretty_print)
        if self.Subject_Alternative_Name is not None:
            self.Subject_Alternative_Name.export(lwrite, level, 'X509CertificateObj:', name_='Subject_Alternative_Name', pretty_print=pretty_print)
        if self.Issuer_Alternative_Name is not None:
            self.Issuer_Alternative_Name.export(lwrite, level, 'X509CertificateObj:', name_='Issuer_Alternative_Name', pretty_print=pretty_print)
        if self.Subject_Directory_Attributes is not None:
            self.Subject_Directory_Attributes.export(lwrite, level, 'X509CertificateObj:', name_='Subject_Directory_Attributes', pretty_print=pretty_print)
        if self.CRL_Distribution_Points is not None:
            self.CRL_Distribution_Points.export(lwrite, level, 'X509CertificateObj:', name_='CRL_Distribution_Points', pretty_print=pretty_print)
        if self.Inhibit_Any_Policy is not None:
            self.Inhibit_Any_Policy.export(lwrite, level, 'X509CertificateObj:', name_='Inhibit_Any_Policy', pretty_print=pretty_print)
        if self.Private_Key_Usage_Period is not None:
            self.Private_Key_Usage_Period.export(lwrite, level, 'X509CertificateObj:', name_='Private_Key_Usage_Period', pretty_print=pretty_print)
        if self.Certificate_Policies is not None:
            self.Certificate_Policies.export(lwrite, level, 'X509CertificateObj:', name_='Certificate_Policies', pretty_print=pretty_print)
        if self.Policy_Mappings is not None:
            self.Policy_Mappings.export(lwrite, level, 'X509CertificateObj:', name_='Policy_Mappings', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Basic_Constraints':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Basic_Constraints(obj_)
        elif nodeName_ == 'Name_Constraints':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name_Constraints(obj_)
        elif nodeName_ == 'Policy_Constraints':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Policy_Constraints(obj_)
        elif nodeName_ == 'Key_Usage':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Key_Usage(obj_)
        elif nodeName_ == 'Extended_Key_Usage':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Extended_Key_Usage(obj_)
        elif nodeName_ == 'Subject_Key_Identifier':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject_Key_Identifier(obj_)
        elif nodeName_ == 'Authority_Key_Identifier':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Authority_Key_Identifier(obj_)
        elif nodeName_ == 'Subject_Alternative_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject_Alternative_Name(obj_)
        elif nodeName_ == 'Issuer_Alternative_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Issuer_Alternative_Name(obj_)
        elif nodeName_ == 'Subject_Directory_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject_Directory_Attributes(obj_)
        elif nodeName_ == 'CRL_Distribution_Points':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_CRL_Distribution_Points(obj_)
        elif nodeName_ == 'Inhibit_Any_Policy':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Inhibit_Any_Policy(obj_)
        elif nodeName_ == 'Private_Key_Usage_Period':
            obj_ = ValidityType.factory()
            obj_.build(child_)
            self.set_Private_Key_Usage_Period(obj_)
        elif nodeName_ == 'Certificate_Policies':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Certificate_Policies(obj_)
        elif nodeName_ == 'Policy_Mappings':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Policy_Mappings(obj_)
# end class X509V3ExtensionsType

class X509NonStandardExtensionsType(GeneratedsSuper):
    """The NonStandardX509ExtensionsType captures some non-standard or
    deprecated X509 extensions that may be useful. Based on the
    OpenSSL "Deprecated Extensions" documentation: https://www.opens
    sl.org/docs/apps/x509v3_config.html#Deprecated_Extensions. Also
    based on the Alvestrand certificateExtension reference:
    http://www.alvestrand.no/objectid/2.5.29.html"""

    subclass = None
    superclass = None
    def __init__(self, Netscape_Comment=None, Netscape_Certificate_Type=None, Old_Authority_Key_Identifier=None, Old_Primary_Key_Attributes=None):
        self.Netscape_Comment = Netscape_Comment
        self.Netscape_Certificate_Type = Netscape_Certificate_Type
        self.Old_Authority_Key_Identifier = Old_Authority_Key_Identifier
        self.Old_Primary_Key_Attributes = Old_Primary_Key_Attributes
    def factory(*args_, **kwargs_):
        if X509NonStandardExtensionsType.subclass:
            return X509NonStandardExtensionsType.subclass(*args_, **kwargs_)
        else:
            return X509NonStandardExtensionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Netscape_Comment(self): return self.Netscape_Comment
    def set_Netscape_Comment(self, Netscape_Comment): self.Netscape_Comment = Netscape_Comment
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Netscape_Certificate_Type(self): return self.Netscape_Certificate_Type
    def set_Netscape_Certificate_Type(self, Netscape_Certificate_Type): self.Netscape_Certificate_Type = Netscape_Certificate_Type
    def get_Old_Authority_Key_Identifier(self): return self.Old_Authority_Key_Identifier
    def set_Old_Authority_Key_Identifier(self, Old_Authority_Key_Identifier): self.Old_Authority_Key_Identifier = Old_Authority_Key_Identifier
    def get_Old_Primary_Key_Attributes(self): return self.Old_Primary_Key_Attributes
    def set_Old_Primary_Key_Attributes(self, Old_Primary_Key_Attributes): self.Old_Primary_Key_Attributes = Old_Primary_Key_Attributes
    def hasContent_(self):
        if (
            self.Netscape_Comment is not None or
            self.Netscape_Certificate_Type is not None or
            self.Old_Authority_Key_Identifier is not None or
            self.Old_Primary_Key_Attributes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509NonStandardExtensionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='X509NonStandardExtensionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='X509NonStandardExtensionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509NonStandardExtensionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Netscape_Comment is not None:
            self.Netscape_Comment.export(lwrite, level, 'X509CertificateObj:', name_='Netscape_Comment', pretty_print=pretty_print)
        if self.Netscape_Certificate_Type is not None:
            self.Netscape_Certificate_Type.export(lwrite, level, 'X509CertificateObj:', name_='Netscape_Certificate_Type', pretty_print=pretty_print)
        if self.Old_Authority_Key_Identifier is not None:
            self.Old_Authority_Key_Identifier.export(lwrite, level, 'X509CertificateObj:', name_='Old_Authority_Key_Identifier', pretty_print=pretty_print)
        if self.Old_Primary_Key_Attributes is not None:
            self.Old_Primary_Key_Attributes.export(lwrite, level, 'X509CertificateObj:', name_='Old_Primary_Key_Attributes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Netscape_Comment':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Netscape_Comment(obj_)
        elif nodeName_ == 'Netscape_Certificate_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Netscape_Certificate_Type(obj_)
        elif nodeName_ == 'Old_Authority_Key_Identifier':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Old_Authority_Key_Identifier(obj_)
        elif nodeName_ == 'Old_Primary_Key_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Old_Primary_Key_Attributes(obj_)
# end class X509NonStandardExtensionsType

class X509CertificateObjectType(cybox_common.ObjectPropertiesType):
    """The X509CertificateObjectType type is intended to characterize X.509
    certificates."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Certificate=None, Raw_Certificate=None, Certificate_Signature=None):
        super(X509CertificateObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Certificate = Certificate
        self.Raw_Certificate = Raw_Certificate
        self.Certificate_Signature = Certificate_Signature
    def factory(*args_, **kwargs_):
        if X509CertificateObjectType.subclass:
            return X509CertificateObjectType.subclass(*args_, **kwargs_)
        else:
            return X509CertificateObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Certificate(self): return self.Certificate
    def set_Certificate(self, Certificate): self.Certificate = Certificate
    def get_Certificate_Signature(self): return self.Certificate_Signature
    def set_Certificate_Signature(self, Certificate_Signature): self.Certificate_Signature = Certificate_Signature
    def hasContent_(self):
        if (
            self.Certificate is not None or
            self.Raw_Certificate is not None or
            self.Certificate_Signature is not None or
            super(X509CertificateObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='X509CertificateObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='X509CertificateObj:', name_='X509CertificateObjectType'):
        super(X509CertificateObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='X509CertificateObjectType')
    def exportChildren(self, lwrite, level, namespace_='X509CertificateObj:', name_='X509CertificateObjectType', fromsubclass_=False, pretty_print=True):
        super(X509CertificateObjectType, self).exportChildren(lwrite, level, 'X509CertificateObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Certificate is not None:
            self.Certificate.export(lwrite, level, 'X509CertificateObj:', name_='Certificate', pretty_print=pretty_print)
        if self.Raw_Certificate is not None:
            self.Raw_Certificate.export(lwrite, level, 'X509CertificateObj:', name_='Raw_Certificate', pretty_print=pretty_print)
        if self.Certificate_Signature is not None:
            self.Certificate_Signature.export(lwrite, level, 'X509CertificateObj:', name_='Certificate_Signature', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(X509CertificateObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Certificate':
            obj_ = X509CertificateContentsType.factory()
            obj_.build(child_)
            self.set_Certificate(obj_)
        elif nodeName_ == 'Raw_Certificate':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Certificate(obj_)
        elif nodeName_ == 'Certificate_Signature':
            obj_ = X509CertificateSignatureType.factory()
            obj_.build(child_)
            self.set_Certificate_Signature(obj_)
        super(X509CertificateObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class X509CertificateObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Error': cybox_common.ErrorType,
    'Policy_Mappings': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Signature_Algorithm': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Old_Authority_Key_Identifier': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Extended_Key_Usage': cybox_common.StringObjectPropertyType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Subject_Directory_Attributes': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Inhibit_Any_Policy': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Netscape_Certificate_Type': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Subject': cybox_common.StringObjectPropertyType,
    'Name_Constraints': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Not_Before': cybox_common.DateTimeObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Serial_Number': cybox_common.StringObjectPropertyType,
    'Certificate_Policies': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Not_After': cybox_common.DateTimeObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Exponent': cybox_common.IntegerObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Old_Primary_Key_Attributes': cybox_common.StringObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Time': cybox_common.TimeType,
    'Public_Key_Algorithm': cybox_common.StringObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Libraries': cybox_common.LibrariesType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Library': cybox_common.LibraryType,
    'CRL_Distribution_Points': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Netscape_Comment': cybox_common.StringObjectPropertyType,
    'Issuer': cybox_common.StringObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Issuer_Alternative_Name': cybox_common.StringObjectPropertyType,
    'Basic_Constraints': cybox_common.StringObjectPropertyType,
    'Subject_Key_Identifier': cybox_common.StringObjectPropertyType,
    'Key_Usage': cybox_common.StringObjectPropertyType,
    'Modulus': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Subject_Alternative_Name': cybox_common.StringObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Authority_Key_Identifier': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Policy_Constraints': cybox_common.StringObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Tool': cybox_common.ToolInformationType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'X509_Certificate'
        rootClass = X509CertificateObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'X509_Certificate'
        rootClass = X509CertificateObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'X509_Certificate'
        rootClass = X509CertificateObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="X509_Certificate",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "X509CertificateObjectType",
    "X509CertificateContentsType",
    "X509CertificateSignatureType",
    "SubjectPublicKeyType",
    "ValidityType",
    "RSAPublicKeyType",
    "X509V3ExtensionsType",
    "X509NonStandardExtensionsType"
    ]
