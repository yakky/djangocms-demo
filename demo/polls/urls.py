# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import IndexView, DetailView, ResultsView, VoteView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', VoteView, name='vote'),
)