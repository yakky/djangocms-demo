# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK

from .models import Poll

@toolbar_pool.register
def poll_toolbar(toolbar, request, is_current_app, app_name):
    if not request.user.is_staff:
        return # no point in adding items the user can't access
    admin_menu = toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Site'))
    position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
    menu = admin_menu.get_or_create_menu('poll-menu', _('Polls'), position=position)
    url = reverse('admin:polls_poll_changelist')
    menu.add_sideframe_item(_('Poll overview'), url=url)
    url = reverse('admin:polls_poll_add')
    menu.add_modal_item(_('Poll add'), url=url)
    for poll in Poll.objects.all():
        url = reverse('admin:polls_poll_change', args=(poll.pk,))
        menu.add_modal_item(_('Modify poll "%s"' % poll), url=url)
    admin_menu.add_break('poll-break', position=menu)