from datetime import datetime
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'news'

class Postinfo(DetailView):
    model = Post
    template_name = 'newsid.html'
    context_object_name = 'newsid'
    pk_url_kwarg = 'id'




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"

        return context







from django.shortcuts import render

# Create your views here.
