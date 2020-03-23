from django.db import models

# Create your models here.
from .utils import generate_random_string


class Event(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )

    public_key = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        default=generate_random_string,
    )

    private_key = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        default=generate_random_string,
    )
