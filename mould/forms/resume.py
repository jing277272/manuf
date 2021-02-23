import random
from django import forms
from mould import models
from mould.forms.bootstrap import BootStrapForm


class CreateModelForm(BootStrapForm, forms.ModelForm):
    """
    注册表单自动生成


    """

    class Meta:
        model = models.Mould
        fields = ['item', 'assy_No', 'part_No', 'tool_No', 'op', 'name', 'equipment', 'line', 'live',
                  'marker', 'order_date', 'zcId', 'qrId', 'user_dp', 'manage_dp', 'site', 'status', 'owner', 'remark',
                  'location', 'img_upper',
                  'img_downer', 'img_assy', 'img_op', 'length', 'width', 'height', 'weight_upper', 'weight_assy'
                  ]
