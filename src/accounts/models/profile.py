from django.core import validators
from django.utils.translation import gettext as _
from django.db import models


class University(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name)


class MajorField(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )

    def __str__(self):
        return '{}'.format(self.name)


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

    def __str__(self):
        return '{}:{}'.format(self.major.name, self.minor_name)


class EducationInfo(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default=None,
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default=None,
    )

    entrance = models.IntegerField(
        null=True,
        blank=False,
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
        ),
        null=True,
        blank=False,
        default=None,
    )

    def __str__(self):
        return '{}'.format(self.user.username)


class Country(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )

    def __str__(self):
        return '{}'.format(self.name)


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

    def __str__(self):
        return '{}:{}'.format(self.country.name, self.name)


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

    def __str__(self):
        return '{}:{}:{}'.format(self.state.country.name, self.state.name, self.name)
