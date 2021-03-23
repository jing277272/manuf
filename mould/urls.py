from django.conf.urls import url, include
from mould.views import resume, mould
urlpatterns = [
    url(r'^listmould', mould.listmoulds, name='mould'),
    url(r'^resume/(?P<tool_no>\d+)/$',resume.resume,name='resume'),
    url(r'^resume/(\d*)$', resume.resume_list),
    url(r'^scearch/$',mould.search1,name='search1'),
    url(r'^repairparts/(?P<tool_id>\d+)/$',mould.r_parts,name='r_parts'),
    

    # 路由分发


]