# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    abstract = HTMLField(blank=True)
    body = PlaceholderField('newsbody')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})


class SortableModel(models.Model):
    news = models.ForeignKey(News)
    others = models.ForeignKey(User)
    item = models.CharField(max_length=10)
    other = models.BooleanField()
    abstract = HTMLField(blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('position',)


class Other(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        app_label = "trythis"


class NewsPlugin(CMSPlugin):
    items = models.IntegerField(default=3)


class NewsPlugin2(CMSPlugin):
    items = models.IntegerField(default=3)

    class Meta:
        app_label = "trythis"


class NewsSelectedPlugin(CMSPlugin):
    items = models.ManyToManyField(News)

    def copy_relations(self, old_instance):
        self.items = old_instance.items.all()