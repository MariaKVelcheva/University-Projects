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
    model = Album
    template_name = 'album/album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'album/album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'album/album-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
