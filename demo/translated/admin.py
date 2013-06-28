# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin

from .models import News


class NewsAdmin(PlaceholderAdmin):
    pass


admin.site.register(News, NewsAdmin)