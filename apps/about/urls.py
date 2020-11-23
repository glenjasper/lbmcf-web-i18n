from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'update/<int:pk>/',
        view = views.AboutUpdate.as_view(),
        name = 'url_about_update'
    ),
]
