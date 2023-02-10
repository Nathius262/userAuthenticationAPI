from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import customUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    objects = customUserManager()

    def __str__(self):

        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True