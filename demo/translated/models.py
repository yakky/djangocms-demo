# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

class TransNews(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        slug=models.SlugField(max_length=255)
    )

    body = PlaceholderField('transbody')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('transnews:detail', (self.pk,),)

class TransNewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)