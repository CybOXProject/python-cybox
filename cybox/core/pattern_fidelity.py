# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_core as core_binding
from cybox.common import StructuredText
from cybox.core.observable import Observables


class ObfuscationTechnique(entities.Entity):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.ObfuscationTechniqueType

    description = fields.TypedField("Description", StructuredText)
    observables = fields.TypedField("Observables", Observables)


class ObfuscationTechniques(entities.EntityList):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.ObfuscationTechniquesType
    obfuscation_technique = fields.TypedField("Obfuscation_Technique", ObfuscationTechnique, multiple=True)


class PatternFidelity(entities.Entity):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _binding_class = core_binding.PatternFidelityType

    noisiness = fields.TypedField("Noisiness")
    ease_of_evasion = fields.TypedField("Ease_of_Evasion")
    evasion_techniques = fields.TypedField("Evasion_Techniques", ObfuscationTechniques)
