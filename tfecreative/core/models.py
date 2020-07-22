from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import (
    ShortUUIDField,
    CreationDateTimeField,
    ModificationDateTimeField,
)
from rest_framework.authtoken.models import Token
from tfecreative import settings


class TfeUser(AbstractUser):
    uuid = ShortUUIDField()

    def __str__(self):
        try:
            return f"{self.username}"
        except AttributeError:
            return ""


class UserProfile(models.Model):
    uuid = ShortUUIDField()
    user = models.OneToOneField(TfeUser, on_delete=models.CASCADE)
    date_created = CreationDateTimeField()
    date_modified = ModificationDateTimeField()

    def __str__(self):
        try:
            return f"{self.user.username} Profile"
        except AttributeError:
            return ""


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserProfile.objects.create(user=instance)
