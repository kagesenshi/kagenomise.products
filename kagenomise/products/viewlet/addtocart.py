from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from kagenomise.products.interfaces import IProductSpecific, IBaseProduct

grok.templatedir('templates')

class AddToCart(grok.Viewlet):
    grok.context(IBaseProduct)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.name('kagenomise.products.addtocart')
    grok.template('addtocart')
    grok.layer(IProductSpecific)

    def available(self):
        return True
