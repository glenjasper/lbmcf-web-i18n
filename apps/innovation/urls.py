from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'patents/',
        view = views.PatentView.as_view(),
        name = 'url_patents'
    ),
]
