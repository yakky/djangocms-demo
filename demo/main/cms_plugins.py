# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase


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
