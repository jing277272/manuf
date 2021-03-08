import os
import sys
import django


username = ""
print("请输入用户名：")
username = input()


nickname = ""
print("请输入姓名：")
nickname = input()

work_id = ""
print("请输入工号：")
work_id = input()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(base_dir)

print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manuf.settings")
django.setup()
print(username+nickname+work_id)


from web import models
from utils import encrypt


models.UserInfo.objects.create(
    username=username, nickname=nickname, avatar='..\static\img\avatar\img_default_avatar.png', email='111@111.com', mobile_phone='111111111', team='T0', work_id=work_id, password=encrypt.md5('123456'))
print("创建完毕！")
