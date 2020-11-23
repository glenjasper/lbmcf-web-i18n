from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'newsdetail/<int:pk>/',
        view = views.NewsDetailView.as_view(),
        name = 'url_newsdetail'
    ),
    path(
        route = 'newsall/',
        view = views.NewsAllView.as_view(),
        name = 'url_newsall'
    ),
]
