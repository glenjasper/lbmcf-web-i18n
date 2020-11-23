from django import forms
from .models import Legal
from parler.forms import TranslatableModelForm

'''
class LegalForm(forms.ModelForm):

    class Meta:
        model = Legal
        # fields = '__all__'
        fields = ['title', 'content', 'order'] # 'status'
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Title'}),
            'content': forms.Textarea(attrs = {'class':'form-control', 'placeholder':'Content'}),
            'order': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Order'}),
            # 'status': forms.NullBooleanSelect(attrs = {'class':'form-control'}),
        }
        labels = {
            'title':'', 'content':'', 'order':'',
        }
'''

class LegalForm(TranslatableModelForm):

    class Meta:
        model = Legal
        # fields = '__all__'
        fields = ['title', 'content', 'order'] # 'status'
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Title'}),
            'content': forms.Textarea(attrs = {'class':'form-control', 'placeholder':'Content'}),
            'order': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Order'}),
            # 'status': forms.NullBooleanSelect(attrs = {'class':'form-control'}),
        }
        labels = {
            'title':'', 'content':'', 'order':'',
        }
