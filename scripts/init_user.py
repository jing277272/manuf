import os
import sys
import django


username = input("请输入用户名：")


nickname = input("请输入姓名：")

work_id = input("请输入工号：")
avatar = '/static/img/avatar/'+work_id+'.jpg'

passw = input("请输入注册密码：")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(base_dir)

#print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manuf.settings")
django.setup()
#print(username+nickname+work_id)

from utils import encrypt
from web import models

models.UserInfo.objects.create(
    username=username, nickname=nickname, avatar=avatar, email='111@111.com', mobile_phone='111111111', team='T0', work_id=work_id, password=encrypt.md5(passw))
print("创建成功！")

