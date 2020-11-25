from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from bootstrap_modal_forms.generic import BSModalUpdateView
from .forms import ControllerModalForm
from .models import Controller

class ControllerView(ListView):
    model = Controller
    queryset = Controller.objects.all()
    template_name = "controller/controller_list.html"
    context_object_name = "context_controllers"

@method_decorator(staff_member_required, name = 'dispatch')
class ControllerUpdateView(BSModalUpdateView):
    model = Controller
    template_name = 'controller/controller_update.html'
    form_class = ControllerModalForm
    # success_message = 'Success: Controller was updated.'
    success_url = reverse_lazy('controller_app:url_controller_list')

def fun_controllers(request):
    data = dict()
    if request.method == 'GET':
        obj_controllers = Controller.objects.all()
        data['table'] = render_to_string(
            'controller/controller_table.html',
            {'context_controllers': obj_controllers},
            request = request
        )
        return JsonResponse(data)
