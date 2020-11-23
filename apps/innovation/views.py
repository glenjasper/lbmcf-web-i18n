from django.shortcuts import render
from django.views.generic import (
    ListView
)
from .models import (
    Patent,
)

class PatentView(ListView):
    model = Patent
    template_name = "innovation/patents.html"
    context_object_name = "context_patents"
