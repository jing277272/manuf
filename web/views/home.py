from django.shortcuts import render
from django.db.models import Q
from mould import models
from web.models import Banner



def index(request):
    banner_list = Banner.objects.all()
    ctx = {'banner_list': banner_list,}
    return render(request, 'web/index.html',ctx)



