# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import IndexView, DetailView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
)