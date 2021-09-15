import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from web import models
from web.forms.issues import IssuesModelForm, IssuesReplyModelForm, IssuesInviteModelForm
from utils.encrypt import uid
from django.utils.safestring import mark_safe
from utils.pagination import Pagination


def die_list(request):
    context={}
    pass
    return render(request, 'testing/dashboard.html', context)

