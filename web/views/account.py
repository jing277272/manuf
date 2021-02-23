from django.shortcuts import render, redirect
from web.forms.account import RegisterModelForm, SendSmsForm, LoginForm, ChangepwdForm, ChangeNicknameForm
from utils.image_code import check_code
from web import models
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, request
from io import BytesIO
from django.db.models import Q
from web.models import UserInfo
from django.template import RequestContext
from django.contrib import auth


# 注册、短信、登录、注销
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    print(request.GET)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库(密码转换成密文)
        instance = form.save()
    else:
        print(form.errors)
        return JsonResponse({'status': True, 'data': '/login/'})
    return JsonResponse({'status': False, 'error': form.errors})


# 发送短信
def send_sms(request):
    form = SendSmsForm(request, data=request.GET)
    # 单独校验手机号,不能为空，格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def login(request):
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'web/login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user_object = models.UserInfo.objects.filter(Q(username=username) | Q(mobile_phone=username)) \
            .filter(password=password).first()

        if user_object:
            # 登陆成功
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)
            return redirect('index')
        form.add_error('username', '用户名或密码错误')
    return render(request, 'web/login.html', {'form': form})


def image_code(request):
    # 生成图片验证码
    image_object, code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(60)  # 60秒过期
    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())


def change_name(request):
    redirect_to = request.GET.get('from', reverse('index'))

    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST, user=request.nickname)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            profile, created = UserInfo.objects.get_or_create(
                user=request.user)
            UserInfo.nickname = nickname_new
            UserInfo.save()
            return redirect(redirect_to)
    else:
        form = ChangeNicknameForm()

    context = {}
    context['page_title'] = '姓名'
    context['form_title'] = '修改姓名'
    context['submit_text'] = '修改'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'web/changename.html', context)


def change_pwd(request):

    if request.method == 'POST':
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
            return render('index', RequestContext(request, {'changepwd_success': True}))
        else:
            context = {}
            context['page_title'] = '修改密码'
            context['form_title'] = '修改密码'
            context['submit_text'] = '提交'
            context['form'] = form
            return render('web/change.html', RequestContext(request,context,  {'oldpassword_is_wrong': True}))

    form = ChangepwdForm()
    context = {}
    context['page_title'] = '修改密码'
    context['form_title'] = '修改密码'
    context['submit_text'] = '提交'
    context['form'] = form
    return render(request, 'web/change.html', context)


def logout(request):
    request.session.flush()
    return redirect('index')
