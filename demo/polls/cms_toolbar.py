# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK

from .models import Poll


@toolbar_pool.register
class PollToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("applications", _('Apps'))
        position = 0
        menu = admin_menu.get_or_create_menu('poll-menu', _('Polls'), position=position)
        url = reverse('admin:polls_poll_changelist')
        menu.add_sideframe_item(_('Poll overview'), url=url)
        url = reverse('admin:polls_poll_add')
        menu.add_modal_item(_('Poll add'), url=url)
        for poll in Poll.objects.all():
            url = reverse('admin:polls_poll_change', args=(poll.pk,))
            menu.add_modal_item(_('Modify poll "%s"' % poll), url=url)
        admin_menu.add_break('poll-break', position=menu)