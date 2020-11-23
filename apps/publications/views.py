from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from .models import (
    Paper,
)
from datetime import date

class PaperView(ListView):
    model = Paper
    template_name = "publications/papers.html"
    context_object_name = "context_papers"

class PaperYearView(ListView):
    model = Paper
    template_name = "publications/papers.html"
    context_object_name = "context_papers"

    def get_queryset(self, **kwargs):
        slug_year = self.kwargs.get('year', None)
        queryset = self.model.objects.all()
        return queryset.filter(published__range = (date(int(slug_year), 1, 1), date(int(slug_year), 12, 31)))
        #return self.model.objects.filter(published__range = (date(int(slug_year), 1, 1), date(int(slug_year), 12, 31)))

class PaperYearView_(DetailView):
    model = Paper
    # pk_url_kwarg = "id"
    slug_url_kwarg = "year"
    template_name = "publications/papers.html"
    context_object_name = "context_papers"

    def get_object(self, queryset = None):
        if queryset is None:
            queryset = self.get_queryset()

        slug_year = self.kwargs.get(self.slug_url_kwarg, None)
        if slug_year is not None:
            queryset = queryset.filter(published__range = (date(int(slug_year), 1, 1), date(int(slug_year), 12, 31)))

        return queryset.all()

'''
    Entry.objects.filter(blog_id=4)
    Entry.objects.all().filter(pub_date__year=2006)
    Entry.objects.filter(pub_date__year=2006)
    Entry.objects.filter(pub_date__lte='2006-01-01')
    # SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
    Entry.objects.get(headline__exact="Cat bites dog")
    Blog.objects.get(id=14)

    MyModel.objects
        .filter(row_id__in=[15,17])\
        .distinct()\
        .values('user_id')\
        .annotate(user_count=Count('user_id'))\
        .filter(user_count__gt=1)\
        .order_by('user_id')

    SELECT DISTINCT user_id, COUNT(*)
    FROM my_model 
    WHERE tag_id = 15 OR tag_id = 17
    GROUP BY user_id 
    HAVING COUNT(*) > 1
'''
