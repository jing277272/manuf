import datetime
import time

from django.http import JsonResponse
import collections
import rander as rander
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helpers import get_page_list, ajax_required
from utils.pagination import Pagination
from django.shortcuts import render
from mould.models import Mould, RepairParts
from django.db.models import Q


def search1(request):

    if request.method == 'POST':
        return render(request, 'web/index.html')
    A1 = request.GET.get('local_mould_id')
    A2 = request.GET.get('local_part_no')

    if A1:
        print("A1")
        search_result = Mould.objects.filter(tool_no__contains=A1)
        count = search_result.count()
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=search_result.count(),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=12,
            pager_page_count=7,

        )

        mould_object_list = search_result[page_object.start:page_object.end]

        context = {
            'search_result': mould_object_list,
            'page_html': page_object.page_html(),
            'count': count
        }
        return render(request, 'mould/search_result.html', context)
    if A2:
        print("A2")
        search_result = Mould.objects.filter(part_no__contains=A2)
        count = search_result.count()
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=search_result.count(),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=12,
            pager_page_count=7,

        )

        mould_object_list = search_result[page_object.start:page_object.end]

        context = {
            'search_result': mould_object_list,
            'page_html': page_object.page_html(),
            'count': count
        }
        return render(request, 'mould/search_result.html', context)
    else:
        error_msg = "对不起！没有找到查询结果!"
        print(locals())
    return render(request,'mould/search_result.html',locals()) 


# 在库备件查询


def r_parts(request, tool_id):
    # 分页获取数据
    queryset = RepairParts.objects.filter(tool_id=tool_id,quantity__gt=0)
    mould = Mould.objects.filter(id=tool_id).values('name')
    print(mould)
    if queryset:
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=queryset.count(),
            base_url=request.path_info,
            query_params=request.GET,
        )

        mould_object_list = queryset[page_object.start:page_object.end]

        context = {
            'mould': mould,

            'search_result': mould_object_list,
            'page_html': page_object.page_html(),

        }
        return render(request, 'mould/repair.html', context)

    error_msg = "出错了！没有备件在库信息！"
    return render(request, 'mould/repair.html', locals())


#form = IssuesModelForm(request, data=request.POST)
'''if form.is_valid():
    form.instance.project = request.web.project
    form.instance.creator = request.web.user
    # 保存
    form.save()
    return JsonResponse({'status': True, })
return JsonResponse({'status': False, 'error': form.errors})'''


def scearch3(request):

    if request.method != 'GET':
        return render(request, 'web/index.html')
    A1 = request.POST.get('local_mould_id')
    A2 = request.POST.get('local_part_no')
    B1 = request.POST.get('r_mould_id')
    B2 = request.POST.get('r_part_no')
    Parts_D = request.POST.get('P')
    Parts_L = request.POST.get('L')
    Parts_P = request.POST.get('P')
    Parts_W = request.POST.get('W')

    print("搜索关键词")
    if not (A1 or A2):
        search_result = Mould.objects.filter(Q(part_no__contains=A2)).first()
        print(search_result)
        return render(request, 'mould/search_result.html', locals())
    elif not (B1 or B2):
        S1 = models.Mould.objects.filter(Q(tool_no=B1) | Q(part_no=B2)).first()
        search_result = models.RepairParts.objects.filter(Q(tool=S1)).first()
        return render(request, 'mould/search_result.html', locals())
    elif not (Parts_D or Parts_L or Parts_p or Parts_W):
        pass
    else:
        error_msg = "您需要输入想要搜索的内容"
        return render(request, 'mould/search_result.html', locals())


# 创建模具档案

def listmoulds(request):
    qs = Mould.objects.values()
    print(qs)
    return render(request, 'mould/home.html')


def dashboard(request, project_id):
    """概览"""
    # 项目状态
    status_dict = collections.OrderedDict()

    for key, text in sorted(models.Issues.status_choices):
        status_dict[key] = {'text': text, 'count': 0}

    issues_data = models.Issues.objects.filter(
        project_id=project_id).values('status').annotate(ct=Count('id'))

    for item in issues_data:
        status_dict[item['status']]['count'] = item['ct']

    join_user = models.ProjectUser.objects.filter(
        project_id=project_id).values_list('user_id', 'user__nickname')

    top_ten = models.Issues.objects.filter(
        project_id=project_id, assign__isnull=False).order_by('-id')[0:10]

    context = {
        'status_dict': status_dict,
        'join_user': join_user,
        'top_ten': top_ten
    }
    print(join_user)
    return render(request, 'web/dashboard.html', context)


def fault_chart(request, project_id):
    """ 在概览页面生成highcharts所需的数据 """
    today = datetime.datetime.now().date()
    date_dict = collections.OrderedDict()
    for i in range(0, 30):
        date = today - datetime.timedelta(days=i)
        date_dict[date.strftime("%Y-%m-%d")
                  ] = [time.mktime(date.timetuple()) * 1000, 0]

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
