from django.db import models

class Player(models.Model):
    screenName = models.CharField(max_length=200)
    def __str__(self):
        return self.screenName
