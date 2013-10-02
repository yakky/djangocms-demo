# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    abstract = HTMLField(blank=True)

    body = PlaceholderField('newsbody')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsdetail', kwargs={'slug': self.slug})


class NewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)