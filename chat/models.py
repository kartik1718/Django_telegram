from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAuth(User):
    active = models.BooleanField(default=False)
    password = None

class JokeCount(models.Model):
    
    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    stupid_count = models.IntegerField(default=0)
    fat_count = models.IntegerField(default=0)
    dumb_count = models.IntegerField(default=0)