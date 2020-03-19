from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bug_upvotes = models.IntegerField(blank=False, default=0)
    feature_upvotes = models.IntegerField(blank=False, default=0)