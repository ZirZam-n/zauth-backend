from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext as _
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class University(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )


class MajorField(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )


class Field(models.Model):
    minor_name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    major = models.ForeignKey(
        MajorField,
        on_delete=models.CASCADE,
    )


class EducationInfo(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
        null=True,
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.SET_NULL,
        null=True,
    )

    entrance = models.IntegerField(
        null=True,
        default=None,
    )

    edu_code_validator = validators.RegexValidator(
        regex=r'\d{8,15}',
        message=_('National code must be a decimal sequence'),
    )
    edu_code = models.CharField(
        validators=[edu_code_validator],
        blank=False,
        null=True,
        default=None,
        unique=True,
        max_length=15,
    )

    grade = models.CharField(
        max_length=20,
        choices=(
            ('before', _('Before university')),
            ('bachelor', _('Bachelor of science')),
            ('master', _('Master of science')),
            ('phd', _('Ph.D')),
            ('after', _('After Ph.D')),
        )
    )


class Country(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )


class State(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )


class City(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
    )


class ZAuthUser(AbstractUser):
    phone = PhoneNumberField(
        blank=False,
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
        blank=False,
        null=True,
        default=None,
        unique=True,
    )

    education = models.OneToOneField(
        EducationInfo,
        on_delete=models.CASCADE,
        null=True,
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
    )

    avatar = models.ImageField(
        null=True,
        default=None,
    )
