# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import News


class NewsMenu(CMSAttachMenu):
    name = _("news menu")

    def get_nodes(self, request):
        nodes = []
        for item in News.objects.all():
            node = NavigationNode(
                item.title,
                item.get_absolute_url(),
                item.pk
            )
            nodes.append(node)
        return nodes
menu_pool.register_menu(NewsMenu)