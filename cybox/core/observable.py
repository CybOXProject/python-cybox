import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
#from cybox.core.structured_text import structured_text
from cybox.common import DefinedObject
from cybox.core import Object, StatefulMeasure

class Observable(cybox.Entity):
    """A single Observable.

    Note that StatefulMeasure and ObservableComposition are the only supported
    properties now.
    """

    def __init__(self, item=None, id_=None):
        """Create an Observable out of 'item'.

        `item` can be any of:
        - a StatefulMeasure
        - an ObservableComposition
        - an Object
        - a DefinedObject (or any of its subclasses).

        In the first two cases, the appropriate property of the Observable will
        be set. In the latter two cases, a StatefulMeasure (and possibly an
        Object as well) will be built automatically to ensure the correct
        object hierarchy is created.
        """
        if not id_:
            id_ = cybox.utils.create_id()

        self.id_ = id_
        self.stateful_measure = None
        self.observable_composition = None

        if not item:
            return

        if isinstance(item, StatefulMeasure):
            self.stateful_measure = item
        elif isinstance(item, ObservableComposition):
            self.observable_composition = item
        elif isinstance(item, (Object, DefinedObject)):
            # StatefulMeasure.__init__() can accept either an Object or a
            # DefinedObject.
            self.stateful_measure = StatefulMeasure(item)

    @property
    def stateful_measure(self):
        return self._stateful_measure

    @stateful_measure.setter
    def stateful_measure(self, value):
        if value:
            if self.observable_composition:
                msg = 'Observable already has an ObservableComposition.'
                raise ValueError(msg)
            if not isinstance(value, StatefulMeasure):
                raise TypeError('value must be a StatefulMeasure')

        self._stateful_measure = value

    @property
    def observable_composition(self):
        return self._observable_composition

    @observable_composition.setter
    def observable_composition(self, value):
        if value:
            if self.stateful_measure:
                raise ValueError('Observable already has a StatefulMeasure.')
            if not isinstance(value, ObservableComposition):
                raise TypeError('value must be an ObservableComposition')

        self._observable_composition = value

    def to_obj(self):
        obs_obj = core_binding.ObservableType(id=self.id_)
        if self.stateful_measure:
            obs_obj.set_Stateful_Measure(self.stateful_measure.to_obj())
        if self.observable_composition:
            obs_obj.set_Observable_Composition(self.observable_composition.to_obj())
        return obs_obj

    def to_dict(self):
        obs_dict = {}
        obs_dict['id'] = self.id_
        if self.stateful_measure:
            obs_dict['stateful_measure'] = self.stateful_measure.to_dict()
        if self.observable_composition:
            obs_dict['observable_composition'] = self.observable_composition.to_dict()
        return obs_dict

    @staticmethod
    def from_obj(observable_obj):
        #TODO: clean up
        obs = Observable()
        obs.id_ = observable_obj.get_id()

        sm_obj = observable_obj.get_Stateful_Measure()
        if sm_obj:
            obs.stateful_measure = StatefulMeasure.from_obj(sm_obj)

        oc_obj = observable_obj.get_Observable_Composition()
        if oc_obj:
            obs.observable_composition = ObservableComposition.from_obj(oc_obj)

        return obs

    @staticmethod
    def from_dict(observable_dict):
        #TODO: clean up
        obs = Observable()
        obs.id_ = observable_dict.get('id')
        sm_dict = observable_dict.get('stateful_measure')
        obs.stateful_measure = StatefulMeasure.from_dict(sm_dict) if sm_dict else None
        oc_dict = observable_dict.get('observable_composition')
        obs.observable_composition = ObservableComposition.from_dict(oc_dict) if oc_dict else None
        
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
#        if observable.get_Stateful_Measure() is not None:
#            observable_dict['stateful_measure'] = stateful_measure.dict_from_object(observable.get_Stateful_Measure())
#        #TODO - add rest of observable components
#        return observable_dict

class Observables(cybox.Entity):
    """The root CybOX Observables object.

    Observable_Package_Source and Pools are not currently supported.
    """

    def __init__(self, observables=None):
        # Assume major_verion and minor_version are immutable for now
        self._major_version = 1
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

 
