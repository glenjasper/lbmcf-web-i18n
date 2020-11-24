from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import (
    Member
)

class OldMembersView(ListView):
    model = Member
    queryset = Member.objects.all().filter(status = True, role_id = 7).order_by('degree__order', 'first_name')
    template_name = "members/old_members.html"
    context_object_name = "context_oldmembers"
