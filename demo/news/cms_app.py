# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from demo.news.menu import NewsMenu


class NewsApphook(CMSApp):
    name = _("News Apphook")
    urls = ["demo.news.urls"]
    menus = [NewsMenu]

apphook_pool.register(NewsApphook)