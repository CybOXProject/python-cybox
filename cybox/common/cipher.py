# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.cybox_common as common_binding
from cybox.common import BaseProperty


class Cipher(BaseProperty):
    _binding = common_binding
    _binding_class = common_binding.CipherType
    _namespace = 'http://cybox.mitre.org/common-2'

    TERM_3DES = "3DES"
    TERM_AES = "AES"
    TERM_BLOWFISH = "Blowfish"
    TERM_CAST128 = "CAST-128"
    TERM_CAST256 = "CAST-256"
    TERM_DES = "DES"
    TERM_IDEA = "IDEA"
    TERM_RIJNDAEL = "Rijndael"
    TERM_RC5 = "RC5"
    TERM_SKIPJACK = "Skipjack"
