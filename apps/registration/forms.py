from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text = _('Required. 254 characters maximum.'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError(_('The e-mail is already registered.'))
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar'] # , 'biography'
        widgets = {
            'avatar': forms.ClearableFileInput(attrs = {'class':'form-control-file mt-3'}),
            # 'biography': forms.Textarea(attrs = {'class':'form-control mt-3', 'rows':3, 'placeholder':'Biography'}),
            # 'link': forms.URLInput(attrs = {'class':'form-control mt-3', 'placeholder':'Link'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required = True, help_text = _('Required. 254 characters maximum.'))

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError(_('The e-mail is already registered.'))
        return email
