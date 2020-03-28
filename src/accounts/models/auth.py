from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import EducationInfo, City
from events.utils import generate_random_string


class ZUser(AbstractUser):
    blank_to_null = ['phone', 'nat_code', 'education', 'city']

    phone = PhoneNumberField(
        blank=True,
        null=True,
        default=None,
        unique=True,
    )

    nat_code_validator = validators.RegexValidator(
        regex=r'\d*',
        message=_('National code must be a decimal sequence'),
    )
    nat_code = models.CharField(
        validators=[nat_code_validator],
        max_length=10,
        blank=True,
        null=True,
        default=None,
        unique=True,
    )

    education = models.OneToOneField(
        EducationInfo,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        related_name='user',
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )

    avatar = models.ImageField()

    def send_activation_email(self):
        pass

    def save(self, *args, **kwargs):
        for field in ZUser.blank_to_null:
            setattr(self, field, getattr(self, field) or None)
        super(ZUser, self).save(*args, **kwargs)


class EmailVerificationToken(models.Model):
    user = models.OneToOneField(
        ZUser,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    token = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        default=generate_random_string,
    )
