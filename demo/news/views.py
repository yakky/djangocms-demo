# -*- coding: utf-8 -*-
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

