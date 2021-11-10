from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=100)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} Profile"
