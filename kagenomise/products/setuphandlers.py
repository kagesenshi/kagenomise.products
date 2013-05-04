from collective.grok import gs
from kagenomise.products import MessageFactory as _

@gs.importstep(
    name=u'kagenomise.products', 
    title=_('kagenomise.products import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('kagenomise.products.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
