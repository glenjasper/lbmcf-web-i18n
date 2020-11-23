# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail # UserCreationForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs = {'class': 'form-control mb-2', 'placeholder': _('User')})
        form.fields['email'].widget = forms.EmailInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'E-mail'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class': 'form-control mb-2', 'placeholder': _('Password')})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class': 'form-control mb-2', 'placeholder': _('Confirm password')})
        # form.fields['username'].label = ''
        return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('registration_app:url_profile')
    template_name = 'registration/profile.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile

@method_decorator(login_required, name = 'dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('registration_app:url_profile')
    template_name = 'registration/profile_email.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'E-mail'})
        return form
