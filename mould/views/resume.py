from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helpers import get_page_list, ajax_required
import rander as rander
from mould.models import Mould


# 创建模具档案

def resume_list(request, pagenum):
    resumes = Mould.objects.all().order_by('-modify_time')
    paginator = Paginator(resumes, 20)
    page = paginator.page(pagenum)

    data = {
        'page': page,
        'pagerange': paginator.page_range,
        'currentpage': page.numer,
        'resumes': resumes,

    }
    return rander(request, 'mould/resume.html', context=data)


# 模具档案
def resume(request, tool_no):
    if request.method == 'GET':
        dsm = tool_no
        mould = Mould.objects.filter(tool_no = dsm)
        print(mould)
    return rander(request, 'mould/resume.html', {'mould':mould})
def ResumeEdit(request):
    pass
