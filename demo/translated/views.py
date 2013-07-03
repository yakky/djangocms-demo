    # -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import TransNews


class IndexView(generic.ListView):
    model = TransNews
    template_name = 'transnews/index.html'
    context_object_name = 'news_list'


class DetailView(generic.DetailView):
    model = TransNews
    template_name = 'transnews/detail.html'
    context_object_name = 'news'

