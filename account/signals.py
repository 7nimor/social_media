from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Person


def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        Person.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_user_profile, sender=User)
