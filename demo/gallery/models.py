# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin


class SuperSizedGallery(CMSPlugin):
    height = models.SmallIntegerField(_("height"),default=200)
    width = models.SmallIntegerField(_("width"), default=300)
    thumb_height = models.SmallIntegerField(_("thumbnail height"), null=True,
                                            blank=True, default=None,
                                            help_text=_('Leave empty for no thumbs.'))
    thumb_width = models.SmallIntegerField(_("thumbnail width"),null=True,
                                           blank=True, default=None,
                                           help_text=_('Leave empty for no thumbs.'))


class ImageSuperSizedGallery(models.Model):
    plugin = models.ForeignKey(SuperSizedGallery, related_name="imagens")
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=("image")) 
