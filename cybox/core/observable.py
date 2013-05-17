# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import ObjectProperties, StructuredText
from cybox.core import Object

class Observable(cybox.Entity):
    """A single Observable.
    """
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, item=None, id_=None):
        """Create an Observable out of 'item'.

        `item` can be any of:
        - an Object
        - an ObservableComposition
        - any subclass of ObjectProperties.

        In the first two cases, the appropriate property of the Observable will
        be set. In the last cases, an Object will be built automatically to 
        ensure the correct hierarchy is created.
        """
        if not id_:
            id_ = cybox.utils.create_id(prefix="Observable")

        self.id_ = id_
        self.title = None
        self.description = None

        self.object_ = None
        self.observable_composition = None

        if not item:
            return

        if isinstance(item, Object):
            self.object_ = item
        elif isinstance(item, ObservableComposition):
            self.observable_composition = item
        elif isinstance(item, ObjectProperties):
            if item.parent:
                self.object_ = item.parent
            else:
                self.object_ = Object(item)

    @property
    def object_(self):
        return self._object

    @object_.setter
    def object_(self, value):
        if value:
            if self.observable_composition:
                msg = 'Observable already has an ObservableComposition.'
                raise ValueError(msg)
            if not isinstance(value, Object):
                raise TypeError('value must be a Object')

        self._object = value

    @property
    def observable_composition(self):
        return self._observable_composition

    @observable_composition.setter
    def observable_composition(self, value):
        if value:
            if self.object_:
                raise ValueError('Observable already has an Object.')
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

    def to_obj(self):
        obs_obj = core_binding.ObservableType()

        obs_obj.set_id(self.id_)
        if self.title is not None:
            obs_obj.set_Title(self.title)
        if self.description is not None:
            obs_obj.set_Description(self.description.to_obj())
        if self.object_:
            obs_obj.set_Object(self.object_.to_obj())
        if self.observable_composition:
            obs_obj.set_Observable_Composition(self.observable_composition.to_obj())

        return obs_obj

    def to_dict(self):
        obs_dict = {}

        obs_dict['id'] = self.id_
        if self.title is not None:
            obs_dict['title'] = self.title
        if self.description is not None:
            obs_dict['description'] = self.description.to_dict()
        if self.object_:
            obs_dict['object'] = self.object_.to_dict()
        if self.observable_composition:
            obs_dict['observable_composition'] = self.observable_composition.to_dict()

        return obs_dict

    @staticmethod
    def from_obj(observable_obj):
        if not observable_obj:
            return None

        obs = Observable()

        obs.id_ = observable_obj.get_id()
        obs.title = observable_obj.get_Title()
        obs.description = StructuredText.from_obj(observable_obj.get_Description())
        obs.object_ = Object.from_obj(observable_obj.get_Object())
        obs.observable_composition = ObservableComposition.from_obj(observable_obj.get_Observable_Composition())

        return obs

    @staticmethod
    def from_dict(observable_dict):
        if not observable_dict:
            return None

        obs = Observable()

        obs.id_ = observable_dict.get('id')
        obs.title = observable_dict.get('title')
        obs.description = StructuredText.from_dict(observable_dict.get('description'))
        obs.object_ = Object.from_dict(observable_dict.get('object'))
        obs.observable_composition = ObservableComposition.from_dict(observable_dict.get('observable_composition'))

        return obs

#    @classmethod
#    def dict_from_object(cls, observable_obj):
#        """Parse the observable into a dictionary-esque representation"""
#        observable_dict = {}
#        if observable.get_id() is not None:
#            observable_dict['id'] = observable.get_id()
#        if observable.get_idref() is not None:
#            observable_dict['idref'] = observable.get_idref()
#        if observable.get_Title() is not None:
#            observable_dict['title'] = observable.get_Title()
#        if observable.get_Description() is not None:
#            observable_dict['description'] = structured_text.dict_from_object(observable.get_Description())
#        #TODO - add rest of observable components
#        return observable_dict

class Observables(cybox.Entity):
    """The root CybOX Observables object.

    Observable_Package_Source and Pools are not currently supported.
    """
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, observables=None):
        # Assume major_verion and minor_version are immutable for now
        self._major_version = 2
        self._minor_version = 0
        self.observables = []

        try:
            for obs in observables:
                self.add(obs)
        except TypeError:
            # A single observable
            self.add(observables)

    def add(self, observable):
        if not observable:
            return
        if not isinstance(observable, Observable):
            observable = Observable(observable)
        self.observables.append(observable)

    def to_obj(self):
        observable_list = [x.to_obj() for x in self.observables]
        return core_binding.ObservablesType(
                                cybox_major_version=self._major_version,
                                cybox_minor_version=self._minor_version,
                                Observable=observable_list)

    def to_dict(self):
        return {
                    'major_version': self._major_version,
                    'minor_version': self._minor_version,
                    'observables': [x.to_dict() for x in self.observables]
               }

    @staticmethod
    def from_obj(observables_obj):

        #TODO: look at major_version and minor_version
        obs = Observables()
        # get_Observable() actually returns a list
        for o in observables_obj.get_Observable():
            obs.add(Observable.from_obj(o))

        return obs

    @staticmethod
    def from_dict(observables_dict):
        #TODO: look at major_version and minor_version
        obs = Observables()
        for o in observables_dict.get("observables", []):
            obs.add(Observable.from_dict(o))

        return obs


class ObservableComposition(cybox.Entity):
    '''The ObservableCompositionType entity defines a logical compositions of
    CybOX Observables. The combinatorial behavior is derived from the operator
    property.'''
    
    OPERATOR_AND = 'AND'
    OPERATOR_OR = 'OR'
    OPERATORS = (OPERATOR_AND, OPERATOR_OR)
    
    def __init__(self, operator='AND', observables=None):
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
        
    
    def to_obj(self):
        observable_list = [x.to_obj() for x in self.observables]
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
        # get_Observable() actually returns a list
        for o in observable_comp_obj.get_Observable():
            obs_comp.add(Observable.from_obj(o))

        return obs_comp

    @staticmethod
    def from_dict(observable_comp_dict):
        if not observable_comp_dict:
            return None
        
        obs_comp = ObservableComposition()
        for o in observable_comp_dict.get("observables", []):
            obs_comp.add(Observable.from_dict(o))

        return obs_comp

 
