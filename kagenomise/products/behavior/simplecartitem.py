from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from kagenomise.products import MessageFactory as _

class ISimpleCartItem(form.Schema):
    """
       Marker/Form interface for SimpleCartItem
    """

    # -*- Your Zope schema definitions here ... -*-

alsoProvides(ISimpleCartItem,IFormFieldProvider)

class SimpleCartItem(object):
    """
       Adapter for SimpleCartItem
    """
    implements(ISimpleCartItem)
    adapts(IDexterityContent)

    # list of attributes name to be delegated to context
    _delegated_attributes = [] 

    def __init__(self,context):
        self.context = context

    def __getattr__(self, key):
        if key in self._delegated_attributes:
            return getattr(self.context, key)
        raise AttributeError(key)
    
    def __setattr__(self, key, value):
        if key in self._delegated_attributes:
            setattr(self.context, key, value)
        self.__dict__[key] = value
        
    def __delattr__(self, key):
        if key in self._delegated_attributes:
            delattr(self.context, key)
        del self.__dict__[key]

    # -*- Your behavior property setters & getters here ... -*-
