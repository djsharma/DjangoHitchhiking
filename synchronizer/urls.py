from django.conf.urls import include, url
from synchronizer.views import basic  
urlpatterns = [
    url(r'^test/$', basic),
]
