from django.urls import re_path
from . import views

app_name = "app01"
urlpatterns = [
    #url(r'^test1/$', findinfo, name='test1'), 
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/ajax/avatar/$', views.ajax_avatar_upload,
            name='ajax_avatar_upload'),

    # 路由分发


]



