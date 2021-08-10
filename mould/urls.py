from django.conf.urls import url, include
from mould.views import resume, mould, repairparts
urlpatterns = [
    url(r'^listmould', mould.listmoulds, name='mould'),
    url(r'^resume/(?P<tool_no>\d+)/$', resume.resume, name='resume'),
    url(r'^resume/(\d*)$', resume.resume_list),
    url(r'^search/$', mould.search1, name='search1'),
    url(r'^search3/$', repairparts.search3, name='search3'),
    url(r'^repairparts/(?P<tool_id>\d+)/$',
        repairparts.r_parts, name='r_parts'),
    url(r'^addrpart/(?P<tool_id>\d+)/$',
        repairparts.add_rpart, name='addrpart'),



    # 路由分发


]
