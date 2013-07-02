# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class TransNewsToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("applications", _('Apps'))
        position = 0
        menu = admin_menu.get_or_create_menu('transnews-menu', _('Translated News'), position=position)
        url = reverse('admin:translated_transnews_changelist')
        menu.add_sideframe_item(_('Translated news list'), url=url)
        url = reverse('admin:translated_transnews_add')
        menu.add_modal_item(_('Translated news add'), url=url)
        admin_menu.add_break('transnews-break', position=menu)