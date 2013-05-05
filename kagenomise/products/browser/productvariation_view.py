from five import grok
from plone.directives import dexterity, form
from kagenomise.products.content.productvariation import IProductVariation

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IProductVariation)
    grok.require('zope2.View')
    grok.template('productvariation_view')
    grok.name('view')

