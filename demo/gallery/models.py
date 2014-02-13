from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin


class SuperSizedGallery(CMSPlugin):
    height = models.SmallIntegerField(("height"),default=200)
    width = models.SmallIntegerField(("width"), default=300)
    thumb_height = models.SmallIntegerField(("thumbnail height"), null=True, blank=True, default=None, help_text=('Leave empty for no thumbs.'))
    thumb_width = models.SmallIntegerField(("thumbnail width"),null=True, blank=True, default=None, help_text=('Leave empty for no thumbs.'))

class ImageSuperSizedGallery(models.Model):
    plugin = models.ForeignKey(SuperSizedGallery, related_name="imagens")
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=("image")) 
