from django import template
from apps.legal.models import Legal

register = template.Library()

@register.simple_tag
def get_page_list():
    queryset = Legal.objects.all().filter(status = True)
    return queryset
