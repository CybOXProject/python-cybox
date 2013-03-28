import cybox
import cybox.utils as utils
import cybox.bindings.cybox_core_1_0 as core_binding
#import cybox.core.structured_text as Structured_Text
from cybox.common.defined_object import DefinedObject
#from cybox.common.measuresource import Measure_Source


class Object(cybox.Entity):
    """The CybOX Object element.

    Currently only supports the following properties:
    - id_
    - idref
    - type_
    - defined_object
    - related_objects
    """

    def __init__(self, defined_object=None, type_=None):
        # TODO: Accept id_ as an argument
        self.id_ = utils.create_id()
        self.idref = None
        self.type_ = type_
        self.defined_object = defined_object
        self.related_objects = []

    @property
    def defined_object(self):
        return self._defined_object

    @defined_object.setter
    def defined_object(self, value):
        if value and not isinstance(value, DefinedObject):
            raise ValueError("Not a DefinedObject")
        self._defined_object = value

        if self._defined_object:
            self._defined_object.parent = self

    def add_related(self, related, relationship, inline=True):
        if not isinstance(related, DefinedObject):
            raise ValueError("Must be a DefinedObject")
        r = RelatedObject()
        if inline:
            r.defined_object = related
        else:
            r.id_ = None
            r.idref = related.parent.id_
        r.relationship = relationship
        self.related_objects.append(r)

    def to_obj(self, bindings_obj=None):
        if bindings_obj == None:
            obj = core_binding.ObjectType()
        else:
            obj = bindings_obj
        obj.set_id(self.id_)
        obj.set_idref(self.idref)
        obj.set_type(self.type_)
        if self.defined_object:
            obj.set_Defined_Object(self.defined_object.to_obj())
        if self.related_objects:
            relobj_obj = core_binding.RelatedObjectsType()
            for x in self.related_objects:
                relobj_obj.add_Related_Object(x.to_obj())
            obj.set_Related_Objects(relobj_obj)

        return obj

    def to_dict(self):
        obj_dict = {}
        if self.id_:
            obj_dict['id'] = self.id_
        if self.idref:
            obj_dict['idref'] = self.idref
        if self.type_:
            obj_dict['type'] = self.type_
        if self.defined_object:
            obj_dict['defined_object'] = self.defined_object.to_dict()
        if self.related_objects:
            obj_dict['related_objects'] = [x.to_dict() for x in
                                                self.related_objects],
        return obj_dict

    @staticmethod
    def from_obj(object_obj, obj_class=None):
        if not object_obj:
            return None

        if obj_class == None:
            obj = Object()
        else:
            obj = obj_class

        obj.id_ = object_obj.get_id()
        obj.idref = object_obj.get_idref()
        obj.type_ = object_obj.get_type()
        obj.defined_object = DefinedObject.from_obj(object_obj.get_Defined_Object())
        rel_objs = object_obj.get_Related_Objects()
        if rel_objs:
            obj.related_objs = [RelatedObject.from_obj(x) for x in
                                rel_objs.get_Related_Object()]

        return obj

    @staticmethod
    def from_dict(object_dict, obj_class=None):
        if not object_dict:
            return None

        if obj_class == None:
            obj = Object()
        else:
            obj = obj_class

        obj.id_ = object_dict.get('id')
        obj.idref = object_dict.get('idref')
        obj.type_ = object_dict.get('type')
        obj.defined_object = DefinedObject.from_dict(
                                    object_dict.get('defined_object'))
        obj.related_objs = [RelatedObject.from_dict(x) for x in
                            object_dict.get('related_objects', [])]

        return obj

#    @classmethod
#    def object_from_dict(cls, object_dict, cybox_obj = None):
#        """Create the Object Python object representation from an input dictionary"""
#        if cybox_obj == None:
#            cybox_obj = core_binding.ObjectType()
#        for key, value in object_dict.items():
#            if key == 'id' and utils.test_value(value): cybox_obj.set_id(value)
#            elif key == 'idref' and utils.test_value(value): cybox_obj.set_idref(value)
#            elif key == 'type' and utils.test_value(value): cybox_obj.set_type(value)
#            elif key == 'object_state' and utils.test_value(value): cybox_obj.set_object_state(value)
#            elif key == 'description' : pass
#            elif key == 'defined_object' : cybox_obj.set_Defined_Object(value)
#                #defined_obj = Defined_Object.object_from_dict(value)
#                #if defined_obj.hasContent_() : cybox_obj.set_Defined_Object(defined_obj)
#            elif key == 'domain-specific_object_attributes': cybox_obj.set_Domain_Specific_Object_Attributes(value)
#            elif key == 'custom_attributes' : pass
#            elif key == 'related_objects':
#                pass
#            elif key == 'defined_effect' :
#                pass
#            elif key == 'discovery_method':
#                measure_source_obj = Measure_Source.object_from_dict(value)
#                if measure_source_obj.hasContent_() : cybox_obj.set_Discovery_Method(measure_source_obj)
#        return cybox_obj

#    @classmethod
#    def dict_from_object(cls, object_obj):
#        """Parse and return a dictionary for an Object"""
#        object_dict = {}
#        if object.get_id() is not None:
#            object_dict['id'] = object.get_id()
#        if object.get_idref() is not None:
#            object_dict['idref'] = object.get_idref()
#        if object.get_type() is not None:
#            object_dict['type'] = object.get_type()
#        if object.get_object_state() is not None:
#            object_dict['object_state'] = object.get_object_state()
#        if object.get_Description() is not None:
#            object_dict['description'] = Structured_Text.dict_from_object(object.get_Description())
#        if object.get_Defined_Object() is not None:
#            object_dict['defined_object'] = defined_object.dict_from_object(object.get_Defined_Object())
#        #TODO - add rest of object components
#        return object_dict

class RelatedObject(Object):

    def __init__(self, *args, **kwargs):
        super(RelatedObject, self).__init__(*args, **kwargs)
        self.relationship = None

    def to_obj(self):
        relobj_obj = core_binding.RelatedObjectType()
        super(RelatedObject, self).to_obj(relobj_obj)
        relobj_obj.set_relationship(self.relationship)

        return relobj_obj

    def to_dict(self):
        relobj_dict = super(RelatedObject, self).to_dict()
        if self.relationship:
            relobj_dict['relationship'] = self.relationship

        return relobj_dict

    @staticmethod
    def from_obj(relobj_obj):
        relobj = RelatedObject()
        Object.from_obj(relobj_obj, relobj)
        relobj.relationship = relobj_obj.get_relationship()

        return relobj

    @staticmethod
    def from_dict(relobj_dict):
        relobj = RelatedObject()
        Object.from_dict(relobj_dict, relobj)
        relobj.relationship = relobj_dict.get('relationship')

        return relobj
