from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Legal
from .forms import LegalForm

def get_page(request, page_id, page_title):
    queryset = get_object_or_404(Legal, id = page_id)
    template_name = "legal/politics.html"
    context_object_name = "context_legal"
    return render(request,
                  template_name,
                  {context_object_name: queryset})

def get_pages(request):
    queryset = Legal.objects.all()
    template_name = "legal/politics.html"
    context_object_name = "context_legals"
    return render(request,
                  template_name,
                  {context_object_name: queryset})

@method_decorator(staff_member_required, name = 'dispatch')
class LegalUpdate(UpdateView):
    model = Legal
    form_class = LegalForm
    template_name = "legal/politics_update.html"
    context_object_name = "context_legal_update"
    # success_url = reverse_lazy("legal_app:url_legal_update")

    def get_success_url(self):
        return reverse_lazy('legal_app:url_legal_update', args = [self.object.id]) + '?ok'
