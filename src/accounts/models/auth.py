from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.core import validators
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import EducationInfo, City
from events.utils import generate_random_string


class ZUser(AbstractUser):
    blank_to_null = ['phone', 'nat_code', 'education', 'city', 'avatar']

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

    avatar = models.ImageField(
        blank=True,
        null=True,
        default=None,
    )

    def setup_verification_token(self):
        self.is_active = False
        if self.verification:
            self.verification.delete()
        self.verification = EmailVerificationToken.objects.create(user=self)
        self.save()

    def send_activation_email(self):
        if not self.verification:
            raise Exception('Must run setup_verification_token method first')
        site = Site.objects.get_current()
        subject = 'Verify your email at {}'.format(site.display_name)
        ctx = {
            'site_domain': site.domain_name,
            'site_name': site.display_name,
            'token': self.verification.token,
        }
        text = render_to_string('accounts/mails/verify_email.txt', ctx)
        msg = EmailMultiAlternatives(
            subject,
            text,
            settings.EMAIL_SENDER,
            [self.email],
        )
        msg.send()

    def save(self, *args, **kwargs):
        for field in ZUser.blank_to_null:
            setattr(self, field, getattr(self, field) or None)
        super(ZUser, self).save(*args, **kwargs)


class EmailVerificationToken(models.Model):
    user = models.OneToOneField(
        ZUser,
        related_name='verification',
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
