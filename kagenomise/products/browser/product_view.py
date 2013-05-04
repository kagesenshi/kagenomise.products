from five import grok
from plone.directives import dexterity, form
from kagenomise.products.content.product import IProduct

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IProduct)
    grok.require('zope2.View')
    grok.template('product_view')
    grok.name('view')

