# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import FrontendEditableAdmin
from .models import *


class ImagesSupersizeInline(admin.TabularInline):
    model = ImageSuperSizedGallery


class SuperSizedGalleryAdmin(FrontendEditableAdmin, admin.ModelAdmin):
    inlines = [ImagesSupersizeInline]


admin.site.register(ImageSuperSizedGallery)
admin.site.register(SuperSizedGallery, SuperSizedGalleryAdmin) 
