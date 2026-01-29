from django.shortcuts import render
from django.views.generic import TemplateView

from musicApp.profiles.models import Profile


class HomeView(TemplateView):
    def get_template_names(self):
        profile = Profile.objects.first()

        if profile is not None:
            return ['common/home-with-profile.html']
        return ['common/home-no-profile.html']