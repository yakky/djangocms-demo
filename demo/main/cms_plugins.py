# -*- coding: utf-8 -*-
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from .models import *

class NestedPlugin(CMSPluginBase):
    name = _(u"Nested plugins")
    module = _('Demo')
    render_template = "demo/nested.html"
    admin_preview = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context
plugin_pool.register_plugin(NestedPlugin)

class CustomTextPlugin(CMSPluginBase):
    name = _(u"Custom text plugin")
    module = _('Demo')
    model = TextModel
    render_template = "demo/text.html"
    admin_preview = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context
plugin_pool.register_plugin(CustomTextPlugin)

class CustomText2Plugin(TextPlugin):
    name = _(u"Custom text 2 plugin")
    module = _('Demo')
    model = TextModel2
    render_template = "demo/text.html"
    admin_preview = False
    allow_children = True

plugin_pool.register_plugin(CustomText2Plugin)
