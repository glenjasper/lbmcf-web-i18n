from django import forms
from .models import Controller
from parler.forms import TranslatableModelForm
from bootstrap_modal_forms.forms import BSModalModelForm

'''
class ControllerForm(TranslatableModelForm):

    class Meta:
        model = Controller
        # fields = '__all__'
        fields = ['name', 'enabler']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Name'}),
            'enabler': forms.NullBooleanSelect(attrs = {'class':'form-control'}),
        }
        labels = {
            'name':'', 'enabler':''
        }
'''

class ControllerModalForm(BSModalModelForm):

    class Meta:
        model = Controller
        fields = ['enabler']
        # widgets = {
        #     'enabler': forms.NullBooleanSelect(attrs = {'class':'form-control'}),
        # }
        labels = {
            'name':'', 'enabler':''
        }
