from django import forms

from musicApp.albums.models import Album
from musicApp.profiles.models import Profile


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['user']

        labels = {
            'album_name': "Album Name",
            'artist_name': "Artist",
            'genre': "Genre",
            'description': "Description",
            'image_url': "Image URL",
            "price": 'Price'
        }

        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Album Name'
            }),

            'artist_name': forms.TextInput(attrs={
                'placeholder': 'Artist Name'
            }),

            'genre': forms.Select(),

            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),

            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            })
        }


class AlbumAddForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
            self.fields[field].readonly = True

