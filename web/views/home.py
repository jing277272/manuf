from django.shortcuts import render
from django.db.models import Q
from mould import models

def index(request):
    return render(request, 'web/index.html')



