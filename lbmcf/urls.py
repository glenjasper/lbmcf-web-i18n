"""lbmcf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from apps.profiles.urls import profiles_patterns
from apps.messenger.urls import messenger_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(('apps.core.urls', 'core_app'), namespace = 'core_app')),
    path('members/', include(('apps.members.urls', 'members_app'), namespace = 'members_app')),
    path('research/', include(('apps.research.urls', 'research_app'), namespace = 'research_app')),
    path('publications/', include(('apps.publications.urls', 'publications_app'), namespace = 'publications_app')),
    path('legal/', include(('apps.legal.urls', 'legal_app'), namespace = 'legal_app')),
    path('contact/', include(('apps.contact.urls', 'contact_app'), namespace = 'contact_app')),
    path('about/', include(('apps.about.urls', 'about_app'), namespace = 'about_app')),
    path('news/', include(('apps.news.urls', 'news_app'), namespace = 'news_app')),
    path('innovation/', include(('apps.innovation.urls', 'innovation_app'), namespace = 'innovation_app')),
    path('profiles/', include(profiles_patterns, namespace = 'profiles_app')),
    path('messenger/', include(messenger_patterns, namespace = 'messenger_app')),
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls'))),
    path('accounts/', include(('apps.registration.urls', 'registration_app'), namespace = 'registration_app')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Custom titles for admin
admin.site.site_title = "LBMCF"
admin.site.site_header = "LBMCF"
# admin.site.index_title = "Painel de administração"
