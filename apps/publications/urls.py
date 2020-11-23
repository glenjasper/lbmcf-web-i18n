from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'papers/',
        view = views.PaperView.as_view(),
        name = 'url_papers'
    ),
    path(
        route = 'papers/<slug:year>/',
        view = views.PaperYearView.as_view(),
        name = 'url_papersyear'
    ),
]
