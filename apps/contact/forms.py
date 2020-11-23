from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Name', required = True, widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': _('Your Name *')}
    ), min_length = 3, max_length = 100)
    email = forms.EmailField(label = 'E-mail', required = True, widget = forms.EmailInput(
        attrs = {'class': 'form-control',
                 'placeholder': _('Your E-mail *')}
    ), min_length = 3, max_length = 100)
    phone = forms.CharField(label = 'phone', required = False, widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': _('YourPhoneNotReq')}
    ), min_length = 3, max_length = 100)
    content = forms.CharField(label = 'Content', required = True, widget = forms.Textarea(
        attrs = {'class': 'form-control',
                 'placeholder': _('Your Message *'),
                 'rows': 4}
    ), min_length = 10, max_length = 1000)

'''
class ContactForm(forms.Form):
    name = forms.CharField(label = 'Name', required = True)
    email = forms.EmailField(label = 'E-mail', required = True)
    phone = forms.CharField(label = 'phone', required = False)
    content = forms.CharField(label = 'Content', required = True, widget = forms.Textarea)
'''
