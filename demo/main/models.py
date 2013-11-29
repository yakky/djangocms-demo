# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import AbstractText


class TextModel(AbstractText):
    title = models.CharField(max_length=100, default='', blank=True)