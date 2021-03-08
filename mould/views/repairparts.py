from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')


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


    error_msg = "出错了！没有备件在库信息！"
    return render(request,'mould/search_result.html',locals()) 