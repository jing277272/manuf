import random
from django import forms
from web import models
from utils import encrypt
from django_redis import get_redis_connection
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from web.forms.bootstrap import BootStrapForm
from django.conf import settings
from twilio.rest import Client
from utils.Twilio.sms import send_message


class RegisterModelForm(BootStrapForm, forms.ModelForm):

    """
    注册表单自动生成
    """
    password = forms.CharField(label='密码', min_length=6, max_length=18, error_messages={
        'min_length': '密码长度不能小于6个字符',
        'max_length': '密码长度不能大于18个字符'
    }, widget=forms.PasswordInput())

    confirm_password = forms.CharField(label='重复密码', min_length=6, max_length=18, error_messages={
        'min_length': '重复密码长度不能小于6个字符',
        'max_length': '重复密码长度不能大于18个字符'
    }, widget=forms.PasswordInput())
    mobile_phone = forms.CharField(label='手机号码',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号码格式错误'), ])

    code = forms.CharField(label='验证码', widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = ['username', 'work_id', 'nickname', 'email',
                  'password', 'confirm_password', 'mobile_phone', 'code']

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('用户名已存在')
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        # 加密 & 返回
        return encrypt.md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = encrypt.md5(self.cleaned_data['confirm_password'])
        if password != confirm_password:
            raise ValidationError("两次密码不一致！")
        return confirm_password

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(
            mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号已注册')
        return mobile_phone

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']

        return nickname

    def clean_work_id(self):
        work_id = self.cleaned_data['work_id']

        return work_id

    def clean_code(self):
        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data.get('mobile_phone')
        if not mobile_phone:
            return code

        conn = get_redis_connection()
        redis_code = conn.get(mobile_phone)
        if not redis_code:
            raise ValidationError('验证码已过期！')

        redis_str_code = redis_code.decode('utf-8')

        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误！')
        return code


class SendSmsForm(forms.Form):

    mobile_phone = forms.CharField(label='手机号码',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号码格式错误'), ])

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_mobile_phone(self):
        """手机号码校验的钩子"""
        mobile_phone = self.cleaned_data['mobile_phone']
        nickname = self.request.GET.get('nickname')
        tpl = self.request.GET.get('tpl')

     # 短信模板验证
        '''if tpl != 'register':
             raise ValidationError('模板类型错误!')
        return tpl'''
        # 存在校验
        exists = models.UserInfo.objects.filter(
            mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号码已存在！')
        # 发短信&写radis
        code = random.randrange(1000, 9999)

        conn = get_redis_connection("default")
        conn.set(mobile_phone, code, ex=60)
        print(code)
        print(nickname)
        sms = send_message(mobile_phone, tpl, code, nickname)

        return mobile_phone


class LoginForm(BootStrapForm, forms.Form):
    """
    密码登陆表单生成
    """
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    code = forms.CharField(label='图片验证码')

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_password(self):
        password = self.cleaned_data['password']
        return encrypt.md5(password)

    def clean_code(self):
        """
        校验图片验证码
        :return:
        """
        code = self.cleaned_data['code']
        session_code = self.request.session.get('image_code')
        if not session_code:
            raise ValidationError("验证码已过期，请重试！")

        if code.strip().upper() != session_code.upper():
            raise ValidationError('验证码错误，请重试！')

        return code


class ChangeNicknameForm(BootStrapForm, forms.Form):
    nickname_new = forms.CharField(
        label='姓名',
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '请输入正确姓名'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangeNicknameForm, self).__init__(*args, **kwargs)

    def clean_nickname_new(self):
        nickname_new = self.cleaned_data.get('nickname_new', '').strip()
        if nickname_new == '':
            raise forms.ValidationError("新的昵称不能为空")
        return nickname_new


class ChangepwdForm(forms.Form):

    old_password = forms.CharField(label='原始密码', required=True, error_messages={
                                   'required': u'请输入原密码'}, widget=forms.PasswordInput(attrs={
                                       'placeholder': u"原密码",
                                   }
    ))

    newpassword1 = forms.CharField(required=True,label=u'修改密码', min_length=6, max_length=18, error_messages={
        'min_length': '密码长度不能小于6个字符',
        'max_length': '密码长度不能大于18个字符'
    }, widget=forms.PasswordInput(attrs={
                'placeholder':u"新密码",
            }
))

    newpassword2 = forms.CharField(label='重复密码', min_length=6, max_length=18, error_messages={
        'min_length': '重复密码长度不能小于6个字符',
        'max_length': '重复密码长度不能大于18个字符'
    }, widget=forms.PasswordInput(attrs={
                'placeholder':u"确认密码",
            }
))

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data
