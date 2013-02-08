import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Digital_Signature(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, digital_signature_dict):
        """Create the Digital Signature object representation from an input dictionary"""
        digital_signature_obj = common_types_binding.DigitalSignatureInfoType()
        for key, value in digital_signature_dict.items():
            if key == 'signature_exists' and utils.test_value(value):
                digital_signature_obj.set_signature_exists(value.get('value'))
            elif key == 'signature_verified' and utils.test_value(value):
                digital_signature_obj.set_signature_verified(value.get('value'))
            elif key == 'certificate_issuer' and utils.test_value(value):
                digital_signature_obj.set_Certificate_Issuer(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'certificate_subject' and utils.test_value(value):
                digital_signature_obj.set_Certificate_Subject(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'certificate_description' and utils.test_value(value):
                digital_signature_obj.set_Certificate_Description(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
        return digital_signature_obj

    @classmethod
    def dict_from_object(cls, digital_signature_obj):
        """Parse and return a dictionary for a Digital Signature object"""
        digital_signature_dict = {}
        if digital_signature_obj.get_signature_exists() is not None: digital_signature_dict['signature_exists'] = {'value' : digital_signature_obj.get_signature_exists()}
        if digital_signature_obj.get_signature_verified() is not None: digital_signature_dict['signature_verified'] = {'value' : digital_signature_obj.get_signature_verified()}
        if digital_signature_obj.get_Certificate_Issuer() is not None: digital_signature_dict['certificate_issuer'] = Base_Object_Attribute.dict_from_object(digital_signature_obj.get_Certificate_Issuer())
        if digital_signature_obj.get_Certificate_Subject() is not None: digital_signature_dict['certificate_subject'] = Base_Object_Attribute.dict_from_object(digital_signature_obj.get_Certificate_Subject())
        if digital_signature_obj.get_Signature_Description() is not None: digital_signature_dict['signature_description'] = Base_Object_Attribute.dict_from_object(digital_signature_obj.get_Signature_Description())
        return digital_signature_dict

class Digital_Signature_List(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, digital_signatures_list):
        """Create the Digital Signatures object representation from an input list"""
        digital_signatures_obj = common_types_binding.DigitalSignaturesType()
        for digital_signature_dict in digital_signatures:
            digital_signature_obj = Digital_Signature.object_from_dict(digital_signature_dict)
            if digital_signature_obj.hasContent_() : digital_signatures_obj.add_Digital_Signature(digital_signature_obj)
        return digital_signatures_obj

    @classmethod
    def list_from_object(cls, digital_signatures_obj):
        """Parse and return a list of Digital Signatures for a Digital Signatures object"""
        digital_signatures_list = []
        if digital_signatures_obj.get_Digital_Signature() is not None:
            for digital_signature_obj in digital_signatures_obj.get_Digital_Signature():
                digital_signatures_list.append(Digital_Signature.dict_from_object(digital_signature_obj))
        return digital_signatures_list