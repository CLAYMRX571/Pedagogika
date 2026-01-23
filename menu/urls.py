"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from apps.home.views import Homeviews, lan_switch
from apps.about.views import Aboutviews, lan_switch_about
from apps.contact.views import Contactviews, lan_switch_contact
from apps.gallery.views import Galleryviews, lan_switch_gallery
from apps.services.views import Servicesviews, lan_switch_services
from apps.team.views import Teamviews, lan_switch_team
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/about/<str:lan>/', lan_switch_about, name='lan_switch_about'),
    path('lan/contact/<str:lan>/', lan_switch_contact, name='lan_switch_contact'),
    path('lan/gallery/<str:lan>/', lan_switch_gallery, name='lan_switch_gallery'),
    path('lan/services/<str:lan>/', lan_switch_services, name='lan_switch_services'),
    path('lan/team/<str:lan>/', lan_switch_team, name='lan_switch_team'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', Homeviews, name='home'),
    path('about/', Aboutviews, name='about'),
    path('contact/', Contactviews, name='contact'),
    path('gallery/', Galleryviews, name='gallery'),
    path('services/', Servicesviews, name='services'),
    path('team/', Teamviews, name='team'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
