from django.shortcuts import render
from django.views.generic import DetailView, DeleteView

from musicApp.profiles.forms import ProfileDeleteForm
from musicApp.profiles.models import Profile


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'


class ProfileDeleteView(DeleteView):
    model = Profile
    form_class = ProfileDeleteForm
    template_name = 'profile/profile-delete.html'


