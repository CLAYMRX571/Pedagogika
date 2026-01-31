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
# from apps.accounts.views import Accountsviews, lan_switch_account
from apps.brain.views import Brainviews, lan_switch_brain
from apps.handshake.views import Handshakeviews, lan_switch_handshake
from apps.health.views import Healthviews, lan_switch_health
from apps.home.views import Homeviews, lan_switch
from apps.model.views import Modelviews, lan_switch_model
from apps.multimedia.views import Multimediaviews, lan_switch_multimedia
from apps.monitor.views import Monitorviews, lan_switch_monitor
from apps.pedagogical.views import Pedagogicalviews, lan_switch_pedagogical
from apps.research.views import Researchviews, lan_switch_research
from apps.student.views import Studentviews, lan_switch_student
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # path('lan/accounts/<str:lan>/', lan_switch_a, name='lan_switch_about'),
    path('lan/brain/<str:lan>/', lan_switch_brain, name='lan_switch_brain'),
    path('lan/handshake/<str:lan>/', lan_switch_handshake, name='lan_switch_handshake'),
    path('lan/health/<str:lan>/', lan_switch_health, name='lan_switch_health'),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/model/<str:lan>/', lan_switch_model, name='lan_switch_model'),
    path('lan/monitor/<str:lan>/', lan_switch_monitor, name='lan_switch_monitor'),
    path('lan/multimedia/<str:lan>/', lan_switch_multimedia, name='lan_switch_multimedia'),
    path('lan/pedagogical/<str:lan>/', lan_switch_pedagogical, name='lan_switch_pedagogical'),
    path('lan/research/<str:lan>/', lan_switch_research, name='lan_switch_research'),
    path('lan/student/<str:lan>/', lan_switch_student, name='lan_switch_student'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # path('accounts/', Accountsviews, name='accounts'),
    path('brain/', Brainviews, name='brain'),
    path('handshake/', Handshakeviews, name='handshake'),
    path('health/', Healthviews, name='health'),
    path('', Homeviews, name='home'),
    path('model/', Modelviews, name='model'),
    path('monitor/', Monitorviews, name='monitor'),
    path('multimedia/', Multimediaviews, name='multimedia'),
    path('pedagogical/', Pedagogicalviews, name='pedagogical'),
    path('research/', Researchviews, name='research'),
    path('student/', Studentviews, name='student'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
