from django.urls import path
from . import views

urlpatterns = [
    path(
        route = '<int:page_id>/<slug:page_title>',
        view = views.get_page,
        name = 'url_pages'
    ),
    path(
        route = 'update/<int:pk>/',
        view = views.LegalUpdate.as_view(),
        name = 'url_legal_update'
    ),
]
