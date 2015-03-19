# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import StructuredText
from cybox.core.observable import Observables

class ObfuscationTechnique(cybox.Entity):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.ObfuscationTechniqueType

    description = cybox.TypedField("Description", StructuredText)
    observables = cybox.TypedField("Observables", Observables)

class ObfuscationTechniques(cybox.EntityList):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.ObfuscationTechniquesType
    _binding_var = "Obfuscation_Technique"
    _contained_type = ObfuscationTechnique

class PatternFidelity(cybox.Entity):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.PatternFidelityType

    noisiness = cybox.TypedField("Noisiness")
    ease_of_evasion = cybox.TypedField("Ease_of_Evasion")
    evasion_techniques = cybox.TypedField("Evasion_Techniques", ObfuscationTechniques)

