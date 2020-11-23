from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

@register.filter(name='startswith')
def startswith(text, starts):
    text = str(text).lower()
    return text.startswith(starts)

@register.filter(name='endswith')
def endswith(text, ends):
    text = str(text).lower()
    return text.endswith(ends)

@register.filter(is_safe=True)
def is_numberic(value):
    return str(value).isdigit()
