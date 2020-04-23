from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bug_upvotes = models.IntegerField(blank=False, default=0)
    feature_upvotes = models.IntegerField(blank=False, default=0)
    forum_upvotes = models.IntegerField(blank=False, default=0)
    points_available = models.IntegerField(blank=False, default=0)
    cash_used = models.IntegerField(blank=False, default=0)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
