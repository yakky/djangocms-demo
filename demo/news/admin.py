# -*- coding: utf-8 -*-
from django.contrib import admin
from adminsortable.admin import SortableInlineAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdmin, FrontendEditableAdmin

from .models import News, SortableModel

class OtherAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = SortableModel


class NewsAdmin(FrontendEditableAdmin, PlaceholderAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (OtherAdmin,)


admin.site.register(News, NewsAdmin)