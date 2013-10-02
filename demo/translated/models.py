# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField


class TransNews(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        slug=models.SlugField(max_length=255)
    )
    non_tradotto = models.CharField(max_length=255, default='')

    body = PlaceholderField('transbody')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('transdetail', kwargs={'slug': self.slug})


class TransNewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)