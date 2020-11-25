from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'list/',
        view = views.ControllerView.as_view(),
        name = 'url_controller_list'
    ),
    path(
        route = 'update/<int:pk>/',
        view = views.ControllerUpdateView.as_view(),
        name = 'url_controller_update'
    ),
    path(
        route = 'list/updated_list/',
        view = views.fun_controllers,
        name = 'url_controllers_updated'
    ),
]
