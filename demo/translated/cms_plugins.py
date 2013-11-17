# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from .models import TransNewsPlugin, TransNews


class TransNewsListPlugin(CMSPluginBase):
    name = _(u"Translated news items")
    model = TransNewsPlugin
    render_template = "transnews/news_plugin.html"
    module = _('Demo')
    admin_preview = False

    def render(self, context, instance, placeholder):
        context.update({
            'newslist': TransNews.objects.all()[:instance.items],
            'instance': instance,
            'placeholder': placeholder,
        })
        return context
plugin_pool.register_plugin(TransNewsListPlugin)
