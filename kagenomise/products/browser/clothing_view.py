from five import grok
from plone.directives import dexterity, form
from kagenomise.products.content.clothing import IClothing

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IClothing)
    grok.require('zope2.View')
    grok.template('clothing_view')
    grok.name('view')

    def item_path(self):
        return '/'.join(self.context.getPhysicalPath())
