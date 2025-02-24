from django.db.models.signals import post_save,post_delete

from base.models import Post,Profile
from django.contrib.auth.models import User

def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user
        )

post_save.connect(createProfile, sender=User)