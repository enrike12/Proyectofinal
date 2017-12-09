"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from comercio import views
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserRegisterView
from comercio.views import BurritosListView
from comercio.views import BurritosDetailView, BurritosCreateView, BurritosUpdateView, BurritosDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.base, name = 'base'),
    url(r'^burritoss/create$',BurritosCreateView.as_view(), name = 'BurritoCreate'),
    url(r'^burritoss/detail/(?P<pk>[0-9]+)/edit$',BurritosUpdateView.as_view(), name = 'BurritoUpdate'),
    url(r'^burritoss/detail/(?P<pk>[0-9]+)/delete$',BurritosDeleteView.as_view(), name = 'BurritoDelete'),
    url(r'^burritoss/detail/(?P<id>[0-9]+)$',BurritosDetailView.as_view(), name = 'BurritoDetail'),
    url(r'^burritoss/list$', BurritosListView.as_view(), name = 'BurritoList'),
    url(r'^api/burritos/',include('comercio.api.urls', namespace='burritos-api')),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
