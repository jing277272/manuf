from django import forms

from mould import models
from mould.forms.bootstrap import BootStrapForm


class RepairpartsModelForm(BootStrapForm, forms.ModelForm):
    """
    表单生成
    """
    type = forms.CharField(label="类型")
    imgs = forms.ImageField(label="图片")
    local = forms.CharField(label="货位号")
    quantity = forms.CharField(label="在库数量")

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

class Deliver(forms.Form):
    pass


    def __init__(self, request, *args, **kwargs):
        uper().__init__(*args, **kwargs)
        self.request = request
