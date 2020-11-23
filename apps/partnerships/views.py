from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import (
    Partnership
)
'''
class PartnershipPlaceView(ListView):
    model = Partnership
    #template_name = "core/model.html"
    template_name = "core/home.html"
    context_object_name = "context_partnerships_place"

    def get_queryset(self, **kwargs):
        slug_code = self.kwargs.get('code', None)
        print("-----------------------")
        print(slug_code)
        print("-----------------------")
        queryset = self.model.objects.all()
        return queryset.filter(institution__state__id = 5)
        # return self.model.objects.filter(institution__state__id = 5)
'''
