import datetime
import time

from django.http import JsonResponse
from django.shortcuts import render
import collections
from web import models
from django.db.models import Count


def dashboard(request, project_id):
    """概览"""
    # 项目状态
    status_dict = collections.OrderedDict()

    for key, text in sorted(models.Issues.status_choices):
        status_dict[key] = {'text': text, 'count': 0}

    issues_data = models.Issues.objects.filter(project_id=project_id).values('status').annotate(ct=Count('id'))

    for item in issues_data:
        status_dict[item['status']]['count'] = item['ct']

    join_user = models.ProjectUser.objects.filter(project_id=project_id).values_list('user_id', 'user__nickname')

    top_ten = models.Issues.objects.filter(project_id=project_id, assign__isnull=False).order_by('-id')[0:10]

    context = {
        'status_dict': status_dict,
        'join_user': join_user,
        'top_ten': top_ten
    }

    return render(request, 'web/dashboard.html', context)


def issues_chart(request, project_id):
    """ 在概览页面生成highcharts所需的数据 """
    today = datetime.datetime.now().date()
    date_dict = collections.OrderedDict()
    for i in range(0, 30):
        date = today - datetime.timedelta(days=i)
        date_dict[date.strftime("%Y-%m-%d")] = [time.mktime(date.timetuple()) * 1000, 0]

    # select xxxx,1 as ctime from xxxx
    # select id,name,email from table;
    # select id,name, strftime("%Y-%m-%d",create_datetime) as ctime from table;
    # "DATE_FORMAT(web_transaction.create_datetime,'%%Y-%%m-%%d')"
    result = models.Issues.objects.filter(project_id=project_id,
                                          create_datetime__gte=today - datetime.timedelta(days=30)).extra(
        select={'ctime': "strftime('%%Y-%%m-%%d',web_issues.create_datetime)"}).values('ctime').annotate(ct=Count('id'))

    for item in result:
        date_dict[item['ctime']][1] = item['ct']

    return JsonResponse({'status': True, 'data': list(date_dict.values())})
