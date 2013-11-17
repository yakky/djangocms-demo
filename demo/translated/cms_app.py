# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class TransNewsApphook(CMSApp):
    name = _("TransNews Apphook")
    urls = ["demo.translated.urls"]

apphook_pool.register(TransNewsApphook)