from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext as _
from django.db import models

# Create your models here.
from phonenumber_field.formfields import PhoneNumberField


class University(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
    )


class MajorField(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
    )


class Field(models.Model):
    minor_name = models.CharField(
        blank=False,
        null=False,
    )
    major = models.ForeignKey(
        MajorField,
        on_delete=models.CASCADE,
    )


class EducationInfo(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.SET_NULL,
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
    )


class City(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
    )
    country = models.ForeignKey(
        Country,
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
        min_length=10,
        max_length=10,
        blank=False,
        null=True,
        default=None,
        unique=True,
    )

    education = models.OneToOneField(
        EducationInfo,
        on_delete=models.CASCADE,
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
    )

    avatar = models.ImageField(
        null=True,
        default=None,
    )
