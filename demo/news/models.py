    # -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    abstract = HTMLField(blank=True)

    body = PlaceholderField('newsbody')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('newsapp:detail', (self.pk,),)

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = FilerImageField(null=True, blank=True, related_name='logo')
    disclaimer = FilerFileField(null=True, blank=True)

class NewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^djangocms_text_ckeditor\.fields\.HTMLField'])
except ImportError:
    pass
