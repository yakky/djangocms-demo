# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser,  PermissionsMixin

from djangocms_text_ckeditor.models import AbstractText


class TextModel(AbstractText):
    title = models.CharField(max_length=100, default='', blank=True)


class MyUser(AbstractUser):
    date_of_birth = models.DateField(null=True)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True