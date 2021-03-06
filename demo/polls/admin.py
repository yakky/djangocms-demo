# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Poll, Choice
from cms.admin.placeholderadmin import FrontendEditableAdmin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(FrontendEditableAdmin, admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)