# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


from .models import News

class NewsMenu(CMSAttachMenu):

    name = _("news menu")

    def get_nodes(self, request):
        nodes = []
        for category in News.objects.all():
            node = NavigationNode(
                category.title,
                category.get_absolute_url(),
                category.pk
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(NewsMenu)