from django import forms
from .models import About
from parler.forms import TranslatableModelForm

'''
class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        # fields = '__all__'
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs = {'class':'form-control'}),
        }
        labels = {
            'description':''
        }
'''

class AboutForm(TranslatableModelForm):

    class Meta:
        model = About
        # fields = '__all__'
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs = {'class':'form-control'}),
        }
        labels = {
            'description':''
        }
