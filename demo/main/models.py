# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import AbstractText


class TextModel(CMSPlugin):
    title = models.CharField(max_length=100)
    body = HTMLField(blank=True)

class TextModel2(AbstractText):
    title = models.CharField(max_length=100)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^djangocms_text_ckeditor\.fields\.HTMLField'])
except ImportError:
    pass