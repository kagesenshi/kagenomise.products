from zope.interface import Interface
from zope import schema
from plone.directives import form
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from kagenomise.products.vocabulary import ProductImageSource

class IProductSpecific(Interface):
    pass

class IBaseProduct(form.Schema):

    currency = schema.Choice(
        title=u'Currency',
        vocabulary='kagenomise.products.currency'
    )

    price = schema.Int(
        title=u'Price',
        default=0,
    )

    weight = schema.Int(
        title=u'Weight (in grams)',
        default=0,
    )

    primary_image = RelationChoice(
        title=u'Primary image',
        required=False,
        source=ProductImageSource()
    )
