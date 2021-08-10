from django.db import models
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
    return os.path.join(str(instance.user.id), sub_folder, filename)


class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    org = models.CharField('Organization', max_length=128, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, default=os.path.join(
        "avatar", "default.jpg"), verbose_name="头像")
    join_date = models.DateTimeField(
        "join date", blank=True, null=True, auto_now_add=True)
    mod_date = models.DateTimeField(
        "Mod date", blank=True, null=True,  auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return "{}'s profile".format(self.user.username)
