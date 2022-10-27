from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .enums import UserRoles
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^998[0-9]{2}[0-9]{7}$',
                                 message="Faqat O`zbekiston mobil raqamlari tasdiqlanadi('+' belgisiz!)")
    username = None
    phone = models.CharField(_('Telefon raqam'), validators=[phone_regex], max_length=17, unique=True)
    first_name = models.CharField(verbose_name='Name', max_length=50)
    last_name = models.CharField(verbose_name='Surname', max_length=50)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=UserRoles.choices(), blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"