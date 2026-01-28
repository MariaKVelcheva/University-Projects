from django.urls import path, include

from musicApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]