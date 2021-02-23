from django.conf.urls import url, include
from mould.views import resume, mould
urlpatterns = [
    url(r'^listmould', mould.listmoulds, name='mould'),
    url(r'^resume/$', resume.resume_list, name='resume'),
    
    url(r'^resume/(\d*)$', resume.resume_list),
    url(r'^scearch1/$',mould.scearch1,name='scearch1'),
    url(r'^scearch1/r/(?P<tool_id>\d+)/$',mould.r_parts,name='r_parts'),
    
    url(r'^scearch3/$',mould.scearch3,name='scearch3'),

    # 路由分发


]