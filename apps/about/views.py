from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import About
from .forms import AboutForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name = 'dispatch')
class AboutUpdate(UpdateView): # (StaffRequiredMixin, UpdateView)
    model = About
    form_class = AboutForm
    template_name = "about/about_update.html"
    context_object_name = "context_about_update"
    # success_url = reverse_lazy("about_app:url_about_update")

    def get_success_url(self):
        return reverse_lazy('about_app:url_about_update', args = [self.object.id]) + '?ok'
