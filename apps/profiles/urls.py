from django.urls import path
from . import views

profiles_patterns = ([
    path(
        route = '',
        view = views.ProfileListView.as_view(),
        name = 'url_profile_list'
    ),
    path(
        route = '<username>/',
        view = views.ProfileDetailView.as_view(),
        name = 'url_profile_detail'
    ),
], 'profiles')
