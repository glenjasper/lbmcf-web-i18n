from django.urls import path
from . import views

urlpatterns = [
    path(
        route = '',
        view = views.HomeView.as_view(),
        name = 'url_home'
    ),
]
