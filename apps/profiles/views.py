from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.registration.models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = "context_profile_list"
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = "context_profile_detail"

    def get_object(self):
        return get_object_or_404(Profile, user__username = self.kwargs['username'])
