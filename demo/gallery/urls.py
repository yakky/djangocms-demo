# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import View

urlpatterns = patterns('',
    url(r'^$', View.as_view()),
) 
