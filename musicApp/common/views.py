from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from musicApp.albums.models import Album
from musicApp.profiles.forms import ProfileCreateForm
from musicApp.profiles.models import Profile
from musicApp.utils import get_user_object


class HomeView(BaseFormView, ListView):
    queryset = Album.objects.all()
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')
    context_object_name = 'albums'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context

    def get_template_names(self):
        profile = get_user_object()

        if profile is not None:
            return ['common/home-with-profile.html']
        return ['common/home-no-profile.html']