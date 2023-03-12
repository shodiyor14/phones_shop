from django.shortcuts import render
from news.models import NewsModel
from django.views.generic import ListView, DetailView


class NewsListView(ListView):
    template_name = 'news.html'
    queryset = NewsModel.objects.order_by('-pk')


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'newsdetail.html'