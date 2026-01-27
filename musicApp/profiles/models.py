from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, \
    RegexValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2),
                    RegexValidator(r'^[a-zA-Z0-9_]+$',
                                   message="Ensure this value contains only letters, numbers, and underscore.")],
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(13),]
    )
