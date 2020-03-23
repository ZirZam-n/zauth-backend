from django.db import models


# Create your models here.
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
    )

    private_key = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True,
    )
