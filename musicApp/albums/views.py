from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class AlbumAddView(CreateView):
    pass


class AlbumDetailView(DetailView):
    pass


class AlbumEditView(UpdateView):
    pass


class AlbumDeleteView(DeleteView):
    pass
