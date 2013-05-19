from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from kagenomise.products import MessageFactory as _
from kagenomise.products.interfaces import IBaseProduct
from kagenomise.orders.interfaces import IOrderTitle

# Interface class; used to define content-type schema.

class IClothing(form.Schema, IImageScaleTraversable, IBaseProduct):
    """
    Description of the Example Type
    """

    available_colors = schema.List(
        title=u'Available Colors',
        description=u'Available color codes (eg: #ffffff, #000000), one each line',
        value_type=schema.TextLine(),
    )

    available_sizes = schema.List(
        title=u'Available Sizes',
        description=u'Available sizes for clothing',
        value_type=schema.Choice(
            vocabulary='kagenomise.products.clothing_sizes'
        )
    )


class ClothingTitle(grok.Adapter):
    grok.context(IClothing)
    grok.implements(IOrderTitle)
    
    def __init__(self, context):
        self.context = context

    def getTitle(self, data):
        return '%s (%s)' % (self.context.Title(), data['size'])

