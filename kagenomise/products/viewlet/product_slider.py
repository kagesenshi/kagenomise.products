from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from kagenomise.products.interfaces import IBaseProduct
from plone.app.layout.viewlets import interfaces as manager
from kagenomise.products.interfaces import IProductSpecific
from Products.ATContentTypes.interfaces.image import IATImage

grok.templatedir('templates')

class ProductSlider(grok.Viewlet):
    grok.context(IBaseProduct)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.template('product_slider')
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def images(self):
        catalog = self.context.portal_catalog
        results = []
        for brain in catalog(object_provides=IATImage.__identifier__,
                path={'query': '/'.join(self.context.getPhysicalPath()),
                    'depth': 2}):
            obj = brain.getObject()
            scales = obj.restrictedTraverse('@@images')
            thumb_scale = scales.scale('image', height=100, width=100,
                    direction="down")
            slide_scale = scales.scale('image',scale='preview')
            results.append({
                'url': obj.absolute_url(),
                'thumb_tag': thumb_scale.tag(),
                'thumb_url': thumb_scale.url,
                'slide_url': slide_scale.url
            })

        return results
