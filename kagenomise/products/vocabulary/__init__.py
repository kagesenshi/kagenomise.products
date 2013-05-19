from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from plone.formwidget.contenttree import ObjPathSourceBinder
from Products.ATContentTypes.interfaces.image import IATImage

class ProductImageSource(object):
    grok.implements(IContextSourceBinder)

    def __call__(self, context):
        path = '/'.join(context.getPhysicalPath())
        return ObjPathSourceBinder(
            object_provides=IATImage.__identifier__,
            path={
                'query': path,
                'depth': 2
            }
        ).__call__(context)

class Currencies(grok.GlobalUtility):
    grok.name('kagenomise.products.currency')
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues([
            'MYR', 'USD'
        ])
