from django.conf.urls import url, include
from welding.views import wsearch
urlpatterns = [
    url(r'^wsearch/$', wsearch, name='wsearch'),
    # 路由分发


]