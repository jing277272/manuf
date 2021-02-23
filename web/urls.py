from django.conf.urls import url
from django.conf import settings
from mould.views.resume import resume
from web.views import account, home, project, wiki, file, setting, issues, dashboard, statistics
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^account/change/name', account.change_name, name='changename'),
    url(r'^account/changepwd', account.change_pwd, name='changepwd'),
    url(r'^logout/', account.logout, name='logout'),
    url(r'^image/code/', account.image_code, name='image_code'),
    url(r'mould/cread', resume, name='resume'),
    path('', home.index, name='index'),  # 默认首页

    # 项目列表
    url(r'^project/list/', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$',
        project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$',
        project.project_unstar, name='project_unstar'),


    # 项目管理
    # 路由分发
    url(r'^manage/(?P<project_id>\d+)/', include([

        url(r'^wiki/$', wiki.wiki, name='wiki'),
        url(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),
        url(r'^wiki/delete/(?P<wiki_id>\d+)/$',
            wiki.wiki_delete, name='wiki_delete'),
        url(r'^wiki/edit/(?P<wiki_id>\d+)/$', wiki.wiki_edit, name='wiki_edit'),
        url(r'^wiki/upload/', wiki.wiki_upload, name='wiki_upload'),
        url(r'^wiki/catalog/', wiki.wiki_catalog, name='wiki_catalog'),

        url(r'^file/$', file.file, name='file'),
        url(r'^file/delete/$', file.file_delete, name='file_delete'),
        url(r'^cos/credential/$', file.cos_credential, name='cos_credential'),
        url(r'^file/post/$', file.file_post, name='file_post'),
        url(r'^file/download/(?P<file_id>\d+)/$',
            file.file_download, name='file_download'),

        url(r'^setting/$', setting.setting, name='setting'),
        url(r'^setting/delete/$', setting.setting_delete, name='setting_delete'),

        url(r'^issues/$', issues.issues, name='issues'),
        url(r'^issues/detail/(?P<issues_id>\d+)/$',
            issues.issues_detail, name='issues_detail'),
        url(r'^issues/record/(?P<issues_id>\d+)/$',
            issues.issues_record, name='issues_record'),
        url(r'^issues/change/(?P<issues_id>\d+)/$',
            issues.issues_change, name='issues_change'),
        url(r'^issues/invite/url/$', issues.invite_url, name='invite_url'),

        url(r'^dashboard/$', dashboard.dashboard, name='dashboard'),
        url(r'^dashboard/issues/chart/$',
            dashboard.issues_chart, name='issues_chart'),

        url(r'^statistics/$', statistics.statistics, name='statistics'),
        url(r'^statistics/priority/$', statistics.statistics_priority,
            name='statistics_priority'),
        url(r'^statistics/project/user/$',
            statistics.statistics_project_user, name='statistics_project_user'),

    ], None)),
]
