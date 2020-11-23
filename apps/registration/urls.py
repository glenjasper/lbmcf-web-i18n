from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'signup/',
        view = views.SignUpView.as_view(),
        name = 'url_signup'
    ),
    path(
        route = 'profile/',
        view = views.ProfileUpdate.as_view(),
        name = 'url_profile'
    ),
    path(
        route = 'profile/email/',
        view = views.EmailUpdate.as_view(),
        name = 'url_profile_email'
    ),
]
