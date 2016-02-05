# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import collections

from mixbox import entities
from mixbox import fields
from mixbox import idgen

from cybox import Unicode
import cybox.bindings.cybox_core as core_binding
from cybox.common import MeasureSource, ObjectProperties, StructuredText
from cybox.core import Object, Event


def validate_operator(instance, value):
    allowed = ObservableComposition.OPERATORS

    if value in allowed:
        return

    error = "Operator must be one of {allowed}. Received '{value}'."
    raise ValueError(error.format(**locals()))


def validate_object(instance, value):
    if not value:
        return
    elif not isinstance(value, Object):
        raise TypeError('value must be an Object')
    elif instance.event:
        raise ValueError("Observable already has an Event.")
    elif instance.observable_composition:
        raise ValueError("Observable already has an ObservableComposition.")


def validate_event(instance, value):
    if not value:
        return
    elif not isinstance(value, Event):
        raise TypeError("value must be an Event")
    elif instance.object_:
        raise ValueError("Observable already has an Object.")
    elif instance.observable_composition:
        raise ValueError("Observable already has an ObservableComposition.")


def validate_observable_composition(instance, value):
    if not value:
        return
    elif not isinstance(value, ObservableComposition):
        raise TypeError('value must be an ObservableComposition')
    elif instance.object_:
        raise ValueError("Observable already has an Object.")
    elif instance.event:
        raise ValueError("Observable already has an Event.")


class Keywords(entities.EntityList):
    _binding = core_binding
    _binding_class = core_binding.KeywordsType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    keyword = fields.TypedField("Keyword", Unicode, multiple=True)

class Observable(entities.Entity):
    """A single Observable.
    """
    _binding = core_binding
    _binding_class = _binding.ObservableType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    title = fields.TypedField("Title")
    description = fields.TypedField("Description", StructuredText)
    object_ = fields.TypedField("Object", Object, preset_hook=validate_object)  # TODO: Add preset hook
    event = fields.TypedField("Event", Event, preset_hook=validate_event)
    observable_composition = fields.TypedField("Observable_Composition", type_="cybox.core.ObservableComposition", preset_hook=validate_observable_composition)
    sighting_count = fields.TypedField("sighting_count")
    observable_source = fields.TypedField("Observable_Source", MeasureSource, multiple=True)
    keywords = fields.TypedField("Keywords", Keywords)
    pattern_fidelity = fields.TypedField("Pattern_Fidelity", type_="cybox.core.PatternFidelity")

    def __init__(self, item=None, id_=None, idref=None, title=None, description=None):
        """Create an Observable out of 'item'.

        `item` can be any of:
        - an Object
        - an Event
        - an ObservableComposition
        - any subclass of ObjectProperties.

        In the first three cases, the appropriate property of the Observable
        will be set. In the last cases, an Object will be built automatically
        to ensure the correct hierarchy is created.
        """
        super(Observable, self).__init__()

        self.id_ = id_ or idgen.create_id(prefix="Observable")
        self.idref = idref
        self.title = title
        self.description = description
        self.keywords = Keywords()

        if item is None:
            return
        elif isinstance(item, Object):
            self.object_ = item
        elif isinstance(item, ObservableComposition):
            self.observable_composition = item
        elif isinstance(item, Event):
            self.event = item
        elif isinstance(item, ObjectProperties):
            if item.parent:
                self.object_ = item.parent
            else:
                self.object_ = Object(item)
        else:
            msg = ("item must be an Object, Event, ObservableComposition, or "
                   "subclass of ObjectProperties. Received an %s" % type(item))
            raise TypeError(msg)

    def add_keyword(self, value):
        self.keywords.append(value)


class Observables(entities.EntityList):
    """The root CybOX Observables object.

    Pools are not currently supported.
    """
    _binding = core_binding
    _binding_class = _binding.ObservablesType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    observable_package_source = fields.TypedField("Observable_Package_Source", MeasureSource)
    observables = fields.TypedField("Observable", Observable, multiple=True, key_name="observables")

    def __init__(self, observables=None):
        super(Observables, self).__init__(observables)
        # Assume major_verion and minor_version are immutable for now
        self._major_version = 2
        self._minor_version = 1
        self._update_version = 0

    def add(self, observable):
        if not observable:
            return
        if not isinstance(observable, Observable):
            observable = Observable(observable)
        self.observables.append(observable)

    def to_obj(self, ns_info=None):
        observables_obj = super(Observables, self).to_obj(ns_info=ns_info)
        observables_obj.cybox_major_version = self._major_version
        observables_obj.cybox_minor_version = self._minor_version
        observables_obj.cybox_update_version = self._update_version
        return observables_obj

    def to_dict(self):
        observables_dict = super(Observables, self).to_dict()
        observables_dict['major_version'] = self._major_version
        observables_dict['minor_version'] = self._minor_version
        observables_dict['update_version'] = self._update_version
        return observables_dict


class ObservableComposition(entities.EntityList):
    """The ObservableCompositionType entity defines a logical compositions of
    CybOX Observables. The combinatorial behavior is derived from the operator
    property."""

    _binding = core_binding
    _binding_class = _binding.ObservableCompositionType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    OPERATOR_AND = 'AND'
    OPERATOR_OR = 'OR'
    OPERATORS = (OPERATOR_AND, OPERATOR_OR)

    operator = fields.TypedField("operator", preset_hook=validate_operator)
    observables = fields.TypedField("Observable", Observable, multiple=True, key_name="observables")

    def __init__(self, operator='AND', observables=None):
        super(ObservableComposition, self).__init__(observables)
        self.operator = operator

    def add(self, observable):
        if not observable:
            raise ValueError("'observable' must not be None")
        self.append(observable)

