# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import vocabs, StructuredText, MeasureSource
from cybox.common.vocabs import EventType
from cybox.core import Actions, Frequency


class Event(cybox.Entity):
    _binding = core_binding
    _binding_class = core_binding.EventType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    id_ = cybox.TypedField("id")
    idref = cybox.TypedField("idref")

    type_ = vocabs.VocabField("Type", EventType)
    description = cybox.TypedField("Description", StructuredText)
    observation_method = cybox.TypedField("Observation_Method", MeasureSource)
    actions = cybox.TypedField("Actions", Actions)
    frequency = cybox.TypedField("Frequency", Frequency)

    event = cybox.TypedField("Event", multiple=True)

# Allow recursive definition of events
Event.event.type_ = Event
