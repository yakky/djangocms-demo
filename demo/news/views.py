# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import News


class IndexView(generic.ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news_list'


class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'

