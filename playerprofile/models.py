from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    screenName = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.screenName
