from django.db.models.expressions import Value
from web import models
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

    Ae = request.GET.get('equipment')

    A2 = request.GET.get('part_no')

    if Ae:
        eqs = Parameters.objects.filter(equipment__contains=Ae).values(
            'equipment').distinct().order_by('equipment')
        print(eqs)
        count = eqs.count()
        if count == 0:
            error_msg = "抱歉！没有找到查询结果!"
            print(locals())
            return render(request, 'welding/search_result.html', locals())
        eqsl = []
        for e in eqs:
            print(e)
            s = e['equipment']
            print(s)
            eqsl.append(Parameters.objects.filter(equipment=s).first())
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=len(eqsl),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=12,
            pager_page_count=7,

        )
        print(eqsl)

        eq_object_list = eqs[page_object.start:page_object.end]

        context = {

            'eq': eqsl,
            'page_html': page_object.page_html(),
            'count': count
        }
        return render(request, 'welding/search_result.html', context)

    if A2:
        print("A2")
        search_result = Recipe.objects.filter(part_no__contains=A2)
        count = search_result.count()
        if count == 0:
            error_msg = "抱歉！没有找到查询结果!"
            print(locals())
            return render(request, 'welding/search_result.html', locals())
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=search_result.count(),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=12,
            pager_page_count=7,

        )

        welding_object_list = search_result[page_object.start:page_object.end]

        context = {

            'search_result': welding_object_list,
            'page_html': page_object.page_html(),
            'count': count
        }
        return render(request, 'welding/search_result.html', context)

    error_msg = "出错了！没有找到查询结果，请输入正确的信息"
    print(locals())
    return render(request, 'welding/search_result.html', locals())
# Create your views here.


def r(request, recipe_id):
    if request.method == 'POST':
        return render(request, 'web/index.html')

    recipe_result = Recipe.objects.filter(id=recipe_id).first

    search_result = Parameters.objects.filter(recipe__id=recipe_id)
    count = search_result.count()
    if count == 0:
        error_msg = "抱歉！没有找到查询结果!"
        print(locals())
        return render(request, 'welding/search_r.html', locals())
    page_object = Pagination(
        current_page=request.GET.get('page'),
        all_count=search_result.count(),
        base_url=request.path_info,
        query_params=request.GET,
        per_page=12,
        pager_page_count=7,

    )

    r_search_result = search_result[page_object.start:page_object.end]

    context = {
        'sr': recipe_result,
        'search_result': r_search_result,
        'page_html': page_object.page_html(),
        'count': count
    }

    return render(request, 'welding/search_r.html', context)


def p(request):
    if request.method == 'POST':
        return render(request, 'web/index.html')
    pass
    context = {
        
    }

    return render(request, 'welding/search_p.html',context)
