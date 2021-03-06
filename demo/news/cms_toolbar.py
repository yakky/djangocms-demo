# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class NewsToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("applications", _('Apps'))
        position = 0
        menu = admin_menu.get_or_create_menu('news-menu', _('News'), position=position)
        url = reverse('admin:news_news_changelist')
        menu.add_sideframe_item(_('News overview'), url=url)
        url = reverse('admin:news_news_add')
        menu.add_modal_item(_('News add'), url=url)
        admin_menu.add_break('news-break', position=menu)