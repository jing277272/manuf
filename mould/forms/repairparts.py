from django import forms

from mould import models
from mould.forms.bootstrap import BootStrapForm


class RepairpartsModelForm(BootStrapForm, forms.ModelForm):


    class Meta:
        model = models.RepairParts
        exclude = ['tool','modify']
        widgets = {
            "type":forms.Select(attrs={'class': "selectpicker", "data-live-search": "true"}),
        }
        fields ="__all__"

class Deliver(forms.Form):
    pass


    def __init__(self, request, *args, **kwargs):
        uper().__init__(*args, **kwargs)
        self.request = request
