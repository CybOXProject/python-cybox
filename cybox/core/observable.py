# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import MeasureSource, ObjectProperties, StructuredText
from cybox.core import Object, Event


class Observable(cybox.Entity):
    """A single Observable.
    """
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'

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
        if not id_ and not idref:
            id_ = cybox.utils.create_id(prefix="Observable")

        self.id_ = id_
        self.title = title
        self.description = description

        self.object_ = None
        self.event = None
        self.observable_composition = None
        self.idref = idref
        self.sighting_count = None
        self.observable_source = []
        self.keywords = Keywords()
        self.pattern_fidelity = None

        if not item:
            return

        if isinstance(item, Object):
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

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None # unset id_ if idref is present 

    @property
    def object_(self):
        return self._object

    @object_.setter
    def object_(self, value):
        if value:
            if self.event:
                msg = 'Observable already has an Event.'
                raise ValueError(msg)
            elif self.observable_composition:
                msg = 'Observable already has an ObservableComposition.'
                raise ValueError(msg)
            if not isinstance(value, Object):
                raise TypeError('value must be an Object')

        self._object = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        if value:
            if self.object_:
                raise ValueError('Observable already has an Object.')
            elif self.observable_composition:
                msg = 'Observable already has an ObservableComposition.'
                raise ValueError(msg)
            if not isinstance(value, Event):
                raise TypeError('value must be an Event')

        self._event = value

    @property
    def observable_composition(self):
        return self._observable_composition

    @observable_composition.setter
    def observable_composition(self, value):
        if value:
            if self.object_:
                raise ValueError('Observable already has an Object.')
            elif self.event:
                msg = 'Observable already has an Event.'
                raise ValueError(msg)
            if not isinstance(value, ObservableComposition):
                raise TypeError('value must be an ObservableComposition')

        self._observable_composition = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, StructuredText):
            value = StructuredText(value)
        self._description = value

    def add_keyword(self, value):
        self.keywords.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        obs_obj = core_binding.ObservableType()

        obs_obj.id = self.id_
        if self.title is not None:
            obs_obj.Title = self.title
        if self.description is not None:
            obs_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.object_:
            obs_obj.Object = self.object_.to_obj(ns_info=ns_info)
        if self.event:
            obs_obj.Event = self.event.to_obj(ns_info=ns_info)
        if self.observable_composition:
            obs_obj.Observable_Composition = self.observable_composition.to_obj(ns_info=ns_info)
        if self.idref is not None: 
            obs_obj.idref = self.idref
        if self.sighting_count is not None:
            obs_obj.sighting_count = self.sighting_count
        if self.observable_source:
            obs_obj.Observable_Source = [x.to_obj(ns_info=ns_info) for x in self.observable_source]
        if self.keywords:
            obs_obj.Keywords = self.keywords.to_obj(ns_info=ns_info)
        if self.pattern_fidelity:
            obs_obj.Pattern_Fidelity = self.pattern_fidelity.to_obj(ns_info=ns_info)

        return obs_obj

    def to_dict(self):
        obs_dict = {}

        if self.id_ is not None:
            obs_dict['id'] = self.id_
        if self.title is not None:
            obs_dict['title'] = self.title
        if self.description is not None:
            obs_dict['description'] = self.description.to_dict()
        if self.object_:
            obs_dict['object'] = self.object_.to_dict()
        if self.event:
            obs_dict['event'] = self.event.to_dict()
        if self.observable_composition:
            obs_dict['observable_composition'] = self.observable_composition.to_dict()
        if self.idref is not None: 
            obs_dict['idref'] = self.idref
        if self.sighting_count is not None:
            obs_dict['sighting_count'] = self.sighting_count
        if self.observable_source:
            obs_dict['observable_source'] = [x.to_dict() for x in self.observable_source]
        if self.keywords:
            obs_dict['keywords'] = self.keywords.to_dict()
        if self.pattern_fidelity:
            obs_dict['pattern_fidelity'] = self.pattern_fidelity.to_dict()

        return obs_dict

    @staticmethod
    def from_obj(observable_obj):
        if not observable_obj:
            return None

        from cybox.core import PatternFidelity
        obs = Observable()

        obs.id_ = observable_obj.id
        obs.title = observable_obj.Title
        obs.description = StructuredText.from_obj(observable_obj.Description)
        obs.object_ = Object.from_obj(observable_obj.Object)
        obs.event = Event.from_obj(observable_obj.Event)
        obs.observable_composition = ObservableComposition.from_obj(observable_obj.Observable_Composition)
        obs.idref = observable_obj.idref
        obs.sighting_count = observable_obj.sighting_count
        if observable_obj.Observable_Source:
            obs.observable_source = [MeasureSource.from_obj(x) for x in observable_obj.Observable_Source]
        obs.keywords = Keywords.from_obj(observable_obj.Keywords)
        obs.pattern_fidelity = PatternFidelity.from_obj(observable_obj.Pattern_Fidelity)

        return obs

    @staticmethod
    def from_dict(observable_dict):
        if not observable_dict:
            return None

        from cybox.core import PatternFidelity
        obs = Observable()

        obs.id_ = observable_dict.get('id')
        obs.title = observable_dict.get('title')
        obs.description = StructuredText.from_dict(observable_dict.get('description'))
        obs.object_ = Object.from_dict(observable_dict.get('object'))
        obs.event = Object.from_dict(observable_dict.get('event'))
        obs.observable_composition = ObservableComposition.from_dict(observable_dict.get('observable_composition'))
        obs.idref = observable_dict.get('idref')
        obs.sighting_count = observable_dict.get('sighting_count')
        if observable_dict.get('observable_source'):
            obs.observable_source = [MeasureSource.from_dict(x) for x in observable_dict.get('observable_source')]
        obs.keywords = Keywords.from_dict(observable_dict.get('keywords'))
        obs.pattern_fidelity = PatternFidelity.from_dict(observable_dict.get('pattern_fidelity'))

        return obs


