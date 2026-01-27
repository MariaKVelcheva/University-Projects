from django.core.validators import MinValueValidator
from django.db import models

from musicApp.profiles.models import Profile


class Album(models.Model):
    GENRE_CHOICES = (
        ('pop music', 'Pop Music'),
        ('jazz music', 'Jazz Music'),
        ('r&b music', 'R&B Music'),
        ('rock music', 'Rock Music'),
        ('country music', 'Country Music'),
        ('dance music', 'Dance Music'),
        ('hip hop music', 'Hip Hop Music'),
        ('other', 'Other'),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist_name = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        default='other',
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )