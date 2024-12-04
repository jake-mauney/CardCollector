from django.db import models
from decks.models import Deck

class Tournament(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Registration(models.Model): #join between user deck and tournament
    deck = models.ForeignKey(Deck, on_delete=models.PROTECT)
    def __str__(self):
        return self.title
