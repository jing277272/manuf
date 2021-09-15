from django.conf.urls import url
from django.conf import settings
from testing.views import dashboard
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    url(r'^testing/$', dashboard.die_list, name='testing'),
    
]
