from django import template
from apps.controller.models import Controller

register = template.Library()

@register.simple_tag
def get_controller_enabler():
    queryset = Controller.objects.get(pk = 1)
    return queryset
