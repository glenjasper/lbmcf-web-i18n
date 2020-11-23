from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import (
    News,
    EventPhoto,
)

class NewsAllView(ListView):
    model = News
    queryset = News.objects.all().filter(status = True)
    template_name = "news/news_all.html"
    context_object_name = "context_newsall"

class NewsDetailView(ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "context_newsdetail"

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        queryset = self.model.objects.all()
        return queryset.filter(id = pk)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)

        # EventPhoto context
        query_eventphotos = EventPhoto.objects.filter(status = True, news__pk = pk).select_related()
        context['context_eventphotos'] = query_eventphotos

        return context
