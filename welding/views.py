from django.shortcuts import render
import datetime
import time

from django.http import JsonResponse
import collections
import rander as rander

from welding.models import Parameters, Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helpers import get_page_list, ajax_required
from utils.pagination import Pagination
from django.db.models import Q


def wsearch(request):

    if request.method == 'POST':
        return render(request, 'web/index.html')
    A1 = request.GET.get('equipment')
    A2 = request.GET.get('part_no')

    if A1:
        print("A1"+A1)

        eqs = Parameters.objects.filter(equipment=A1).values("id")
        print(eqs)
        search_result = []
        cc = []
        for part in eqs:
            x = part.values()
            print(cc)
            print(x)
            cc.append(x)
        print(cc)
        for x in cc:
            id = int(x)
            search = Recipe.objects.get(id=id)

            search_result.append[search]
        print(search_result)
        return render(request, 'welding/search_result.html', {'search_result': search_result})

    if A2:
        print("A2")
        search_result = Recipe.objects.filter(part_no__contains=A2)
        print(search_result)
        return render(request, 'welding/search_result.html', {'search_result': search_result})

    error_msg = "出错了！没有找到查询结果，请输入正确的信息"
    print(locals())
    return render(request, 'welding/search_result.html', locals())
# Create your views here.
