# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin, FrontendEditableAdmin

from .models import News


class NewsAdmin(FrontendEditableAdmin, PlaceholderAdmin):
    pass


admin.site.register(News, NewsAdmin)