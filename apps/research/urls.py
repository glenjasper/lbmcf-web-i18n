from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'projects/',
        view = views.ProjectView.as_view(),
        name = 'url_projects'
    ),
    path(
        route = 'protocols/',
        view = views.ProtocolView.as_view(),
        name = 'url_protocols'
    ),
    path(
        route = 'files/',
        view = views.FileView.as_view(),
        name = 'url_files'
    ),
]
