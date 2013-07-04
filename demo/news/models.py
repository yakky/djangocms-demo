# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    abstract =models.TextField(default="")

    body = PlaceholderField('newsbody')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('newsapp:detail', (self.pk,),)


class NewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)