class Observables(cybox.Entity):
    """The root CybOX Observables object.

    Pools are not currently supported.
    """
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, observables=None):
        super(Observables, self).__init__()
        # Assume major_verion and minor_version are immutable for now
        self._major_version = 2
        self._minor_version = 1
        self._update_version = 0
        self.observable_package_source = None
        self.observables = []

        try:
            for obs in observables:
                self.add(obs)
        except TypeError:
            # A single observable
            self.add(observables)

    @property
    def __iter__(self):
        return self.observables.__iter__

    @property
    def __len__(self):
        return self.observables.__len__

    def add(self, observable):
        if not observable:
            return
        if not isinstance(observable, Observable):
            observable = Observable(observable)
        self.observables.append(observable)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        observables_obj = core_binding.ObservablesType(
                                cybox_major_version=self._major_version,
                                cybox_minor_version=self._minor_version,
                                cybox_update_version=self._update_version)

        #Required
        observables_obj.Observable = [x.to_obj(ns_info=ns_info) for x in self.observables]

        #Optional
        if self.observable_package_source:
            observables_obj.Observable_Package_Source = self.observable_package_source.to_obj(ns_info=ns_info)

        return observables_obj

    def to_dict(self):
        observables_dict = {}

        #Required
        observables_dict['major_version'] = self._major_version
        observables_dict['minor_version'] = self._minor_version
        observables_dict['update_version'] = self._update_version
        observables_dict['observables'] = [x.to_dict() for x in self.observables]

        #Optional
        if self.observable_package_source:
            observables_dict['observable_package_source'] = self.observable_package_source.to_dict()

        return observables_dict

    @staticmethod
    def from_obj(observables_obj):
        if not observables_obj:
            return None

        #TODO: look at major_version and minor_version
        obs = Observables()

        # get_Observable() actually returns a list
        for o in observables_obj.Observable:
            obs.add(Observable.from_obj(o))

        obs.observable_package_source = MeasureSource.from_obj(observables_obj.Observable_Package_Source)

        return obs

    @staticmethod
    def from_dict(observables_dict):
        if observables_dict is None:
            return None

        #TODO: look at major_version and minor_version
        obs = Observables()

        for o in observables_dict.get("observables", []):
            obs.add(Observable.from_dict(o))
        obs.observable_package_source = MeasureSource.from_dict(observables_dict.get('observable_package_source'))

        return obs


class ObservableComposition(cybox.Entity):
    '''The ObservableCompositionType entity defines a logical compositions of
    CybOX Observables. The combinatorial behavior is derived from the operator
    property.'''
    _namespace = 'http://cybox.mitre.org/cybox-2'

    OPERATOR_AND = 'AND'
    OPERATOR_OR = 'OR'
    OPERATORS = (OPERATOR_AND, OPERATOR_OR)

    def __init__(self, operator='AND', observables=None):
        super(ObservableComposition, self).__init__()
        self.operator = operator
        self.observables = []

        if observables:
            try:
                for obs in observables:
                    self.add(obs)
            except TypeError as t:
                # A single observable
                self.add(observables)

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if value not in self.OPERATORS:
            raise ValueError('value must be one of: %s' % ' '.join(self.OPERATORS) )

        self._operator = value

    def add(self, observable):
        if not observable:
            raise ValueError("'observable' must not be None")
        if not isinstance(observable, Observable):
            observable = Observable(observable)
        self.observables.append(observable)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        observable_list = [x.to_obj(ns_info=ns_info) for x in self.observables]
        return core_binding.ObservableCompositionType(
                                operator = self._operator,
                                Observable=observable_list)

    def to_dict(self):
        return {
                    'operator': self._operator,
                    'observables': [x.to_dict() for x in self.observables]
               }

    @staticmethod
    def from_obj(observable_comp_obj):
        if not observable_comp_obj: 
            return None

        obs_comp = ObservableComposition()
        obs_comp.operator = observable_comp_obj.operator
        # get_Observable() actually returns a list
        for o in observable_comp_obj.Observable:
            obs_comp.add(Observable.from_obj(o))

        return obs_comp

    @staticmethod
    def from_dict(observable_comp_dict):
        if not observable_comp_dict:
            return None

        obs_comp = ObservableComposition()
        obs_comp.operator = observable_comp_dict.get('operator', 'AND')
        for o in observable_comp_dict.get("observables", []):
            obs_comp.add(Observable.from_dict(o))

        return obs_comp


class Keywords(cybox.EntityList):
    _binding = core_binding
    _binding_class = core_binding.KeywordsType
    _binding_var = "Keyword"
    _contained_type = cybox.Unicode
    _namespace = 'http://cybox.mitre.org/cybox-2'
