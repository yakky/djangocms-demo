# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import AbstractText


class TextModel(CMSPlugin):
    title = models.CharField(max_length=100)
    body = HTMLField(blank=True)


class TextModel2(AbstractText):
    title = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = FilerImageField(null=True, blank=True, related_name='logo')
    disclaimer = FilerFileField(null=True, blank=True)
