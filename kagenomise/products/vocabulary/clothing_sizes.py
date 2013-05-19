from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class ClothingSizes(grok.GlobalUtility):
    grok.name('kagenomise.products.clothing_sizes')
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(
            ['S','M','L','XL','XXL', 'XXXL']
        )
