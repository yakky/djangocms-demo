# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from .models import NewsPlugin, News


class NewsListPlugin(CMSPluginBase):
    name = _(u"News items")
    model = NewsPlugin
    render_template = "news/news_plugin.html"
    module = _('Demo')
    admin_preview = False

    def render(self, context, instance, placeholder):
        context.update({
            'newslist': News.objects.all()[:instance.items],
            'instance': instance,
            'placeholder': placeholder,
        })
        return context
plugin_pool.register_plugin(NewsListPlugin)
