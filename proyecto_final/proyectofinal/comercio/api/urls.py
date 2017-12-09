from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import BurritosListAPIView
#from comercio.views import BurritosListView

urlpatterns = [
    url(r'^$', BurritosListAPIView.as_view(), name='list'),
    #url(r'^$', BurritosListView.as_view(), name = 'BurritoList'),


]
