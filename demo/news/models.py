# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from django.db import models
from cms.models.fields import PlaceholderField


class News(models.Model):
    title = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255)

    body = PlaceholderField('newsbody')

    def __unicode__(self):
        return self.title
