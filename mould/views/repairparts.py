from django.shortcuts import render
from mould.forms.repairparts import RepairpartsModelForm
from utils.pagination import Pagination
from django.http import HttpResponse, JsonResponse, request
from mould.models import Mould, RepairParts


def index(request):
    return render(request, 'web/index.html')


# 在库备件查询
def r_parts(request, tool_id):
    if request.method == 'GET':
        # 分页获取数据
        queryset = RepairParts.objects.filter(tool_id=tool_id, quantity__gt=0)
        moulds = Mould.objects.filter(id=tool_id)  # .values('name')
        print(tool_id)

        if queryset:
            page_object = Pagination(
                current_page=request.GET.get('page'),
                all_count=queryset.count(),
                base_url=request.path_info,
                query_params=request.GET,
            )

            mould_object_list = queryset[page_object.start:page_object.end]

            context = {
                'tool_id': tool_id,
                'mould': moulds,
                'search_result': mould_object_list,
                'page_html': page_object.page_html(),
            }
            return render(request, 'mould/repair.html', context)

        error_msg = "出错了！没有备件在库信息！"

        return render(request, 'mould/repair.html', locals())
    form = RepairpartsModelForm(request, data=request.POST)
    if form.is_valid():

        return JsonResponse({'status': True, })
    return JsonResponse({'status': False, 'error': form.errors})


def add_rpart(request, tool_id):
    if request.method == 'GET':
        print('tool_id')
        print(request.GET)
        form = RepairpartsModelForm()
        return render(request, 'mould/r_parts.html', {'form': form})
    print('post')
    print(request.POST)
    form = RepairpartsModelForm(request,data=request.POST)
    if form.is_valid():
        form.instance.tool_id = request.tool_id
        form.instance.modify = request.web.user
        form.save()
        return JsonResponse({'status': True, })
    return JsonResponse({'status': False, 'error': form.errors})


def none_rparts(request):
    pass
    context =  "查询失败"
    return HttpResponse(context)
