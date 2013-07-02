# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

from .models import TransNews


class NewsAdmin(TranslatableAdmin, PlaceholderAdmin):
    pass


admin.site.register(TransNews, NewsAdmin)