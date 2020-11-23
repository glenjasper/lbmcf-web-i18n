from django.urls import path
from . import views

messenger_patterns = ([
    path(
        route = '',
        view = views.ThreadList.as_view(),
        name = 'url_messenger_list'),
    path(
        route = 'thread/<int:pk>/',
        view = views.ThreadDetail.as_view(),
        name = 'url_messenger_detail'),
    path(
        route = 'thread/<int:pk>/add/',
        view = views.add_message,
        name = 'url_messenger_add'),
    path(
        route = 'thread/start/<username>/',
        view = views.start_thread,
        name = 'url_messenger_start'),
], 'messenger')
