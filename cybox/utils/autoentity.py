from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
from sphinx.util.pycompat import class_types

from mixbox import entities
from mixbox import fields


def make_class_ref(cls):
    return ":py:class:`%s.%s`" % (cls.__module__, cls.__name__)


class EntityDocumenter(ClassDocumenter):

    objtype = "class"
    priority = 99

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, class_types) and \
               issubclass(member, entities.Entity)

    def add_content(self, more_content, no_docstring=False):
        ClassDocumenter.add_content(self, more_content, no_docstring)
        obj = self.object

        try:
            binding_class = make_class_ref(obj._binding_class)
        except AttributeError:
            binding_class = "<undefined>"
        self.add_line("|  XML binding class: %s\n" % binding_class, "<autoentity>")


class TypedFieldDocumenter(AttributeDocumenter):

    objtype = "attribute"
    priority = 99

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, fields.TypedField)

    def add_content(self, more_content, no_docstring=False):
        AttributeDocumenter.add_content(self, more_content, no_docstring)
        if self.object.multiple:
            self.add_line("|  (List of values permitted)", "<autoentity>")
        type_ = self.object.type_
        if type_:
            self.add_line("|  Type: %s\n" % make_class_ref(type_), "<autoentity>")
        self.add_line("|  XML Binding class name: ``%s``\n" % self.object.name, "<autoentity>")
        self.add_line("|  Dictionary key name: ``%s``\n" % self.object.key_name, "<autoentity>")


def setup(app):
    app.add_autodocumenter(EntityDocumenter)
    app.add_autodocumenter(TypedFieldDocumenter)
