# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import DataSegment


class DefinedEffectFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        return cybox.lookup_extension(key, default=DefinedEffect)


class DefinedEffect(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.DefinedEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = None    # overridden by subclasses

    TERM_STATE_CHANGED = 'State_Changed'
    TERM_DATA_READ = 'Data_Read'
    TERM_DATA_WRITTEN = 'Data_Written'
    TERM_DATA_RECEIVED = 'Data_Received'
    TERM_PROPERTIES_READ = 'Properties_Read'
    TERM_PROPERTIES_ENUMERATED = 'Properties_Enumerated'
    TERM_VALUES_ENUMERATED = 'Values_Enumerated'
    TERM_CONTROLCODE_SENT = 'ControlCode_Sent'

    effect_type = fields.TypedField("effect_type")

    def to_dict(self):
        d = super(DefinedEffect, self).to_dict()

        if self._XSI_TYPE:
            d["xsi:type"] = self._XSI_TYPE

        return d

    @staticmethod
    def lookup_class(xsi_type):
        return cybox.lookup_extension(xsi_type, default=DefinedEffect)


@cybox.register_extension
class StateChangeEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.StateChangeEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:StateChangeEffectType"

    old_object = fields.TypedField("Old_Object", type_="cybox.core.object.Object")
    new_object = fields.TypedField("New_Object", type_="cybox.core.object.Object")


@cybox.register_extension
class DataReadEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.DataReadEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:DataReadEffectType"

    data = fields.TypedField("Data", DataSegment)


@cybox.register_extension
class DataWrittenEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.DataWrittenEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:DataWrittenEffectType"

    data = fields.TypedField("Data", DataSegment)


@cybox.register_extension
class DataSentEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.DataSentEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:DataSentEffectType"

    data = fields.TypedField("Data", DataSegment)


@cybox.register_extension
class DataReceivedEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.DataReceivedEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:DataReceivedEffectType"

    data = fields.TypedField("Data", DataSegment)


@cybox.register_extension
class PropertyReadEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.PropertyReadEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:PropertyReadEffectType"

    name = fields.TypedField("Name")
    value = fields.TypedField("Value")


class Properties(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.PropertiesType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    property_ = fields.TypedField("Property", multiple=True)


@cybox.register_extension
class PropertiesEnumeratedEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.PropertiesEnumeratedEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:PropertiesEnumeratedEffectType"

    properties = fields.TypedField("Properties", Properties)


class Values(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ValuesType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    value = fields.TypedField("Value", multiple=True)


@cybox.register_extension
class ValuesEnumeratedEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.ValuesEnumeratedEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:ValuesEnumeratedEffectType"

    values = fields.TypedField("Values", Values)


@cybox.register_extension
class SendControlCodeEffect(DefinedEffect):
    _binding = core_binding
    _binding_class = core_binding.SendControlCodeEffectType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    _XSI_TYPE = "cybox:SendControlCodeEffectType"

    control_code = fields.TypedField("Control_Code")
