from django.conf.urls import url, include
from welding.views import wsearch
urlpatterns = [
    url(r'^wsearch/$', wsearch.wsearch, name='wsearch'),
    url(r'^wsearch/r/(?P<recipe_id>\d+)/$', wsearch.r, name='wsearch_r'),
    url(r'^wsearch/p/$', wsearch.p, name='wsearch_p'),


    # 路由分发


]