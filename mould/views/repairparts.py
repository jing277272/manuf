from django.shortcuts import render , redirect
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
        mould_object = Mould.objects.filter(id=tool_id).first()  # .values('name')
        '''print(tool_id)'''
        form = RepairpartsModelForm(request)

        if queryset:
            page_object = Pagination(
                current_page=request.GET.get('page'),
                all_count=queryset.count(),
                base_url=request.path_info,
                query_params=request.GET,
                per_page=9
            )

            rparts_object_list = queryset[page_object.start:page_object.end]
            print(mould_object)

            

            context = {
                'tool_id': tool_id,
                'mould': mould_object,
                'search_result': rparts_object_list,
                'page_html': page_object.page_html(),
                'form': form,
            }
            return render(request, 'mould/repair.html', context)

        error_msg = "出错了！没有备件在库信息！"


        return render(request, 'mould/repair.html', locals())
     # 备件出库
    print('Post')
    tool_id = request.POST.get('tool_id')
    rpartid= request.POST.get('rpartid')
    used=  request.POST.get('use')
    print(used)
    oldquantity = RepairParts.objects.get(id=rpartid).quantity
    
    newquantity= int(oldquantity) - int(used)
    print(newquantity)
    RepairParts.objects.filter(id=rpartid).update(quantity=newquantity)
    context = {
                'tool_id': tool_id,
            }

    return redirect('r_parts',tool_id=tool_id,)
    


def add_rpart(request, tool_id):
    if request.method == 'GET':
        print(request.GET)

        context = {
                'tool_id': tool_id,
                'form': RepairpartsModelForm(request),
            }
        
        return render(request, 'mould/a_rparts.html',context)

        form = RepairpartsModelForm()
        return render(request, 'mould/a_rparts.html', {'form': form})
    print('post')
    #获得上传的文件
    pic = request.FILES.get('imgs')
    print(pic)

    print(request.FILES)
    print(tool_id)
    form = RepairpartsModelForm(request,data=request.POST)
    if form.is_valid():
        print('post成功')
        form.instance.tool_id = tool_id
        form.instance.modify = request.web.user
        form.instance.imgs = request.FILES
        form.save()
        return JsonResponse({'status': True, })
    return JsonResponse({'status': False, 'error': form.errors})


def none_rparts(request):
    pass
    context =  "查询失败"
    return HttpResponse(context)
