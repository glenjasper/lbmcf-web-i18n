from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'oldmembers/',
        view = views.OldMembersView.as_view(),
        name = 'url_oldmembers'
    ),
]
