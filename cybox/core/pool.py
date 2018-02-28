# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_core as core_binding
from cybox.common import Property
from cybox.core import Action, Event, Object


class EventPool(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.EventPoolType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    events = fields.TypedField("Event", Event, multiple=True, key_name="events")


class ActionPool(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.ActionPoolType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    actions = fields.TypedField("Action", Action, multiple=True, key_name="actions")


class ObjectPool(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.ObjectPoolType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    objects = fields.TypedField("Object", Object, multiple=True, key_name="objects")


class PropertyPool(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.PropertyPoolType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    properties = fields.TypedField("Property", Property, multiple=True, key_name="properties")


class Pools(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.PoolsType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    event_pool = fields.TypedField("Event_Pool", EventPool)
    action_pool = fields.TypedField("Action_Pool", ActionPool)
    object_pool = fields.TypedField("Object_Pool", ObjectPool)
    property_pool = fields.TypedField("Property_Pool", PropertyPool)
