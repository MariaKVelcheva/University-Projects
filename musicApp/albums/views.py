from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from musicApp.albums.forms import AlbumAddForm, AlbumDeleteForm, AlbumEditForm
from musicApp.albums.models import Album
from musicApp.utils import get_user_object


class AlbumAddView(CreateView):
    model = Album
    form_class = AlbumAddForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_object()
        return super().form_valid(form)


class AlbumDetailView(DetailView):
    pass


class AlbumEditView(UpdateView):
    pass


class AlbumDeleteView(DeleteView):
    pass
