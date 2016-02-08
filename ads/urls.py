from django.conf.urls import url

from .views import AdDetailVew

urlpatterns = [
    url(r'^ad/(?P<pk>\d+)/', AdDetailVew.as_view(), name='ad_detail'),
]
