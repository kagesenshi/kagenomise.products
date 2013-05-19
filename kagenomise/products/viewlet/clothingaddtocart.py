from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from kagenomise.products.interfaces import IProductSpecific
from kagenomise.products.content.clothing import IClothing

grok.templatedir('templates')

class ClothingAddToCart(grok.Viewlet):
    grok.context(IClothing)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.name('kagenomise.products.addtocart')
    grok.template('clothingaddtocart')
    grok.layer(IProductSpecific)

    def available(self):
        return True
