import rander as rander
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helpers import get_page_list, ajax_required
from utils.pagination import Pagination
from django.shortcuts import render
from mould.models import Item, Mould ,RepairParts
from django.db.models import Q

def scearch1(request):
    
    if request.method == 'POST':
        return render(request, 'web/index.html')
    A1 = request.GET.get('local_mould_id')
    A2 = request.GET.get('local_part_no')

    if A1:
        print("A1")
        search_result = Mould.objects.filter(tool_no__contains=A1)
        print(search_result)
        return render(request,'web/search_result.html',{'search_result':search_result}) 
        
    if A2:
        print("A2")
        search_result = Mould.objects.filter(part_no__contains=A2)
        print(search_result)
        return render(request,'web/search_result.html',{'search_result':search_result}) 
      
    error_msg = "出错了！没有找到查询结果，请输入正确的信息"
    return render(request,'web/search_result.html',locals()) 



   
##在库备件查询
def r_parts(request, tool_id):
    # 分页获取数据
    queryset = RepairParts.objects.filter(tool_id=tool_id)
    mould = Mould.objects.filter(id = tool_id).values('name')
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


    error_msg = "出错了！没有模具在库信息！"
    return render(request,'web/search_result.html',locals()) 

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
        search_result =  Mould.objects.filter(Q(part_no__contains=A2)).first()
        print(search_result)
        return render(request,'web/search_result.html',locals())
    elif not (B1 or B2):
        S1=  models.Mould.objects.filter(Q(tool_No=B1) | Q(part_No=B2)).first()
        search_result =  models.RepairParts.objects.filter(Q(tool=S1)).first()
        return render(request,'web/search_result.html',locals())
    elif not (Parts_D or Parts_L or Parts_p or Parts_W):
        pass
    else:
        error_msg = "您需要输入想要搜索的内容"
        return render(request,'web/search_result.html',locals())


# 创建模具档案

def listmoulds(request):
    qs = Mould.objects.values()
    print (qs)
    return render(request, 'mould/home.html')


# 模具档案
def resume(request):
    pass


def ResumeEdit(request):
    pass
